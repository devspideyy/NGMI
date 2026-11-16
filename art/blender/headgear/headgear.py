"""NGMI — "The Headgear" enemy, built procedurally in Blender (bpy).

A floating reverse-pull orthodontic face mask: forehead pad, central rod,
cross-bar with hooks, chin cup, and taut rubber bands stretching to the walls.
Outputs:
  out/headgear_render.png   preview render (Cycles, eerie green lighting)
  out/SM_Headgear.fbx       for Unreal Engine 5 (static mesh)
  out/SM_Headgear.glb       glTF copy (Blender/web preview)
Run:  python3 headgear.py
"""
import math
import os

import bpy
from mathutils import Vector

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)

# ---------- clean scene ----------
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene


def mat(name, color, metallic=0.0, rough=0.5, transmission=0.0, emission=None, em_strength=0.0, alpha=1.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Metallic"].default_value = metallic
    b.inputs["Roughness"].default_value = rough
    if transmission:
        b.inputs["Transmission Weight"].default_value = transmission
    if emission:
        b.inputs["Emission Color"].default_value = (*emission, 1)
        b.inputs["Emission Strength"].default_value = em_strength
    if alpha < 1:
        b.inputs["Alpha"].default_value = alpha
    return m


M_METAL = mat("M_Headgear_Steel", (0.62, 0.64, 0.62), metallic=1.0, rough=0.28)
M_RUST = mat("M_Headgear_RustSteel", (0.36, 0.22, 0.13), metallic=0.7, rough=0.65)
M_PAD = mat("M_Headgear_Pad", (0.78, 0.72, 0.60), rough=0.8)
M_BAND = mat("M_Headgear_Band", (0.95, 0.85, 0.55), rough=0.35, transmission=0.6)
M_WALL = mat("M_Wall", (0.018, 0.022, 0.018), rough=0.95)
M_RING = mat("M_RingLight", (0.02, 0.1, 0.04), emission=(0.27, 1.0, 0.52), em_strength=25)

parts = []


def add(obj, material):
    obj.data.materials.append(material)
    parts.append(obj)
    return obj


def bevel(obj, width=0.01, segs=3):
    m = obj.modifiers.new("Bevel", "BEVEL")
    m.width = width
    m.segments = segs
    obj.modifiers.new("WN", "WEIGHTED_NORMAL")


# ---------- the mask ----------
# Forehead pad: flattened, curved rounded block
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.62))
pad = bpy.context.object
pad.name = "ForeheadPad"
pad.scale = (0.30, 0.07, 0.11)
bpy.ops.object.transform_apply(scale=True)
sd = pad.modifiers.new("Bend", "SIMPLE_DEFORM")
sd.deform_method = "BEND"
sd.deform_axis = "Z"
sd.angle = math.radians(-35)
bevel(pad, 0.03, 4)
add(pad, M_PAD)

# Chin cup: half sphere, opening up toward the face
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.13, location=(0, 0.02, -0.38), segments=40, ring_count=20)
chin = bpy.context.object
chin.name = "ChinCup"
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="DESELECT")
bpy.ops.object.mode_set(mode="OBJECT")
for v in chin.data.vertices:
    v.select = v.co.y > 0.01
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.delete(type="VERT")
bpy.ops.object.mode_set(mode="OBJECT")
chin.scale = (1.15, 1.0, 0.8)
sol = chin.modifiers.new("Thick", "SOLIDIFY")
sol.thickness = 0.015
chin.modifiers.new("Smooth", "SUBSURF").levels = 2
add(chin, M_PAD)

# Central rod (slightly rusted steel), forehead -> chin
bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.90, location=(0, -0.15, 0.16), vertices=24)
rod = bpy.context.object
rod.name = "CentralRod"
add(rod, M_RUST)

# Cross-bar at mouth height, bowed forward
bpy.ops.curve.primitive_bezier_curve_add(location=(0, 0, 0))
bar = bpy.context.object
bar.name = "CrossBar"
sp = bar.data.splines[0]
sp.bezier_points[0].co = (-0.24, -0.04, 0.0)
sp.bezier_points[0].handle_left = (-0.30, -0.02, 0.0)
sp.bezier_points[0].handle_right = (-0.12, -0.16, 0.0)
sp.bezier_points[1].co = (0.24, -0.04, 0.0)
sp.bezier_points[1].handle_left = (0.12, -0.16, 0.0)
sp.bezier_points[1].handle_right = (0.30, -0.02, 0.0)
bar.data.bevel_depth = 0.011
bar.data.bevel_resolution = 4
bar.data.use_fill_caps = True
bar.data.materials.append(M_METAL)
bpy.ops.object.convert(target="MESH")
bar = bpy.context.object
parts.append(bar)

# Clamp where bar meets rod
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -0.15, 0.0))
clamp = bpy.context.object
clamp.name = "Clamp"
clamp.scale = (0.05, 0.035, 0.06)
bpy.ops.object.transform_apply(scale=True)
bevel(clamp, 0.006, 2)
add(clamp, M_METAL)

# Hooks at each end of the cross-bar (small J shapes)
hook_tips = []
for side in (-1, 1):
    bpy.ops.mesh.primitive_torus_add(major_radius=0.03, minor_radius=0.006,
                                     location=(side * 0.26, -0.03, -0.02),
                                     rotation=(0, math.radians(90), 0))
    h = bpy.context.object
    h.name = f"Hook_{'L' if side < 0 else 'R'}"
    add(h, M_METAL)
    hook_tips.append(Vector((side * 0.26, -0.03, -0.05)))

