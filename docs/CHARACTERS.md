# NGMI — Characters

Every character: who they are, how they play, what they say.

**Story structure (D13):** five **allies** each give Kevin one **power** after a moment of trust, then join his phone group chat (GLOW UP GANG). Four **influencer bosses** are *hooked* by the Concierge; beating them frees them, they leave with a funny line, and they return to help in the finale. In the story you always play Kevin. Every character below is **playable in replay modes** (Night Shift, Floor Replay) with the full kit listed in their sheet. Use the **Code ID** everywhere in Unreal (Data Tables, Blueprints, save keys, localisation keys).

> **Parody rule.** Player-facing content uses only the **Game name**. The "Inspired by" column is internal reference for the team and must never appear in the game, store page, trailers, or tags. See [LEGAL.md](LEGAL.md).

---

## Roster at a glance

| Game name | Code ID | Inspired by (internal only) | Known for | Story role | Gives Kevin | Playstyle (replay) |
| --- | --- | --- | --- | --- | --- | --- |
| Kevin "Mid" Averageface | `kevin_mid` | Original character | The player, a 5/10 normie | Player | — | All-rounder |
| Clavicoolar | `clavicoolar` | Clavicular (Braden Peters), streamer | "King of looksmaxxing" | **F3 ally** | Bone Smash | Tank |
| Kareem Shammy ("Skincare Psycho") | `kareem_shammy` | Kareem Shami (@syrianpsycho) | "Godfather of looksmaxxing", skincare | **F1 ally** (tutorial guide) | Routine Combo | Support |
| Androjenic | `androjenic` | Androgenic, streamer | Hardmaxxing, harsh face ratings | **F4 boss** (hooked → freed) | — | Scout |
| Baby Stinkley | `baby_stinkley` | Baby Stickley | Viral before/after glow-up | **F5 ally** | Before Form | Stealth |
| Oliver Forsmile | `oliver_forsmile` | Oliver Forslin | Before/after transformation | **F5 ally** | Smile Flash | Support |
| Dylan Lathered | `dylan_lathered` | Dillon Latham | TikTok looksmaxxer | **F6 boss** (hooked → freed) | — | Mobility |
| **Dr. Mike Meow** (PAID) | `dr_meow` | Mike Mew, orthodontist | Mewing, jaw theory | **F2 ally** · paid hero in replay | Silent Mewing | Tank + control |
| Grandpa Jon Meow | `grandpa_meow` | John Mew | Started the theory | Tannoy voice F2, quests, gum | Grandpa's Gum (item) | Secret unlock |
| Chico Lackjawski | `chico_lackjawski` | Chico Lachowski, model | The ideal face | Cryptid, 1 in 50 runs | — | Secret unlock |
| Jordan Ferret | `jordan_ferret` | Jordan Barrett, model | Model | **F7 boss** (hooked → freed) | — | Infiltrator |
| Sean O'Fry | `sean_ofry` | Sean O'Pry, model | Model, "hunter eyes" | **F7 boss** (hooked → freed) | — | DPS |

---

## Character sheets

Format for each: **Role · Gimmick · Active · Ultimate · Passive (if any) · Weakness · Signature line · Visual notes · Voice notes.**

### Kevin "Mid" Averageface — `kevin_mid`
- **Role:** the player. Clicked an ad for a "free jawline consultation".
- **Passive – Mid Energy:** monsters ignore him 30% of the time.
- **Perk – No Gimmick:** can use every Maxx item.
- **Ultimate – Touch Grass:** once per run, leaves reality for 5 s, full heal. NPCs: "He… went outside?"
- **Weakness:** bosses forget his name mid-monologue. **Ortho Dread:** terrified of orthodontic gear (had braces + headgear in Year 8); near it, his rating drains.
- **Signature line:** "Bro, I just wanted a haircut."
- **Visual:** grey hoodie, average everything, slightly confused face. First-person hands: bitten nails, cheap watch.
- **Voice:** deadpan, tired, mid-20s.

### Clavicoolar — `clavicoolar`
- **Role:** F3 ally. Trapped in a cage by Mid Management's snipers. **Gives Kevin Bone Smash** after Kevin frees him and bonks himself once.
- **Gimmick:** bone smashing, mogging stare.
- **Active – Bone Smash:** hits his own face with a hammer. For 20 s headshots do 0 damage and bullets bounce off with a **"TOO MUCH BONE"** ping (slow-mo + sound sting). Cartoon slapstick only.
- **Ultimate – Ascend:** floats in green light; every enemy in view kneels, mogged, stunned 6 s.
- **Weakness:** stops for 3 s at every mirror to check his jaw.
- **Signature line:** "They shot me in the head. The bullet apologised."
- **Visual:** absurdly sharp jaw, perfect hair, tank top, carries a rubber-gripped hammer.
- **Voice:** calm, confident, monotone; treats everything as a rating.

