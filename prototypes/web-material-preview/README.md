# Web material preview (Three.js)

A quick browser test of the NGMI look: a rusty clinic corridor with real CC0 Poly Haven textures,
flickering green ring lights (one broken), flashlight with shadows, bloom, green grade, film grain, vignette,
rusted shutters, knocked-over chairs, the "ASCENSION CLINIC – NO REFUNDS" sign and the Exit Mirror.

**Purpose:** pick materials and lighting values before building in UE5. It is *not* the game.

Run locally:
```bash
python3 -m http.server 8080   # from this folder
# open http://localhost:8080
```
Controls: drag to look, scroll to zoom, W/S or ↑/↓ to walk. Panel: swap wall/floor materials, toggle flashlight, flicker, 2K textures.

Textures stream from `dl.polyhaven.org` (CC0, CORS-enabled), so an internet connection is needed.
Hosted privately on the owner's Vercel project `ngmi-asset-sandbox` (share links expire after 23 h).

Values worth copying into UE5 are listed in `docs/ART_DIRECTION.md`.
