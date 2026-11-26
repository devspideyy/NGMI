"""NGMI — shared Blender toolkit (bpy 5.x) used by props.py, scenes.py, greybox_l3.py.

Everything is built in METRES, facing -Y (the camera looks along +Y).
Materials have two layers:
  * a plain Principled BSDF (base colour / metallic / roughness). This is what
    FBX/GLB export carries into Unreal; there you swap in Megascans materials
    by slot name (see art/blender/README.md).
  * optional procedural "wear" (grime in cavities, rust, scratches, bumps,
    roughness variation). Render-only; added with apply_wear_all() AFTER export.
"""
import math
import os
import random

import bmesh
import bpy
from mathutils import Matrix, Vector

DEG = math.radians
HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")

# ------------------------------------------------------------------ scene

def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    _parts.clear()
    MATS.clear()
    _fonts.clear()
    random.seed(7)


def link(o):
    bpy.context.collection.objects.link(o)
    return o


# ------------------------------------------------------------------ fonts
_fonts = {}
FONT_FILES = {
    "sign": "BebasNeue-Regular.ttf",       # OFL — signage, neon
    "notice": "SpecialElite-Regular.ttf",  # Apache-2.0 — typed notices
    "marker": "PermanentMarker-Regular.ttf",  # Apache-2.0 — graffiti
    "scratch": "RockSalt-Regular.ttf",     # Apache-2.0 — scratched text
}


# 3D text uses clean fonts; the distressed ones are only for 2D decals (they explode the triangle count)
FONT_3D = {"notice": "builtin", "scratch": "marker"}


def font(kind="sign"):
    """Load a bundled font; fall back to Blender's built-in font if missing."""
    if kind in _fonts:
        return _fonts[kind]
    if kind == "builtin":
        return None
    f = None
    path = os.path.join(FONT_DIR, FONT_FILES.get(kind, ""))
    if os.path.isfile(path):
        f = bpy.data.fonts.load(path)
    _fonts[kind] = f
    return f


# ------------------------------------------------------------------ materials
MATS = {}  # name -> (material, wear dict or None)


def mat(name, color, metallic=0.0, rough=0.5, transmission=0.0, emission=None, em=0.0,
        ior=1.45, coat=0.0, sss=0.0, sheen=0.0, wear=None):
    """Create (or reuse) a Principled material. `wear` = dict for apply_wear()."""
    if name in MATS:
        return MATS[name][0]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Metallic"].default_value = metallic
    b.inputs["Roughness"].default_value = rough
    b.inputs["IOR"].default_value = ior
    if transmission:
        b.inputs["Transmission Weight"].default_value = transmission
    if emission:
        b.inputs["Emission Color"].default_value = (*emission, 1)
        b.inputs["Emission Strength"].default_value = em
    if coat:
        b.inputs["Coat Weight"].default_value = coat
    if sss:
        b.inputs["Subsurface Weight"].default_value = sss
    if sheen:
        b.inputs["Sheen Weight"].default_value = sheen
    m.diffuse_color = (*color, 1)
    MATS[name] = (m, wear)
    return m


def _n(nt, kind, x=0, y=0, **props):
    n = nt.nodes.new(kind)
    n.location = (x, y)
    for k, v in props.items():
        setattr(n, k, v)
    return n


def _sock(node, ident):
    for s in list(node.inputs) + list(node.outputs):
        if s.identifier == ident:
            return s
    raise KeyError(ident)


def _mix_col(nt, fac, a, b, x=0, y=0, blend="MIX"):
    """Colour mix; fac/a/b may be sockets or plain values."""
    n = _n(nt, "ShaderNodeMix", x, y)
    n.data_type = "RGBA"
    n.blend_type = blend
    L = nt.links
    for ident, val in (("Factor_Float", fac), ("A_Color", a), ("B_Color", b)):
        s = _sock(n, ident)
        if isinstance(val, bpy.types.NodeSocket):
            L.new(val, s)
        else:
            s.default_value = val if ident == "Factor_Float" else (*val[:3], 1)
    return _sock(n, "Result_Color")


def _math(nt, op, a, b=0.0, x=0, y=0, clamp=False):
    n = _n(nt, "ShaderNodeMath", x, y, operation=op, use_clamp=clamp)
    for i, v in enumerate((a, b)):
        if isinstance(v, bpy.types.NodeSocket):
            nt.links.new(v, n.inputs[i])
        else:
            n.inputs[i].default_value = v
    return n.outputs[0]


def _ramp(nt, fac, p0, p1, x=0, y=0):
    n = _n(nt, "ShaderNodeValToRGB", x, y)
    n.color_ramp.elements[0].position = p0
    n.color_ramp.elements[1].position = p1
    nt.links.new(fac, n.inputs["Fac"])
    return n.outputs["Color"]


