# NGMI — Game Design Document

Last updated: 2026-11-16 · Owner: @devspideyy · Status: pre-production

This is the master design. Detail lives in the linked docs:
[CHARACTERS](CHARACTERS.md) · [LEVELS](LEVELS.md) · [SCRIPT](SCRIPT.md) · [ART_DIRECTION](ART_DIRECTION.md) · [MONETIZATION](MONETIZATION.md) · [VIRAL_HOOKS](VIRAL_HOOKS.md) · [LEGAL](LEGAL.md)

---

## 1. High concept

NGMI is a 1–4 player first-person horror-comedy in Unreal Engine 5. You are trapped overnight in the **Ascension Clinic**, a haunted looksmaxxing clinic lit in eerie green, and must reach the **Exit Mirror** on the top floor before 6:00 AM without your **Face Rating** hitting 0.

**Pitch line:** *"Five Nights at Freddy's meets a looksmaxxing forum — and the forum is trying to kill you."*
(Comparison for internal pitching only; never in marketing.)

**Comedy rule:** every character treats jawlines as life or death. The joke is how serious they are.

**Legal line (credits + store page):** "Parody. Not affiliated with any real person."

---

## 2. Player fantasy and goals

- Fantasy: an ordinary person surviving an absurd, scary world of beauty-obsessed weirdos, and being the only one with common sense.
- Short-term goal: get through the current floor alive.
- Mid-term goal: beat the floor's boss and pick an upgrade.
- Long-term goal: reach the Exit Mirror, unlock all 11 characters, see all 5 endings (one secret).

---

## 3. Story

Theme: **the obsession is the real horror.** Every boss is trapped chasing a number; Kevin wins by caring less than they do.

- **Villain:** the **Concierge**, the clinic's cheerful AI voice on every PA speaker. It rates you, sells to you, and keeps sending the elevator *down*. On Floor 8 it is revealed to be the Front Camera. Motive: "Nobody ever leaves a mirror. That's engagement."
- **Kevin's goal:** he just wanted a haircut. Opens the game, pays off in the post-credits barbershop scene.
- **Allies:** each boss becomes an ally; all of them return (in spa robes) for the final fight.
- **Endings:** Ascend (9+), Cope (<4), Jester (20+ laughs), Fine (everything else), and the secret Touch Grass.

Full scene-by-scene script with line IDs: [SCRIPT.md](SCRIPT.md). Small touches: [DETAILS.md](DETAILS.md).

## 3b. Structure and length

| Mode | Structure | Length |
| --- | --- | --- |
| **Story campaign** | 8 floors in fixed order, with cutscenes | ≈ 2 hours first time (8 × ~15 min) |
| **Night Shift (replay)** | Same floors, floors 3–7 shuffled, random room layouts, roguelite upgrades | 20–40 min per run |
| **Floor replay** | Pick any cleared floor | ~15 min |

Floor order (story): 1 Waiting Room → 2 Mewing Catacombs → 3 Bone Smash Basement → 4 Rating Chamber → 5 Glow-Up Graveyard → 6 Lathered Spa → 7 Runway of the Damned → 8 The Front Camera. Details: [LEVELS.md](LEVELS.md).

---

## 4. Core loop

```
Explore floor → loot Maxx items → sneak or fight monsters → solve the floor's gimmick
      → beat the boss → pick 1 of 3 upgrades → next floor
```

Moment-to-moment: first-person movement, flashlight, interact, crouch, sprint, one active ability, one ultimate. Combat exists but sneaking and gimmicks are often better.

---

## 5. Face Rating (health + sanity)

- Range 0.0–10.0, starts at **5.0**.
- Monsters "mog" you on hit: −0.25 to −1.0 depending on enemy.
- Standing in **Bad Lighting** slowly drains rating; standing under a ring light slowly restores it (cap 7.0 from lighting alone).
- Pickups: skincare (+0.5), water bottle (+0.25), "Jaw Juice" (fake item, +1.0 for 10 s then −0.5 crash).
- At **0** you become a **Sub-5 Ghoul**. Solo: run ends. Co-op: you haunt teammates (slow them, block light) until revived at a mirror.
- **Ortho Dread:** Kevin had braces and headgear as a kid. Near orthodontic horrors (expanders, headgear, retainers, cheek retractors) his screen edges pinch, breathing quickens and rating drains −0.05/s. See [DETAILS.md](DETAILS.md) §13.
- Rating at escape decides the ending (see [SCRIPT.md](SCRIPT.md) → Endings).

UI: a minimalist number top-left with a tiny face icon that gets more "mid" as rating drops. Rating changes pop as "+0.5 GLOW" / "−1.0 MOGGED".

---

## 6. Player character: Kevin "Mid" Averageface (`kevin_mid`)

- 5/10 normie who clicked an ad for a "free jawline consultation".
- **Passive – Mid Energy:** monsters ignore him 30% of the time (too forgettable to hunt).
- **Perk – No Gimmick:** the only character who can use every Maxx item.
- **Ultimate – Touch Grass:** once per run, steps outside reality for 5 s and fully heals. NPCs gasp: "He… went outside?"
- **Weakness:** zero hype. Every boss starts a monologue, then forgets his name mid-sentence.
- Voice: deadpan. First line: "Bro, I just wanted a haircut."
- Arc: every character tries to recruit him into their method; his choices decide the ending.

---

## 7. Cast summary

