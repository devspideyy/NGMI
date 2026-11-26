"""NGMI — prop pack v2 (Blender 5.x, bpy). Run:  python3 props.py [--no-render] [--only Name,Name]

Builds every in-house prop at real-world scale, joins each into SM_<Name>,
exports FBX (Unreal) + GLB, then renders a thumbnail per prop and contact
sheets grouped by floor. Outputs go to ./out/props/.
All content is fictional. No real brands, people or likenesses.
"""
import math
import os
import random
import sys

import bpy
from mathutils import Matrix, Vector

import ngmi_kit as K
from ngmi_kit import (DEG, arc, box, cyl, lathe, mark, neon_text, place, skin_body, slab, sphere,
                      text, torus, transform_since, tube)

OUT = os.path.join(K.HERE, "out", "props")
MODELS = os.path.join(OUT, "models")
THUMBS = os.path.join(OUT, "thumbs")
M = {}


def extra_mats():
    M["band"] = K.mat("M_RubberBand", (0.95, 0.85, 0.55), rough=0.35, transmission=0.6)
    M["water"] = K.mat("M_WaterBottle", (0.62, 0.85, 0.78), rough=0.05, transmission=0.95, ior=1.33)
    M["ui"] = K.mat("M_UIWhite", (1, 1, 1), emission=(0.9, 0.95, 1.0), em=3)
    M["notif"] = K.mat("M_NotificationWhite", (0.82, 0.85, 0.84), rough=0.3, coat=0.5, wear=K.W_LIGHT)
    M["grey_text"] = K.mat("M_TextGrey", (0.3, 0.32, 0.31), rough=0.6)
    M["flower_pink"] = K.mat("M_FlowerPink", (0.9, 0.3, 0.45), rough=0.6, sss=0.3)
    M["flower_yellow"] = K.mat("M_FlowerYellow", (0.95, 0.75, 0.15), rough=0.6, sss=0.3)
    M["leaf"] = K.mat("M_Leaf", (0.12, 0.3, 0.08), rough=0.6, sss=0.2)
    M["mouth"] = K.mat("M_MouthDark", (0.08, 0.01, 0.015), rough=0.4)
    M["tooth"] = K.mat("M_Tooth", (0.85, 0.84, 0.76), rough=0.25, sss=0.2)
    M["foil"] = K.mat("M_FoilPink", (0.85, 0.55, 0.62), metallic=0.8, rough=0.25, wear=K.W_PLASTIC)
    M["cover_a"] = K.mat("M_MagCoverRed", (0.6, 0.08, 0.08), rough=0.3, wear=K.W_PAINT)
    M["cover_b"] = K.mat("M_MagCoverTeal", (0.05, 0.35, 0.35), rough=0.3, wear=K.W_PAINT)
    M["cover_c"] = K.mat("M_MagCoverYellow", (0.85, 0.7, 0.1), rough=0.3, wear=K.W_PAINT)
    M["skin_care"] = K.mat("M_BottleWhite", (0.85, 0.85, 0.82), rough=0.25, coat=0.4, wear=K.W_PLASTIC)
    M["serum"] = K.mat("M_SerumAmber", (0.7, 0.35, 0.05), rough=0.05, transmission=0.9, ior=1.5)
    M["spf"] = K.mat("M_SPFOrange", (0.95, 0.5, 0.1), rough=0.3, wear=K.W_PLASTIC)
    M["toner"] = K.mat("M_TonerBlue", (0.5, 0.75, 0.95), rough=0.05, transmission=0.85, ior=1.4)
    M["tape_line"] = K.mat("M_TapeWhiteLine", (0.8, 0.8, 0.78), rough=0.6, wear=K.W_PAINT)


# =================================================================== ORTHODONTIC HORROR

def p_palate_expander():
    for s in (-1, 1):
        sphere(0.016, loc=(s * 0.0105, 0, 0.004), scale=(0.75, 1.25, 0.28), m=M["acrylic"])
    box((0.013, 0.011, 0.005), loc=(0, 0, 0.0075), m=M["steel"], bev=0.0012)
    box((0.0012, 0.006, 0.0004), loc=(0, 0, 0.0101), m=M["ink"])  # turn arrow
    cyl(0.0019, 0.024, loc=(0, 0, 0.0075), rot=(0, DEG(90), 0), m=M["steel"], verts=16)
    cyl(0.0012, 0.002, loc=(0, 0.002, 0.0101), m=M["black_plastic"], verts=12)
    for sx in (-1, 1):  # MSE-style mini-screw sleeves
        for sy in (-1, 1):
            cyl(0.0016, 0.004, loc=(sx * 0.0065, sy * 0.0045, 0.0085), m=M["steel"], verts=12)
            cyl(0.0008, 0.0065, loc=(sx * 0.0065, sy * 0.0045, 0.0105), m=M["chrome"], verts=10)
    for s in (-1, 1):
        for y in (-0.012, 0.012):
            tube([(s * 0.005, y * 0.35, 0.0075), (s * 0.012, y * 0.8, 0.0085), (s * 0.0205, y, 0.0065)], 0.0009, M["steel"])
            lathe([(0.0046, 0.0035), (0.0046, 0.009)], 20, M["steel"], loc=(s * 0.0235, y, 0), solid=0.0006)


def p_expander_key():
    box((0.012, 0.004, 0.035), loc=(0, 0, 0.0175), m=M["teal_plastic"], bev=0.003, segs=3)
    for i in range(5):
        box((0.0125, 0.0046, 0.0012), loc=(0, 0, 0.006 + i * 0.004), m=M["teal_plastic"])
    tube([(0, 0, 0.034), (0, 0, 0.06), (0, -0.004, 0.066), (0, -0.012, 0.068)], 0.0007, M["steel"])


def p_specimen_jar():
    lathe([(0.048, 0.0), (0.055, 0.006), (0.056, 0.02), (0.056, 0.15), (0.052, 0.165), (0.046, 0.172), (0.046, 0.182)],
          48, M["glass"], cap_bottom=True, solid=0.003)
    lathe([(0.051, 0.004), (0.052, 0.02), (0.052, 0.13)], 48, M["jar_liquid"], cap_bottom=True, cap_top=True)
    lathe([(0.05, 0.176), (0.05, 0.2), (0.044, 0.205)], 48, M["rust"], cap_top=True, solid=0.003)
    for z in (0.182, 0.19, 0.197):
        torus(0.0505, 0.0016, loc=(0, 0, z), m=M["rust"], major=48, minor=6)
    lathe([(0.0566, 0.04), (0.0566, 0.085)], 48, M["paper"], solid=0.0008)
    text("No. 0451", 0.011, loc=(0, -0.0575, 0.071), m=M["ink"], kind="notice")
    text("FORWARD", 0.011, loc=(0, -0.0575, 0.055), m=M["ink"], kind="notice")
    sphere(0.04, loc=(0, 0, 0.006), scale=(1, 1, 0.1), m=M["moss"])
    st = mark()
    p_palate_expander()
    transform_since(st, loc=(0, 0.004, 0.058), rot=(DEG(72), DEG(12), 0), scale=1.5)


def p_expander_spider():
    H = 0.2
    for s in (-1, 1):
        sphere(0.085, loc=(s * 0.05, 0, H), scale=(0.72, 1.15, 0.32), m=M["acrylic"])
    box((0.062, 0.05, 0.03), loc=(0, 0, H + 0.012), m=M["rust"], bev=0.005)
    cyl(0.009, 0.13, loc=(0, 0, H + 0.012), rot=(0, DEG(90), 0), m=M["steel_dirty"], verts=16)
    cyl(0.009, 0.006, loc=(0, 0, H + 0.029), m=M["black_plastic"], verts=16)
    cyl(0.0045, 0.004, loc=(0, 0, H + 0.032), m=M["glow_green"], verts=12)  # the keyhole "eye"
    for i in range(8):
        side = -1 if i < 4 else 1
        k = i % 4
        y = -0.075 + k * 0.05
        spread = -0.07 + k * 0.045
        hip = Vector((side * 0.085, y, H))
        knee = Vector((side * 0.2, y + spread, H + 0.11))
        foot = Vector((side * 0.3, y + spread * 1.8, 0.012))
        for a, b in ((hip, knee), (knee, foot)):
            d = b - a
            rot = d.to_track_quat("Z", "Y").to_euler()
            cyl(0.0062, d.length, loc=(a + b) / 2, rot=rot, m=M["steel_dirty"], verts=10)
            n = int(d.length / 0.014)
            for t in range(1, n):
                torus(0.0072, 0.0018, loc=a + d * (t / n), rot=rot, m=M["steel_dirty"], major=10, minor=4)
        sphere(0.013, loc=knee, m=M["rust"], segs=12, rings=8)
        sphere(0.011, loc=hip, m=M["rust"], segs=12, rings=8)
        lathe([(0.014, 0.0), (0.014, 0.012)], 14, M["rust"], loc=foot - Vector((0, 0, 0.012)), solid=0.002)
    for s in (-1, 1):
        tube([(s * 0.02, -0.1, H - 0.01), (s * 0.03, -0.15, H - 0.03), (s * 0.018, -0.165, H - 0.075)], 0.003, M["chrome"])


def _arch_teeth(mat_key, z0=0.0, flip=False):
    W = [0.0042, 0.0036, 0.0041, 0.0037, 0.0037, 0.005, 0.0052]
    D = [0.003, 0.003, 0.0038, 0.0042, 0.0042, 0.005, 0.0052]
    Hh = [0.0058, 0.0052, 0.0062, 0.005, 0.005, 0.0045, 0.0045]
    rx, ry = 0.024, 0.026
    pts = []
    for side in (-1, 1):
        for j in range(7):
            ang = side * DEG(8 + j * 13.5)
            x, y = rx * math.sin(ang), -ry * math.cos(ang)
            phi = math.atan2(ry * math.sin(ang), rx * math.cos(ang))
            zc = z0 + (-1 if flip else 1) * Hh[j] * 0.9
            sphere(1.0, loc=(x, y, zc), scale=(W[j] * 1.3, D[j] * 1.45, Hh[j] * 1.15), rot=(0, 0, phi),
                   m=M[mat_key], segs=16, rings=10)
            pts.append((x, y, z0 + (-0.002 if flip else 0.002)))
    pts.sort(key=lambda p: math.atan2(p[0], -p[1]))
    tube(pts, 0.0028, M[mat_key])


def p_retainer():
    _arch_teeth("clear")


def p_chatterer_base():
    st = mark()
    _arch_teeth("clear", z0=0.0)
    for s in (-1, 1):  # little orange wind-up feet
        sphere(1.0, loc=(s * 0.011, -0.014, -0.004), scale=(0.006, 0.011, 0.0042), m=M["orange_plastic"], segs=16, rings=8)
    cyl(0.0022, 0.02, loc=(0, 0.012, 0.003), rot=(DEG(90), 0, 0), m=M["steel"], verts=10)
    for s in (-1, 1):
        torus(0.006, 0.0014, loc=(s * 0.006, 0.023, 0.003), rot=(DEG(90), 0, 0), m=M["steel"], major=16, minor=6)
    transform_since(st, scale=3.0)


def p_chatterer_jaw():
    st = mark()
    _arch_teeth("clear", z0=0.0115, flip=True)
    transform_since(st, scale=3.0)


def p_headgear_mask(limp=True):
    pad = box((0.3, 0.07, 0.11), loc=(0, 0, 0.62), m=M["beige_plastic"], bev=0.03, segs=3)
    sd = pad.modifiers.new("Bend", "SIMPLE_DEFORM")
    sd.deform_method, sd.deform_axis, sd.angle = "BEND", "Z", DEG(-35)
    chin = sphere(0.13, loc=(0, 0.02, -0.38), m=M["beige_plastic"], segs=24, rings=12)
    K.delete_verts(chin, lambda co: co.y > 0.01)
    chin.scale = (1.15, 1.0, 0.8)
    chin.modifiers.new("Thick", "SOLIDIFY").thickness = 0.015
    chin.modifiers.new("Sub", "SUBSURF").levels = 1
    cyl(0.012, 0.9, loc=(0, -0.15, 0.16), m=M["rust"], verts=16)
    tube([(-0.24, -0.04, 0), (-0.12, -0.16, 0), (0.12, -0.16, 0), (0.24, -0.04, 0)], 0.011, M["steel"])
    box((0.05, 0.035, 0.06), loc=(0, -0.15, 0.0), m=M["steel"], bev=0.006)
    for s in (-1, 1):
        torus(0.03, 0.006, loc=(s * 0.26, -0.03, -0.02), rot=(0, DEG(90), 0), m=M["steel"], major=20, minor=6)
        if limp:
            tube([(s * 0.26, -0.03, -0.05), (s * 0.28, -0.06, -0.25), (s * 0.25, -0.05, -0.34),
                  (s * 0.23, -0.02, -0.2), (s * 0.26, -0.03, -0.06)], 0.006, M["band"])
    for z in (0.42, -0.18):
        cyl(0.022, 0.04, loc=(0, -0.165, z), rot=(DEG(90), 0, 0), m=M["steel"], verts=6)


def p_headgear_rack():
    box((2.0, 0.04, 0.55), loc=(0, 0.02, 1.75), m=M["wood"], bev=0.01)
    box((2.1, 0.07, 0.06), loc=(0, 0.0, 2.05), m=M["wood"], bev=0.01)
    random.seed(3)
    for i in range(7):
        x = -0.85 + i * 0.283
        tube([(x, 0, 1.8), (x, -0.07, 1.8), (x, -0.085, 1.84)], 0.006, M["steel_dirty"])
        box((0.14, 0.004, 0.04), loc=(x, -0.002, 1.93), m=M["paper"])
        text(f"No. {i + 1}", 0.024, loc=(x, -0.0045, 1.93), m=M["ink"], kind="notice")
        if i != 4:  # hook No. 5 is empty. The Headgear is out there.
            place(p_headgear_mask, loc=(x, -0.09, 1.46), rot=(DEG(6), 0, DEG(random.uniform(-6, 6))), scale=0.5)