def _noise(nt, vec, scale, detail=6.0, rough=0.6, x=0, y=0, distortion=0.0):
    n = _n(nt, "ShaderNodeTexNoise", x, y)
    nt.links.new(vec, n.inputs["Vector"])
    n.inputs["Scale"].default_value = scale
    n.inputs["Detail"].default_value = detail
    n.inputs["Roughness"].default_value = rough
    n.inputs["Distortion"].default_value = distortion
    return n


def apply_wear(m, w):
    """Add procedural grime / rust / scratches / bumps to material m (Cycles)."""
    if not w:
        return
    nt = m.node_tree
    L = nt.links
    b = nt.nodes["Principled BSDF"]
    base = tuple(b.inputs["Base Color"].default_value)[:3]
    rough = b.inputs["Roughness"].default_value
    metal = b.inputs["Metallic"].default_value
    s = w.get("scale", 10.0)
    tc = _n(nt, "ShaderNodeTexCoord", -1400, 0)
    vec = tc.outputs["Object"]
    if w.get("stretch"):  # vertical streaks (water / rust runs)
        mp = _n(nt, "ShaderNodeMapping", -1250, 0)
        mp.inputs["Scale"].default_value = (1, 1, w["stretch"])
        L.new(vec, mp.inputs["Vector"])
        vec_streak = mp.outputs["Vector"]
    else:
        vec_streak = vec

    # grime = cavities (AO) + blotches
    col = base
    grime_amt = w.get("grime", 0.35)
    n1 = _noise(nt, vec_streak, s, 7, 0.62, -1100, 300)
    blot = _ramp(nt, n1.outputs["Fac"], 0.42, 0.78, -900, 300)
    if w.get("ao", True):
        ao = _n(nt, "ShaderNodeAmbientOcclusion", -1100, 600, samples=4)
        ao.inputs["Distance"].default_value = w.get("ao_dist", 0.06)
        cav = _math(nt, "SUBTRACT", 1.0, ao.outputs["AO"], -900, 600)
        cav = _math(nt, "MULTIPLY", cav, 1.6, -750, 600)
        g = _math(nt, "ADD", cav, _math(nt, "MULTIPLY", blot, 0.7, -750, 400), -600, 500, clamp=True)
    else:
        g = _math(nt, "MULTIPLY", blot, 0.8, -600, 500, clamp=True)
    g = _math(nt, "MULTIPLY", g, grime_amt, -450, 500, clamp=True)
    grime_col = w.get("grime_col", (0.025, 0.03, 0.02))
    col = _mix_col(nt, g, base, grime_col, -300, 400)

    rough_s = None
    met_s = None
    # rust patches
    rust = w.get("rust", 0.0)
    if rust > 0:
        n2 = _noise(nt, vec_streak, s * 0.7, 10, 0.72, -1100, -200, distortion=0.3)
        lo = 0.66 - 0.32 * rust
        rmask = _ramp(nt, n2.outputs["Fac"], lo, lo + 0.06, -900, -200)
        n3 = _noise(nt, vec, s * 3, 4, 0.5, -1100, -450)
        rust_col = _mix_col(nt, n3.outputs["Fac"], (0.28, 0.11, 0.04), (0.12, 0.05, 0.025), -750, -350)
        col = _mix_col(nt, rmask, col, rust_col, -150, 200)
        r_bw = _math(nt, "MULTIPLY", rmask, 1.0, -600, -200)  # colour -> float
        met_s = _math(nt, "MULTIPLY", _math(nt, "SUBTRACT", 1.0, r_bw, -450, -150), metal, -300, -150)
        rough_s = _math(nt, "ADD", rough, _math(nt, "MULTIPLY", r_bw, 0.5, -450, -260), -300, -260)

    # scratches (thin bright lines, smoother)
    if w.get("scratch", 0):
        vo = _n(nt, "ShaderNodeTexVoronoi", -1100, -700, feature="DISTANCE_TO_EDGE")
        L.new(vec, vo.inputs["Vector"])
        vo.inputs["Scale"].default_value = s * 2.5
        sc = _ramp(nt, vo.outputs["Distance"], 0.0, 0.025, -900, -700)
        sc = _math(nt, "SUBTRACT", 1.0, sc, -750, -700)
        sc = _math(nt, "MULTIPLY", sc, w["scratch"], -600, -700, clamp=True)
        lighter = tuple(min(1, c * 1.6 + 0.08) for c in base)
        col = _mix_col(nt, sc, col, lighter, 0, 100)

    # roughness variation + grime makes it rougher
    n4 = _noise(nt, vec, s * 4, 3, 0.5, -1100, -950)
    rv = _n(nt, "ShaderNodeMapRange", -900, -950)
    L.new(n4.outputs["Fac"], rv.inputs[0])
    rv.inputs[1].default_value, rv.inputs[2].default_value = 0.3, 0.7
    rv.inputs[3].default_value, rv.inputs[4].default_value = -w.get("rough_var", 0.12), w.get("rough_var", 0.12)
    rbase = rough_s if rough_s is not None else rough
    rt = _math(nt, "ADD", rbase, rv.outputs[0], -600, -900)
    rt = _math(nt, "ADD", rt, _math(nt, "MULTIPLY", g, 0.35, -600, -1050), -450, -950, clamp=True)
    L.new(rt, b.inputs["Roughness"])
    if met_s is not None:
        L.new(met_s, b.inputs["Metallic"])
    L.new(col, b.inputs["Base Color"])

    # bump
    bump = w.get("bump", 0.15)
    if bump:
        n5 = _noise(nt, vec, s * w.get("bump_scale", 14), 9, 0.65, -600, -1300)
        bp = _n(nt, "ShaderNodeBump", -300, -1300)
        bp.inputs["Strength"].default_value = bump
        bp.inputs["Distance"].default_value = w.get("bump_dist", 0.02)
        L.new(n5.outputs["Fac"], bp.inputs["Height"])
        L.new(bp.outputs["Normal"], b.inputs["Normal"])


