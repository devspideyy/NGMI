# NGMI — Levels (the 8 floors of the Ascension Clinic)

Story order is fixed. In Night Shift (replay) mode, floors 3–7 are shuffled. Each floor ≈ 15 minutes first time. Chico Lackjawski (cryptid) can appear on any floor (1 in 50 runs).

Each floor has: a **host** (main NPC), an **objective**, a **gimmick** (the mechanic that makes it different), a **boss**, the **funniest moment** (the clip we design for), and **UE5 build notes**.

---

## Overview

| # | Floor | Host | Objective | Boss | Funniest moment |
| --- | --- | --- | --- | --- | --- |
| 1 | The Waiting Room | Kareem Shammy | Find your appointment card; learn Routine Combos | Business Card Duel (tutorial) | The receptionist is a skeleton with flawless skin |
| 2 | Mewing Catacombs | Dr. Meow + Grandpa Meow | Sneak past Mouth Breathers silently; tongue-posture door puzzles | Giant Mouth Breather | Grandpa narrates 40 years of theory while you're being chased |
| 3 | Bone Smash Basement | Clavicoolar | Dodge hammer traps; rescue Clav from headshot snipers | The Headhunter Squad | Snipers land perfect headshots, "TOO MUCH BONE" plays, they quit on the spot |
| 4 | The Rating Chamber | Androjenic | Win 3 Mog Battles (stare-down rhythm game) | Androjenic | He rates his own boss music 4/10 and it switches mid-fight |
| 5 | Glow-Up Graveyard | Baby Stinkley + Oliver Forsmile | Swap forms to sneak; teeth are your only light | Your Before Photo | Your Before Photo has better hair than you do now |
| 6 | The Lathered Spa | Dylan Lathered | Slide through foam halls before the spa floods | Dylan's Foam Storm | The whole team slides into the boss room like bowling pins |
| 7 | Runway of the Damned | Jordan Ferret + Sean O'Fry | Win a haunted walk-off while mannequins rate you live | Ferret & O'Fry duo | A mannequin judge's scorecard just says "NGMI" |
| 8 | The Front Camera | Everyone | Reach the Exit Mirror | The Front Camera | Its weak spot: flip it to rear camera and it loses all power |

---

## Floor details

