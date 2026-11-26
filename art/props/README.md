# NGMI prop pack (in-house, made in Blender)

79 props + the Headgear, all made by us with Blender scripts. No third-party models.

| Folder | What |
| --- | --- |
| `models/` | `SM_*.fbx` (import this into UE5) and `SM_*.glb` (for previews/web) |
| `thumbnails/` | one render per prop (77) |
| `sheets/` | 6 contact sheets, grouped by floor |
| `PROP_LIST.csv` | name, triangles, size in metres, pivot, where it's used |
| `../blender/props/` | scripts that rebuild everything |
| `../blender/headgear/` | the Headgear model + its script |

## Importing into UE5
1. Content Browser → `Content/NGMI/Props/` → Import → pick the `.fbx` files.
2. Settings: scale 1.0, "Combine Meshes" on, "Generate Lightmap UVs" on, Nanite on for big props.
3. Materials come in as simple placeholders. Swap for real `M_`/`MI_` materials later.

## Rebuilding (optional)
Needs Blender 5.x with Python (`bpy`):
```
cd art/blender/props
blender -b -P props.py                # all models + thumbnails into ./out/props/
blender -b -P props.py -- --no-render # models only (fast)
```

## Git LFS
`.fbx`, `.glb`, `.png`, `.ttf` are stored with Git LFS. Run `git lfs install` once before cloning.