def apply_wear_all():
    for name, (m, w) in MATS.items():
        if w and not m.get("_wear_done"):
            apply_wear(m, w)
            m["_wear_done"] = True


# Wear presets
W_PAINT = dict(grime=0.45, scratch=0.25, bump=0.08, scale=6)
W_METAL = dict(grime=0.4, rust=0.25, scratch=0.35, bump=0.1, scale=8)
W_RUSTY = dict(grime=0.55, rust=0.6, bump=0.25, scale=6, stretch=0.35)
W_PLASTIC = dict(grime=0.35, scratch=0.15, bump=0.05, scale=7)
W_STONE = dict(grime=0.6, bump=0.45, scale=4, bump_scale=10, rough_var=0.08, stretch=0.5)
W_FABRIC = dict(grime=0.25, bump=0.25, scale=12, bump_scale=30, rough_var=0.05)
W_RUBBER = dict(grime=0.3, bump=0.1, scale=9)
W_WOOD = dict(grime=0.45, scratch=0.2, bump=0.12, scale=5)
W_LIGHT = dict(grime=0.2, bump=0.03, scale=8, ao=False)


def standard_mats():
    """The shared palette. Names = Unreal material slot names."""
    M = {}
    M["steel"] = mat("M_Steel", (0.62, 0.64, 0.62), metallic=1, rough=0.25, wear=W_METAL)
    M["steel_dirty"] = mat("M_SteelDirty", (0.42, 0.43, 0.4), metallic=1, rough=0.5, wear=W_RUSTY)
    M["rust"] = mat("M_RustSteel", (0.3, 0.17, 0.09), metallic=0.5, rough=0.75, wear=dict(W_RUSTY, rust=0.8))
    M["chrome"] = mat("M_Chrome", (0.8, 0.82, 0.8), metallic=1, rough=0.08, wear=dict(W_METAL, rust=0.05))
    M["brass"] = mat("M_Brass", (0.62, 0.45, 0.16), metallic=1, rough=0.3, wear=dict(W_METAL, rust=0.1))
    M["gold"] = mat("M_GildedFrame", (0.7, 0.5, 0.15), metallic=1, rough=0.28, wear=dict(W_METAL, rust=0.0, grime=0.55))
    M["acrylic"] = mat("M_AcrylicPink", (0.82, 0.38, 0.42), rough=0.2, coat=0.7, sss=0.15, wear=W_PLASTIC)
    M["clear"] = mat("M_ClearPlastic", (0.92, 0.96, 0.93), rough=0.12, transmission=1, ior=1.5)
    M["glass"] = mat("M_Glass", (0.88, 0.96, 0.9), rough=0.04, transmission=1, ior=1.5)
    M["glass_green"] = mat("M_GlassGreen", (0.12, 0.7, 0.28), rough=0.05, transmission=1, ior=1.5)
    M["jar_liquid"] = mat("M_JarLiquid", (0.5, 0.72, 0.38), rough=0.05, transmission=0.85, ior=1.33)
    M["juice"] = mat("M_JawJuice", (0.2, 0.9, 0.3), rough=0.1, transmission=0.6, emission=(0.2, 1.0, 0.35), em=1.2)
    M["vinyl"] = mat("M_VinylTeal", (0.06, 0.24, 0.21), rough=0.42, coat=0.3, wear=dict(W_PLASTIC, grime=0.5, scratch=0.3))
    M["vinyl_dark"] = mat("M_VinylCracked", (0.05, 0.14, 0.12), rough=0.7, wear=dict(W_PLASTIC, grime=0.6, bump=0.2))
    M["white_paint"] = mat("M_PaintOffWhite", (0.66, 0.66, 0.6), rough=0.5, wear=W_PAINT)
    M["green_paint"] = mat("M_PaintClinicGreen", (0.12, 0.28, 0.2), rough=0.5, wear=W_PAINT)
    M["beige_plastic"] = mat("M_PlasticYellowed", (0.56, 0.5, 0.38), rough=0.45, wear=W_PLASTIC)
    M["black_plastic"] = mat("M_BlackPlastic", (0.02, 0.022, 0.02), rough=0.4, wear=W_PLASTIC)
    M["teal_plastic"] = mat("M_PlasticTeal", (0.05, 0.4, 0.36), rough=0.35, wear=W_PLASTIC)
    M["orange_plastic"] = mat("M_PlasticOrange", (0.85, 0.25, 0.03), rough=0.35, wear=W_PLASTIC)
    M["red_plastic"] = mat("M_RedPlastic", (0.55, 0.03, 0.02), rough=0.32, wear=W_PLASTIC)
    M["rubber"] = mat("M_Rubber", (0.025, 0.025, 0.022), rough=0.85, wear=W_RUBBER)
    M["hardhat"] = mat("M_HardHatYellow", (0.9, 0.55, 0.02), rough=0.3, coat=0.4, wear=dict(W_PLASTIC, scratch=0.45, grime=0.5))
    M["wood"] = mat("M_WoodDark", (0.28, 0.15, 0.07), rough=0.55, wear=W_WOOD)
    M["wood_light"] = mat("M_WoodLight", (0.55, 0.38, 0.2), rough=0.6, wear=W_WOOD)
    M["paper"] = mat("M_Paper", (0.86, 0.84, 0.75), rough=0.9, wear=dict(W_FABRIC, grime=0.35))
    M["ink"] = mat("M_Ink", (0.02, 0.02, 0.02), rough=0.8)
    M["stone"] = mat("M_Stone", (0.14, 0.15, 0.13), rough=0.92, wear=W_STONE)
    M["carve"] = mat("M_StoneCarved", (0.36, 0.4, 0.35), rough=0.95, wear=W_STONE)
    M["moss"] = mat("M_Moss", (0.06, 0.16, 0.04), rough=1.0, wear=dict(W_FABRIC, grime=0.2))
    M["mirror"] = mat("M_Mirror", (0.95, 0.97, 0.96), metallic=1, rough=0.02)
    M["ceramic"] = mat("M_Ceramic", (0.82, 0.83, 0.78), rough=0.15, coat=0.5, wear=dict(W_PLASTIC, grime=0.6))
    M["tape"] = mat("M_Tape", (0.86, 0.83, 0.74), rough=0.6, wear=W_FABRIC)
    M["fabric_grey"] = mat("M_FabricHoodieGrey", (0.18, 0.18, 0.18), rough=0.95, sheen=0.4, wear=W_FABRIC)
    M["towel"] = mat("M_FabricTowel", (0.8, 0.78, 0.74), rough=1.0, sheen=0.5, wear=W_FABRIC)
    M["towel_pink"] = mat("M_FabricTowelPink", (0.78, 0.45, 0.5), rough=1.0, sheen=0.5, wear=W_FABRIC)
    M["mannequin"] = mat("M_MannequinIvory", (0.7, 0.66, 0.58), rough=0.3, coat=0.3, wear=dict(W_PLASTIC, grime=0.5))
    M["foam"] = mat("M_Foam", (0.9, 0.92, 0.9), rough=0.6, sss=0.6)
    M["hazard_y"] = mat("M_HazardYellow", (0.85, 0.6, 0.02), rough=0.45, wear=W_PAINT)
    M["hazard_k"] = mat("M_HazardBlack", (0.02, 0.02, 0.02), rough=0.5, wear=W_PAINT)
    M["sepia"] = mat("M_PhotoSepia", (0.45, 0.33, 0.2), rough=0.5, wear=dict(W_PAINT, grime=0.6))
    M["egg_white"] = mat("M_EggWhite", (0.92, 0.9, 0.85), rough=0.25, sss=0.3)
    M["egg_yolk"] = mat("M_EggYolk", (0.95, 0.55, 0.05), rough=0.2, coat=0.6)
    M["gum"] = mat("M_GumPink", (0.85, 0.42, 0.55), rough=0.55, sss=0.2, wear=dict(W_PLASTIC, grime=0.3, bump=0.25))
    M["cucumber"] = mat("M_Cucumber", (0.55, 0.75, 0.35), rough=0.3, sss=0.3)
    M["cucumber_skin"] = mat("M_CucumberSkin", (0.06, 0.2, 0.05), rough=0.4)
    # emissives
    M["glow_green"] = mat("M_GlowGreen", (0.6, 1, 0.7), emission=(0.27, 1.0, 0.52), em=12)
    M["glow_ring"] = mat("M_RingLightGlow", (0.9, 1, 0.92), emission=(0.55, 1.0, 0.65), em=10)
    M["glow_warm"] = mat("M_GlowWarm", (1, 0.95, 0.85), emission=(1.0, 0.92, 0.78), em=12)
    M["glow_tube"] = mat("M_TubeLight", (1, 1, 1), emission=(0.85, 1.0, 0.9), em=9)
    M["glow_tube_dead"] = mat("M_TubeLightDead", (0.5, 0.52, 0.5), rough=0.3, emission=(0.6, 0.8, 0.65), em=0.3)
    M["glow_orange"] = mat("M_GlowFurnace", (1, 0.5, 0.1), emission=(1.0, 0.38, 0.06), em=18)
    M["glow_red"] = mat("M_GlowLEDRed", (1, 0.1, 0.05), emission=(1.0, 0.08, 0.03), em=8)
    M["glow_pink"] = mat("M_NeonPink", (1, 0.4, 0.7), emission=(1.0, 0.25, 0.6), em=14)
    M["glow_magenta"] = mat("M_GlowMagenta", (1, 0.2, 0.9), emission=(1.0, 0.12, 0.85), em=14)
    M["glow_teal"] = mat("M_GlowTeal", (0.3, 1, 0.9), emission=(0.1, 1.0, 0.8), em=6)
    M["glow_screen"] = mat("M_ScreenGlow", (0.02, 0.08, 0.04), rough=0.08, emission=(0.18, 0.95, 0.4), em=2.5)
    M["glow_phone"] = mat("M_PhoneScreen", (0.03, 0.04, 0.05), rough=0.06, emission=(0.55, 0.75, 1.0), em=2.0)
    M["glow_portal"] = mat("M_ExitMirrorPortal", (0.9, 1, 0.95), metallic=1, rough=0.05, emission=(0.65, 1.0, 0.8), em=3)
    M["neon_dead"] = mat("M_NeonDead", (0.15, 0.17, 0.15), rough=0.2, transmission=0.5)
    M["lens"] = mat("M_LensGlass", (0.01, 0.02, 0.015), rough=0.02, coat=1.0, ior=1.6)
    return M