### L1 — The Waiting Room (`L_L1_WaitingRoom`)
- **Purpose:** tutorial for movement, flashlight, interact, Face Rating, Routine Combos.
- **Space:** reception desk, rows of chairs, broken TVs showing before/after ads, a corridor to exam rooms, elevator (locked).
- **Gimmick:** Routine Combo tutorial at sinks (cleanse → tone → serum → SPF).
- **Enemies:** 2–3 Sub-5 Ghouls (slow), Bad Lighting patches.
- **Boss:** Business Card Duel with Kareem Shammy (compare card textures in a QTE; comedic, can't die).
- **Secret:** walk straight back out of the front door within 60 s → **Touch Grass** ending.
- **Assets:** modular hospital (Fab), dirty tiles, concrete walls, chairs, reception desk, "ASCENSION CLINIC – NO REFUNDS" neon sign (in-house).
- **Mood:** fluorescent hum, one flickering green ring light, muzak playing slightly too slow.

### L2 — Mewing Catacombs (`L_L2_MewingCatacombs`)
- **Purpose:** introduce stealth and sound.
- **Space:** old sewer tunnels under the clinic, brick arches, water channels, grates.
- **Gimmick:** Mouth Breathers hunt by sound. Tongue-posture doors open only if the player holds the "mew" input (no sprinting, no talking). Optional mic mode.
- **Enemies:** Mouth Breathers, Recessed Chin Crawlers on ceilings.
- **Boss:** Giant Mouth Breather — lure it with thrown objects into steam vents.
- **Assets:** Fab sewer modular pack (PropHaus) or asylum pack; Megascans brick/wet concrete; rusty pipes.
- **Mood:** dripping water, distant breathing, green bioluminescent mould.

### L3 — Bone Smash Basement (`L_L3_BoneSmashBasement`) ← **first vertical slice**
- **Purpose:** first real combat floor + the signature gag.
- **Space:** boiler room, rusted catwalks, furnace, hammer-press machines, cages.
- **Gimmick:** hammer traps on timers; rescue Clavicoolar; after rescue, his Bone Smash makes snipers' headshots useless.
- **Enemies:** Sub-5 Ghouls, Double Chin Blobs, the Headhunter Squad (4 snipers with laser sights).
- **Boss:** Headhunter Squad. They land perfect headshots on Clavicoolar → slow-mo → "TOO MUCH BONE" ping → snipers look at each other and quit.
- **Assets:** industrial pipes, boiler/furnace (Fab), rusty metal + grate (Megascans/Poly Haven), hammers (in-house).
- **Mood:** orange furnace glow fighting the green ring lights, steam, metal clangs.

### L4 — The Rating Chamber (`L_L4_RatingChamber`)
- **Purpose:** rhythm/stare mechanic + first big boss.
- **Space:** a surgical theatre turned courtroom; observation gallery full of silhouettes holding score paddles.
- **Gimmick:** Mog Battles — hold eye contact (keep crosshair on target) while timing button prompts.
- **Boss:** Androjenic. Phase 2: he rates the boss music 4/10 and it switches genre.
- **Assets:** Fab mortuary/autopsy environment, asylum pack, operating lamps.

### L5 — Glow-Up Graveyard (`L_L5_GlowUpGraveyard`)
- **Purpose:** darkness + light-as-resource.
- **Space:** the clinic's walled rooftop garden turned graveyard for "failed glow-ups"; tombstones carved with before photos.
- **Gimmick:** Baby Stinkley's form swap for stealth; Oliver Forsmile's smile is the only light.
- **Enemies:** Before Photos, Sub-5 Ghouls, Bad Lighting fog.
- **Boss:** your own Before Photo (has better hair than you).
- **Assets:** Megascans graveyard/stone, iron fences, dead trees, fog.

### L6 — The Lathered Spa (`L_L6_LatheredSpa`)
- **Purpose:** movement / sliding chaos.
- **Space:** tiled spa: showers, steam rooms, pools, rusted plumbing; floods over time.
- **Gimmick:** foam floors = sliding; water level rises; escape before it floods.
- **Boss:** Dylan's Foam Storm (foam cannons, slippery arena).
- **Assets:** bathroom/restroom kit (Fab), dirty tiles, worn tile floor, rusted shutters.

### L7 — Runway of the Damned (`L_L7_RunwayOfTheDamned`)
- **Purpose:** spectacle floor before the finale.
- **Space:** abandoned theatre converted to a catwalk; mannequin audience that turns its heads.
- **Gimmick:** walk-off: hit poses on beat while mannequins score you live.
- **Boss:** Jordan Ferret (vents) + Sean O'Fry (eye lasers).
- **Assets:** Fab Theater pack, horror mannequin pack, catwalk (in-house kitbash).

### L8 — The Front Camera (`L_L8_FrontCamera`)
- **Purpose:** finale; every ally returns.
- **Space:** the top floor is the inside of a giant phone: glass walls, notification pop-ups as platforms, a huge front-camera lens.
- **Gimmick:** never look straight at the camera; use mirrors to aim.
- **Boss:** The Front Camera. Weak spot: flip it to rear camera.
- **Exit:** the Exit Mirror. Rating at this moment picks the ending.
- **Assets:** in-house (giant phone arena, Exit Mirror), glass/metal Megascans.

---

## Level build checklist (per floor)

- [ ] Greybox in UE5 with BSP/modeling tools, playable start to finish
- [ ] Enemy placement + boss arena
- [ ] Lighting pass (green ring lights + one contrasting colour per floor)
- [ ] Megascans/Fab dressing
- [ ] Audio pass (ambience, stingers, VO)
- [ ] Funniest-moment clip works and reads in 15 s
- [ ] Playtest: time to complete ≈ 15 min