Eleven characters. Each starts as an NPC or boss and unlocks as playable after you beat or help them. Dr. Mike Meow is the paid hero. Full sheets in [CHARACTERS.md](CHARACTERS.md).

| Character | Story role | Playstyle |
| --- | --- | --- |
| Clavicoolar | L3 ally | Tank |
| Kareem Shammy | L1 tutorial guide | Support |
| Androjenic | L4 boss | Scout |
| Baby Stinkley | L5 NPC | Stealth |
| Oliver Forsmile | L5 co-star | Support (light source) |
| Dylan Lathered | L6 boss → ally | Mobility |
| Dr. Mike Meow (PAID) | Premium hero | Tank + control |
| Grandpa Jon Meow | Hub NPC, quests | Secret unlock |
| Chico Lackjawski | Cryptid (1 in 50 runs) | Secret unlock |
| Jordan Ferret | L7 boss | Infiltrator |
| Sean O'Fry | L7 boss duo | DPS |

---

## 8. Enemies

Eight monster types, each a horror version of a looksmaxxing fear, each with one clear counter.

| Enemy | What it does | Counter | Rating damage |
| --- | --- | --- | --- |
| **Sub-5 Ghoul** | Crawls in packs; every touch drops rating | Light: Oliver's smile, ring lights | −0.5 |
| **Mouth Breather** | Blind, hunts by sound. Optional mic mode: hears your real voice (local processing only) | Stay silent (mew); Dr. Meow is immune | −1.0 |
| **The Bad Lighting** | Living shadow; standing in it drains rating | Stand under a ring light | −0.1/s |
| **Double Chin Blob** | Splits in two every time you hit it | Aim chin-up: headshots only | −0.5 |
| **Recessed Chin Crawler** | Hangs on the ceiling, drops on you | Look up; flashlight scares it | −0.75 |
| **Mirror Self** | Your reflection; moves only when you look away | Keep eyes on it while backing off | −1.0 |
| **Before Photo** | Your old self, haunting Level 5 | Out-glow it: Glow-Up or Smile Flash | −0.5 |
| **The Headgear** | Floating reverse-pull face mask; its rubber bands pull you toward it. Recurring stalker (L2, L4, L8) | Cut the bands (scissors); hide behind pillars | −0.5 + pull |
| **Expander Spiders** | Expander-shaped crawlers; latch onto your face and stretch your FOV wider and wider | Mash to shake off; flashlight scatters them | −0.25/s latched |
| **Retainer Chatterers** | Chattering clear retainers; harmless alone, nibble in swarms; drawn to noise | Stomp; throw something to lure them | −0.1 each |
| **Brace Face** | Mannequins in cheek retractors; move when unobserved, smile widens each time | Keep them in view | −0.75 |
| **The Front Camera** | Elite stalker phone; if it catches you, plays your worst-angle jumpscare and halves your rating | Never face it directly; it is the final boss | ×0.5 |

---

## 9. Upgrades ("Maxxes") — pick 1 of 3 after each floor

| Maxx | Effect |
| --- | --- |
| Sleepmaxxing | Regenerate rating while crouched |
| Hydromaxxing | Water bottles become throwable grenades |
| Jestermaxxing | Emotes stun enemies for 2 s |
| Hairmaxxing | Your hair absorbs one hit per floor |
| Mogmaxxing | Stare at an enemy 2 s to stun it |
| Posturemaxxing | +15% sprint speed, −noise |
| Skinmaxxing | Healing pickups +50% |
| Lookmaxxing Lite | +0.5 starting rating next floor |

More can be added; each must be one sentence and one number.

---

## 10. Replayability systems

- **Random clinic** (Night Shift mode): floors built from shuffled room tiles; floors 3–7 in random order.
- **Daily Face:** one global rule per day (e.g. *Bad Lighting Night*: half the lamps off; *Mirror Tuesday*: double mirrors).
- **11 playable characters**, each needs a different route (tank, stealth, support, scout, DPS).
- **5 endings (one secret) + collectibles:** 50 hidden Before Photos; Chico sightings (1 in 50 runs).
- **Co-op 1–4** with friendly mogging on: teammates can lower each other's rating.
- **Ascension levels 1–10:** harder runs that unlock jaw and hammer skins.

---

## 11. Viral hooks (summary)

Rating Card share image after every run, Mog Cam (one key saves last 30 s), Streamer Chat Mode (Twitch/Kick chat votes horror events every 60 s), mic-reactive Mouth Breathers, "TOO MUCH BONE" slow-mo gag, Chico cryptid sightings, Touch Grass secret ending. Full spec: [VIRAL_HOOKS.md](VIRAL_HOOKS.md).

---

## 12. Monetization (summary)

Paid base game; Dr. Mike Meow hero pack; cosmetic jaw and hammer skins; seasonal Ascension Pass. Paid heroes are side-grades; every level is beatable free. Prices not set yet. Full spec: [MONETIZATION.md](MONETIZATION.md).

---

## 13. Technical targets

- Unreal Engine 5, Lumen + Nanite, Windows PC first.
- Target: 60 fps at 1080p on a GTX 1660 / RX 5600-class GPU with Lumen on "Medium"; scalability settings for lower.
- Save system: per-character unlocks, collectibles, endings, settings.
- Input: keyboard/mouse first, gamepad second.
- Accessibility: subtitles on by default, jump-scare intensity slider, colour-blind-safe UI (the green grade is mood, not information), photosensitivity toggle for flicker.

---

## 14. Out of scope for v1

PvP, VR, mobile, consoles, user-generated content, real-money trading.