# ------------------------------------------------------------------ parts
_parts = []


def _take(o, material=None, smooth=False):
    if material is not None and o.data is not None and hasattr(o.data, "materials"):
        o.data.materials.clear()
        o.data.materials.append(material)
    if smooth and o.type == "MESH":
        for p in o.data.polygons:
            p.use_smooth = True
        if hasattr(o.data, "set_sharp_from_angle"):
            o.data.set_sharp_from_angle(angle=DEG(40))
    _parts.append(o)
    return o


def mark():
    return len(_parts)


def transform_since(start, loc=(0, 0, 0), rot=(0, 0, 0), scale=1.0):
    """Move/rotate/scale every part created since `mark()` as one group."""
    s = scale if isinstance(scale, (tuple, list)) else (scale, scale, scale)
    M = Matrix.Translation(loc) @ Matrix.Rotation(rot[2], 4, "Z") @ Matrix.Rotation(rot[1], 4, "Y") @ \
        Matrix.Rotation(rot[0], 4, "X") @ Matrix.Diagonal((*s, 1))
    bpy.context.view_layer.update()
    for o in _parts[start:]:
        o.matrix_world = M @ o.matrix_world


def place(fn, loc=(0, 0, 0), rot=(0, 0, 0), scale=1.0, **kw):
    st = mark()
    out = fn(**kw)
    transform_since(st, loc, rot, scale)
    return out