def p_dental_chair():
    lathe([(0.34, 0.0), (0.34, 0.03), (0.3, 0.06), (0.12, 0.09), (0.11, 0.4)], 48, M["white_paint"], cap_top=True)
    cyl(0.085, 0.3, loc=(0, 0, 0.5), m=M["steel_dirty"], verts=32)
    lathe([(0.1, 0.36), (0.13, 0.42), (0.13, 0.5)], 32, M["rubber"])
    box((0.55, 0.72, 0.12), loc=(0, 0.05, 0.6), m=M["white_paint"], bev=0.03)
    box((0.5, 0.62, 0.11), loc=(0, 0.05, 0.71), m=M["vinyl"], bev=0.045, segs=4)
    back = box((0.48, 0.11, 0.8), loc=(0, -0.42, 1.06), rot=(DEG(-28), 0, 0), m=M["vinyl"], bev=0.045, segs=4)
    tp = back.modifiers.new("Taper", "SIMPLE_DEFORM")
    tp.deform_method, tp.deform_axis, tp.factor = "TAPER", "Z", -0.25
    box((0.3, 0.1, 0.16), loc=(0, -0.64, 1.5), rot=(DEG(-42), 0, 0), m=M["vinyl_dark"], bev=0.045, segs=4)
    box((0.44, 0.66, 0.1), loc=(0, 0.62, 0.6), rot=(DEG(-22), 0, 0), m=M["vinyl"], bev=0.045, segs=4)
    for s in (-1, 1):
        box((0.075, 0.42, 0.06), loc=(s * 0.31, 0.02, 0.89), m=M["vinyl_dark"], bev=0.025, segs=3)
        cyl(0.015, 0.17, loc=(s * 0.31, 0.02, 0.8), m=M["steel"], verts=16)
    cyl(0.03, 1.55, loc=(0.42, -0.45, 1.22), m=M["steel_dirty"], verts=20)
    tube([(0.42, -0.45, 1.98), (0.3, -0.2, 2.08), (0.1, 0.1, 2.0), (0.0, 0.26, 1.88)], 0.02, M["white_paint"])
    lathe([(0.04, 0.0), (0.17, -0.06), (0.19, -0.11)], 32, M["white_paint"], loc=(0, 0.3, 1.9), rot=(DEG(22), 0, 0), solid=0.01)
    cyl(0.17, 0.01, loc=(0, 0.3 - 0.04, 1.79), rot=(DEG(22), 0, 0), m=M["glow_warm"], verts=32)
    cyl(0.035, 0.9, loc=(-0.45, 0.2, 0.45), m=M["white_paint"], verts=16)
    lathe([(0.04, 0.0), (0.12, 0.05), (0.14, 0.09)], 32, M["ceramic"], loc=(-0.45, 0.2, 0.9), cap_bottom=True, solid=0.008)
    tube([(-0.3, -0.2, 0.62), (-0.45, 0.0, 0.85), (-0.42, 0.25, 0.98)], 0.015, M["steel"])
    box((0.32, 0.22, 0.015), loc=(-0.42, 0.32, 1.0), m=M["steel"], bev=0.005)
    for i in range(4):
        cyl(0.004, 0.15, loc=(-0.52 + i * 0.06, 0.32, 1.013), rot=(DEG(90), 0, DEG(6 * i)), m=M["chrome"], verts=8)
    for i in range(3):
        tube([(-0.3 + i * 0.04, 0.38, 1.0), (-0.28 + i * 0.05, 0.45, 0.8), (-0.2 + i * 0.03, 0.3, 0.55)], 0.006, M["black_plastic"])
    cyl(0.1, 0.035, loc=(0.35, -0.7, 0.018), m=M["steel_dirty"], verts=24, bev=0.006)
    tube([(0.35, -0.6, 0.02), (0.25, -0.35, 0.02), (0.15, -0.1, 0.05)], 0.008, M["black_plastic"])


