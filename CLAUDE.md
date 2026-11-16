# CLAUDE.md — instructions for AI assistants working on NGMI

This file is for Claude (or any AI coding/writing assistant) working in this repository.
Read it fully before doing anything. Then read `README.md`. Then read the doc that matches the task (table in README → "Documents, and when to read each").

---

## 1. What this project is

NGMI is a **first-person horror-comedy game for PC in Unreal Engine 5**, realistic and atmospheric, with a dark eerie-green look. The player is a 5/10 normie (Kevin "Mid" Averageface) trapped overnight in the haunted **Ascension Clinic**, a looksmaxxing clinic, and must reach the Exit Mirror before 6:00 AM. The cast are **parodies** of looksmaxxing influencers with changed names. Campaign target ≈ 2 hours across 8 floors.

Current phase: **pre-production**. There is no UE5 project in the repo yet. Most work right now is design docs, scripts, asset lists, and planning. The first build milestone is the **Level 3 (Bone Smash Basement) vertical slice**.

People:
- **Owner:** @devspideyy (final say on design, money, legal).
- **Collaborator:** @rexyysilent (full contributor).
Both are beginner-to-intermediate. Explain technical things simply, give complete working steps, and avoid jargon without a one-line explanation.

---

## 2. Hard rules (never break these, even if asked casually)

1. **Parody names only in anything player-facing.** Use the names in `docs/CHARACTERS.md` (Clavicoolar, Kareem Shammy, Androjenic, Dr. Mike Meow, etc.). Never write the real influencer names into game text, dialogue, UI strings, store copy, trailers, achievements, file names of shipped content, or Steam tags. Internal design docs may note who a parody is inspired by.
2. **No real likeness.** Never add, generate, or suggest real photos, voice clones, face scans, or deepfakes of real people.
3. **No jokes about real people's real-life legal, medical, or drug events.** Jokes are about the *trend* (jawlines, mewing, ratings, mogging, skincare routines), never about what real people did in real life.
4. **Bone smashing / "hardmaxxing" are cartoon slapstick only.** Never present them as real advice, never add realistic injury detail, never include real substances, injections, peptides or steroids as items. Use clearly fake items (e.g. "Jaw Juice").
5. **Every third-party asset needs a license record** in `docs/ASSETS.md` (source URL, license, date) before it is committed.
6. **Mic features process audio locally only.** Never design anything that uploads or stores player voice.
7. **Keep the repo private.** Don't add public links, telemetry, or secrets.
8. **Never commit secrets** (API keys, tokens, passwords). Use environment variables or UE config not committed.
9. **Never force-push `main`** or rewrite shared history. Work on a branch, open a PR.
10. **Locked decisions** in `docs/DECISIONS.md` are not changed without the owner's explicit OK. If a request conflicts with one, say so and ask.

---

## 3. Tone and comedy guide

- Characters are **deadly serious** about absurd beauty goals. The humour comes from that seriousness, not from insults.
- Horror is real (dark, tense, jump scares), comedy breaks the tension right after.
- Lines are short (one breath), quotable, and clip-friendly.
- Punch at the trend and at vanity, not at anyone's real body, race, disability, or identity.
- Kevin (player) is deadpan and grounded: "Bro, I just wanted a haircut."
- Avoid: slurs, sexual content, real-world tragedy, self-harm references, disordered eating jokes.

Good: *"You walked in: 3.5. The door you walked through: 6. The door mogs you."*
Bad: anything that names a real person or mocks a real person's appearance.

---

## 4. Where things live

| Need | File |
| --- | --- |
| Whole design | `docs/GAME_DESIGN.md` |
| Characters, abilities, lines, code IDs | `docs/CHARACTERS.md` |
| Floors / level design | `docs/LEVELS.md` |
| Dialogue / cutscenes / endings | `docs/SCRIPT.md` |
| Assets to get, licenses | `docs/ASSETS.md` |
| Look & lighting values | `docs/ART_DIRECTION.md` |
| Paid content rules | `docs/MONETIZATION.md` |
| Viral features | `docs/VIRAL_HOOKS.md` |
| Legal / parody / licenses | `docs/LEGAL.md` |
| Why things are decided | `docs/DECISIONS.md` |
| What to do next | `docs/ROADMAP.md` |
| Web material preview (Three.js) | `prototypes/web-material-preview/` |
| Texture download script | `tools/download_textures.sh` |

Code IDs (use these exact snake_case IDs for Blueprints, data tables, save keys, localisation keys):
`kevin_mid, clavicoolar, kareem_shammy, androjenic, baby_stinkley, oliver_forsmile, dylan_lathered, dr_meow, grandpa_meow, chico_lackjawski, jordan_ferret, sean_ofry`.

---

## 5. How to work on tasks

1. **Read before writing.** Open the relevant doc(s) first. Keep new content consistent with existing names, numbers and rules.
2. **Keep docs as source of truth.** If you change design, edit the doc in the same change. If it's a decision, append to `docs/DECISIONS.md` (date, decision, reason, who).
3. **Small, reviewable changes.** One topic per branch/PR. Branch names: `name/topic`.
4. **Unreal work (once the project exists):**
   - Follow the naming prefixes in README → Asset pipeline.
   - Put content under `Content/NGMI/...` folders listed in README.
   - Prefer Blueprints for gameplay until a system clearly needs C++.
   - Data-driven where possible: characters, abilities and upgrades in Data Tables keyed by the code IDs above.
   - Binary assets via Git LFS. Tell the other person before editing a shared `.umap`.
5. **When unsure, ask the human.** Especially for: anything touching rules in section 2, money/pricing, deleting content, or changing locked decisions.
6. **Explain at beginner–intermediate level.** Give complete steps and complete code, not fragments.

---

## 6. Glossary (short)

Face Rating = health+sanity (0–10, start 5.0) · Mog = attack that lowers rating · Maxx = roguelite upgrade · Ascend = best ending / Clavicoolar ult · Exit Mirror = goal · Sub-5 Ghoul = basic enemy · NGMI = "Not Gonna Make It".

Full glossary in README.
