# NGMI — Assets (UE5, realistic)

Prices and availability checked on store pages on **2026-11-16**. Re-check before buying.
Rule: **no asset is committed without a row here** (source, license, date).

Legend — Tier: **Core free** / **Paid upgrade** / **Make in-house** · Status: To get / Downloaded / In game / Skip

---

## 1. Use these (fit UE5 realistic)

| Tier | Level / area | What it covers | Source | Price | License | Notes | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Core free | All | ~23,000 photoscanned surfaces, props, decals | [Quixel Megascans on Fab](https://www.fab.com) | Free (since 12 Nov 2026) | Fab Standard License (any engine) | **Primary source.** Claim with your own Epic account, or use the Fab plugin in UE5 | To get |
| Core free | All | Rusty metal, concrete, tile textures + models | [Poly Haven](https://polyhaven.com) | Free | CC0 | 10 test materials listed below | Downloaded (test set) |
| Core free | All | Big PBR material library | [ambientCG](https://ambientcg.com) | Free | CC0 | | To get |
| Core free | All | Industrial textures: pipes, vents, doors, stairs | [Seamless Industrial Textures (OpenGameArt)](https://opengameart.org/content/seamless-industrial-textures) | Free | CC-BY 3.0 | **Credit the author** in game credits | To get |
| Core free | All | Decals: grunge, rust, blood, graffiti | [3D Tudor Free Decal Pack](https://threedtudor.artstation.com/projects/b5oNyn) | Free | Check page | Confirm commercial use before shipping | To get |
| Core free | L3 | Stairs, platforms, scaffolding, pipes, ducts, cables, lights | [RenderCrate Modern Industrial Pack](https://www.cgchannel.com/?p=138173) | Free | Check RenderCrate terms | Link is the announcement article | To get |
| Core free | L3 | Worn industrial pipes | [Industrial Pipes Asset Pack (RenderHub)](https://www.renderhub.com/magiccgistudios/industrial-pipes-asset-pack) | Free | RenderHub Extended Use | Same author has storage tanks | To get |
| Paid upgrade | L1, L4 | Modular abandoned hospital, any engine | [Abandoned Hospital Interior Modular Kit (CGTrader)](https://www.cgtrader.com/3d-models/interior/hall/abandoned-hospital-interior-modular-kit) | $13.99 | Royalty free | FBX/GLB | To get |
| Paid upgrade | L4 | Mortuary + autopsy room | [Abandoned Hospital Mortuary Environment (Fab)](https://www.fab.com/listings/ef1e3661-2b7d-47ec-af8f-a7c402433bbb) | Check Fab | Fab license | Operating tables for boss room | To get |
| Paid upgrade | L2, L4 | Asylum/prison: cells, padded room, stairwell (75 meshes) | [Prison and Abandoned Horror Asylum (Fab)](https://www.fab.com/listings/708dfdbf-0f8d-4b68-a19a-5157509a1b83) | Check Fab | Fab license | | To get |
| Paid upgrade | L2 | Sewer tunnels, 255 meshes, grid snap, 4K | [Sewer Tunnels – Modular Pack, PropHaus (Fab)](https://www.fab.com/listings/dbedea93-46dd-4aa9-bf85-4844ed2e67d8) | Check Fab | Fab license | UE5 + Lumen | To get |
| Paid upgrade | L7 | Modular theater: stage, seats | [Theater (Fab)](https://www.fab.com/listings/8a2de479-42f8-4272-a993-52e92a80f602) | Check Fab | Fab license | Turn stage into catwalk | To get |
| Paid upgrade | L7 | 38 horror mannequins | [Horror Mannequin Pack, Glossy Studio](https://forums.unrealengine.com/t/glossy-studio-horror-mannequin-pack-creppy-3d-props/2844121) | Check store | Store license | 2K textures | To get |
| Paid upgrade | All | 50 photoscanned rust decals | [Rust Stains Decals Vol. 1 (Fab)](https://www.fab.com/listings/b845e5c8-ea5c-4d40-a548-a1429ee90553) | Check Fab | Fab license | | To get |
| Make in-house | All | Green ring lights + flickering fluorescent tubes | Blender → UE5 | — | Ours | The game's signature look | To get |
| Make in-house | L1 | "ASCENSION CLINIC – NO REFUNDS" neon sign + clinic branding | Blender + emissive material | — | Ours | | To get |
| Make in-house | All, L8 | Reflective mirrors + Exit Mirror portal | Blender + UE5 planar reflections / Lumen | — | Ours | Mirrors drive the Mirror Self enemy | To get |
| Make in-house | L7 | Catwalk runway + mannequin scorecards | Kitbash from Theater pack | — | Ours | | To get |
| Make in-house | L8 | Final boss arena: giant phone | Blender | — | Ours | | To get |
| Make in-house | L2 | Tongue-posture puzzle doors | Blender | — | Ours | | To get |

### Poly Haven test materials (used in the web preview)

All CC0, 2K JPG (diffuse, normal GL, roughness). Download with `tools/download_textures.sh`.

| Slug | Use |
| --- | --- |
| `rusty_metal_03` | pipes, frames |
| `green_metal_rust` | wall panels, doors |
| `rust_coarse_01` | heavy rust |
| `rusted_shutter` | shutters (L1, L6) |
| `metal_grate_rusty` | catwalks (L3) |
| `painted_concrete_02` | walls |
| `concrete_wall_004` | walls, ceilings |
| `dirty_tiles` | floors (L1, L6) |
| `worn_tile_floor` | floors |
| `concrete_floor_damaged_01` | basement floor |

---

## 2. Skipped (don't fit UE5 realistic)

Kept here so nobody re-researches them. Reason in brackets.

- SBS Horror Texture Pack (PSX resolution, 128–512 px)
- PSX Modular Pipes Pack · Modular 3D Hospital Environment · Retro Horror Item Kit · PSX Horror Puzzle Item Pack · Sewers PSX · PSX Retro Interior Pack (PSX low-poly)
- PSX Hospital Kit (Lowbit Lab) · PSX Hospital Pack · Abandoned Asylum PSX · PSX Sewer Pack (Tillion) · Modular PSX Sewer Kit · Public Restroom PSX Pack · PSX Graveyard Pack · Final Exam PSX Survival Horror Pack (PSX low-poly)
- Bathroom 3D Asset Pack · NecroPoly Graveyard Kit (stylized)
- PBR Hospital Horror Pack Free · Abandoned Room Free Horror Pack · Graveyard Halloween · HE Abandoned Hospital v.2 · Graveyard And Cemetery Pack 2 · Theatre exterior and interior pack (Unity-only listings)

---

## 3. Process for adding an asset

1. Check license allows commercial use in a paid game.
2. Add a row in section 1 (source URL, price, license, date if not today).
3. Import into UE5 under `Content/NGMI/...` with correct prefix (`SM_`, `T_`, `M_`, …).
4. Commit via Git LFS.
5. Set Status to "In game".