def bevel(o, w=0.005, segs=2, angle=40):
    m = o.modifiers.new("Bevel", "BEVEL")
    m.width = w
    m.segments = segs
    m.limit_method = "ANGLE"
    m.angle_limit = DEG(angle)
    m.harden_normals = False
    o.modifiers.new("WN", "WEIGHTED_NORMAL").keep_sharp = True
    return o


def box(size, loc=(0, 0, 0), rot=(0, 0, 0), m=None, bev=0.0, segs=2):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    o = bpy.context.object
    o.scale = size
    bpy.ops.object.transform_apply(scale=True)
    if bev:
        bevel(o, bev, segs)
    return _take(o, m)


def cyl(r, depth, loc=(0, 0, 0), rot=(0, 0, 0), m=None, verts=32, bev=0.0, r2=None, cap=True):
    if r2 is None:
        bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=depth, location=loc, rotation=rot,
                                            vertices=verts, end_fill_type="NGON" if cap else "NOTHING")
    else:
        bpy.ops.mesh.primitive_cone_add(radius1=r, radius2=r2, depth=depth, location=loc, rotation=rot,
                                        vertices=verts, end_fill_type="NGON" if cap else "NOTHING")
    o = bpy.context.object
    if bev:
        bevel(o, bev, 2)
    return _take(o, m, smooth=True)


def sphere(r, loc=(0, 0, 0), scale=(1, 1, 1), m=None, segs=32, rings=16, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=loc, segments=segs, ring_count=rings, rotation=rot)
    o = bpy.context.object
    o.scale = scale
    bpy.ops.object.transform_apply(scale=True)
    return _take(o, m, smooth=True)


