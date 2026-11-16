#!/usr/bin/env bash
# Downloads the 10 CC0 Poly Haven test materials used in the NGMI web preview.
# 2K JPG maps: diffuse, normal (OpenGL), roughness. ~76 MB total.
# Usage:  bash tools/download_textures.sh   -> ./ngmi_textures/<material>/
# License: CC0 (https://polyhaven.com/license): commercial use OK, no credit needed.
set -euo pipefail
OUT="${1:-ngmi_textures}"
RES="${RES:-2k}"   # set RES=1k or RES=4k to change resolution
MATERIALS=(rusty_metal_03 green_metal_rust rust_coarse_01 rusted_shutter metal_grate_rusty \
           painted_concrete_02 concrete_wall_004 dirty_tiles worn_tile_floor concrete_floor_damaged_01)
mkdir -p "$OUT"
for m in "${MATERIALS[@]}"; do
  mkdir -p "$OUT/$m"
  for map in diff nor_gl rough; do
    f="$OUT/$m/${m}_${map}_${RES}.jpg"
    if [[ -s "$f" ]]; then echo "skip  $f"; continue; fi
    url="https://dl.polyhaven.org/file/ph-assets/Textures/jpg/${RES}/${m}/${m}_${map}_${RES}.jpg"
    echo "get   $m $map"
    curl -fsSL --retry 3 -o "$f" "$url"
  done
done
echo "Done -> $OUT  (CC0, polyhaven.com)"
echo "UE5 tip: import nor_gl as Normal Map and tick 'Flip Green Channel' (UE uses DirectX normals)."