### Kareem Shammy ("Skincare Psycho") — `kareem_shammy`
- **Role:** F1 ally and tutorial guide; appears in a robe and sheet mask. **Gives Kevin Routine Combo** after the skincare test and the Business Card Duel. Creates the GLOW UP GANG group chat.
- **Gimmick:** the 13-step routine; business-card duel energy.
- **Active – Routine Combo:** player inputs a 4-step combo (cleanse, tone, serum, SPF). Right order = big buff; wrong order = face goes red, −1 rating.
- **Ultimate – Halo Effect:** so pretty that allies within 10 m heal and enemies forget why they were angry.
- **Weakness:** windows burn him if he skipped SPF.
- **Signature line:** "Is that a two-step routine? In this economy?"
- **Visual:** slicked hair, robe, sheet mask, gleaming skin; carries a tiny leather product case.
- **Voice:** smooth, intense, over-precise.

### Androjenic — `androjenic`
- **Role:** F4 boss, **hooked** through a green earpiece that feeds him numbers. Freed when Kevin rates *him* a 7; leaves to "rate a sunset"; returns in the finale.
- **Gimmick:** brutal face ratings.
- **Active – Rate:** scans an enemy and shows its number; anything under 3.0 cries and despawns.
- **Ultimate – Brutal Honesty:** rates the whole room; every enemy is stunned by the insult.
- **Weakness:** rates teammates too: stand near him too long and lose 0.5 rating.
- **Signature line:** "You: 3.5. Your shoes: 6. Your shoes mog you."
- **Visual:** clipboard, laser pointer, lab goggles.
- **Voice:** clinical, bored, judgmental.

### Baby Stinkley — `baby_stinkley`
- **Role:** F5 ally. Has been following Kevin since F1 unnoticed. **Gives Kevin Before Form** because Kevin is the first person who ever noticed him.
- **Gimmick:** before/after glow-up.
- **Active – Form Swap:** Before form is invisible (nobody notices him); After form hits hard but is loud.
- **Ultimate – Glow-Up:** dramatic transformation cutscene; his Before Photo ghost fights for the team.
- **Weakness:** After form runs toward every camera flash.
- **Signature line:** "Don't look at me. No, seriously, it's my build."
- **Visual:** two models (Before: hunched, hoodie; After: glowing, chiselled).
- **Voice:** shy in Before, loud in After.

### Oliver Forsmile — `oliver_forsmile`
- **Role:** F5 ally. **Gives Kevin Smile Flash** after Kevin keeps coffee away from him through the dark graveyard.
- **Gimmick:** blinding smile.
- **Active – Smile Flash:** his teeth are the team's flashlight; stuns Ghouls.
- **Ultimate – Veneer Nova:** one smile so bright it clears the room.
- **Weakness:** battery = tooth whiteness; coffee pickups drain it.
- **Signature line:** "Stay behind me. And bring sunglasses."
- **Visual:** huge white teeth with emissive material; lens flare on smile.
- **Voice:** cheerful, always smiling (audible in the voice).

### Dylan Lathered — `dylan_lathered`
- **Role:** F6 boss, **hooked** through the foam hose in his backpack. Freed when the hose is cut; leaves robes for Kevin's friends; returns in the finale.
- **Gimmick:** skincare foam.
- **Active – Lather:** foams the floor; team slides fast, enemies slip.
- **Ultimate – Triple Cleanse Bubble:** foam bubble shield around the team.
- **Weakness:** foam in his eyes blinds him 4 s.
- **Signature line:** "You've never double cleansed? Then you've never truly lived."
- **Visual:** towel turban, face covered in foam, foam-cannon backpack.
- **Voice:** spa-relaxed, suddenly aggressive about skincare.

