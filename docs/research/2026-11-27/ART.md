# Art, asset and background handoff

Candidate inventory: [ASSETS.csv](ASSETS.csv). P0 = first slice or provenance; P1 = production candidate; P2 = optional. Rows are research, not purchases/imports or blanket license clearance. Before any use record exact asset/version, acquisition date, license URL and transaction/tier evidence in the canonical asset register. Current public visibility is a reason to keep raw licensed binaries out of Git.

## Reuse first

The newer prop pack contains 79 manifest entries plus Headgear, across all eight floors. [Manifest](https://github.com/devspideyy/NGMI/blob/16b37cb74df664ba6950c3f612684579785674ca/art/props/PROP_LIST.csv), [generator](https://github.com/devspideyy/NGMI/blob/16b37cb74df664ba6950c3f612684579785674ca/art/blender/props/props.py), [material/export helper](https://github.com/devspideyy/NGMI/blob/16b37cb74df664ba6950c3f612684579785674ca/art/blender/props/ngmi_kit.py).

Audit: five parsed GLBs (Catwalk, Ring Light, Retainer Chatterer Jaw, Mannequin, Headgear) have no embedded texture images, skin, animation or morph target. Generator applies procedural wear after export for thumbnails; UE will not automatically reproduce this. Keep the geometry and rebuild material instances. Mannequin head/body and Headgear mask/tethers need separation or rigging. Catwalk outer dimensions ~4.04 m vs intended 4 m snap pitch: use intended pivot/grid, not bounds. This is a five-file sample, not certification of all exports.

L3 first import batch: BonkPress_Frame, BonkPress_Ram, HangingCage, Furnace, Catwalk_400, straight/elbow/valve pipes, RingLight, BonkHammer, PracticeHelmet, DaysSinceSign. Check FBX scale (UE cm), transforms, intended pivot, UV, normal direction, collision, material slots and movable components. Separate cage door, controls and other moving parts; do not purchase duplicate custom props.

## Materials and lighting

First four PBR tests: Painted Concrete 02, Concrete Floor Damaged 01, Rusty Metal 03, Metal Grate Rusty. Use neutral test lighting then L3. Begin at 2K; validate texel density and correct GL/DX normal convention, sRGB for color, linear data for normals/roughness/masks. Build shared parameterized materials for painted steel/rust, concrete, tile, glass, fabric, emissive lights. Prefer directional grime caused by contact, water and rust over indiscriminate overlay.

| Floor | Accent | Lighting purpose |
|---|---|---|
| Arrival | Headlight white / cold sky | Silhouette building, isolated green window |
| L1 | Dirty fluorescent white | Reception, face and wayfinding readability |
| L2 | Teal | Wet depth, dry route silhouettes |
| L3 | Orange furnace | Visible cage landmark, usable catwalk edges |
| L4 | Surgical cold white | Exposed rating stage, chair warning |
| L5 | Moonlight blue | Crypt and escort anchors |
| L6 | Pink spa neon | False comfort, wet/dry readability |
| L7 | Stage magenta | Performance and safe wings |
| L8 | Phone white/blue | Surveillance, final warm release |

Scale -> exposure -> neutral materials -> focal lights -> green practicals -> contrast -> fog -> grade. Give ring emissives controlled real lights; do not rely on tiny high-emission surfaces for stable illumination. Test moving flashlight fog ghosting and low-quality fallback. Use Nanite where appropriate for static opaque geometry, not as a universal performance remedy. [Emissive material guidance](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-emissive-material-input-in-unreal-engine), [Volumetric fog](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-fog-in-unreal-engine).

## Asset choices

Start at a proposed $0 acquisition cap for L3 and use existing props + CC0 surfaces. After greybox, audit missing modular architecture, not screenshots. Compare hospital kit for L1/L4; sewer kit for L2; theatre/spa/graveyard only when chapter plans are stable. Static mannequin packs are not animation-ready; first prove separate head/rig in existing model. Mixamo applies to bipedal humanoids; use original designs, no real likeness/voice clones. [Adobe FAQ](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html).

[Quixel announcement 5 Nov 2026](https://quixel.com/news/update-megascans-are-going-free-again) supports the library becoming free, not a verified exact rollout date for every asset. Check exact listing/tier before acquisition. [Fab EULA](https://www.fab.com/eula), [Poly Haven CC0](https://polyhaven.com/license), [ambientCG](https://ambientcg.com/), [Sonniss](https://gdc.sonniss.com/), [Freesound](https://freesound.org/): preserve license evidence; avoid NC assets and standalone redistribution restrictions.

## Backgrounds

Two actual 8192x4096 LDR JPEGs were acquired in the original research bundle (not included in this text PR):

| Asset | Creator | Source | SHA256 of previously acquired file |
|---|---|---|---|
| Moonlit Golf | Greg Zaal | https://polyhaven.com/a/moonlit_golf | 11ca27720c85d6983955da711bdfb20f51100166b7ae341819b7b36c1b639bb1 |
| Solitude Night | Andreas Mischok | https://polyhaven.com/a/solitude_night | 275257fb27ef82ea9e8ac09cef03b3bdf594a2039f554126aa38b09d656a910c |

CC0, acquired 2026-11-27. Download the source JPEG for distant non-traversable backdrops/reference; use separate HDR/EXR for lighting. Moonlit Golf for tree horizon, Solitude Night as alternate reference (avoid its bright building conflicting with the clinic). Near roads, walls, gates and trees remain real geometry with parallax. Do not use arbitrary web photographs as shipped textures.

## 14 art slots

| Slot | Build method |
|---|---|
| Main menu background | Capture actual clinic entrance in engine |
| Exterior horizon | CC0 backdrop on distant sky geometry |
| Inaccessible window view | Perspective-correct cropped background, test angles |
| Environment reference | License-recorded mood board, not shipped automatically |
| Before/after ads | Original fictional character art + editable type |
| Elevator CRT | Reusable screen material and six authored ads; final static |
| Appointment notice | Editable text over worn paper texture |
| Safety signs | Shared signage material/decals, readable at expected distance |
| Before Photo | Original fictional Kevin portrait consistent with character |
| Group-chat portraits | Original character portraits, no real likeness |
| Ending Rating Card | Rendered UI, no personal player data |
| Grime masks | Authored or CC0 masks, PBR-compatible |
| Floor maps | Derived from actual greybox, editable clues |
| Road billboards | Four spatially triggered signs, original fictional advertising |

Stop sourcing when the modular kit satisfies the measured coverage and effort. Finish one representative room, not a giant asset inventory. Every asset must pass import and rights checks before promotion to production.
