# NGMI

**Brainrot looksmaxxing horror comedy game in UE5.**

> A 3D first-person **horror-comedy** game for PC, built in **Unreal Engine 5**.
> You are a 5/10 normie trapped overnight in a haunted looksmaxxing clinic.
> Escape before sunrise, or stay mid forever.

**Status:** pre-production (design + asset sourcing). No UE5 project yet.
**Owner:** [@devspideyy](https://github.com/devspideyy) · **Collaborator:** [@rexyysilent](https://github.com/rexyysilent)
**Repo visibility:** private. Do not make it public (see [Legal](docs/LEGAL.md)).

---

## Table of contents

1. [The game in 60 seconds](#the-game-in-60-seconds)
2. [Locked decisions](#locked-decisions)
3. [Open decisions](#open-decisions)
4. [Repo map](#repo-map)
5. [Documents, and when to read each](#documents-and-when-to-read-each)
6. [Live previews and links](#live-previews-and-links)
7. [How we work (people and AI assistants)](#how-we-work-people-and-ai-assistants)
8. [Getting started](#getting-started)
9. [Asset pipeline](#asset-pipeline)
10. [Unreal Engine 5 setup (planned)](#unreal-engine-5-setup-planned)
11. [Roadmap](#roadmap)
12. [Rules that must never be broken](#rules-that-must-never-be-broken)
13. [Glossary](#glossary)

---

## The game in 60 seconds

| | |
| --- | --- |
| **Genre** | First-person horror-comedy, light roguelite structure |
| **Platform** | PC (Windows first). Steam is the target store |
| **Engine** | Unreal Engine 5 (Lumen + Nanite) |
| **Look** | Realistic, atmospheric, **dark eerie green** colour grade. Not low-poly, not PSX |
| **Length** | Full campaign ≈ **2 hours** (8 floors × ~15 min). Floors are replayable |
| **Players** | Designed for 1–4 co-op. Solo is the v1 target (see open decisions) |
| **Tone** | Every character treats jawlines as life or death. The joke is how serious they are |
| **Setting** | *The Ascension Clinic*: an abandoned 24/7 looksmaxxing clinic, rusty, flooded with green ring-light glow. Neon sign: "ASCENSION CLINIC – NO REFUNDS" |
| **Goal** | Reach the **Exit Mirror** on the top floor before 6:00 AM without your **Face Rating** hitting 0 |
| **Cast** | 11 parody characters inspired by looksmaxxing influencers, with **changed names** (e.g. Clavicoolar, Kareem Shammy, Dr. Mike Meow) |
| **Signature gag** | Clavicoolar bone-smashes his own face with a hammer; for 20 s headshots do 0 damage and bullets bounce off with a "TOO MUCH BONE" ping |
| **Business** | Paid base game + paid hero (Dr. Mike Meow) + cosmetics + seasonal pass. Paid heroes are side-grades, never pay-to-win |
| **Virality** | Shareable Rating Cards, one-key clips ("Mog Cam"), Twitch/Kick chat-controlled scares, mic-reactive monsters, rare "Chico" cryptid sightings |

Full detail: **[docs/GAME_DESIGN.md](docs/GAME_DESIGN.md)**.

---

## Locked decisions

These are decided. Do not change them without the owner agreeing. Dates are when they were decided. Full log: [docs/DECISIONS.md](docs/DECISIONS.md).

| # | Decision | Date |
| --- | --- | --- |
| D1 | Engine is **Unreal Engine 5** | 2026-11-16 |
| D2 | Art style is **realistic and atmospheric**, not low-poly / PSX / stylized | 2026-11-16 |
| D3 | Characters use **parody names**, close enough to recognise, different enough to be parody | 2026-11-16 |
| D4 | No real photos, voices, likeness scans or real names in the game or store page | 2026-11-16 |
| D5 | Jokes target the **looksmaxxing trend**, never the real people's real-life controversies (arrests, hospital visits, drugs) | 2026-11-16 |
| D6 | Campaign length target ≈ 2 hours, 8 floors | 2026-11-16 |
| D7 | Colour identity: dark eerie green, green ring lights, film grain, vignette | 2026-11-16 |
| D8 | Primary asset source: **Quixel Megascans on Fab** (free again since 12 Nov 2026), then Poly Haven / ambientCG (CC0) | 2026-11-16 |

## Open decisions

| # | Question | Default if nobody decides |
| --- | --- | --- |
| O1 | Solo-only v1, or co-op from day one? Co-op roughly doubles the work | Solo v1, co-op later |
| O2 | Price points for base game, hero pack, cosmetics | Decide after checking comparable Steam horror-comedies |
| O3 | Mic mode (monsters hear your real voice): ship in v1? Must be local-only audio | Yes, opt-in, local only |
| O4 | Voice acting: real actors or AI voices (ElevenLabs is available to the owner) | AI temp voices, real actors for launch |
| O5 | Which floor is the first vertical slice | Level 3, Bone Smash Basement (has the signature gag) |

---

## Repo map

```
ngmi/
├── README.md                  ← you are here: start here
├── CLAUDE.md                  ← rules + context for AI coding assistants (Claude etc.)
├── .gitignore                 ← Unreal Engine 5 ignore rules
├── .gitattributes             ← Git LFS rules for .uasset/.umap/textures/audio
├── docs/
│   ├── GAME_DESIGN.md         ← full GDD: concept, player, cast, enemies, levels, script, systems
│   ├── CHARACTERS.md          ← every character: role, gimmick, abilities, lines, code IDs
│   ├── LEVELS.md              ← all 8 floors in detail, with UE5 build notes
│   ├── SCRIPT.md              ← full campaign script with line IDs: prologue, 8 floors, endings, barks
│   ├── DETAILS.md             ← little details: UI, audio, easter eggs, achievements (cost + priority)
│   ├── ASSETS.md              ← asset sourcing list for UE5 realistic (what to get, from where, license)
│   ├── ART_DIRECTION.md       ← lighting, colour grade, materials, reference values
│   ├── MONETIZATION.md        ← what is sold, rules for fairness
│   ├── VIRAL_HOOKS.md         ← features designed to create clips and shares
│   ├── LEGAL.md               ← parody rules, asset licenses, privacy
│   ├── DECISIONS.md           ← decision log (append-only)
│   └── ROADMAP.md             ← milestones and task breakdown
├── tools/
│   └── download_textures.sh   ← downloads the 10 CC0 Poly Haven test materials (2K)
└── prototypes/
    └── web-material-preview/
        ├── index.html         ← Three.js corridor used to test materials + lighting mood
        └── README.md
```

The UE5 project itself does not exist yet. When it is created it goes in `/Game/` at the repo root as `NGMI.uproject` (see [UE5 setup](#unreal-engine-5-setup-planned)).

---

## Documents, and when to read each

| If you want to… | Read |
| --- | --- |
| Understand the whole game | [docs/GAME_DESIGN.md](docs/GAME_DESIGN.md) |
| Write dialogue, barks, or a character | [docs/CHARACTERS.md](docs/CHARACTERS.md) + [docs/SCRIPT.md](docs/SCRIPT.md) |
| Add polish, jokes, easter eggs, achievements | [docs/DETAILS.md](docs/DETAILS.md) |
| Build or block out a level | [docs/LEVELS.md](docs/LEVELS.md) + [docs/ART_DIRECTION.md](docs/ART_DIRECTION.md) |
| Find or buy assets | [docs/ASSETS.md](docs/ASSETS.md) |
| Check if a joke, name or asset is allowed | [docs/LEGAL.md](docs/LEGAL.md) |
| Know what to do next | [docs/ROADMAP.md](docs/ROADMAP.md) |
| Know why something is the way it is | [docs/DECISIONS.md](docs/DECISIONS.md) |
| Use an AI assistant on this repo | [CLAUDE.md](CLAUDE.md) |

---

## Live previews and links

| What | Where | Notes |
| --- | --- | --- |
| Web material/lighting preview | Vercel project `ngmi-asset-sandbox` (owner's account) | Private. Opened with a share link that expires after 23 h; ask the owner for a fresh one. Source is in `prototypes/web-material-preview/` |
| Original design doc + asset sheet | Owner's Claude workspace | Mirrored in full in `docs/` here, so you never need those links |

---

## How we work (people and AI assistants)

- **Branches:** `main` is always the agreed state. Do work on a branch named `yourname/short-topic` (e.g. `rexy/level3-blockout`) and open a pull request into `main`.
- **Never force-push `main`.** Never rewrite shared history.
- **Commits:** short imperative subject, e.g. `Add Level 3 enemy list`. One topic per commit.
- **Docs are the source of truth.** If you change the design, update the matching file in `docs/` in the same PR, and add a line to `docs/DECISIONS.md` if it is a decision.
- **Big binary files** (`.uasset`, `.umap`, textures, audio, video) go through **Git LFS** (already configured in `.gitattributes`). Run `git lfs install` once.
- **Unreal locking:** binary assets cannot be merged. Before editing a `.umap` or shared `.uasset`, tell the other person (or use `git lfs lock <file>`).
- **AI assistants:** read [CLAUDE.md](CLAUDE.md) first. It tells Claude (or any assistant) the rules, the tone, and what not to do.

---

## Getting started

```bash
# 1. Clone (private repo: you must have accepted the collaborator invite)
git clone https://github.com/devspideyy/ngmi.git
cd ngmi

# 2. Git LFS (needed before any Unreal content lands)
git lfs install

# 3. Optional: grab the CC0 test textures used by the web preview (~76 MB)
bash tools/download_textures.sh        # creates ./ngmi_textures/<material>/

# 4. Optional: open the web preview locally
cd prototypes/web-material-preview && python3 -m http.server 8080
# then open http://localhost:8080
```

---

## Asset pipeline

1. **Megascans on Fab first.** Log in at <https://www.fab.com> with your own Epic account and claim the Megascans you need, or use the **Fab plugin inside UE5**. Megascans became free again on 12 Nov 2026 under the Fab Standard License (usable in any engine).
2. **Poly Haven / ambientCG** for anything Megascans lacks. Both are **CC0** (no credit needed).
3. **Fab paid packs** for big modular sets (hospital, asylum, sewer, theater, mannequins). See [docs/ASSETS.md](docs/ASSETS.md) for the shortlist with links.
4. **Build in-house** (Blender → UE5): ring lights, neon sign, mirrors/Exit Mirror, catwalk, giant-phone boss arena, tongue-puzzle doors.
5. **Record every third-party asset** in `docs/ASSETS.md` with source, license and date before it is committed. No unlicensed assets, ever.

Naming convention inside UE5 (standard Epic style):
`SM_` static mesh · `SK_` skeletal mesh · `M_` material · `MI_` material instance · `T_` texture (`_D` diffuse, `_N` normal, `_ORM` packed AO/rough/metal) · `BP_` blueprint · `WBP_` widget · `NS_` Niagara · `SFX_` / `MUS_` audio · `L_` level.

---

## Unreal Engine 5 setup (planned)

Not created yet. When it is:

- Engine: latest stable **UE 5.x** at the time, both of us on the **same version**.
- Template: First Person, Blueprint (C++ added later only if needed).
- Rendering: Lumen GI + reflections, Nanite for static meshes, Virtual Shadow Maps.
- Post-process: green grade via a LUT, film grain, vignette, bloom. Reference values in [docs/ART_DIRECTION.md](docs/ART_DIRECTION.md).
- Folder layout under `Content/NGMI/`: `Characters/`, `Enemies/`, `Levels/L1_WaitingRoom` … `L8_FrontCamera`, `Props/`, `Materials/`, `UI/`, `Audio/`, `Systems/`.
- Do **not** commit `Binaries/`, `Intermediate/`, `Saved/`, `DerivedDataCache/` (already in `.gitignore`).

---

## Roadmap

| Milestone | Goal | Status |
| --- | --- | --- |
| M0 Pre-production | Design doc, cast, script, asset list, mood test | ✅ done |
| M1 UE5 project + Level 3 vertical slice | Bone Smash Basement playable: movement, Face Rating, 2 enemies, "TOO MUCH BONE" gag, boss | ⏳ next |
| M2 Core systems | Rating meter, upgrades (Maxxes), save, settings, Rating Card share | — |
| M3 All 8 floors blocked out | Greybox the full 2-hour campaign | — |
| M4 Art + audio pass | Megascans dressing, lighting, VO, music | — |
| M5 Viral features | Mog Cam clips, streamer chat mode, Chico cryptid | — |
| M6 Steam page + demo | Store page, trailer, Next Fest demo | — |

Task breakdown: [docs/ROADMAP.md](docs/ROADMAP.md).

---

## Rules that must never be broken

1. **Never use real names** of the influencers anywhere players can see it (game text, VO, store page, trailer, tags, achievements). Internal docs may mention who a parody is based on.
2. **Never use real photos, voice clips, or face scans** of real people.
3. **Never joke about real people's real-life legal or medical events.**
4. **Every third-party asset must have a recorded license** in `docs/ASSETS.md`.
5. **Mic audio stays on the player's machine.** Never upload it.
6. **Keep this repo private.**

Details: [docs/LEGAL.md](docs/LEGAL.md).

---

## Glossary

| Term | Meaning |
| --- | --- |
| **Looksmaxxing** | Internet trend about maximising physical attractiveness |
| **Mog / mogging** | Being better-looking than someone; in-game, an attack that lowers your rating |
| **Mewing** | Tongue-posture technique for jawline; Dr. Meow's whole kit |
| **Bone smashing** | Meme of hitting your face to "grow bone"; Clavicoolar's gag. Shown as cartoon slapstick only, never as advice |
| **Ascend** | Become hotter; in-game, Clavicoolar's ultimate and the best ending |
| **Face Rating** | The game's health + sanity meter, 0–10, starts at 5.0 |
| **Maxx** | A roguelite upgrade picked after each floor (Sleepmaxxing, Hydromaxxing, …) |
| **Sub-5 Ghoul** | Basic enemy; what you become at rating 0 |
| **Exit Mirror** | The goal at the top of the clinic |
| **NGMI** | "Not Gonna Make It". The title, and what the game tells you when you die |

---

*Parody. NGMI is not affiliated with, endorsed by, or about any real person.*