### Dr. Mike Meow — `dr_meow` — PAID HERO
- **Role:** F2 ally. **Gives Kevin Silent Mewing** after Kevin follows him across the Mouth Breather nest without a sound. In replay modes he is the **paid hero** with the full kit below.
- **Gimmick:** mewing, MSX (parody of MSE, a palate expander), jaw theory.
- **Passive – Silent Mewing:** tongue on roof of mouth = invisible to Mouth Breathers.
- **Active 1 – Palate Expander:** cranks a key; face widens; shockwave knockback.
- **Active 2 – MSX Mode:** face so wide it blocks bullets for the whole team (moving shield).
- **Ultimate – Jaw Forward:** his whole face slides forward like a battering ram and breaks walls.
- **Extra – Orthotropic Mallet:** a bone-smash hammer that works on *enemies*.
- **Weakness:** opening his mouth (voice chat or emote) resets all buffs.
- **Signature line:** "Mmmhm. Mm-mm." (won't open his mouth)
- **Visual:** lab coat, enormous square jaw, cat-themed name tag (Meow).
- **Voice:** closed-mouth humming only; subtitles translate.
- **Fairness:** side-grade, not pay-to-win (see [MONETIZATION.md](MONETIZATION.md)).

### Grandpa Jon Meow — `grandpa_meow`
- **Role:** voice on the F2 tannoy (never seen in person); lore, side quests, gives Kevin the 40 kg gum used in the finale.
- **Active – Lecture:** gives one quest per run ("chew this 40 kg gum").
- **Ultimate – Original Theory** (secret unlock after 10 quests): resets every face in the room to factory settings.
- **Weakness:** rants 10 s before every action.
- **Signature line:** "In my day we chewed rocks, and we liked it."
- **Visual:** cardigan, pointer stick, skull diagrams.
- **Voice:** old, rambling, proud.

### Chico Lackjawski — `chico_lackjawski`
- **Role:** cryptid. 1-in-50 chance per run to appear in a random room. Screenshot him for a badge.
- **Active – Too Pretty To Kill:** enemies refuse to attack him.
- **Ultimate – Perfect:** ends any fight by standing still.
- **Weakness:** has no flaws, so NPCs have nothing to say; his dialogue boxes are blank.
- **Signature line:** "…" (blank box, choir sound)
- **Visual:** soft god-light follows him; always slightly out of focus (depth of field), like a Bigfoot photo.

### Jordan Ferret — `jordan_ferret`
- **Role:** F7 boss, **hooked** by the Concierge's stage lights. Freed when the lights die; returns in the finale.
- **Active – Vent Crawl:** squeezes through vents; Model Stare freezes one enemy.
- **Ultimate – Catwalk:** walks in slow motion; every bullet misses.
- **Weakness:** chases anything shiny.
- **Signature line:** "Walk with me. Or under me. I'm in the vents."

### Sean O'Fry — `sean_ofry`
- **Role:** F7 boss, **hooked** by the stage lights. Freed by the sandwich walk; returns in the finale.
- **Active – Hunter Eyes:** sees enemies through walls; eye lasers fry them.
- **Ultimate – Deep Fry Stare:** cooks every enemy in a cone, with sizzle sound.
- **Weakness:** if he blinks, powers off for 10 s.
- **Signature line:** "Don't make me blink."

---

## Kevin's earned powers (story)

| Power | From | Earned when | Effect (starting values) | Cooldown |
| --- | --- | --- | --- | --- |
| **Routine Combo** | Kareem Shammy, F1 | Passes the skincare test + card duel | 4-button combo; right = +1.0 rating and +25% speed 15 s; wrong = −1.0 | 30 s |
| **Silent Mewing** | Dr. Mike Meow, F2 | Crosses the Mouth Breather nest silently | Hold: make no sound at all (drains stamina) | — |
| **Bone Smash** | Clavicoolar, F3 | Frees him, bonks himself once | 20 s headshot immunity; head hits PING off | 45 s |
| **Smile Flash** | Oliver Forsmile, F5 | Keeps coffee off him in the dark | Cone of light; stuns Ghouls 3 s | 8 s |
| **Before Form** | Baby Stinkley, F5 | Notices him | 6 s invisible; can't attack | 25 s |
| **Touch Grass** (ultimate) | Kevin's own | Start | Leave reality 5 s, full heal | Once per run |

Controls: powers on 1–5 (or a radial wheel on gamepad), ultimate on Q.

## Unlock conditions (replay modes)

| Character | Unlock |
| --- | --- |
| Kevin | Start |
| Kareem Shammy | Finish Level 1 |
| Clavicoolar | Rescue him on F3 |
| Androjenic | Beat him in Level 4 |
| Baby Stinkley, Oliver Forsmile | Finish Level 5 |
| Dylan Lathered | Beat him in Level 6 |
| Jordan Ferret, Sean O'Fry | Beat them in Level 7 |
| Grandpa Jon Meow | Complete 10 of his quests |
| Chico Lackjawski | Screenshot him 3 times |
| Dr. Mike Meow | Paid hero pack (he is a free ally in the story) |