def torus(R, r, loc=(0, 0, 0), rot=(0, 0, 0), m=None, major=48, minor=12, scale=None):
    bpy.ops.mesh.primitive_torus_add(major_radius=R, minor_radius=r, location=loc, rotation=rot,
                                     major_segments=major, minor_segments=minor)
    o = bpy.context.object
    if scale:
        o.scale = scale
        bpy.ops.object.transform_apply(scale=True)
    return _take(o, m, smooth=True)


def tube(points, r, m=None, res=6, kind="NURBS", taper=None):
    """Round tube through 3D points (wires, cables, legs, rails)."""
    cu = bpy.data.curves.new("tube", "CURVE")
    cu.dimensions = "3D"
    cu.bevel_depth = r
    cu.bevel_resolution = max(1, res // 2)
    cu.use_fill_caps = True
    cu.resolution_u = 8
    if kind == "POLY":
        sp = cu.splines.new("POLY")
        sp.points.add(len(points) - 1)
        for p, co in zip(sp.points, points):
            p.co = (*co, 1)
    else:
        sp = cu.splines.new("NURBS")
        sp.points.add(len(points) - 1)
        for p, co in zip(sp.points, points):
            p.co = (*co, 1)
        sp.use_endpoint_u = True
        sp.order_u = min(4, len(points))
    o = bpy.data.objects.new("tube", cu)
    link(o)
    if m:
        cu.materials.append(m)
    _parts.append(o)
    return o


def text(body, size, loc=(0, 0, 0), rot=(DEG(90), 0, 0), m=None, depth=0.0015, align="CENTER",
         kind="sign", bevel_d=0.0):
    """3D text. Default orientation: readable from -Y (front)."""
    cu = bpy.data.curves.new("txt", "FONT")
    cu.body = body
    cu.size = size
    cu.extrude = depth
    cu.align_x = align
    cu.align_y = "CENTER"
    cu.bevel_depth = bevel_d
    cu.resolution_u = 3          # low curve resolution keeps 3D text game-friendly
    f = font(FONT_3D.get(kind, kind))
    if f:
        cu.font = f
    o = bpy.data.objects.new("txt", cu)
    o.location = loc
    o.rotation_euler = rot
    link(o)
    if m:
        cu.materials.append(m)
    _parts.append(o)
    return o


def neon_text(body, size, loc=(0, 0, 0), m=None, tube_r=0.006, kind="sign", dead_index=None,
              dead_m=None, gap=0.08):
    """Neon tubes following the letter outlines, one object per letter.
    dead_index = index of a letter drawn with dead_m (a broken tube)."""
    x = 0.0
    objs = []
    f = font(kind)
    for i, ch in enumerate(body):
        if ch == " ":
            x += size * 0.35
            continue
        cu = bpy.data.curves.new("n", "FONT")
        cu.body = ch
        cu.size = size
        if f:
            cu.font = f
        o = bpy.data.objects.new("n", cu)
        link(o)
        bpy.context.view_layer.update()
        w = o.dimensions.x
        bpy.ops.object.select_all(action="DESELECT")
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
        bpy.ops.object.convert(target="CURVE")
        o = bpy.context.object
        o.data.dimensions = "3D"
        o.data.fill_mode = "FULL"
        o.data.bevel_depth = tube_r
        o.data.bevel_resolution = 2
        o.data.resolution_u = 6
        mm = dead_m if (dead_index is not None and i == dead_index and dead_m) else m
        o.data.materials.clear()
        if mm:
            o.data.materials.append(mm)
        objs.append((o, x))
        _parts.append(o)
        x += w + size * gap
    total = x - size * gap
    # centre the word on loc; letters stand up facing -Y
    for o, xi in objs:
        o.matrix_world = Matrix.Translation(loc) @ Matrix.Rotation(DEG(90), 4, "X") @ Matrix.Translation((xi - total / 2, 0, 0))
    return total


def lathe(profile, segs=32, m=None, loc=(0, 0, 0), rot=(0, 0, 0), cap_bottom=False, cap_top=False,
          smooth=True, solid=0.0):
    """Surface of revolution around Z from [(radius, z), ...] (bottom to top)."""
    bm = bmesh.new()
    rings = []
    for (r, z) in profile:
        rings.append([bm.verts.new((r * math.cos(2 * math.pi * i / segs), r * math.sin(2 * math.pi * i / segs), z))
                      for i in range(segs)])
    for j in range(len(rings) - 1):
        for i in range(segs):
            a, b2 = rings[j][i], rings[j][(i + 1) % segs]
            c, d = rings[j + 1][(i + 1) % segs], rings[j + 1][i]
            bm.faces.new((a, b2, c, d))
    if cap_bottom:
        bm.faces.new(list(reversed(rings[0])))
    if cap_top:
        bm.faces.new(rings[-1])
    me = bpy.data.meshes.new("lathe")
    bm.to_mesh(me)
    bm.free()
    o = link(bpy.data.objects.new("lathe", me))
    o.location = loc
    o.rotation_euler = rot
    if solid:
        s = o.modifiers.new("Solid", "SOLIDIFY")
        s.thickness = solid
        s.offset = -1
    _take(o, m, smooth=smooth)
    return o


def arc(cx, cz, r, a0, a1, n):
    return [(cx + r * math.cos(DEG(a0 + (a1 - a0) * i / (n - 1))), cz + r * math.sin(DEG(a0 + (a1 - a0) * i / (n - 1))))
            for i in range(n)]


def slab(outline, depth, loc=(0, 0, 0), rot=(0, 0, 0), m=None, bev=0.0, segs=2):
    """Flat shape from a 2D outline [(x, z), ...] extruded along Y (centred)."""
    bm = bmesh.new()
    vs = [bm.verts.new((x, -depth / 2, z)) for (x, z) in outline]
    f = bm.faces.new(vs)
    ext = bmesh.ops.extrude_face_region(bm, geom=[f])
    nv = [e for e in ext["geom"] if isinstance(e, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, vec=(0, depth, 0), verts=nv)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new("slab")
    bm.to_mesh(me)
    bm.free()
    o = link(bpy.data.objects.new("slab", me))
    o.location = loc
    o.rotation_euler = rot
    if bev:
        bevel(o, bev, segs)
    return _take(o, m)


def skin_body(verts, edges, radii, m=None, levels=2):
    """Organic body from a stick skeleton (Skin + Subdivision modifiers)."""
    me = bpy.data.meshes.new("body")
    me.from_pydata(verts, edges, [])
    o = link(bpy.data.objects.new("body", me))
    o.modifiers.new("Skin", "SKIN")
    if len(me.skin_vertices) == 0:
        me.skin_vertices.new()
    for i, r in enumerate(radii):
        me.skin_vertices[0].data[i].radius = r if isinstance(r, (tuple, list)) else (r, r)
    me.skin_vertices[0].data[0].use_root = True
    sub = o.modifiers.new("Sub", "SUBSURF")
    sub.levels = sub.render_levels = levels
    return _take(o, m, smooth=True)


def delete_verts(o, pred):
    """Delete vertices of mesh object o where pred(co) is True (object space)."""
    bpy.context.view_layer.objects.active = o
    bpy.ops.object.select_all(action="DESELECT")
    o.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode="OBJECT")
    for v in o.data.vertices:
        v.select = pred(v.co)
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.delete(type="VERT")
    bpy.ops.object.mode_set(mode="OBJECT")


def dent(o, centre, radius, depth):
    c = Vector(centre)
    for v in o.data.vertices:
        d = (v.co - c).length
        if d < radius:
            f = (1 - d / radius) ** 2
            v.co -= v.normal * depth * f


# ------------------------------------------------------------------ finishing / export

def _bake_parts():
    """Evaluate modifiers/curves/text of every pending part into plain mesh objects."""
    dg = bpy.context.evaluated_depsgraph_get()
    out = []
    for o in _parts:
        me = bpy.data.meshes.new_from_object(o.evaluated_get(dg), preserve_all_data_layers=False, depsgraph=dg)
        if not me.materials and hasattr(o.data, "materials"):
            for mm in o.data.materials:
                me.materials.append(mm)
        # exactly one UV layer called UVMap (keeps the FBX clean for Unreal)
        while len(me.uv_layers) > 1:
            me.uv_layers.remove(me.uv_layers[-1])
        if len(me.uv_layers) == 0:
            me.uv_layers.new(name="UVMap")
        me.uv_layers[0].name = "UVMap"
        no = link(bpy.data.objects.new(o.name + "_m", me))
        no.matrix_world = o.matrix_world.copy()
        out.append(no)
    for o in _parts:
        bpy.data.objects.remove(o, do_unlink=True)
    _parts.clear()
    return out


def finish(name, origin="bottom", uv=True):
    """Join pending parts into SM_<name>. origin: 'bottom' (bottom centre) or 'world' (keep 0,0,0)."""
    meshes = _bake_parts()
    bpy.ops.object.select_all(action="DESELECT")
    for o in meshes:
        o.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    if len(meshes) > 1:
        bpy.ops.object.join()
    o = bpy.context.object
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    o.name = o.data.name = "SM_" + name
    if origin == "bottom":
        co = [v.co for v in o.data.vertices]
        mn = Vector((min(v.x for v in co), min(v.y for v in co), min(v.z for v in co)))
        mx = Vector((max(v.x for v in co), max(v.y for v in co), max(v.z for v in co)))
        shift = Vector(((mn.x + mx.x) / 2, (mn.y + mx.y) / 2, mn.z))
        for v in o.data.vertices:
            v.co -= shift
    o.location = (0, 0, 0)
    if uv:
        bpy.ops.object.select_all(action="DESELECT")
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        try:
            bpy.ops.uv.smart_project(angle_limit=DEG(66), island_margin=0.01)
        except Exception as e:  # never block a build on UVs
            print("UV warning", name, e)
        bpy.ops.object.mode_set(mode="OBJECT")
    return o


def tri_count(o):
    return sum(len(p.vertices) - 2 for p in o.data.polygons)


def export(o, folder):
    os.makedirs(folder, exist_ok=True)
    bpy.ops.object.select_all(action="DESELECT")
    o.hide_set(False)
    o.select_set(True)
    bpy.context.view_layer.objects.active = o
    base = os.path.join(folder, o.name)
    bpy.ops.export_scene.fbx(filepath=base + ".fbx", use_selection=True, object_types={"MESH"},
                             apply_scale_options="FBX_SCALE_UNITS", mesh_smooth_type="FACE",
                             add_leaf_bones=False, path_mode="AUTO", use_tspace=True)
    bpy.ops.export_scene.gltf(filepath=base + ".glb", use_selection=True, export_format="GLB",
                              export_apply=True)


# ------------------------------------------------------------------ render helpers

def cycles(samples=32, w=1280, h=720, look="AgX - Medium High Contrast", denoise=True):
    s = bpy.context.scene
    s.render.engine = "CYCLES"
    s.cycles.device = "CPU"
    s.cycles.samples = samples
    s.cycles.use_adaptive_sampling = True
    s.cycles.adaptive_threshold = 0.03
    s.cycles.use_denoising = denoise
    s.cycles.max_bounces = 6
    s.cycles.diffuse_bounces = 3
    s.cycles.glossy_bounces = 3
    s.cycles.transmission_bounces = 6
    s.cycles.volume_bounces = 0
    s.cycles.caustics_reflective = False
    s.cycles.caustics_refractive = False
    s.cycles.blur_glossy = 1.0
    s.render.resolution_x = w
    s.render.resolution_y = h
    s.render.resolution_percentage = 100
    s.render.film_transparent = False
    s.view_settings.view_transform = "AgX"
    try:
        s.view_settings.look = look
    except TypeError:
        pass
    s.render.image_settings.file_format = "PNG"


def world(color=(0.003, 0.008, 0.005), strength=1.0, fog=0.0, fog_color=(0.5, 0.9, 0.6), anisotropy=0.3):
    s = bpy.context.scene
    w = bpy.data.worlds.new("World")
    s.world = w
    w.use_nodes = True
    nt = w.node_tree
    bg = nt.nodes["Background"]
    bg.inputs["Color"].default_value = (*color, 1)
    bg.inputs["Strength"].default_value = strength
    if fog:
        out = nt.nodes["World Output"]
        v = nt.nodes.new("ShaderNodeVolumePrincipled")
        v.inputs["Density"].default_value = fog
        v.inputs["Color"].default_value = (*fog_color, 1)
        v.inputs["Anisotropy"].default_value = anisotropy
        nt.links.new(v.outputs[0], out.inputs["Volume"])
        s.cycles.volume_step_rate = 4.0
        s.cycles.volume_max_steps = 128
    return w


def area_light(loc, target, energy, size=1.0, color=(1, 1, 1), shape="SQUARE", size_y=None):
    bpy.ops.object.light_add(type="AREA", location=loc)
    l = bpy.context.object
    l.data.energy = energy
    l.data.shape = shape if size_y is None else "RECTANGLE"
    l.data.size = size
    if size_y is not None:
        l.data.size_y = size_y
    l.data.color = color
    aim(l, target)
    return l


def point_light(loc, energy, color=(1, 1, 1), radius=0.1):
    bpy.ops.object.light_add(type="POINT", location=loc)
    l = bpy.context.object
    l.data.energy = energy
    l.data.color = color
    l.data.shadow_soft_size = radius
    return l


def spot_light(loc, target, energy, color=(1, 1, 1), angle=35, blend=0.3, radius=0.05):
    bpy.ops.object.light_add(type="SPOT", location=loc)
    l = bpy.context.object
    l.data.energy = energy
    l.data.color = color
    l.data.spot_size = DEG(angle)
    l.data.spot_blend = blend
    l.data.shadow_soft_size = radius
    aim(l, target)
    return l


def sun_light(direction_target, energy, color=(1, 1, 1), angle=2.0):
    bpy.ops.object.light_add(type="SUN", location=(0, 0, 10))
    l = bpy.context.object
    l.data.energy = energy
    l.data.color = color
    l.data.angle = DEG(angle)
    aim(l, direction_target)
    return l


def aim(obj, target):
    d = Vector(target) - obj.location
    obj.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()


def camera(loc, target, lens=24, name="Cam"):
    bpy.ops.object.camera_add(location=loc)
    c = bpy.context.object
    c.name = name
    c.data.lens = lens
    c.data.clip_start = 0.02
    c.data.clip_end = 400
    aim(c, target)
    bpy.context.scene.camera = c
    return c


def render(path):
    s = bpy.context.scene
    s.render.filepath = path
    bpy.ops.render.render(write_still=True)