def p_giant_calipers():
    box((0.14, 0.05, 2.1), loc=(0, 0, 1.05), m=M["steel"], bev=0.004)
    for i in range(42):
        h = 0.06 if i % 5 == 0 else 0.03
        box((h, 0.004, 0.004), loc=(-0.07 + h / 2, -0.027, 0.24 + i * 0.04), m=M["ink"])
    for i in range(0, 42, 10):
        text(str(i // 10 * 5), 0.04, loc=(0.03, -0.027, 0.24 + i * 0.04), m=M["ink"])
    upper = [(0.05, 2.10), (0.62, 2.10), (0.84, 1.96), (0.87, 1.62), (0.82, 1.62), (0.74, 1.90), (0.05, 1.96)]
    slab(upper, 0.045, m=M["steel"], bev=0.004)
    slab([(-0.05, 2.1), (-0.32, 2.1), (-0.34, 2.0), (-0.05, 2.02)], 0.03, m=M["steel"], bev=0.003)
    z0 = 0.8
    lower = [(0.05, z0), (0.62, z0), (0.84, z0 + 0.14), (0.87, z0 + 0.48), (0.82, z0 + 0.48), (0.74, z0 + 0.2), (0.05, z0 + 0.14)]
    slab(lower, 0.045, m=M["steel"], bev=0.004)
    box((0.26, 0.11, 0.3), loc=(0, 0, 0.95), m=M["steel_dirty"], bev=0.012)
    torus(0.05, 0.012, loc=(-0.02, -0.065, 0.78), rot=(DEG(90), 0, 0), m=M["steel"], major=24, minor=8)
    cyl(0.03, 0.05, loc=(0.06, -0.08, 1.04), rot=(DEG(90), 0, 0), m=M["black_plastic"], verts=24)
    text("PRECISION", 0.03, loc=(-0.02, -0.0565, 0.98), m=M["ink"])
    for z in (0.4, 1.6):
        box((0.1, 0.1, 0.12), loc=(0, 0.07, z), m=M["steel_dirty"], bev=0.01)


def p_braces_fence():
    cols = [M["flower_pink"], M["teal_plastic"], M["glow_green"]]
    for i, x in enumerate((-1.0, 1.0)):
        cyl(0.04, 1.45, loc=(x, 0, 0.725), m=M["steel_dirty"], verts=16)
        for j, z in enumerate((0.75, 1.35)):
            box((0.2, 0.12, 0.17), loc=(x, 0, z), m=M["steel"], bev=0.015)
            for dz in (-0.05, 0.05):
                box((0.24, 0.09, 0.04), loc=(x, -0.005, z + dz), m=M["steel"], bev=0.01)
            torus(0.085, 0.016, loc=(x, -0.01, z), rot=(DEG(90), 0, DEG(45)), m=cols[(i + j) % 3], major=24, minor=8)
    for z in (0.75, 1.35):
        tube([(-1.1, -0.065, z), (0, -0.075, z - 0.03), (1.1, -0.065, z)], 0.018, M["chrome"])


def p_mannequin(hoodie=False, brace=False, head_turn=0.0, stand=True):
    V = [(0, 0, 1.0), (0, 0, 1.16), (0, 0, 1.36), (0, 0, 1.5), (-0.19, 0, 1.44), (0.19, 0, 1.44),
         (-0.25, 0.02, 1.17), (0.25, 0.02, 1.17), (-0.27, -0.02, 0.93), (0.27, -0.02, 0.93),
         (-0.1, 0, 0.94), (0.1, 0, 0.94), (-0.11, 0.0, 0.52), (0.11, 0.0, 0.52), (-0.11, 0.02, 0.1), (0.11, 0.02, 0.1)]
    E = [(0, 1), (1, 2), (2, 3), (2, 4), (2, 5), (4, 6), (5, 7), (6, 8), (7, 9), (0, 10), (0, 11), (10, 12), (11, 13),
         (12, 14), (13, 15)]
    R = [(0.15, 0.11), (0.125, 0.09), (0.165, 0.11), (0.055, 0.055), (0.06, 0.06), (0.06, 0.06), (0.042, 0.042),
         (0.042, 0.042), (0.03, 0.03), (0.03, 0.03), (0.085, 0.085), (0.085, 0.085), (0.055, 0.055), (0.055, 0.055),
         (0.038, 0.038), (0.038, 0.038)]
    skin_body(V, E, R, M["mannequin"])
    for i in (4, 5, 6, 7, 12, 13):
        sphere(R[i][0] * 1.12, loc=V[i], m=M["mannequin"], segs=16, rings=10)
    for i in (8, 9):
        sphere(1.0, loc=(V[i][0], V[i][1], V[i][2] - 0.07), scale=(0.028, 0.045, 0.075), m=M["mannequin"], segs=16, rings=10)
    for i in (14, 15):
        sphere(1.0, loc=(V[i][0], V[i][1] - 0.06, 0.035), scale=(0.045, 0.12, 0.04), m=M["mannequin"], segs=16, rings=10)
    st = mark()
    cyl(0.045, 0.12, loc=(0, 0, 1.56), m=M["mannequin"], verts=20)
    sphere(0.1, loc=(0, 0, 1.68), scale=(0.95, 1.05, 1.25), m=M["mannequin"], segs=32, rings=16)
    if brace:  # Brace Face: a forced smile held open by a cheek retractor
        sphere(1.0, loc=(0, -0.093, 1.62), scale=(0.05, 0.02, 0.02), m=M["mouth"], segs=20, rings=10)
        wire = []
        for k in range(10):
            a = DEG(-60 + k * 13.3)
            x, y = 0.045 * math.sin(a), -0.1 - 0.008 * math.cos(a)
            box((0.0075, 0.004, 0.012), loc=(x, y, 1.627), rot=(0, 0, a), m=M["tooth"], bev=0.0015)
            box((0.004, 0.002, 0.004), loc=(x, y - 0.0025, 1.628), rot=(0, 0, a), m=M["chrome"])
            wire.append((x, y - 0.0035, 1.628))
        tube(wire, 0.0009, M["chrome"])
        for s in (-1, 1):
            tube([(s * 0.045, -0.098, 1.648), (s * 0.068, -0.106, 1.62), (s * 0.045, -0.098, 1.592)], 0.0045, M["clear"])
            tube([(s * 0.068, -0.106, 1.62), (s * 0.1, -0.12, 1.62), (s * 0.12, -0.115, 1.6)], 0.004, M["clear"])
    if head_turn:
        bpy.context.view_layer.update()
        for o in K._parts[st:]:
            o.matrix_world = Matrix.Rotation(head_turn, 4, "Z") @ o.matrix_world
    if hoodie:
        Eh = [e for e in E if e[0] < 10 and e[1] < 10]
        Rh = [(r[0] * 1.25 + 0.012, r[1] * 1.3 + 0.012) for r in R[:10]]
        Rh[3] = (0.085, 0.08)
        skin_body(V[:10], Eh, Rh, M["fabric_grey"])
        hood = sphere(0.15, loc=(0, 0.035, 1.66), scale=(1.0, 1.0, 1.08), m=M["fabric_grey"], segs=24, rings=14)
        K.delete_verts(hood, lambda co: co.y < -0.06)
        hood.modifiers.new("Thick", "SOLIDIFY").thickness = 0.018
        for s in (-1, 1):
            tube([(s * 0.03, -0.12, 1.47), (s * 0.032, -0.135, 1.38), (s * 0.03, -0.13, 1.3)], 0.0035, M["paper"])
    if stand:
        cyl(0.24, 0.025, loc=(0, 0.05, 0.0125), m=M["chrome"], verts=40, bev=0.005)
        cyl(0.012, 0.6, loc=(0.11, 0.05, 0.3), m=M["chrome"], verts=12)


def p_brace_face():
    p_mannequin(brace=True, head_turn=DEG(-12), stand=False)


# =================================================================== FLOOR 1 — WAITING ROOM

def p_neon_sign():
    box((3.4, 0.05, 1.05), loc=(0, 0.06, 0), m=M["black_plastic"], bev=0.01)
    for x in (-1.55, 1.55):
        for z in (-0.42, 0.42):
            cyl(0.012, 0.06, loc=(x, 0.02, z), rot=(DEG(90), 0, 0), m=M["chrome"], verts=12)
    neon_text("ASCENSION CLINIC", 0.38, loc=(0, 0, 0.15), m=M["glow_green"], tube_r=0.007)
    neon_text("NO REFUNDS", 0.26, loc=(0, 0, -0.32), m=M["glow_pink"], tube_r=0.006, dead_index=5,
              dead_m=M["neon_dead"])
    box((0.25, 0.1, 0.18), loc=(1.45, 0.12, -0.6), m=M["steel_dirty"], bev=0.008)
    tube([(1.45, 0.12, -0.69), (1.4, 0.1, -0.95), (1.1, 0.08, -1.3)], 0.008, M["rubber"])


def p_ring_light():
    for i in range(3):
        a = DEG(90 + i * 120)
        tube([(0, 0, 0.55), (math.cos(a) * 0.2, math.sin(a) * 0.2, 0.25), (math.cos(a) * 0.38, math.sin(a) * 0.38, 0.0)],
             0.012, M["black_plastic"])
        sphere(0.02, loc=(math.cos(a) * 0.38, math.sin(a) * 0.38, 0.012), m=M["rubber"], segs=12, rings=6)
    cyl(0.025, 0.12, loc=(0, 0, 0.55), m=M["black_plastic"], verts=20)
    cyl(0.016, 1.0, loc=(0, 0, 1.05), m=M["steel"], verts=20)
    cyl(0.012, 0.1, loc=(0, 0, 1.55), m=M["black_plastic"], verts=16)
    torus(0.23, 0.032, loc=(0, 0, 1.75), rot=(DEG(90), 0, 0), m=M["black_plastic"], major=64, minor=14)
    torus(0.23, 0.02, loc=(0, -0.022, 1.75), rot=(DEG(90), 0, 0), m=M["glow_ring"], major=64, minor=10)
    box((0.085, 0.01, 0.16), loc=(0, -0.012, 1.75), m=M["black_plastic"], bev=0.008)
    box((0.012, 0.012, 0.2), loc=(0, 0, 1.66), m=M["black_plastic"])
    tube([(0.02, 0.03, 1.52), (0.025, 0.03, 1.0), (0.03, 0.03, 0.62), (0.15, 0.1, 0.3), (0.45, 0.3, 0.01), (0.9, 0.4, 0.01)],
         0.005, M["rubber"])
    box((0.05, 0.03, 0.02), loc=(0.6, 0.35, 0.012), m=M["black_plastic"], bev=0.004)


def p_ticket_machine():
    lathe([(0.2, 0.0), (0.2, 0.03), (0.17, 0.045), (0.04, 0.05)], 40, M["steel_dirty"], cap_top=True)
    cyl(0.035, 0.85, loc=(0, 0, 0.47), m=M["steel_dirty"], verts=24)
    box((0.3, 0.2, 0.38), loc=(0, 0, 1.08), m=M["red_plastic"], bev=0.05, segs=4)
    box((0.22, 0.012, 0.11), loc=(0, -0.1, 1.17), m=M["paper"], bev=0.004)
    text("TAKE A", 0.035, loc=(0, -0.107, 1.19), m=M["ink"])
    text("NUMBER", 0.035, loc=(0, -0.107, 1.15), m=M["ink"])
    box((0.12, 0.03, 0.012), loc=(0, -0.1, 1.02), m=M["black_plastic"])
    box((0.07, 0.002, 0.11), loc=(0, -0.108, 0.96), rot=(DEG(-12), 0, 0), m=M["paper"])
    text("5", 0.06, loc=(0, -0.1135, 0.955), rot=(DEG(78), 0, 0), m=M["ink"])
    cyl(0.03, 0.02, loc=(0.1, -0.1, 0.94), rot=(DEG(90), 0, 0), m=M["steel"], verts=24)
    box((0.14, 0.04, 0.05), loc=(0, 0, 1.3), m=M["black_plastic"], bev=0.006)
    text("05", 0.04, loc=(0, -0.021, 1.3), m=M["glow_red"])


def p_now_serving():
    box((0.75, 0.12, 0.34), loc=(0, 0, 0.17), m=M["black_plastic"], bev=0.015)
    box((0.7, 0.01, 0.08), loc=(0, -0.06, 0.28), m=M["green_paint"])
    text("NOW SERVING", 0.055, loc=(0, -0.066, 0.28), m=M["paper"])
    box((0.42, 0.01, 0.17), loc=(0, -0.06, 0.12), m=M["mouth"])
    text("05", 0.17, loc=(0, -0.068, 0.12), m=M["glow_red"])
    box((0.06, 0.1, 0.3), loc=(0, 0.1, 0.5), m=M["steel_dirty"])


def p_desk_bell():
    lathe([(0.045, 0.0), (0.045, 0.012), (0.04, 0.016)], 32, M["black_plastic"], cap_bottom=True, cap_top=True)
    dome = sphere(0.036, loc=(0, 0, 0.016), m=M["chrome"], segs=32, rings=16)
    K.delete_verts(dome, lambda co: co.z < 0.0)
    cyl(0.004, 0.02, loc=(0, 0, 0.058), m=M["chrome"], verts=10)
    sphere(0.007, loc=(0, 0, 0.069), scale=(1, 1, 0.6), m=M["chrome"], segs=12, rings=8)


def p_rejected_stamp():
    sphere(0.022, loc=(0, 0, 0.085), scale=(1, 1, 0.8), m=M["wood"], segs=20, rings=10)
    cyl(0.01, 0.04, loc=(0, 0, 0.06), m=M["wood"], verts=16)
    box((0.07, 0.04, 0.025), loc=(0, 0, 0.0285), m=M["wood"], bev=0.004)
    box((0.066, 0.036, 0.008), loc=(0, 0, 0.004), m=M["red_plastic"], bev=0.001)
    box((0.06, 0.001, 0.014), loc=(0, -0.0205, 0.03), m=M["paper"])
    text("REJECTED", 0.0095, loc=(0, -0.0212, 0.03), m=M["red_plastic"])


def p_crt(small=False):
    box((0.46, 0.38, 0.36), loc=(0, 0.05, 0.25), m=M["beige_plastic"], bev=0.03, segs=3)
    box((0.3, 0.26, 0.26), loc=(0, 0.3, 0.25), m=M["beige_plastic"], bev=0.03, segs=3)
    sphere(0.17, loc=(-0.04, -0.12, 0.26), scale=(1.0, 0.18, 0.82), m=M["glow_screen"], segs=32, rings=16)
    for (sx, sz, x, z) in ((0.36, 0.03, -0.04, 0.395), (0.36, 0.03, -0.04, 0.125), (0.03, 0.3, -0.205, 0.26), (0.03, 0.3, 0.125, 0.26)):
        box((sx, 0.03, sz), loc=(x, -0.135, z), m=M["black_plastic"], bev=0.008)
    for z in (0.33, 0.25):
        cyl(0.018, 0.02, loc=(0.18, -0.145, z), rot=(DEG(90), 0, 0), m=M["steel"], verts=16)
    for i in range(6):
        box((0.2, 0.004, 0.008), loc=(0, 0.432, 0.18 + i * 0.025), m=M["black_plastic"])
    if not small:
        cyl(0.03, 0.22, loc=(0, 0.2, 0.54), m=M["steel_dirty"], verts=16)
        box((0.22, 0.22, 0.02), loc=(0, 0.2, 0.66), m=M["steel_dirty"], bev=0.004)


def p_reception_desk():
    random.seed(11)
    box((2.4, 0.12, 1.1), loc=(0, -0.35, 0.55), m=M["white_paint"], bev=0.01)
    box((2.5, 0.35, 0.05), loc=(0, -0.42, 1.125), m=M["wood"], bev=0.01)
    box((2.4, 0.8, 0.04), loc=(0, 0.05, 0.75), m=M["wood_light"], bev=0.005)
    for x in (-1.14, 1.14):
        box((0.12, 0.8, 0.75), loc=(x, 0.05, 0.375), m=M["white_paint"], bev=0.01)
    box((2.41, 0.006, 0.12), loc=(0, -0.413, 0.85), m=M["green_paint"])
    text("RECEPTION", 0.1, loc=(0, -0.418, 0.58), m=M["green_paint"], depth=0.004)
    place(p_crt, loc=(-0.6, 0.25, 0.77), rot=(0, 0, DEG(200)), scale=0.75, small=True)
    box((0.42, 0.15, 0.025), loc=(-0.6, -0.1, 0.785), m=M["beige_plastic"], bev=0.004)
    place(p_desk_bell, loc=(0.3, -0.45, 1.15))
    place(p_rejected_stamp, loc=(0.78, -0.05, 0.77))
    place(p_rejected_stamp, loc=(0.9, -0.02, 0.77), rot=(0, 0, DEG(30)))
    box((0.32, 0.06, 0.07), loc=(-0.25, -0.48, 1.185), rot=(DEG(-15), 0, 0), m=M["brass"], bev=0.004)
    text("BRENDA", 0.045, loc=(-0.25, -0.512, 1.19), rot=(DEG(75), 0, 0), m=M["ink"])
    for i in range(7):
        box((0.21, 0.297, 0.002), loc=(0.45 + random.uniform(-0.02, 0.02), 0.25, 0.772 + i * 0.003),
            rot=(0, 0, DEG(random.uniform(-8, 8))), m=M["paper"])
    lathe([(0.07, 0.0), (0.085, 0.12), (0.09, 0.13)], 24, M["ceramic"], loc=(1.0, 0.25, 0.77), cap_bottom=True, solid=0.004)
    for k in range(6):
        a = DEG(k * 60 + random.uniform(-20, 20))
        tube([(1.0, 0.25, 0.87), (1.0 + 0.05 * math.cos(a), 0.25 + 0.05 * math.sin(a), 1.02),
              (1.0 + 0.12 * math.cos(a), 0.25 + 0.12 * math.sin(a), 0.97)], 0.0025, M["wood"])
    box((0.3, 0.004, 0.14), loc=(-0.85, -0.47, 1.22), rot=(DEG(-10), 0, 0), m=M["paper"])
    text("BACK IN 5 MINS", 0.028, loc=(-0.85, -0.475, 1.24), rot=(DEG(80), 0, 0), m=M["ink"], kind="marker")
    text("(since 1997)", 0.02, loc=(-0.85, -0.477, 1.195), rot=(DEG(80), 0, 0), m=M["ink"], kind="marker")


def p_waiting_chairs(n=3):
    W = 0.56
    box((n * W + 0.1, 0.06, 0.06), loc=(0, 0.05, 0.38), m=M["steel_dirty"], bev=0.006)
    for x in (-(n * W) / 2 + 0.12, (n * W) / 2 - 0.12):
        cyl(0.025, 0.38, loc=(x, 0.05, 0.19), m=M["steel_dirty"], verts=16)
        box((0.06, 0.56, 0.03), loc=(x, 0.05, 0.015), m=M["steel_dirty"], bev=0.006)
    for i in range(n):
        x = (i - (n - 1) / 2) * W
        seat = box((0.48, 0.46, 0.04), loc=(x, 0.0, 0.46), m=M["teal_plastic"], bev=0.018, segs=3)
        bd = seat.modifiers.new("Bend", "SIMPLE_DEFORM")
        bd.deform_method, bd.deform_axis, bd.angle = "BEND", "X", DEG(10)
        box((0.48, 0.04, 0.42), loc=(x, 0.25, 0.73), rot=(DEG(-12), 0, 0), m=M["teal_plastic"], bev=0.018, segs=3)
        box((0.05, 0.05, 0.12), loc=(x, 0.05, 0.42), m=M["steel_dirty"])
        box((0.04, 0.04, 0.28), loc=(x, 0.22, 0.55), rot=(DEG(-12), 0, 0), m=M["steel_dirty"])
    lathe([(0.03, 0.0), (0.04, 0.1)], 20, M["paper"], loc=(W, 0.0, 0.48), cap_bottom=True, solid=0.002)
    box((0.15, 0.21, 0.004), loc=(-W, 0.02, 0.485), rot=(0, 0, DEG(20)), m=M["cover_b"])


def p_water_cooler():
    box((0.33, 0.33, 0.95), loc=(0, 0, 0.475), m=M["white_paint"], bev=0.02)
    box((0.2, 0.06, 0.06), loc=(0, -0.18, 0.62), m=M["black_plastic"], bev=0.006)
    for x, c in ((-0.05, M["glow_red"]), (0.05, M["teal_plastic"])):
        box((0.03, 0.04, 0.05), loc=(x, -0.2, 0.62), m=c, bev=0.005)
    box((0.22, 0.12, 0.02), loc=(0, -0.2, 0.45), m=M["steel_dirty"])
    lathe([(0.03, 0.95), (0.03, 1.0), (0.13, 1.06), (0.135, 1.08), (0.135, 1.36), (0.12, 1.42), (0.06, 1.44)],
          32, M["water"], cap_top=True, solid=0.004)
    for z in (1.15, 1.28):
        torus(0.137, 0.006, loc=(0, 0, z), m=M["water"], major=32, minor=6)
    cyl(0.04, 0.28, loc=(0.2, 0, 0.75), m=M["clear"], verts=20)
    for i in range(6):
        lathe([(0.03, 0.0), (0.038, 0.07)], 16, M["paper"], loc=(0.2, 0, 0.62 + i * 0.03), solid=0.001)


def p_vending_machine():
    box((0.92, 0.8, 1.85), loc=(0, 0, 0.925), m=M["green_paint"], bev=0.02)
    box((0.62, 0.02, 1.3), loc=(-0.1, -0.41, 1.07), m=M["glass"])
    box((0.62, 0.02, 1.3), loc=(-0.1, -0.2, 1.07), m=M["black_plastic"])
    for (sx, sz, x, z) in ((0.68, 0.04, -0.1, 1.73), (0.68, 0.04, -0.1, 0.41), (0.04, 1.34, -0.42, 1.07), (0.04, 1.34, 0.22, 1.07)):
        box((sx, 0.04, sz), loc=(x, -0.4, z), m=M["steel_dirty"], bev=0.005)
    for r in range(5):
        z = 0.5 + r * 0.26
        box((0.6, 0.2, 0.012), loc=(-0.1, -0.3, z), m=M["steel"])
        for c in range(6):
            x = -0.37 + c * 0.1
            lathe([(0.028, 0.0), (0.03, 0.005), (0.03, 0.12), (0.012, 0.16), (0.012, 0.19)], 12, M["glass_green"],
                  loc=(x, -0.3, z + 0.006), cap_bottom=True, cap_top=True)
            cyl(0.026, 0.1, loc=(x, -0.3, z + 0.06), m=M["juice"], verts=12)
            box((0.06, 0.004, 0.018), loc=(x, -0.39, z - 0.012), m=M["paper"])
    box((0.88, 0.03, 0.2), loc=(0, -0.405, 1.78), m=M["black_plastic"], bev=0.01)
    text("JAW JUICE", 0.13, loc=(0, -0.422, 1.78), m=M["glow_green"], depth=0.004)
    box((0.18, 0.02, 0.6), loc=(0.35, -0.405, 1.2), m=M["black_plastic"], bev=0.005)
    text("ALL ITEMS: 5", 0.025, loc=(0.35, -0.417, 1.45), m=M["glow_red"])
    for i in range(4):
        for j in range(3):
            box((0.035, 0.015, 0.03), loc=(0.31 + j * 0.04, -0.418, 1.08 + i * 0.05), m=M["steel"], bev=0.003)
    box((0.06, 0.02, 0.012), loc=(0.35, -0.417, 1.32), m=M["mouth"])
    box((0.6, 0.04, 0.16), loc=(-0.1, -0.405, 0.2), m=M["mouth"], bev=0.01)


def p_magazine_rack():
    covers = [("JAWLINE WEEKLY", "cover_a"), ("PORE MECHANICS", "cover_b"), ("IS YOUR CHIN\nLYING TO YOU?", "cover_c"),
              ("MEWING TODAY", "cover_b"), ("SYMMETRY\nMONTHLY", "cover_a"), ("RING LIGHT\nLIVING", "cover_c")]
    box((0.8, 0.03, 0.9), loc=(0, 0.06, 0.45), m=M["wood"], bev=0.008)
    for t in range(3):
        z = 0.12 + t * 0.29
        tube([(-0.38, -0.06, z), (0.38, -0.06, z)], 0.006, M["chrome"], kind="POLY")
        tube([(-0.38, 0.04, z - 0.02), (-0.38, -0.06, z), (-0.38, -0.06, z + 0.08)], 0.005, M["chrome"], kind="POLY")
        tube([(0.38, 0.04, z - 0.02), (0.38, -0.06, z), (0.38, -0.06, z + 0.08)], 0.005, M["chrome"], kind="POLY")
        for k in range(2):
            title, ck = covers[t * 2 + k]
            x = -0.19 + k * 0.38
            box((0.3, 0.012, 0.25), loc=(x, -0.02, z + 0.12), rot=(DEG(-14), 0, 0), m=M[ck])
            text(title, 0.026, loc=(x, -0.05, z + 0.2), rot=(DEG(76), 0, 0), m=M["paper"])


def p_sink_station():
    lathe([(0.05, 0.0), (0.2, 0.04), (0.24, 0.15), (0.25, 0.17)], 40, M["ceramic"], loc=(0, 0, 0.72),
          cap_bottom=True, solid=0.012)
    box((0.7, 0.3, 0.06), loc=(0, 0.08, 0.86), m=M["ceramic"], bev=0.01)
    cyl(0.04, 0.72, loc=(0, 0.1, 0.36), m=M["ceramic"], verts=24)
    tube([(0, 0.16, 0.89), (0, 0.16, 1.02), (0, 0.06, 1.05), (0, 0.0, 0.98)], 0.012, M["chrome"])
    for s in (-1, 1):
        cyl(0.02, 0.05, loc=(s * 0.12, 0.15, 0.91), m=M["chrome"], verts=16)
    box((0.62, 0.03, 0.75), loc=(0, 0.2, 1.5), m=M["steel_dirty"], bev=0.01)
    box((0.56, 0.01, 0.69), loc=(0, 0.18, 1.5), m=M["mirror"])
    box((0.62, 0.12, 0.02), loc=(0, 0.14, 1.08), m=M["glass"])
    names = [("CLEANSE", "skin_care", 0.13), ("TONE", "toner", 0.12), ("SERUM", "serum", 0.08), ("SPF", "spf", 0.11)]
    for i, (nm, mk, h) in enumerate(names):
        x = -0.21 + i * 0.14
        lathe([(0.025, 0.0), (0.027, 0.005), (0.027, h * 0.75), (0.012, h * 0.9), (0.01, h)], 20, M[mk],
              loc=(x, 0.13, 1.09), cap_bottom=True, cap_top=True)
        box((0.045, 0.002, 0.03), loc=(x, 0.1025, 1.09 + h * 0.4), m=M["paper"])
        text(nm, 0.009, loc=(x, 0.1015, 1.09 + h * 0.4), m=M["ink"])
    text("1   2   3   4", 0.03, loc=(0, 0.17, 1.92), m=M["glow_green"])


def p_fluorescent_light(broken=True):
    box((1.25, 0.3, 0.08), loc=(0, 0, -0.04), m=M["white_paint"], bev=0.01)
    for i, y in enumerate((-0.06, 0.06)):
        mm = M["glow_tube_dead"] if (broken and i == 1) else M["glow_tube"]
        cyl(0.013, 1.18, loc=(0, y, -0.1), rot=(0, DEG(90), 0), m=mm, verts=12)
        for s in (-1, 1):
            box((0.02, 0.03, 0.03), loc=(s * 0.6, y, -0.095), m=M["white_paint"])
    for i in range(11):
        box((0.004, 0.28, 0.05), loc=(-0.55 + i * 0.11, 0, -0.12), m=M["chrome"])
    for s in (-1, 1):
        box((1.24, 0.004, 0.05), loc=(0, s * 0.14, -0.12), m=M["chrome"])


def p_suggestion_box():
    box((0.32, 0.22, 0.34), loc=(0, 0, 0.17), m=M["wood"], bev=0.008)
    box((0.14, 0.03, 0.006), loc=(0, 0, 0.342), m=M["mouth"])
    box((0.24, 0.004, 0.06), loc=(0, -0.112, 0.25), m=M["paper"])
    text("SUGGESTIONS", 0.03, loc=(0, -0.115, 0.25), m=M["ink"])
    random.seed(4)
    for k in range(7):
        box((0.08, 0.06, 0.001), loc=(random.uniform(-0.05, 0.05), random.uniform(-0.01, 0.01), 0.36 + k * 0.004),
            rot=(DEG(random.uniform(-30, 30)), DEG(random.uniform(-30, 30)), DEG(random.uniform(0, 90))), m=M["paper"])
    text("let me out", 0.014, loc=(0.0, -0.035, 0.38), rot=(DEG(60), 0, DEG(10)), m=M["ink"], kind="marker")


# =================================================================== FLOOR 3 — BONE SMASH BASEMENT

def p_bonk_hammer():
    lathe([(0.017, 0.0), (0.019, 0.01), (0.017, 0.2), (0.015, 0.42)], 20, M["wood"], cap_bottom=True, cap_top=True)
    cyl(0.0205, 0.17, loc=(0, 0, 0.09), m=M["rubber"], verts=20)
    for z in (0.005, 0.175):
        torus(0.021, 0.003, loc=(0, 0, z), m=M["rubber"], major=20, minor=6)
    text("MAXX", 0.02, loc=(0, -0.021, 0.09), rot=(DEG(90), DEG(90), 0), m=M["white_paint"])
    cyl(0.022, 0.03, loc=(0, 0, 0.43), m=M["steel_dirty"], verts=20)
    cyl(0.058, 0.17, loc=(0, 0, 0.47), rot=(0, DEG(90), 0), m=M["steel"], verts=40, bev=0.012)
    for s in (-1, 1):
        cyl(0.052, 0.014, loc=(s * 0.09, 0, 0.47), rot=(0, DEG(90), 0), m=M["rubber"], verts=40, bev=0.004)
    torus(0.059, 0.005, loc=(0, 0, 0.47), rot=(0, DEG(90), 0), m=M["rust"], major=40, minor=8)


def p_practice_helmet():
    o = sphere(0.14, loc=(0, 0, 0.0), scale=(1, 1.15, 0.85), m=M["hardhat"], segs=48, rings=24)
    K.delete_verts(o, lambda co: co.z < -0.001)
    for c, r, d in (((0.05, -0.06, 0.1), 0.05, 0.022), ((-0.07, 0.03, 0.09), 0.045, 0.018), ((0.0, 0.06, 0.115), 0.04, 0.014),
                    ((-0.03, -0.1, 0.06), 0.035, 0.012)):
        K.dent(o, c, r, d)
    o.modifiers.new("Thick", "SOLIDIFY").thickness = 0.006
    b = cyl(0.17, 0.008, loc=(0, 0, 0.0), m=M["hardhat"], verts=48)
    b.scale = (1, 1.2, 1)
    t = torus(0.135, 0.008, loc=(0, 0, 0.015), m=M["hardhat"], major=48, minor=8)
    t.scale = (1, 1.14, 1)
    for a in (0, 90):
        tube([(0.11 * math.cos(DEG(a)), 0.13 * math.sin(DEG(a)), 0.02), (0, 0, 0.07),
              (-0.11 * math.cos(DEG(a)), -0.13 * math.sin(DEG(a)), 0.02)], 0.006, M["black_plastic"])
    box((0.11, 0.002, 0.03), loc=(0, -0.152, 0.068), rot=(DEG(-28), 0, 0), m=M["paper"])
    text("PRACTICE", 0.017, loc=(0, -0.1535, 0.068), rot=(DEG(62), 0, 0), m=M["ink"])


def p_bonk_press_frame():
    for x in (-0.85, 0.85):
        box((0.28, 0.32, 2.9), loc=(x, 0, 1.45), m=M["green_paint"], bev=0.02)
        for z in (0.6, 1.6, 2.5):
            box((0.3, 0.34, 0.06), loc=(x, 0, z), m=M["steel_dirty"], bev=0.008)
    box((2.1, 0.42, 0.45), loc=(0, 0, 3.0), m=M["green_paint"], bev=0.02)
    cyl(0.16, 0.7, loc=(0, 0, 2.55), m=M["steel_dirty"], bev=0.01)
    box((1.5, 1.1, 0.25), loc=(0, 0, 0.125), m=M["steel_dirty"], bev=0.015)
    for i in range(14):
        box((0.1, 0.012, 0.08), loc=(-0.7 + i * 0.107, -0.556, 0.18), m=M["hazard_y"] if i % 2 == 0 else M["hazard_k"])
    box((0.5, 0.02, 0.36), loc=(-0.85, -0.17, 1.7), m=M["hazard_y"], bev=0.01)
    text("MIND THE", 0.07, loc=(-0.85, -0.182, 1.77), m=M["ink"])
    text("BONK", 0.15, loc=(-0.85, -0.182, 1.64), m=M["ink"])
    tube([(0.1, -0.1, 3.0), (0.5, -0.25, 3.25), (0.85, -0.22, 2.8), (0.95, -0.17, 2.2)], 0.025, M["rubber"])


def p_bonk_press_ram():
    cyl(0.06, 0.9, loc=(0, 0, 1.75), m=M["chrome"], verts=24)
    box((0.16, 0.16, 0.12), loc=(0, 0, 1.36), m=M["steel_dirty"], bev=0.01)
    cyl(0.34, 0.95, loc=(0, 0, 1.0), rot=(0, DEG(90), 0), m=M["steel"], bev=0.04, verts=48)
    for s in (-1, 1):
        cyl(0.32, 0.06, loc=(s * 0.5, 0, 1.0), rot=(0, DEG(90), 0), m=M["rubber"], bev=0.015, verts=48)
    torus(0.345, 0.02, loc=(0, 0, 1.0), rot=(0, DEG(90), 0), m=M["rust"], major=48, minor=8)


def p_hammer_pegboard():
    box((1.8, 0.03, 1.1), loc=(0, 0.015, 1.5), m=M["wood_light"], bev=0.005)
    for i in range(17):
        for j in range(10):
            cyl(0.006, 0.004, loc=(-0.8 + i * 0.1, -0.0012, 1.0 + j * 0.1), rot=(DEG(90), 0, 0), m=M["ink"], verts=8)
    for z in (0.94, 2.07):
        box((1.84, 0.05, 0.05), loc=(0, 0, z), m=M["wood"], bev=0.005)
    box((0.9, 0.01, 0.12), loc=(0, -0.01, 1.97), m=M["hazard_y"])
    text("PICK YOUR BONE", 0.075, loc=(0, -0.017, 1.97), m=M["ink"])
    for k in range(6):
        x = -0.75 + k * 0.3
        sc = 0.55 + k * 0.1
        tube([(x, 0, 1.78), (x, -0.06, 1.78), (x, -0.07, 1.81)], 0.005, M["steel"])
        place(p_bonk_hammer, loc=(x, -0.075, 1.78 - 0.5 * sc), scale=sc)
        box((0.16, 0.004, 0.035), loc=(x, -0.003, 1.08), m=M["paper"])
        text(f"BONE LVL {k + 1}", 0.02, loc=(x, -0.006, 1.08), m=M["ink"])


def p_days_since_sign():
    box((1.0, 0.03, 0.72), loc=(0, 0, 0.36), m=M["white_paint"], bev=0.01)
    box((1.0, 0.032, 0.16), loc=(0, -0.001, 0.63), m=M["green_paint"])
    text("SAFETY FIRST", 0.08, loc=(0, -0.019, 0.63), m=M["paper"])
    text("DAYS SINCE LAST", 0.068, loc=(0, -0.018, 0.48), m=M["ink"])
    text("BONK", 0.11, loc=(0, -0.018, 0.375), m=M["ink"])
    box((0.26, 0.03, 0.24), loc=(0, -0.025, 0.16), m=M["black_plastic"], bev=0.006)
    text("0", 0.2, loc=(0, -0.042, 0.16), m=M["paper"])
    for x in (-0.45, 0.45):
        for z in (0.06, 0.66):
            cyl(0.012, 0.008, loc=(x, -0.017, z), rot=(DEG(90), 0, 0), m=M["steel"], verts=10)


def p_hanging_cage():
    R = 0.62
    for z, rr in ((0.06, 0.025), (1.85, 0.025), (0.95, 0.018)):
        torus(R, rr, loc=(0, 0, z), m=M["rust"], major=48, minor=8)
    cyl(R, 0.04, loc=(0, 0, 0.04), m=M["steel_dirty"], verts=48)
    for i in range(6):
        box((2 * R, 0.03, 0.02), loc=(0, 0, 0.012), rot=(0, 0, DEG(i * 30)), m=M["rust"])
    nb = 22
    for i in range(nb):
        a = 2 * math.pi * i / nb
        x, y = R * math.cos(a), R * math.sin(a)
        cyl(0.011, 1.8, loc=(x, y, 0.95), m=M["rust"], verts=8)
        if i % 2 == 0:
            tube([(x, y, 1.85), (x * 0.78, y * 0.78, 2.12), (x * 0.3, y * 0.3, 2.32), (0, 0, 2.37)], 0.011, M["rust"])
    torus(0.05, 0.012, loc=(0, 0, 2.43), rot=(DEG(90), 0, 0), m=M["steel_dirty"], major=20, minor=6)
    for k in range(12):
        torus(0.035, 0.009, loc=(0, 0, 2.52 + k * 0.058), rot=(DEG(90), 0, DEG(90 * (k % 2))), m=M["steel_dirty"], major=16, minor=6)
    box((0.07, 0.03, 0.08), loc=(0, -R - 0.03, 0.95), m=M["brass"], bev=0.008)
    torus(0.025, 0.006, loc=(0, -R - 0.03, 1.0), rot=(DEG(90), 0, 0), m=M["steel"], major=16, minor=6)


def p_valve():
    torus(0.12, 0.012, loc=(0, -0.12, 0), rot=(DEG(90), 0, 0), m=M["red_plastic"], major=32, minor=8)
    for k in range(4):
        box((0.24, 0.012, 0.012), loc=(0, -0.12, 0), rot=(0, DEG(45 * k), 0), m=M["red_plastic"])
    cyl(0.015, 0.12, loc=(0, -0.06, 0), rot=(DEG(90), 0, 0), m=M["steel"], verts=12)
    box((0.12, 0.1, 0.16), loc=(0, 0, 0), m=M["steel_dirty"], bev=0.015)


def p_pipe_straight(L=2.0, r=0.08):
    cyl(r, L, loc=(0, 0, r + 0.04), rot=(0, DEG(90), 0), m=M["rust"], verts=24)
    for s in (-1, 1):
        cyl(r + 0.04, 0.03, loc=(s * (L / 2 - 0.015), 0, r + 0.04), rot=(0, DEG(90), 0), m=M["steel_dirty"], verts=24, bev=0.004)
        for k in range(6):
            a = DEG(k * 60)
            cyl(0.008, 0.05, loc=(s * (L / 2 - 0.015), (r + 0.025) * math.cos(a), r + 0.04 + (r + 0.025) * math.sin(a)),
                rot=(0, DEG(90), 0), m=M["steel"], verts=6)


def p_pipe_elbow(r=0.08, R=0.3):
    pts = [(R * math.cos(DEG(a)) - R, 0, R * math.sin(DEG(a)) + r + 0.04) for a in range(0, 91, 10)]
    tube(pts, r, M["rust"], res=8)
    cyl(r + 0.04, 0.03, loc=(0, 0, r + 0.04), rot=(DEG(90), 0, 0), m=M["steel_dirty"], verts=24)
    cyl(r + 0.04, 0.03, loc=(-R, 0, R + r + 0.04), m=M["steel_dirty"], verts=24)


def p_pipe_valve():
    p_pipe_straight(L=0.8)
    place(p_valve, loc=(0, 0, 0.12))


def p_catwalk(L=4.0, W=1.2):
    for s in (-1, 1):
        box((L, 0.06, 0.16), loc=(0, s * W / 2, 0.08), m=M["steel_dirty"], bev=0.004)
        box((L, 0.008, 0.12), loc=(0, s * (W / 2 + 0.035), 0.22), m=M["steel_dirty"])
        for i in range(5):
            cyl(0.022, 1.0, loc=(-L / 2 + 0.05 + i * (L - 0.1) / 4, s * W / 2, 0.66), m=M["hazard_y"], verts=12)
        tube([(-L / 2, s * W / 2, 1.16), (L / 2, s * W / 2, 1.16)], 0.025, M["hazard_y"], kind="POLY")
        tube([(-L / 2, s * W / 2, 0.66), (L / 2, s * W / 2, 0.66)], 0.018, M["hazard_y"], kind="POLY")
    for i in range(int(L / 0.04) + 1):
        box((0.008, W, 0.03), loc=(-L / 2 + i * 0.04, 0, 0.145), m=M["steel_dirty"])
    for i in range(int(L / 0.5) + 1):
        box((0.04, W, 0.05), loc=(-L / 2 + i * 0.5, 0, 0.11), m=M["steel_dirty"])


def p_furnace():
    lathe([(0.85, 0.25), (0.9, 0.3), (0.9, 2.0), (0.8, 2.25), (0.5, 2.45), (0.18, 2.52)], 48, M["rust"], cap_top=True)
    lathe([(0.6, 0.22), (0.85, 0.25)], 48, M["rust"])
    for z in (0.5, 1.1, 1.7):
        torus(0.905, 0.02, loc=(0, 0, z), m=M["steel_dirty"], major=64, minor=6)
        for k in range(24):
            a = 2 * math.pi * k / 24
            sphere(0.012, loc=(0.92 * math.cos(a), 0.92 * math.sin(a), z + 0.035), m=M["steel_dirty"], segs=8, rings=5)
    for a in (45, 135, 225, 315):
        box((0.12, 0.12, 0.3), loc=(0.6 * math.cos(DEG(a)), 0.6 * math.sin(DEG(a)), 0.15), m=M["steel_dirty"], bev=0.01)
    box((0.64, 0.14, 0.56), loc=(0, -0.86, 0.85), m=M["steel_dirty"], bev=0.02)
    box((0.48, 0.02, 0.4), loc=(0, -0.94, 0.85), m=M["glow_orange"])
    for i in range(7):
        cyl(0.013, 0.42, loc=(-0.21 + i * 0.07, -0.955, 0.85), m=M["steel_dirty"], verts=8)
    cyl(0.09, 0.05, loc=(0.45, -0.83, 1.65), rot=(DEG(90), 0, 0), m=M["brass"], verts=32)
    cyl(0.075, 0.01, loc=(0.45, -0.86, 1.65), rot=(DEG(90), 0, 0), m=M["paper"], verts=32)
    box((0.005, 0.004, 0.065), loc=(0.47, -0.867, 1.66), rot=(0, DEG(-50), 0), m=M["red_plastic"])
    tube([(0, 0, 2.5), (0, 0, 3.1), (0, 0.15, 3.4), (0, 0.6, 3.5), (0, 1.2, 3.5)], 0.15, M["rust"])
    tube([(0.85, 0, 1.3), (1.3, 0, 1.3), (1.35, 0, 1.9), (1.35, 0, 2.9)], 0.06, M["rust"])
    place(p_valve, loc=(1.12, 0, 1.3), rot=(0, 0, DEG(90)))


# =================================================================== FLOOR 4 — RATING CHAMBER

def p_score_paddle(label="4", size=0.22):
    cyl(0.015, 0.32, loc=(0, 0, 0.16), m=M["wood"], verts=12)
    box((0.3, 0.012, 0.3), loc=(0, 0, 0.45), m=M["paper"], bev=0.02, segs=3)
    text(label, size, loc=(0, -0.0075, 0.45), m=M["ink"])


def p_judge_bench():
    box((3.0, 0.9, 1.25), loc=(0, 0.1, 0.625), m=M["wood"], bev=0.015)
    for i in range(5):
        box((0.48, 0.02, 0.7), loc=(-1.2 + i * 0.6, -0.355, 0.6), m=M["wood_light"], bev=0.01)
    box((3.1, 1.0, 0.06), loc=(0, 0.1, 1.28), m=M["wood"], bev=0.01)
    box((0.62, 0.04, 0.13), loc=(0, -0.37, 1.05), m=M["brass"], bev=0.005)
    text("THE RATER", 0.075, loc=(0, -0.393, 1.05), m=M["ink"])
    cyl(0.08, 0.03, loc=(0.6, -0.05, 1.325), m=M["wood"], verts=24)
    cyl(0.04, 0.16, loc=(0.62, -0.02, 1.4), rot=(0, DEG(90), 0), m=M["wood"], verts=20, bev=0.006)
    cyl(0.012, 0.28, loc=(0.62, -0.15, 1.39), rot=(DEG(80), 0, 0), m=M["wood"], verts=12)
    tube([(-0.6, 0.1, 1.31), (-0.6, 0.0, 1.45), (-0.62, -0.15, 1.5)], 0.008, M["black_plastic"])
    sphere(0.025, loc=(-0.62, -0.17, 1.5), scale=(1, 1.5, 1), m=M["black_plastic"], segs=16, rings=8)
    place(p_score_paddle, loc=(1.1, 0.0, 1.31), rot=(DEG(-70), 0, DEG(15)), label="4")


def p_scoreboard():
    box((2.4, 0.12, 1.0), loc=(0, 0, 0.5), m=M["black_plastic"], bev=0.02)
    box((2.25, 0.01, 0.86), loc=(0, -0.06, 0.5), m=M["mouth"])
    text("HIGHEST RATING EVER", 0.12, loc=(0, -0.068, 0.82), m=M["glow_red"])
    text("6.2", 0.38, loc=(0, -0.068, 0.5), m=M["glow_red"])
    text("(A DOOR)", 0.09, loc=(0, -0.068, 0.22), m=M["glow_red"])


def p_symmetry_projector():
    for i in range(3):
        a = DEG(90 + i * 120)
        tube([(0, 0, 1.2), (math.cos(a) * 0.35, math.sin(a) * 0.35, 0.0)], 0.012, M["steel_dirty"], kind="POLY")
    cyl(0.03, 0.15, loc=(0, 0, 1.25), m=M["steel_dirty"], verts=16)
    box((0.32, 0.4, 0.2), loc=(0, 0, 1.42), m=M["beige_plastic"], bev=0.02)
    for i in range(6):
        box((0.33, 0.01, 0.12), loc=(0, 0.12 + i * 0.02, 1.42), m=M["black_plastic"])
    cyl(0.06, 0.12, loc=(0, -0.24, 1.42), rot=(DEG(90), 0, 0), m=M["black_plastic"], verts=24)
    cyl(0.045, 0.01, loc=(0, -0.3, 1.42), rot=(DEG(90), 0, 0), m=M["glow_green"], verts=24)
    text("SYMMETRY", 0.035, loc=(0, -0.201, 1.5), m=M["ink"])


def p_operating_lamp():
    cyl(0.15, 0.04, loc=(0, 0, -0.02), m=M["white_paint"], verts=32)
    cyl(0.03, 0.4, loc=(0, 0, -0.24), m=M["white_paint"], verts=16)
    for s in (-1, 1):
        tube([(0, 0, -0.44), (s * 0.3, 0, -0.5), (s * 0.55, 0, -0.62)], 0.025, M["white_paint"])
        lathe([(0.05, 0.0), (0.24, -0.06), (0.3, -0.16)], 40, M["white_paint"], loc=(s * 0.6, 0, -0.55), solid=0.012)
        cyl(0.27, 0.01, loc=(s * 0.6, 0, -0.705), m=M["glow_warm"], verts=40)
        cyl(0.03, 0.12, loc=(s * 0.6, 0, -0.77), m=M["steel"], verts=16)


# =================================================================== FLOOR 5 — GLOW-UP GRAVEYARD
TOMBS = {
    "A": ("DEREK", ["Tried 47 serums.", "Should have tried sleep."], "round"),
    "B": ("GARY", ["Rated himself daily.", "Final score: tired."], "gothic"),
    "C": ("STEVE", ["Took 3,000 selfies.", "Found his angle.", "Too late."], "slab"),
    "D": ("UNKNOWN", ["His lighting was", "never right."], "photo"),
    "E": ("KYLE", ["Went to the gym.", "Forgot to leave."], "obelisk"),
    "F": ("MUM", ["Thought I looked fine."], "flowers"),
}


def p_tombstone(v="A"):
    random.seed(ord(v))
    name, lines, shape = TOMBS[v]
    base_z = 0.1
    if shape == "obelisk":
        cyl(0.2, 1.3, loc=(0, 0, base_z + 0.65), rot=(0, 0, DEG(45)), r2=0.14, m=M["stone"], verts=4)
        cyl(0.15, 0.2, loc=(0, 0, base_z + 1.4), rot=(0, 0, DEG(45)), r2=0.0, m=M["stone"], verts=4)
        face_y, top = -0.122, 1.2
    else:
        if shape in ("round", "photo", "flowers"):
            w = {"round": 0.3, "photo": 0.26, "flowers": 0.23}[shape]
            h = {"round": 0.75, "photo": 0.55, "flowers": 0.45}[shape]
            outline = [(-w, 0), (w, 0)] + arc(0, h, w, 0, 180, 24)
            top = h + w
        elif shape == "gothic":
            w, h = 0.28, 0.8
            right = [(-w + 2 * w * math.cos(DEG(a)), h + 2 * w * math.sin(DEG(a))) for a in range(0, 61, 6)]
            left = [(w - 2 * w * math.cos(DEG(a)), h + 2 * w * math.sin(DEG(a))) for a in range(54, -1, -6)]
            outline = [(-w, 0), (w, 0)] + right + left
            top = h + 2 * w * math.sin(DEG(60))
        else:  # slab with chamfered corners
            w, h = 0.36, 0.95
            outline = [(-w, 0), (w, 0), (w, h - 0.09), (w - 0.09, h), (-w + 0.09, h), (-w, h - 0.09)]
            top = h
        d = 0.18 if shape == "slab" else 0.14
        slab(outline, d, loc=(0, 0, base_z), m=M["stone"], bev=0.012, segs=2)
        face_y = -d / 2 - 0.001
    box((0.85 if shape != "flowers" else 0.65, 0.34, 0.1), loc=(0, 0, 0.05), m=M["stone"], bev=0.012)
    zt = base_z + top - 0.2
    text("HERE LIES", 0.05, loc=(0, face_y, zt), m=M["carve"], depth=0.002)
    text(name, 0.1 if len(name) < 7 else 0.075, loc=(0, face_y, zt - 0.11), m=M["carve"], depth=0.002)
    for i, ln in enumerate(lines):
        text(ln, 0.036, loc=(0, face_y, zt - 0.23 - i * 0.055), m=M["carve"], depth=0.002, kind="notice")
    if shape == "photo":
        z = base_z + 0.2
        t = torus(0.075, 0.012, loc=(0, face_y - 0.004, z), rot=(DEG(90), 0, 0), m=M["brass"], major=32, minor=8)
        t.scale = (0.8, 1, 1.0)
        c = cyl(0.07, 0.006, loc=(0, face_y, z), rot=(DEG(90), 0, 0), m=M["sepia"], verts=32)
        c.scale = (0.78, 1, 1)
    if shape == "flowers":
        lathe([(0.04, 0.0), (0.05, 0.1), (0.035, 0.16), (0.045, 0.2)], 24, M["ceramic"], loc=(0.0, -0.13, 0.1),
              cap_bottom=True, solid=0.004)
        for k in range(7):
            a = DEG(k * 51)
            tip = (0.07 * math.cos(a), -0.13 + 0.05 * math.sin(a), 0.42 + 0.06 * math.sin(a * 2))
            tube([(0, -0.13, 0.25), (tip[0] * 0.5, -0.13 + (tip[1] + 0.13) * 0.5, 0.36), tip], 0.0035, M["leaf"])
            sphere(0.028, loc=tip, scale=(1, 1, 0.6), m=M["flower_pink"] if k % 2 else M["flower_yellow"], segs=12, rings=8)
    for _ in range(8):
        x = random.uniform(-0.32, 0.32)
        sphere(random.uniform(0.025, 0.05), loc=(x, random.uniform(-0.12, 0.12), 0.1 + random.uniform(0, 0.03)),
               scale=(1.4, 1.0, 0.45), m=M["moss"], segs=10, rings=6)
    if shape in ("round", "slab"):
        tube([(-0.1, face_y - 0.001, base_z + top - 0.02), (-0.06, face_y - 0.001, base_z + top - 0.12),
              (-0.09, face_y - 0.001, base_z + top - 0.22)], 0.003, M["ink"], kind="POLY")


def p_before_photo_boss():
    box((1.0, 0.08, 1.3), loc=(0, 0, 1.9), m=M["gold"], bev=0.03)
    box((0.84, 0.01, 1.12), loc=(0, -0.045, 1.9), m=M["sepia"])
    sphere(0.18, loc=(0, -0.05, 2.05), scale=(1, 0.05, 1.2), m=M["mouth"], segs=24, rings=12)
    box((0.5, 0.01, 0.35), loc=(0, -0.05, 1.62), m=M["mouth"], bev=0.05)
    text("BEFORE", 0.12, loc=(0, -0.052, 1.4), m=M["glow_red"])
    for sx, sy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        hip = Vector((sx * 0.4, sy * 0.03, 1.3))
        knee = Vector((sx * 0.85, sy * 0.45, 1.45))
        foot = Vector((sx * 1.05, sy * 0.75, 0.02))
        for a, b, r in ((hip, knee, 0.018), (knee, foot, 0.013)):
            d = b - a
            rot = d.to_track_quat("Z", "Y").to_euler()
            for k in range(3):
                cyl(r * (1 - k * 0.18), d.length / 3 + 0.02, loc=a + d * ((k + 0.5) / 3), rot=rot, m=M["black_plastic"], verts=10)
        sphere(0.03, loc=knee, m=M["chrome"], segs=12, rings=8)
        box((0.08, 0.05, 0.03), loc=foot + Vector((0, 0, 0.01)), m=M["black_plastic"], bev=0.008)


# =================================================================== FLOOR 6 — LATHERED SPA

def p_spa_bench():
    for i in range(5):
        box((1.6, 0.075, 0.035), loc=(0, -0.18 + i * 0.09, 0.45), m=M["wood_light"], bev=0.006)
    for s in (-1, 1):
        box((0.05, 0.45, 0.04), loc=(s * 0.65, 0, 0.415), m=M["steel"], bev=0.004)
        for y in (-0.18, 0.18):
            cyl(0.02, 0.41, loc=(s * 0.65, y, 0.205), m=M["steel"], verts=12)


def p_towel_stack():
    for n, z in ((3, 0.0), (2, 0.11), (1, 0.22)):
        for i in range(n):
            x = (i - (n - 1) / 2) * 0.13
            mm = M["towel"] if (i + n) % 2 else M["towel_pink"]
            cyl(0.062, 0.36, loc=(x, 0, 0.062 + z), rot=(DEG(90), 0, 0), m=mm, verts=24)
            torus(0.04, 0.012, loc=(x, -0.181, 0.062 + z), rot=(DEG(90), 0, 0), m=mm, major=20, minor=6)


def p_shower_head():
    tube([(0, 0.0, 0.0), (0, 0.0, 1.85), (0, -0.05, 2.0), (0, -0.28, 2.05)], 0.014, M["chrome"])
    lathe([(0.02, 0.0), (0.06, -0.02), (0.075, -0.05)], 32, M["chrome"], loc=(0, -0.32, 2.05), solid=0.006)
    cyl(0.073, 0.008, loc=(0, -0.32, 2.0), m=M["steel"], verts=32)
    for k in range(18):
        r = 0.02 + 0.045 * (k % 2)
        a = DEG(k * 40)
        cyl(0.004, 0.004, loc=(r * math.cos(a), -0.32 + r * math.sin(a), 1.995), m=M["black_plastic"], verts=6)
    for s, c in ((-1, M["glow_red"]), (1, M["teal_plastic"])):
        cyl(0.03, 0.05, loc=(s * 0.12, -0.03, 1.1), rot=(DEG(90), 0, 0), m=M["chrome"], verts=16)
        box((0.012, 0.012, 0.03), loc=(s * 0.12, -0.06, 1.1), m=c)


def p_foam_blob():
    random.seed(9)
    for _ in range(40):
        r = random.uniform(0.04, 0.16)
        a = random.uniform(0, 2 * math.pi)
        d = random.uniform(0, 0.45) ** 0.8
        sphere(r, loc=(d * math.cos(a), d * math.sin(a), r * 0.55 + random.uniform(0, 0.12) * (1 - d)),
               m=M["foam"], segs=16, rings=10)


def p_cucumber_slices():
    lathe([(0.0, 0.0), (0.09, 0.0), (0.13, 0.015), (0.14, 0.02)], 40, M["ceramic"], solid=0.004)
    random.seed(5)
    for k in range(8):
        a = DEG(k * 45)
        x, y = 0.07 * math.cos(a), 0.07 * math.sin(a)
        cyl(0.021, 0.005, loc=(x, y, 0.012 + k * 0.0005), rot=(DEG(random.uniform(-8, 8)), 0, 0), m=M["cucumber_skin"], verts=24)
        cyl(0.019, 0.0055, loc=(x, y, 0.0122 + k * 0.0005), m=M["cucumber"], verts=24)


def p_sheet_mask_pack():
    box((0.13, 0.18, 0.006), loc=(0, 0, 0.003), m=M["foil"], bev=0.004)
    text("SHEET MASK", 0.018, loc=(0, 0.03, 0.0065), rot=(0, 0, 0), m=M["paper"])
    text("ULTRA GLOW", 0.012, loc=(0, 0.0, 0.0065), rot=(0, 0, 0), m=M["ink"], kind="notice")
    text("ghost mode", 0.01, loc=(0, -0.05, 0.0065), rot=(0, 0, 0), m=M["ink"], kind="marker")


# =================================================================== FLOOR 7 — RUNWAY

def p_mannequin_plain():
    p_mannequin()


def p_mannequin_hoodie():
    p_mannequin(hoodie=True, head_turn=DEG(25))


def p_stage_spotlight():
    lathe([(0.12, 0.0), (0.14, 0.05), (0.14, 0.38), (0.12, 0.42)], 32, M["black_plastic"], rot=(DEG(90), 0, 0),
          loc=(0, 0.2, 0.6), cap_bottom=True, solid=0.006)
    cyl(0.115, 0.01, loc=(0, -0.21, 0.6), rot=(DEG(90), 0, 0), m=M["glow_magenta"], verts=32)
    for k in range(6):
        box((0.29, 0.01, 0.01), loc=(0, -0.225, 0.6), rot=(0, DEG(k * 30), 0), m=M["black_plastic"])
    tube([(-0.17, 0.0, 0.6), (-0.17, 0.0, 0.85), (0.17, 0.0, 0.85), (0.17, 0.0, 0.6)], 0.012, M["black_plastic"], kind="POLY")
    cyl(0.02, 0.12, loc=(0, 0, 0.91), m=M["steel"], verts=12)
    box((0.08, 0.06, 0.1), loc=(0, 0, 1.0), m=M["steel_dirty"], bev=0.008)
    for s in (-1, 1):
        cyl(0.03, 0.02, loc=(s * 0.165, 0, 0.6), rot=(0, DEG(90), 0), m=M["steel"], verts=16)


def p_mirror_bulbs():
    box((1.1, 0.05, 0.9), loc=(0, 0, 0.45), m=M["wood"], bev=0.01)
    box((0.9, 0.01, 0.7), loc=(0, -0.026, 0.45), m=M["mirror"])
    pos = [(-0.5 + i * 0.2, 0.86) for i in range(6)] + [(-0.5 + i * 0.2, 0.04) for i in range(6)] + \
          [(-0.51, 0.25 + i * 0.2) for i in range(3)] + [(0.51, 0.25 + i * 0.2) for i in range(3)]
    for k, (x, z) in enumerate(pos):
        cyl(0.012, 0.02, loc=(x, -0.03, z), rot=(DEG(90), 0, 0), m=M["steel"], verts=10)
        sphere(0.028, loc=(x, -0.055, z), m=M["glow_warm"] if k not in (3, 13) else M["glow_tube_dead"], segs=16, rings=8)
    for (x, z, rt, t1) in ((-0.3, 0.7, 5, "Smile with\nyour eyes."), (0.28, 0.25, -7, "Don't blink.")):
        box((0.14, 0.002, 0.12), loc=(x, -0.032, z), rot=(0, DEG(rt), 0), m=M["cover_c"])
        text(t1, 0.02, loc=(x, -0.034, z), rot=(DEG(90), DEG(rt), 0), m=M["ink"], kind="marker")


def p_runway(L=4.0, W=1.6, H=0.8):
    box((L, W, 0.05), loc=(0, 0, H - 0.025), m=M["black_plastic"], bev=0.005)
    box((L, W - 0.1, H - 0.05), loc=(0, 0, (H - 0.05) / 2), m=M["mouth"])
    for s in (-1, 1):
        box((L, 0.02, 0.02), loc=(0, s * (W / 2 - 0.01), H - 0.06), m=M["glow_magenta"])
        box((L, 0.03, H - 0.05), loc=(0, s * (W / 2 - 0.02), (H - 0.05) / 2), m=M["black_plastic"])
    for i in range(int(L / 0.5)):
        box((0.04, 0.4, 0.002), loc=(-L / 2 + 0.25 + i * 0.5, 0, H + 0.001), m=M["tape_line"])


def p_vent_grate():
    box((0.62, 0.04, 0.42), loc=(0, 0, 0.21), m=M["steel_dirty"], bev=0.008)
    box((0.54, 0.02, 0.34), loc=(0, -0.012, 0.21), m=M["mouth"])
    for i in range(8):
        box((0.54, 0.008, 0.03), loc=(0, -0.022, 0.06 + i * 0.043), rot=(DEG(-35), 0, 0), m=M["steel_dirty"])
    for k, (x, z) in enumerate(((-0.28, 0.03), (0.28, 0.03), (-0.28, 0.39), (0.28, 0.39))):
        if k == 3:
            cyl(0.006, 0.01, loc=(x, -0.021, z), rot=(DEG(90), 0, 0), m=M["mouth"], verts=10)
        else:
            cyl(0.008, 0.01, loc=(x, -0.024, z), rot=(DEG(90), 0, 0), m=M["steel"], verts=10)


# =================================================================== FLOOR 8 — FRONT CAMERA

def p_exit_mirror():
    pz = 0.45
    outline = [(-0.75, 0.0), (0.75, 0.0)] + arc(0, 1.9, 0.75, 0, 180, 28)
    slab(outline, 0.14, loc=(0, 0.0, pz), m=M["gold"], bev=0.012)
    inner = [(-0.62, 0.1), (0.62, 0.1)] + arc(0, 1.9, 0.62, 0, 180, 28)
    slab(inner, 0.02, loc=(0, -0.072, pz), m=M["glow_portal"])
    path = [(-0.75, 0.0), (-0.75, 1.9)] + arc(0, 1.9, 0.75, 180, 0, 40)[1:] + [(0.75, 0.0)]
    tube([(x, -0.075, z + pz) for (x, z) in path], 0.022, M["gold"], kind="POLY")
    for k in range(11):
        a = DEG(15 + k * 15)
        tip = Vector((0.95 * math.cos(a), -0.03, 1.9 + 0.95 * math.sin(a) + pz))
        mid = Vector((0.78 * math.cos(a), -0.03, 1.9 + 0.78 * math.sin(a) + pz))
        d = tip - mid
        cyl(0.03, d.length, loc=(tip + mid) / 2, rot=d.to_track_quat("Z", "Y").to_euler(), r2=0.0, m=M["gold"], verts=8)
    for i, (w, d) in enumerate(((2.2, 1.2), (1.9, 1.0), (1.65, 0.8))):
        box((w, d, 0.15), loc=(0, 0.05, 0.075 + i * 0.15), m=M["stone"], bev=0.012)
    text("EXIT", 0.12, loc=(0, -0.551, 0.2), m=M["glow_green"], depth=0.003)


def p_notification(title="GLOW UP GANG", body="3 people viewed your profile."):
    box((2.6, 1.1, 0.24), loc=(0, 0, 0.12), m=M["notif"], bev=0.11, segs=4)
    box((0.34, 0.34, 0.03), loc=(-0.98, 0.12, 0.25), m=M["glow_green"], bev=0.07, segs=3)
    text(title, 0.13, loc=(-0.72, 0.24, 0.242), rot=(0, 0, 0), m=M["ink"], align="LEFT")
    text(body, 0.1, loc=(-0.72, -0.02, 0.242), rot=(0, 0, 0), m=M["grey_text"], align="LEFT", kind="notice")
    text("now", 0.09, loc=(1.15, 0.24, 0.242), rot=(0, 0, 0), m=M["grey_text"], align="RIGHT")


def p_camera_lens():
    st = mark()
    lathe([(1.6, 0.0), (1.62, 0.22), (1.5, 0.3), (1.35, 0.32)], 64, M["black_plastic"], cap_bottom=True)
    lathe([(1.35, 0.32), (1.3, 0.45), (1.2, 0.5)], 64, M["chrome"])
    torus(1.22, 0.03, loc=(0, 0, 0.5), m=M["glow_phone"], major=96, minor=10)
    sphere(1.2, loc=(0, 0, 0.3), scale=(1, 1, 0.35), m=M["lens"], segs=64, rings=24)
    for r, z in ((0.85, 0.64), (0.6, 0.69), (0.38, 0.715)):
        torus(r, 0.012, loc=(0, 0, z), m=M["chrome"], major=64, minor=8)
    torus(0.26, 0.04, loc=(0, 0, 0.73), m=M["glow_green"], major=48, minor=10)
    sphere(0.12, loc=(-0.3, 0, 0.66), scale=(1, 0.6, 0.2), m=M["glow_warm"], segs=16, rings=8)
    transform_since(st, rot=(DEG(90), 0, 0))
    transform_since(st, loc=(0, 0, 1.62))


def p_elevator_panel():
    box((0.2, 0.02, 0.6), loc=(0, 0, 0.3), m=M["steel"], bev=0.004)
    for i in range(10):
        n = i + 1
        x = -0.045 + (i % 2) * 0.09
        z = 0.12 + (i // 2) * 0.085
        if n == 10:
            box((0.042, 0.002, 0.042), loc=(x, -0.011, z), rot=(0, DEG(6), 0), m=M["paper"])
            text("10", 0.024, loc=(x, -0.0125, z), m=M["ink"], kind="marker")
            continue
        cyl(0.02, 0.012, loc=(x, -0.014, z), rot=(DEG(90), 0, 0), m=M["brass"] if n == 5 else M["chrome"], verts=24, bev=0.002)
        if n != 5:
            text(str(n), 0.018, loc=(x, -0.0205, z), m=M["ink"])
    cyl(0.022, 0.012, loc=(0, -0.014, 0.05), rot=(DEG(90), 0, 0), m=M["red_plastic"], verts=24)
    text("ASCENSION LIFT", 0.016, loc=(0, -0.0105, 0.57), m=M["ink"])


# =================================================================== ITEMS

def p_jaw_juice():
    lathe([(0.035, 0.0), (0.038, 0.006), (0.038, 0.15), (0.03, 0.18), (0.016, 0.205), (0.015, 0.23)], 40,
          M["glass_green"], cap_bottom=True, solid=0.002)
    lathe([(0.034, 0.004), (0.035, 0.01), (0.035, 0.155)], 40, M["juice"], cap_bottom=True, cap_top=True)
    lathe([(0.017, 0.226), (0.017, 0.252)], 32, M["black_plastic"], cap_top=True)
    for z in (0.232, 0.24, 0.248):
        torus(0.0172, 0.0012, loc=(0, 0, z), m=M["black_plastic"], major=32, minor=4)
    lathe([(0.0386, 0.055), (0.0386, 0.125)], 40, M["green_paint"], solid=0.0006)
    text("JAW", 0.024, loc=(0, -0.0395, 0.104), m=M["paper"])
    text("JUICE", 0.017, loc=(0, -0.0395, 0.08), m=M["paper"])
    text("100% JAW", 0.007, loc=(0, -0.0395, 0.064), m=M["paper"], kind="notice")


def p_hand_mirror():
    t = torus(0.08, 0.009, loc=(0, 0, 0.19), rot=(DEG(90), 0, 0), m=M["gold"], major=48, minor=10)
    t.scale = (0.85, 1, 1.15)
    c = cyl(0.08, 0.014, loc=(0, 0.004, 0.19), rot=(DEG(90), 0, 0), m=M["gold"], verts=48)
    c.scale = (0.85, 1, 1.15)
    c2 = cyl(0.073, 0.004, loc=(0, -0.005, 0.19), rot=(DEG(90), 0, 0), m=M["mirror"], verts=48)
    c2.scale = (0.85, 1, 1.15)
    lathe([(0.009, 0.02), (0.013, 0.05), (0.011, 0.09), (0.014, 0.1)], 20, M["gold"], cap_bottom=True, cap_top=True)
    sphere(0.016, loc=(0, 0, 0.012), m=M["gold"], segs=16, rings=8)


def p_kevin_phone():
    box((0.072, 0.0085, 0.15), loc=(0, 0, 0.075), m=M["black_plastic"], bev=0.008, segs=4)
    box((0.066, 0.001, 0.142), loc=(0, -0.0045, 0.075), m=M["glow_phone"])
    text("3:12", 0.016, loc=(0, -0.0052, 0.12), m=M["ui"])
    text("Barbershop - opens 9 AM", 0.0035, loc=(0, -0.0052, 0.105), m=M["ui"])
    text("4%", 0.004, loc=(0.025, -0.0052, 0.143), m=M["glow_red"])
    box((0.024, 0.003, 0.03), loc=(0.016, 0.0055, 0.128), m=M["black_plastic"], bev=0.003)
    cyl(0.005, 0.002, loc=(0.016, 0.007, 0.134), rot=(DEG(90), 0, 0), m=M["glass"], verts=16)
    tube([(0.03, -0.0053, 0.145), (0.02, -0.0053, 0.13), (0.012, -0.0053, 0.126)], 0.0003, M["paper"], kind="POLY")
    tube([(0.02, -0.0053, 0.13), (0.026, -0.0053, 0.118)], 0.0003, M["paper"], kind="POLY")


def p_mouth_tape():
    lathe([(0.019, 0.0), (0.03, 0.0), (0.03, 0.025), (0.019, 0.025), (0.019, 0.0)], 48, M["tape"])
    lathe([(0.017, 0.0), (0.019, 0.0), (0.019, 0.025), (0.017, 0.025), (0.017, 0.0)], 48, M["wood_light"])
    box((0.026, 0.0005, 0.024), loc=(0.012, -0.031, 0.0125), rot=(0, 0, DEG(-25)), m=M["tape"])


def p_scissors():
    for s in (-1, 1):
        t = torus(0.018, 0.0045, loc=(s * 0.018, 0.045, 0.004), m=M["orange_plastic"], major=24, minor=8)
        t.scale = (1, 1.35, 1)
        slab([(-0.006, 0.0), (0.006, 0.0), (0.003, 0.09), (-0.001, 0.092)], 0.002, loc=(s * 0.004, 0.025, 0.004),
             rot=(DEG(90), 0, DEG(s * 5)), m=M["steel"])
    cyl(0.004, 0.006, loc=(0, 0.02, 0.006), m=M["steel"], verts=12)


def p_gum_brick():
    box((0.4, 0.25, 0.18), loc=(0, 0, 0.09), m=M["gum"], bev=0.045, segs=4)
    box((0.16, 0.258, 0.188), loc=(0, 0, 0.09), m=M["paper"], bev=0.01)
    text("GRANDPA'S", 0.028, loc=(0, -0.13, 0.12), m=M["ink"])
    text("GUM", 0.05, loc=(0, -0.13, 0.08), m=M["red_plastic"])
    text("40 kg", 0.018, loc=(0, -0.13, 0.045), m=M["ink"], kind="notice")


def p_sandwich_flyer():
    box((0.15, 0.21, 0.002), loc=(0, 0, 0.001), m=M["paper"])
    box((0.15, 0.05, 0.0025), loc=(0, 0.08, 0.0012), m=M["hazard_y"])
    text("SANDWICH SHOP", 0.016, loc=(0, 0.08, 0.0028), rot=(0, 0, 0), m=M["ink"])
    text("2 FOR 1", 0.026, loc=(0, 0.02, 0.0022), rot=(0, 0, 0), m=M["red_plastic"])
    text("TUESDAYS", 0.014, loc=(0, -0.012, 0.0022), rot=(0, 0, 0), m=M["ink"])
    text("A normal place\nfor normal people.", 0.008, loc=(0, -0.06, 0.0022), rot=(0, 0, 0), m=M["ink"], kind="notice")


def p_fried_egg():
    random.seed(8)
    for k in range(6):
        a = DEG(k * 60 + random.uniform(-15, 15))
        sphere(0.04, loc=(0.025 * math.cos(a), 0.025 * math.sin(a), 0.003), scale=(1.2, 1.0, 0.12), m=M["egg_white"], segs=20, rings=8)
    sphere(0.022, loc=(0.004, -0.004, 0.008), scale=(1, 1, 0.55), m=M["egg_yolk"], segs=24, rings=12)


def p_brenda_badge():
    box((0.085, 0.004, 0.032), loc=(0, 0, 0.016), m=M["brass"], bev=0.002)
    text("BRENDA", 0.012, loc=(0, -0.0025, 0.022), m=M["ink"])
    text("Reception - Since 1997", 0.0042, loc=(0, -0.0025, 0.011), m=M["ink"])
    text("Do not wake", 0.004, loc=(0, -0.0025, 0.005), m=M["ink"])


def p_power_bank():
    box((0.07, 0.04, 0.12), loc=(0, 0, 0.06), m=M["black_plastic"], bev=0.008)
    for i in range(4):
        box((0.012, 0.002, 0.006), loc=(-0.02 + i * 0.013, -0.0205, 0.1), m=M["glow_green"] if i < 1 else M["mouth"])
    text("RING LIGHT", 0.008, loc=(0, -0.021, 0.06), m=M["paper"])
    text("POWER", 0.012, loc=(0, -0.021, 0.045), m=M["glow_green"])


def p_ticket5():
    pts = [(-0.03, 0.0), (0.03, 0.0)] + [(0.03 - i * 0.006, 0.09 + (0.004 if i % 2 else 0)) for i in range(11)]
    slab(pts, 0.0008, rot=(DEG(-90), 0, 0), loc=(0, -0.045, 0.0004), m=M["paper"])
    text("5", 0.05, loc=(0, 0.0, 0.0012), rot=(0, 0, 0), m=M["ink"])
    text("YOUR NUMBER", 0.006, loc=(0, -0.03, 0.0012), rot=(0, 0, 0), m=M["ink"])


# =================================================================== REGISTRY
SHEETS = ["Orthodontic horror", "Floor 1 - Waiting Room", "Floor 3 - Bone Smash Basement",
          "Floors 4-5 - Rating Chamber, Graveyard", "Floors 6-8 and Elevator", "Items and pickups"]
# (sheet, name, builder, origin, view, note[, "pair" = render with the previous one])
R = [
    (0, "PalateExpander", p_palate_expander, "bottom", "top", "L2 jars, Dr. Meow, item"),
    (0, "ExpanderKey", p_expander_key, "bottom", "front", "L2 Expander Key doors (x30 = door key)"),
    (0, "SpecimenJar", p_specimen_jar, "bottom", "front", "L2 Expander Wall (instance many)"),
    (0, "ExpanderSpider", p_expander_spider, "bottom", "angle", "Enemy L2/L4"),
    (0, "Retainer", p_retainer, "bottom", "top", "L1 Lost & Found"),
    (0, "RetainerChatterer_Base", p_chatterer_base, "world", "angle", "Enemy, static part (origin = hinge)"),
    (0, "RetainerChatterer_Jaw", p_chatterer_jaw, "world", "angle", "Enemy jaw (rotate on X)", "pair"),
    (0, "HeadgearRack", p_headgear_rack, "bottom", "front", "L2/L4 rack, hook No. 5 empty"),
    (0, "DentalChair", p_dental_chair, "bottom", "angle", "L4 'The Chair' chase"),
    (0, "GiantCalipers", p_giant_calipers, "bottom", "front", "L4 wall trap"),
    (0, "BracesFence_200", p_braces_fence, "bottom", "front", "L5 fence segment, 2 m"),
    (0, "BraceFace", p_brace_face, "bottom", "front", "Enemy L5/L7"),
    (1, "NeonSign_Ascension", p_neon_sign, "bottom", "front", "L1 NO REFUNDS (the F is dead)"),
    (1, "ReceptionDesk", p_reception_desk, "bottom", "angle", "L1 Brenda's desk"),
    (1, "TicketMachine", p_ticket_machine, "bottom", "front", "L1 always prints 5"),
    (1, "NowServingDisplay", p_now_serving, "bottom", "front", "L1 Brenda boss"),
    (1, "WaitingChairs", p_waiting_chairs, "bottom", "angle", "L1 beam seating x3"),
    (1, "WaterCooler", p_water_cooler, "bottom", "front", "L1 interactable (+0.25)"),
    (1, "VendingMachine_JawJuice", p_vending_machine, "bottom", "angle", "L1 'ALL ITEMS: 5'"),
    (1, "MagazineRack", p_magazine_rack, "bottom", "front", "L1 magazines"),
    (1, "SinkStation", p_sink_station, "bottom", "front", "L1 Routine Combo sink"),
    (1, "FluorescentLight", p_fluorescent_light, "top", "under", "Ceiling, one dead tube"),
    (1, "RingLight", p_ring_light, "bottom", "front", "Safe rooms, all floors"),
    (1, "SuggestionBox", p_suggestion_box, "bottom", "front", "L1 'let me out'"),
    (1, "DeskBell", p_desk_bell, "bottom", "front", "L1 boss: ring the bell"),
    (1, "RejectedStamp", p_rejected_stamp, "bottom", "front", "L1 Brenda's stamps"),
    (2, "BonkPress_Frame", p_bonk_press_frame, "world", "angle", "L3 hammer press"),
    (2, "BonkPress_Ram", p_bonk_press_ram, "world", "angle", "L3 moving ram (slide on Z)", "pair"),
    (2, "HangingCage", p_hanging_cage, "bottom", "front", "L3 Clavicoolar's cage"),
    (2, "Furnace", p_furnace, "bottom", "angle", "L3 boiler (orange glow)"),
    (2, "HammerPegboard", p_hammer_pegboard, "bottom", "front", "L3 'PICK YOUR BONE'"),
    (2, "DaysSinceSign", p_days_since_sign, "bottom", "front", "L3 JS_07 flips to 0"),
    (2, "Catwalk_400", p_catwalk, "bottom", "angle", "L3 kit, 4 m"),
    (2, "Pipe_Straight_200", p_pipe_straight, "bottom", "angle", "L3 kit, 2 m"),
    (2, "Pipe_Elbow_90", p_pipe_elbow, "bottom", "angle", "L3 kit"),
    (2, "Pipe_Valve", p_pipe_valve, "bottom", "angle", "L3 kit"),
    (2, "BonkHammer", p_bonk_hammer, "bottom", "front", "Clavicoolar's hammer (cartoon)"),
    (2, "PracticeHelmet", p_practice_helmet, "bottom", "angle", "L3 shelf / item"),
    (3, "JudgeBench", p_judge_bench, "bottom", "angle", "L4 Androjenic's bench"),
    (3, "Scoreboard", p_scoreboard, "bottom", "front", "L4 '6.2 (A DOOR)'"),
    (3, "ScorePaddle_4", lambda: p_score_paddle("4"), "bottom", "front", "L4 gallery paddles"),
    (3, "SymmetryProjector", p_symmetry_projector, "bottom", "angle", "L4 grid projector"),
    (3, "OperatingLamp", p_operating_lamp, "top", "under", "L4 ceiling lamp"),
    (3, "Tombstone_A_Derek", lambda: p_tombstone("A"), "bottom", "front", "L5"),
    (3, "Tombstone_B_Gary", lambda: p_tombstone("B"), "bottom", "front", "L5 (JS_13)"),
    (3, "Tombstone_C_Steve", lambda: p_tombstone("C"), "bottom", "front", "L5"),
    (3, "Tombstone_D_Unknown", lambda: p_tombstone("D"), "bottom", "front", "L5 photo grave"),
    (3, "Tombstone_E_Kyle", lambda: p_tombstone("E"), "bottom", "front", "L5"),
    (3, "Tombstone_F_Mum", lambda: p_tombstone("F"), "bottom", "front", "L5 fresh flowers"),
    (3, "BeforePhoto_Boss", p_before_photo_boss, "bottom", "angle", "L5 boss proxy (selfie-stick legs)"),
    (4, "SpaBench", p_spa_bench, "bottom", "angle", "L6"),
    (4, "TowelStack", p_towel_stack, "bottom", "angle", "L6"),
    (4, "ShowerHead", p_shower_head, "bottom", "front", "L6 wall shower"),
    (4, "FoamBlob", p_foam_blob, "bottom", "angle", "L6 foam pile"),
    (4, "Mannequin", p_mannequin_plain, "bottom", "front", "L7"),
    (4, "Mannequin_Hoodie", p_mannequin_hoodie, "bottom", "front", "L7 audience, head turned"),
    (4, "StageSpotlight", p_stage_spotlight, "bottom", "angle", "L7 stage light"),
    (4, "MirrorBulbs", p_mirror_bulbs, "bottom", "front", "L7 backstage mirror"),
    (4, "Runway_400", p_runway, "bottom", "angle", "L7 kit, 4 m"),
    (4, "VentGrate", p_vent_grate, "bottom", "front", "L7 vents (one screw missing)"),
    (4, "ScoreCard_NGMI", lambda: p_score_paddle("NGMI", 0.09), "bottom", "front", "L7 mannequin judge"),
    (4, "ExitMirror", p_exit_mirror, "bottom", "front", "L8 goal"),
    (4, "Notification_Platform", p_notification, "bottom", "top", "L8 platform"),
    (4, "FrontCameraLens", p_camera_lens, "bottom", "front", "L8 boss eye (3.2 m)"),
    (4, "ElevatorCRT", p_crt, "bottom", "front", "Elevator ads"),
    (4, "ElevatorPanel", p_elevator_panel, "bottom", "front", "Worn 5, sticker 10"),
    (5, "JawJuice", p_jaw_juice, "bottom", "front", "+0.5 rating"),
    (5, "HandMirror", p_hand_mirror, "bottom", "front", "Throwable"),
    (5, "KevinPhone", p_kevin_phone, "bottom", "front", "Torch / map / menu"),
    (5, "MouthTape", p_mouth_tape, "bottom", "angle", "30 s silence"),
    (5, "Scissors", p_scissors, "bottom", "top", "Cuts Headgear bands"),
    (5, "GrandpasGum", p_gum_brick, "bottom", "angle", "40 kg brick"),
    (5, "SandwichFlyer", p_sandwich_flyer, "bottom", "top", "Collectible 1 of 8"),
    (5, "FriedEgg", p_fried_egg, "bottom", "top", "+0.25 (fried by a stare)"),
    (5, "BrendaBadge", p_brenda_badge, "bottom", "front", "Collectible"),
    (5, "PowerBank", p_power_bank, "bottom", "front", "Torch recharge"),
    (5, "Ticket5", p_ticket5, "bottom", "top", "Key item"),
    (5, "SheetMask", p_sheet_mask_pack, "bottom", "top", "+1.0 over 10 s"),
    (5, "CucumberSlices", p_cucumber_slices, "bottom", "top", "Night vision 15 s"),
]


def build_all(only=None):
    built = []
    for e in R:
        sheet, name, fn, origin, view, note = e[:6]
        if only and not any(name.startswith(o) for o in only):
            continue
        fn()
        o = K.finish(name, origin=origin)
        built.append(dict(sheet=sheet, name=name, obj=o, view=view, note=note, origin=origin, pair=len(e) > 6))
        print(f"built {name:28s} {K.tri_count(o):7d} tris")
    return built


def export_all(built):
    csv_path = os.path.join(OUT, "PROP_LIST.csv")
    old = {}
    if os.path.exists(csv_path):
        for line in open(csv_path).read().splitlines()[1:]:
            old[line.split(",")[0]] = line
    rows = ["name,triangles,size_x_m,size_y_m,size_z_m,origin,use"]
    for b in built:
        o = b["obj"]
        K.export(o, MODELS)
        d = o.dimensions
        old[f"SM_{b['name']}"] = f"SM_{b['name']},{K.tri_count(o)},{d.x:.3f},{d.y:.3f},{d.z:.3f},{b['origin']},\"{b['note']}\""
        o.hide_render = True
        o.hide_set(True)
    for e in R:
        if "SM_" + e[1] in old:
            rows.append(old["SM_" + e[1]])
    open(csv_path, "w").write("\n".join(rows) + "\n")


# ------------------------------------------------------------------ thumbnails

def thumb_stage():
    K.cycles(samples=28, w=512, h=512)
    K.world((0.002, 0.005, 0.0035))
    floor = K.mat("M_ThumbFloor", (0.012, 0.018, 0.014), rough=0.28)
    wall = K.mat("M_ThumbWall", (0.02, 0.03, 0.024), rough=0.9)
    bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 0, 0))
    bpy.context.object.data.materials.append(floor)
    bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 2.2, 0), rotation=(DEG(90), 0, 0))
    bpy.context.object.data.materials.append(wall)
    K.area_light((-2.2, -2.8, 3.2), (0, 0, 0.7), 750, size=1.4, color=(1.0, 0.93, 0.84))
    K.area_light((2.6, 1.6, 2.6), (0, 0, 0.8), 650, size=1.2, color=(0.35, 1.0, 0.5))
    K.area_light((2.5, -3.0, 0.8), (0, 0, 0.6), 110, size=3.0, color=(0.55, 0.95, 0.75))
    K.area_light((0, 1.5, 4.0), (0, 2.2, 0.5), 220, size=4.0, color=(0.3, 0.9, 0.5))
    K.camera((0, -3.55, 1.45), (0, 0, 0.72), lens=50)