# Adjustment screws on the rod
for z in (0.42, -0.18):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.022, depth=0.04, location=(0, -0.165, z),
                                        rotation=(math.radians(90), 0, 0), vertices=6)
    s = bpy.context.object
    s.name = f"Screw_{z}"
    add(s, M_METAL)

# ---------- rubber bands: from hooks, stretched taut to the walls ----------
anchors = [Vector((-1.9, 1.6, 0.9)), Vector((-1.9, 1.2, -1.1)), Vector((1.9, 1.5, 1.0)), Vector((1.9, 1.3, -0.9))]
for i, a in enumerate(anchors):
    tip = hook_tips[0] if a.x < 0 else hook_tips[1]
    bpy.ops.curve.primitive_bezier_curve_add(location=(0, 0, 0))
    c = bpy.context.object
    c.name = f"Band_{i}"
    p = c.data.splines[0].bezier_points
    p[0].co = tip
    p[1].co = a
    for bp in p:
        bp.handle_left_type = bp.handle_right_type = "VECTOR"
    c.data.bevel_depth = 0.004
    c.data.bevel_resolution = 2
    c.data.materials.append(M_BAND)
    bpy.ops.object.convert(target="MESH")
    parts.append(bpy.context.object)

# ---------- join the enemy into one mesh, centred ----------
bpy.ops.object.select_all(action="DESELECT")
for o in parts:
    o.select_set(True)
bpy.context.view_layer.objects.active = parts[0]
for o in parts:
    bpy.context.view_layer.objects.active = o
    for m in list(o.modifiers):
        bpy.ops.object.modifier_apply(modifier=m.name)
bpy.context.view_layer.objects.active = parts[0]
bpy.ops.object.join()
headgear = bpy.context.object
headgear.name = "SM_Headgear"
bpy.ops.object.shade_smooth()
tri = sum(len(p.vertices) - 2 for p in headgear.data.polygons)

# ---------- export for UE5 (before adding the preview set) ----------
bpy.ops.object.select_all(action="DESELECT")
headgear.select_set(True)
bpy.ops.export_scene.fbx(filepath=os.path.join(OUT, "SM_Headgear.fbx"), use_selection=True,
                         apply_scale_options="FBX_SCALE_UNITS", mesh_smooth_type="FACE",
                         axis_forward="-Z", axis_up="Y")
bpy.ops.export_scene.gltf(filepath=os.path.join(OUT, "SM_Headgear.glb"), use_selection=True)

# ---------- preview set: dark corridor, green ring light, fog ----------
bpy.ops.mesh.primitive_plane_add(size=8, location=(0, 2.0, 0), rotation=(math.radians(90), 0, 0))
add(bpy.context.object, M_WALL)
bpy.ops.mesh.primitive_plane_add(size=8, location=(0, 0, -1.6))
add(bpy.context.object, M_WALL)
for x in (-2.0, 2.0):
    bpy.ops.mesh.primitive_plane_add(size=8, location=(x, 0, 0), rotation=(0, math.radians(90), 0))
    add(bpy.context.object, M_WALL)
bpy.ops.mesh.primitive_torus_add(major_radius=0.35, minor_radius=0.02, location=(0, 0.6, 1.9))
add(bpy.context.object, M_RING)

# key light from above (green), cold rim from behind, faint fill
bpy.ops.object.light_add(type="AREA", location=(0, -0.2, 1.7))
k = bpy.context.object
k.data.energy = 70
k.data.color = (0.35, 1.0, 0.55)
k.data.size = 0.5
bpy.ops.object.light_add(type="SPOT", location=(0.9, 1.6, 1.0))
r = bpy.context.object
r.data.energy = 600
r.data.color = (0.6, 1.0, 0.8)
r.data.spot_size = math.radians(40)
r.rotation_euler = (math.radians(-60), math.radians(30), math.radians(160))
bpy.ops.object.light_add(type="POINT", location=(-0.6, -1.5, -0.4))
f = bpy.context.object
f.data.energy = 3
f.data.color = (0.7, 0.85, 0.75)
bpy.ops.object.light_add(type="POINT", location=(0, -0.7, -1.1))
u = bpy.context.object
u.data.energy = 25
u.data.color = (0.2, 1.0, 0.4)

# volumetric haze
world = bpy.data.worlds.new("W")
scene.world = world
world.use_nodes = True
nt = world.node_tree
bg = nt.nodes["Background"]
bg.inputs["Color"].default_value = (0.004, 0.01, 0.005, 1)
vol = nt.nodes.new("ShaderNodeVolumePrincipled")
vol.inputs["Density"].default_value = 0.012
vol.inputs["Color"].default_value = (0.5, 1.0, 0.6, 1)
nt.links.new(vol.outputs["Volume"], nt.nodes["World Output"].inputs["Volume"])

# camera: slightly low, three-quarter, looking up at it
bpy.ops.object.camera_add(location=(0.9, -2.35, -0.05))
cam = bpy.context.object
direction = Vector((0, 0.0, 0.1)) - cam.location
cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
cam.data.lens = 38
scene.camera = cam

scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = 96
scene.cycles.use_denoising = True
scene.render.resolution_x = 1280
scene.render.resolution_y = 800
scene.view_settings.view_transform = "AgX"
scene.view_settings.look = "AgX - Punchy"
scene.render.filepath = os.path.join(OUT, "headgear_render.png")
bpy.ops.render.render(write_still=True)

print(f"SM_Headgear triangles: {tri}")
for fn in sorted(os.listdir(OUT)):
    print(fn, os.path.getsize(os.path.join(OUT, fn)), "bytes")
