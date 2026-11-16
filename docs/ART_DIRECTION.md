# NGMI — Art direction

**One line:** realistic, rusty, abandoned clinic drowned in sick green light, with one warm colour per floor fighting it.

## Pillars

1. **Realistic materials, absurd content.** Photoscanned rust and grime (Megascans) make the silly characters scarier and funnier.
2. **Green is the clinic's breath.** Ring lights, neon, mould, monitors. Green = "the clinic is watching".
3. **Darkness is gameplay.** Light is a resource (flashlight, Oliver's smile, ring lights restore rating).
4. **Every floor has one contrast colour** so screenshots are recognisable.

| Floor | Contrast colour |
| --- | --- |
| L1 Waiting Room | dirty white fluorescent |
| L2 Mewing Catacombs | teal bioluminescence |
| L3 Bone Smash Basement | furnace orange |
| L4 Rating Chamber | surgical cold white |
| L5 Glow-Up Graveyard | moonlight blue |
| L6 Lathered Spa | pink spa neon |
| L7 Runway | stage-spot magenta |
| L8 Front Camera | phone-screen white/blue |

## Lighting reference (from the web preview, translate to UE5)

- Ring light colour: **#46FF86** (emissive), point light ~9 intensity in Three.js units → in UE5 start ~2,000–4,000 cd, attenuation 8–9 m, no shadows on most, shadows on 1 hero light per room.
- Fog: exponential height fog, colour **#041008**, fairly dense.
- Flashlight: warm **#FFF2D6**, inner cone ~15°, outer ~25°, shadows on, slight hand sway.
- One deliberately broken ring light per corridor (flickers dead) for tension.

## Post-process (UE5 Post Process Volume)

- Tonemapper: ACES (default filmic).
- Colour grade: shift midtones/shadows toward green (≈ R×0.82, G×1.08, B×0.88 blended 55%) — build as a LUT.
- Vignette: ~0.5.
- Film grain: subtle (intensity ~0.15–0.25).
- Bloom: on, threshold so only emissives (ring lights, neon, Oliver's teeth) bloom.
- Chromatic aberration: very light, only during scares.
- Exposure: manual or clamped auto-exposure so dark stays dark.

## Materials

- Use Megascans surfaces; tile size ≈ 2 m.
- Add decals (rust streaks, grime, water stains) at every wall-floor seam.
- Wet/puddle layer on L2 and L6.

## Characters

- Semi-realistic proportions with **exaggerated signature features** (Clavicoolar's jaw, Oliver's teeth, Dr. Meow's jaw). Caricature, not likeness — must not look like the real person's face.
- MetaHuman is allowed as a base **only** if the final face is clearly an original caricature.

## Accessibility

- Flicker can be reduced via a photosensitivity setting.
- Never use colour alone to show information (green grade is mood).