def _bbox_world(objs):
    bpy.context.view_layer.update()
    pts = [o.matrix_world @ Vector(c) for o in objs for c in o.bound_box]
    mn = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    mx = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return mn, mx


def thumb(objs, view, path, pose=None):
    inst = []
    for o in objs:
        c = o.copy()
        c.hide_render = False
        c.hide_set(False)
        K.link(c)
        inst.append(c)
    if pose:
        pose(inst)
    rot = {"front": (0, DEG(-22)), "angle": (0, DEG(-35)), "top": (DEG(58), DEG(-12)), "under": (DEG(205), DEG(-20))}[view]
    R3 = Matrix.Rotation(rot[1], 4, "Z") @ Matrix.Rotation(rot[0], 4, "X")
    for c in inst:
        c.matrix_world = R3 @ c.matrix_world
    mn, mx = _bbox_world(inst)
    k = 1.55 / max(mx - mn)
    for c in inst:
        c.matrix_world = Matrix.Diagonal((k, k, k, 1)) @ c.matrix_world
    mn, mx = _bbox_world(inst)
    off = Vector((-(mn.x + mx.x) / 2, -(mn.y + mx.y) / 2, -mn.z))
    for c in inst:
        c.matrix_world = Matrix.Translation(off) @ c.matrix_world
    K.render(path)
    for c in inst:
        bpy.data.objects.remove(c, do_unlink=True)


def contact_sheets(built):
    from PIL import Image, ImageDraw, ImageFont
    try:
        title_f = ImageFont.truetype(os.path.join(K.FONT_DIR, "BebasNeue-Regular.ttf"), 64)
        lab_f = ImageFont.truetype("DejaVuSans-Bold.ttf", 22)
        note_f = ImageFont.truetype("DejaVuSans.ttf", 17)
    except OSError:
        title_f = lab_f = note_f = ImageFont.load_default()
    T = 512
    for si, title in enumerate(SHEETS):
        items = [b for b in built if b["sheet"] == si and not b["pair"]]
        if not items:
            continue
        cols = 4
        rows = math.ceil(len(items) / cols)
        img = Image.new("RGB", (cols * T, rows * T + 110), (5, 12, 8))
        d = ImageDraw.Draw(img)
        d.text((28, 18), f"NGMI PROP PACK  ·  {title.upper()}", fill=(120, 255, 150), font=title_f)
        for i, b in enumerate(items):
            x, y = (i % cols) * T, 110 + (i // cols) * T
            p = os.path.join(THUMBS, b["name"] + ".png")
            if os.path.exists(p):
                img.paste(Image.open(p).convert("RGB"), (x, y))
            d.rectangle([x, y + T - 64, x + T, y + T], fill=(0, 0, 0))
            d.text((x + 14, y + T - 60), "SM_" + b["name"], fill=(140, 255, 160), font=lab_f)
            d.text((x + 14, y + T - 30), b["note"][:52], fill=(190, 205, 195), font=note_f)
        img.save(os.path.join(OUT, f"props_sheet_{si + 1}.png"))


def main():
    if "--sheets" in sys.argv:  # rebuild contact sheets from existing thumbnails
        contact_sheets([dict(sheet=e[0], name=e[1], note=e[5], pair=len(e) > 6) for e in R])
        print("sheets rebuilt")
        return
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1].split(",")
    K.reset()
    M.update(K.standard_mats())
    extra_mats()
    built = build_all(only)
    export_all(built)
    print("exported", len(built))
    if "--no-render" in sys.argv:
        return
    K.apply_wear_all()
    thumb_stage()
    os.makedirs(THUMBS, exist_ok=True)
    for i, b in enumerate(built):
        if b["pair"]:
            continue
        objs = [b["obj"]]
        pose = None
        if i + 1 < len(built) and built[i + 1]["pair"]:
            objs.append(built[i + 1]["obj"])
            if b["name"].startswith("RetainerChatterer"):
                def pose(inst):
                    inst[1].rotation_euler = (DEG(-28), 0, 0)
                    bpy.context.view_layer.update()
        thumb(objs, b["view"], os.path.join(THUMBS, b["name"] + ".png"), pose)
        print("thumb", b["name"], flush=True)
    if not only:
        contact_sheets(built)
    print("sheets done")


if __name__ == "__main__":
    main()
