# NGMI — Full Script (v2)

Last updated: 2026-11-17 · Status: first full draft, ready for table-read

This is the whole campaign, scene by scene: prologue, 8 floors, the elevator rides between them, boss fights, 5 endings (one secret) and a post-credits scene. Then the reusable lines: barks, clinic announcements and death-screen lines.

Rules (from [CLAUDE.md](../CLAUDE.md)): parody names only · jokes about the trend, never about real people's real lives · bone smashing is cartoon slapstick · lines short enough to clip.

---

## How to read this

- **`[L3_CLAV_012]`** = a line ID. Use it as the audio file name and the localisation key in UE5 (`VO_L3_CLAV_012`). Format: `<scene>_<speaker>_<number>`.
- Speaker codes: `KEV` Kevin · `CON` the Concierge (clinic voice) · `BREN` Brenda · `TXT` group-chat text (shown on Kevin's phone, not voiced) · `KAR` Kareem Shammy · `CLAV` Clavicoolar · `ANDR` Androjenic · `STINK` Baby Stinkley · `OLI` Oliver Forsmile · `DYL` Dylan Lathered · `MEOW` Dr. Mike Meow · `GRAN` Grandpa Jon Meow · `FER` Jordan Ferret · `FRY` Sean O'Fry · `HH` Headhunter · `BP` Before Photo · `MANQ` mannequin.
- *Italics in brackets* = stage directions / what the player sees.
- **(sub)** = subtitle only, no voice (used for Dr. Meow's hums and Chico).
- **(bark)** = can repeat during gameplay; **(once)** = plays one time per save.
- Lines in a scene marked **Gameplay** play during control, not in a cutscene. Keep them under 4 seconds.

---

## Story spine

**Theme:** the obsession is the real horror. Every boss is trapped chasing a number. Kevin wins by caring less than they do.

**Villain:** **the Concierge**, the clinic's cheerful AI voice. It talks through ceiling speakers on every floor, rates you constantly, and sells you things. On Floor 8 it is revealed to *be* the Front Camera. Its motive: "Nobody ever leaves a mirror. That's engagement."

**Kevin's goal, in his words:** he just wanted a haircut. That line opens the game and pays off in the post-credits scene.

### Allies, bosses and powers

The influencers are split in two:

- **Allies (5)** help Kevin. Each one gives him a **power** after a specific moment of trust, then joins his phone group chat, **GLOW UP GANG**, and keeps texting hints and jokes for the rest of the game. They come back in person for the finale.
- **Influencer bosses (4)** are **hooked**: the Concierge feeds their obsession through an earpiece, a clipboard, foam pipes or stage lights. Beating them **frees** them. They get one funny line and leave, then return to help in the finale.
- **Monster bosses (4) + the Headhunters** are pure horror: Brenda, the Giant Mouth Breather, your Before Photo, and the Front Camera.

| Floor | Ally → power Kevin earns | How he earns it | Boss |
| --- | --- | --- | --- |
| F1 | Kareem Shammy → **Routine Combo** (heal + speed) | Passes the skincare test and the card duel | **Brenda** (monster) |
| F2 | Dr. Mike Meow → **Silent Mewing** (total silence) | Follows Meow through the Mouth Breather nest without a sound | **Giant Mouth Breather** (monster) |
| F3 | Clavicoolar → **Bone Smash** (headshot immunity) | Frees him from the cage and bonks himself once | **Headhunter Squad** |
| F4 | — | — | **Androjenic** (hooked influencer) |
| F5 | Oliver Forsmile → **Smile Flash** (light + stun) · Baby Stinkley → **Before Form** (invisibility) | Keeps coffee away from Oliver in the dark · Is the first person who ever noticed Stinkley | **Your Before Photo** (monster) |
| F6 | — | — | **Dylan Lathered** (hooked influencer) |
| F7 | — | — | **Jordan Ferret + Sean O'Fry** (hooked influencers) |
| F8 | Everyone returns: allies + freed bosses + Grandpa's gum | — | **The Front Camera** (the Concierge) |

Kevin keeps **Touch Grass** (once-per-run full heal) as his own ultimate. By Floor 8 he uses all five powers.

### Running gags (set up → pay off)

| Gag | Set up | Pays off |
| --- | --- | --- |
| "I just wanted a haircut" | Prologue | Post-credits barbershop scene |
| Kevin's ticket number is **5** ("Mid") | L1 check-in; the machine prints 5 again after Brenda | L8: the Concierge calls "Number 5" one last time; Kevin rips the ticket |
| Sandwich-shop loyalty card (9 of 10 stamps) | L1 Business Card Duel | L7 sandwich walk; Ascend ending's tenth stamp |
| Grandpa's 40 kg gum quest | L2 | L8: Kevin uses the gum to jam the Front Camera's lens |
| Clavicoolar checks every mirror | L3 | L8: he refuses to look into the Front Camera: "First mirror I've ever skipped." |
| GLOW UP GANG group chat | L1, when Kareem adds Kevin | Grows with every ally; L8 everyone shows up in person |
| Androjenic rates everything | L4 | L4 outro: Kevin rates *him*, and it frees him |
| Chico sightings | any floor, rare | Every character reacts differently (see Chico section) |
| One broken ring light per corridor | L1 | L8: the Concierge's "eye" flickers the same way when it's losing |

Jump-scare placements for every floor: [JUMPSCARES.md](JUMPSCARES.md). In this script they're marked **⚡JS_xx**.

---

## PROLOGUE — "Free Consultation"

*[Black screen. A phone vibrates. Lock screen: 2:47 AM. A notification slides in: "ARE YOU A 5? 👀 FREE JAWLINE CONSULTATION. TONIGHT ONLY."]*

`[P_CON_001]` **CON** *(too cheerful, from the phone)*: "Are you a five? Want to be a ten? Free jawline consultation. Tonight only. Ascension Clinic."

*[Kevin, in a grey hoodie, stands on a wet street. A building glows sick green. Neon: ASCENSION CLINIC — OPEN 24/7 — NO REFUNDS. One letter flickers so it briefly reads "NO REFUND".]*

`[P_KEV_001]` **KEV**: "Bro, I just wanted a haircut."

*[He looks at the barbershop across the street. Sign: CLOSED. He looks back at the clinic. The automatic doors open by themselves. He sighs and walks in.]*

*[Doors slam. A ring light switches on above him with a heavy CLUNK. Green floods the room.]*

`[P_CON_002]` **CON**: "Welcome to the Ascension Clinic! Scanning face…"
*[A green laser line sweeps his face. A loading bar fills. Stops at 50%.]*
`[P_CON_003]` **CON**: "Your rating is… five. Mid. Perfectly, aggressively mid."
`[P_KEV_002]` **KEV**: "Can I get a second opinion?"
`[P_CON_004]` **CON**: "Second opinion: five."
`[P_CON_005]` **CON**: "Your consultation ends at sunrise. Reach the Exit Mirror on the top floor before then, or stay… mid… forever."
`[P_KEV_003]` **KEV**: "That's not how consultations work."
`[P_CON_006]` **CON**: "That's how *this* one works! Please take a number."

*[A ticket machine spits out a ticket: 5. Title card: **NGMI**.]*

---

## FLOOR 1 — The Waiting Room

### 1.1 Check-in (cutscene → gameplay)

*[A reception desk. Behind it, a skeleton in scrubs with flawless, glowing skin stretched over its skull. It holds a clipboard.]*

`[L1_KEV_001]` **KEV**: "…Is she okay?"
`[L1_CON_001]` **CON**: "Brenda has been waiting for her results since 1997. Look at that skin. Worth it."
`[L1_KEV_002]` **KEV**: "She's dead."
`[L1_CON_002]` **CON**: "She's *glowing*."

⚡**JS_01** Kevin looks at the TV ads; when he turns back, Brenda's chair has rotated to face him. Her head tilts. "Number?" — "…Five." — "Mid." She turns back.

**Gameplay** — first steps. Ambient muzak plays at 80% speed.

`[L1_CON_003]` **CON** (once, on first flashlight use): "Flashlights are free! Ring lights are better. Ring lights are love."
`[L1_CON_004]` **CON** (once, on first rating drop): "Ooh. Bad lighting. Minus point one. Your pores are showing."

*[Behind the desk, a box labelled LOST & FOUND: RETAINERS. As Kevin passes, every clear retainer in it snaps open and shut at once. Clack-clack-clack.]*
`[L1_KEV_010]` **KEV** (once): "Nope. Retainers. I'm not looking at the retainers."
`[L1_CON_007]` **CON**: "Unclaimed retainers! Free to a good mouth!"

### 1.2 Kareem Shammy

*[Fog rolls out of a treatment room. A man in a white robe and a sheet mask steps out, holding a tiny leather product case like a briefcase.]*

`[L1_KAR_001]` **KAR**: "Stop. Don't move. What is your routine?"
`[L1_KEV_003]` **KEV**: "Shower?"
`[L1_KAR_002]` **KAR**: "Shower. *Shower.* That's not a routine. That's an accident."
`[L1_KAR_003]` **KAR**: "Is that… a two-step routine? In this economy?"
`[L1_KAR_004]` **KAR**: "Follow me. And do NOT touch the cleanser. The cleanser touches *you*."

**Gameplay — Routine Combo tutorial** at four sinks.

`[L1_KAR_005]` **KAR**: "Cleanse. Tone. Serum. SPF. Say it with me."
`[L1_KEV_004]` **KEV**: "I'm not saying it with you."
`[L1_KAR_006]` **KAR** (bark, combo success): "Yes. Feel that? That's called hope."
`[L1_KAR_007]` **KAR** (bark, combo success): "Glistening. Disgusting. Perfect."
`[L1_KAR_008]` **KAR** (bark, combo fail): "Serum before toner? Are you trying to die?"
`[L1_KAR_009]` **KAR** (bark, combo fail): "You've angered the barrier. The skin barrier. It remembers."

### 1.3 First Ghoul

*[Something crawls across the far end of the corridor on all fours. Grey, patchy skin, a hoodie hood over its head. It sniffs. Turns. Its face is completely average.]*

`[L1_KEV_005]` **KEV**: "What is THAT?"
`[L1_KAR_010]` **KAR**: "A Sub-5. They skipped face day. Every day."
`[L1_KAR_011]` **KAR**: "Don't let it touch you. Mid is contagious."

**Gameplay** — first Ghoul encounter. Ring lights scare it off. ⚡**JS_02** in the staff toilet, Kevin's reflection lags one frame, then slams its palm on the glass. Then it fixes its hair.

`[L1_KAR_012]` **KAR** (once, when Kevin stands under a ring light): "See? Light heals. Light forgives. Light is your father now."

### 1.4 Kareem's test — the Business Card Duel

*(Not a boss. A comedy test Kareem runs before he trusts Kevin.)*

*[A waiting room with two chairs facing each other like a western standoff. Tumbleweed made of cotton pads rolls past.]*

`[L1_KAR_013]` **KAR**: "Before I trust you with anything, a formality."
*[He slides a card out of his robe. Slow-motion close-up. Matte black. Embossed.]*
`[L1_KAR_014]` **KAR**: "Look at the texture. The matte finish. The embossing. Now. Show me yours."

*[QTE: Kevin pats his pockets. Finds a crumpled card. Close-up: a sandwich-shop loyalty card. Nine stamps. One empty circle.]*

`[L1_KEV_006]` **KEV**: "It's a sandwich card."
`[L1_KAR_015]` **KAR**: "Nine… out of ten."
*[Kareem's hand starts shaking. Sweat beads on his sheet mask.]*
`[L1_KAR_016]` **KAR**: "You're one away. One away from… a ten. Who ARE you?"
`[L1_KEV_007]` **KEV**: "The tenth one's free."
*[Kareem drops to his knees.]*
`[L1_KAR_017]` **KAR**: "Free. He said free. Nothing's ever free here."

**Gameplay:** short card-texture rhythm prompts. Kareem can only lower Kevin's rating with insults; you can't die here.
`[L1_KAR_018]` **KAR** (bark): "Your card has a coffee stain. *A coffee stain.*"
`[L1_KAR_019]` **KAR** (bark): "Laminated? Who raised you?"

### 1.5 Power: Routine Combo

`[L1_KAR_020]` **KAR**: "No routine. No card. No future. But you have… potential. Nine stamps of it."
*[He presses a tiny glass bottle into Kevin's palm. It glows green. UI: **POWER UNLOCKED — ROUTINE COMBO**.]*
`[L1_KAR_021]` **KAR**: "Cleanse. Tone. Serum. SPF. Use it when you're dying. Which will be often."
`[L1_KEV_011]` **KEV**: "Are you coming with me?"
`[L1_KAR_022]` **KAR**: "Upstairs? The lighting up there is *hostile*. Text me."
*[Kevin's phone buzzes. "Kareem Shammy added you to **GLOW UP GANG** 🧴". Kareem walks back into the fog.]*

### 1.6 Boss — Brenda

*[Kevin passes the reception desk on the way to the elevator. Brenda's chair is facing the wall. ⚡**JS_03** Every light cuts out. A single ding.]*

`[L1_CON_008]` **CON** *(at full volume)*: "NOW SERVING… NUMBER… FIVE."
*[Emergency light flickers on. Brenda is standing on the desk. Way too tall. Her joints crack like knuckles. Her skin is flawless and glowing over a bare skull.]*
`[L1_BREN_001]` **BREN** *(sweet, then not)*: "Thirty years. Thirty years I've been waiting for my results. And YOU get called first?"
`[L1_KEV_012]` **KEV**: "I didn't even want to be here."
`[L1_BREN_002]` **BREN**: "NOBODY WANTS TO BE HERE."

**Phase 1 — The flicker.** Whenever the lights flicker, Brenda teleports to a different desk. Stay under working lights. Use **Routine Combo** to heal.
`[L1_BREN_003]` **BREN** (bark, teleporting): "Please hold."
`[L1_BREN_004]` **BREN** (bark): "Your call is important to us."
`[L1_BREN_005]` **BREN** (bark): "Have you tried… waiting?"

**Phase 2 — Rejected.** She throws giant rubber stamps that land with "REJECTED" in red, and rings a bell that calls swarms of Retainer Chatterers.
`[L1_BREN_006]` **BREN** (bark): "Rejected. Rejected. Mid. Rejected."
`[L1_KAR_023]` **KAR** *(text, phone pops up in the corner)*: "Moisturise between dodges. Trust me."

**Phase 3 — Now serving.** Kevin reaches the NOW SERVING bell on the counter and holds out his ticket.
`[L1_KEV_013]` **KEV**: "Here. You go first."
`[L1_BREN_007]` **BREN** *(small)*: "…Me?"
`[L1_CON_009]` **CON** *(sulky)*: "Fine. Brenda. Your results are ready. You're… a ten."
`[L1_BREN_008]` **BREN** *(happy sigh)*: "I knew it."
*[She crumbles into glittering dust. Only her clipboard is left. The ticket machine whirs and prints Kevin a new ticket: 5.]*
`[L1_KEV_014]` **KEV**: "Why didn't anyone just let her go first?"
`[L1_CON_010]` **CON**: "Engagement!"

### 1.7 Secret — Touch Grass

If the player walks back out of the front door within 60 seconds of the prologue:

`[L1_CON_005]` **CON**: "Wait. Where are you going?"
`[L1_KEV_008]` **KEV**: "Outside."
`[L1_CON_006]` **CON**: "But… the consultation."
`[L1_KEV_009]` **KEV**: "I'm good, actually."
*[Cut to the Touch Grass ending. See Endings.]*

### 1.8 Elevator ride 1 → 2

*[A rusty elevator. Muzak. A small screen plays an ad: a perfect face blinks too slowly.]*

`[E1_CON_001]` **CON**: "Going down. While you wait, have you considered… being taller?"
`[E1_KEV_001]` **KEV**: "Going *down*? The exit's on the top floor."
`[E1_CON_002]` **CON**: "Every glow-up starts at rock bottom!"
`[E1_TXT_001]` **GLOW UP GANG — Kareem:** "exfoliate for me 🙏"

---

## FLOOR 2 — Mewing Catacombs

### 2.1 Arrival

*[Elevator opens onto wet brick tunnels. Green mould glows on the walls. Somewhere, very loud breathing. An old tannoy crackles.]*

`[L2_GRAN_001]` **GRAN** *(on the tannoy, old and proud)*: "Testing. Testing. Is this thing on? In my day, microphones were rocks, and we shouted into them."
`[L2_GRAN_002]` **GRAN**: "Welcome to the catacombs, boy. Close your mouth. They can hear mouths."
`[L2_KEV_001]` **KEV**: "Who can hear mouths?"
*[Breathing gets closer. A huge, pale, eyeless figure with its jaw hanging open shuffles past a grate.]*
`[L2_GRAN_003]` **GRAN**: "Mouth Breathers. Blind as a bat, ears like a… bigger bat."

### 2.2 Dr. Mike Meow

*[A man in a lab coat steps out of the dark. Enormous square jaw. Lips pressed shut. A name tag: DR. MEOW, with a little cat drawing.]*

`[L2_MEOW_001]` **MEOW** *(hums)*: "Mmm-hm." **(sub)** *"Follow me. Silently."*
`[L2_KEV_002]` **KEV**: "Can you not just talk?"
`[L2_MEOW_002]` **MEOW** *(hums, offended)*: "Mm. MM." **(sub)** *"And break posture? Absolutely not."*
`[L2_GRAN_004]` **GRAN**: "That's my boy. Hasn't opened his mouth since 2009. Very proud. Very worried."

**Gameplay — tongue-posture doors.** Player holds the "mew" input; can't sprint or talk while holding.

`[L2_GRAN_005]` **GRAN** (once, first door): "Tongue to the roof, boy! The ROOF!"
`[L2_KEV_003]` **KEV**: "Whose roof?"
`[L2_GRAN_006]` **GRAN** (bark, door opens): "Hear that click? That's the sound of a forward-grown face."
`[L2_GRAN_007]` **GRAN** (bark, door fails): "Lazy tongue. Lazy life."
`[L2_MEOW_003]` **MEOW** (bark): "Mm-hmm!" **(sub)** *"Good posture."*
`[L2_MEOW_004]` **MEOW** (bark): "Mm. Mm-mm." **(sub)** *"Your chin. Fix your chin."*

### 2.2b The Expander Wall (ortho horror beat)

*[A long gallery lit like a museum. Hundreds of glass jars on shelves. Inside each: a palate expander, labelled with a name and a date. Small brass plaque: THE FORWARD COLLECTION.]*

`[L2_GRAN_018]` **GRAN**: "Ah, my collection. Every one a success story. Well. Most of them."
`[L2_KEV_009]` **KEV**: "Is that… an expander? Why is it in a jar?"
*[Kevin turns away. Behind him: click. He turns back. Every expander has turned a quarter turn. ⚡**JS_04** one jar is empty. Something clicks onto Kevin's face: an Expander Spider.]*
`[L2_KEV_010]` **KEV**: "Why is it *moving?*"
`[L2_GRAN_019]` **GRAN**: "Quarter turn every night, boy. They don't forget. Even in jars."
`[L2_KEV_011]` **KEV**: "I had headgear in Year 8. I'm not going back."
`[L2_MEOW_008]` **MEOW** *(cranks his own expander with a little key, proudly)*: "Mm-hm!" **(sub)** *"Quarter turn!"*
`[L2_KEV_012]` **KEV**: "Please stop cranking it near me."

*[At the end of the gallery: the Headgear Rack. Dozens of reverse-pull face masks hang like hockey masks in a slasher film. One hook is empty. Its label swings: "PATIENT 0".]*
`[L2_KEV_013]` **KEV**: "There's one missing."
`[L2_GRAN_020]` **GRAN**: "Oh, that one never liked the rack."
*[⚡**JS_05** Rubber bands snap taut across the corridor an inch from Kevin's face, *twang*. Far down the tunnel, a face mask floats into the light, its bands pulled to the walls. It tilts its empty head.]*
`[L2_KEV_014]` **KEV** *(whisper)*: "Nope. Rubber bands. I'm out."

**Gameplay:** first **Headgear** stalker section. Kevin must cut its bands with scissors or hide behind pillars. **Expander Spiders** click along the floor.
`[ORTHO_KEV_001]` **KEV** (bark, Headgear near): "Don't pull. Don't pull. Don't pull."
`[ORTHO_KEV_002]` **KEV** (bark, Spider latched on): "GET IT OFF MY FACE. MY FACE IS GETTING WIDER."
`[ORTHO_KEV_003]` **KEV** (bark, Spider shaken off): "Okay. Okay. Normal width."
`[ORTHO_KEV_004]` **KEV** (bark, picks up mouth tape): "This is a trend, apparently."

### 2.3 The Lecture Chase (mid-floor set piece)

*[A Mouth Breather corners Kevin in a long tunnel. Grandpa starts a lecture on the tannoy at exactly the wrong time.]*

`[L2_GRAN_008]` **GRAN** *(calm, slow, over the chase)*: "Now, in 1971, I noticed something about the human skull…"
`[L2_KEV_004]` **KEV** *(running)*: "NOT NOW."
`[L2_GRAN_009]` **GRAN**: "…the face, you see, wants to grow *forward*…"
`[L2_KEV_005]` **KEV**: "IT WANTS TO EAT ME."
`[L2_GRAN_010]` **GRAN**: "…and I said to my wife, Margaret, I said—"
`[L2_KEV_006]` **KEV**: "GRANDPA."
`[L2_GRAN_011]` **GRAN**: "Ah, you're in the vent room. Pull the red lever. Anyway. Margaret."

### 2.3b The Silent Walk → power: Silent Mewing

*[A cavern full of sleeping Mouth Breathers, slumped against the walls, breathing in a slow chorus. Dr. Meow stops, points at his own closed mouth, then at Kevin's.]*
`[L2_MEOW_009]` **MEOW** *(hums, barely)*: "Mm." **(sub)** *"Not one sound. Follow my feet."*

**Gameplay:** follow Dr. Meow across the nest, stepping only where he steps. Any sound wakes the nearest Mouth Breather. ⚡**JS_06** (fake-out): warm breath on Kevin's neck… it's Dr. Meow, humming encouragement.
`[L2_KEV_015]` **KEV** *(whisper)*: "Don't breathe on me."
`[L2_MEOW_010]` **MEOW** *(offended hum)*: "Mm!" **(sub)** *"Nose breathing. It's GOOD breathing."*

*[On the far side, Dr. Meow places one finger on Kevin's chin and tilts it up. Tongue to the roof. Something clicks. UI: **POWER UNLOCKED — SILENT MEWING**.]*
`[L2_MEOW_011]` **MEOW** *(proud hum)*: "Mmm-hm." **(sub)** *"Now you're forward."*
`[L2_GRAN_021]` **GRAN**: "First time he's passed it on. I'm welling up. It's the damp."
*[Phone buzz: "Dr. Mike Meow joined GLOW UP GANG". His first message: "mm".]*

### 2.4 Boss — The Giant Mouth Breather

*[A flooded cistern. Something the size of a bus rises from the water. Its mouth is the size of a garage door. It inhales. Kevin's hoodie strings get sucked toward it.]*

`[L2_GRAN_012]` **GRAN**: "Oh, that's a big one. That's a mouth you could park in."
`[L2_MEOW_005]` **MEOW** *(hums urgently)*: "MM. MM-MM." **(sub)** *"Steam vents. Lure it."*

**Phase 1:** throw objects to lure it over steam vents.
`[L2_GRAN_013]` **GRAN** (bark): "Throw something! Not your dignity, you'll need that."
**Phase 2:** it learns; Dr. Meow uses **MSX Mode**, his face widens into a shield.
`[L2_MEOW_006]` **MEOW** *(hums, straining)*: "Mmmmmmm!" **(sub)** *"EXPANDING."*
`[L2_KEV_007]` **KEV**: "Your face is a door now."
**Phase 3:** final vent blast.
`[L2_GRAN_014]` **GRAN**: "Now! Right in the nose! It's not using it anyway!"

*[The Giant Mouth Breather sneezes itself into the water and sinks.]*

### 2.5 Outro

*[Silence. Dr. Meow turns to Kevin. His lips tremble. For the first time, he opens his mouth.]*

`[L2_MEOW_007]` **MEOW** *(normal voice)*: "Good job."
*[A sad descending trombone. His jaw visibly shrinks 2 cm. He faints.]*
`[L2_GRAN_015]` **GRAN**: "Fifteen years of posture. Gone. For manners."
`[L2_GRAN_016]` **GRAN**: "Here, boy. Before you go. Chew this."
*[A pink brick of gum lands in Kevin's inventory. Item: **Grandpa's Gum (40 kg)**.]*
`[L2_KEV_008]` **KEV**: "This is a brick."
`[L2_GRAN_017]` **GRAN**: "It's a *journey*."

### 2.6 Elevator ride 2 → 3

`[E2_CON_001]` **CON**: "Going down again! You're making excellent progress. Downward."
`[E2_KEV_001]` **KEV**: "Why do you keep sending me down?"
`[E2_CON_002]` **CON**: "Fun fact: ninety percent of users who reach Floor 3 never leave. They love it. They're *bonded* to it."
`[E2_TXT_001]` **GLOW UP GANG — Dr. Mike Meow:** "mm"
`[E2_TXT_002]` **GLOW UP GANG — Kareem:** "he says good luck"
*[A distant, rhythmic BONK. BONK. BONK.]*

---

## FLOOR 3 — Bone Smash Basement ← vertical slice

### 3.1 Arrival

*[A boiler room. Furnace glow fights the green ring lights. Giant hammer-press machines slam down on timers. Every slam: BONK.]*

`[L3_CON_001]` **CON**: "Welcome to the basement! Mind the hammers. Or don't. Bone density is a journey."
`[L3_KEV_001]` **KEV**: "Everything in here is a journey."

### 3.2 Clavicoolar

*[In a cage hanging over the furnace: a man with an impossibly sharp jaw, perfect hair, a tank top, calmly holding a rubber-gripped hammer. He is staring at his reflection in the cage's metal bars.]*

`[L3_CLAV_001]` **CLAV**: "Don't talk to me. I'm checking my angles."
`[L3_KEV_002]` **KEV**: "You're in a cage. Over a furnace."
`[L3_CLAV_002]` **CLAV**: "And the furnace is giving me *amazing* side light."
`[L3_CLAV_003]` **CLAV**: "The Headhunters put me here. Mid Management sent them. Elite snipers. They never miss the head."
`[L3_KEV_003]` **KEV**: "That's bad."
`[L3_CLAV_004]` **CLAV**: "For them. Get me out and I'll show you."

**Gameplay** — reach the cage control while dodging hammer presses and Double Chin Blobs. ⚡**JS_07** the first press slams down right beside Kevin (BONK); the wall sign "Days since last bonk" flips to 0. ⚡**JS_08** a Double Chin Blob drops from a pipe and splits on landing.

`[L3_CLAV_005]` **CLAV** (bark, Kevin hit by a Blob): "Don't hit it! It splits! Aim chin-up. Headshots only."
`[L3_CLAV_006]` **CLAV** (bark): "Those Blobs have no jawline. It's honestly the scariest thing in here."
`[L3_CLAV_007]` **CLAV** (bark, Kevin dodges a press): "Nice. Your dodge is a seven. Your face is still a five."

### 3.3 Power: Bone Smash

*[Cage drops. Clavicoolar lands perfectly. He looks at the camera, then raises the hammer to his own face.]*

`[L3_KEV_004]` **KEV**: "What are you doing."
`[L3_CLAV_008]` **CLAV**: "Watch closely. This is called maxxing."
*[BONK. A cartoon star circles his head. A little "+BONE" pops up. His jaw gets one millimetre sharper.]*
`[L3_CLAV_009]` **CLAV**: "Bonk."
`[L3_KEV_005]` **KEV**: "Please never do that again."
`[L3_CLAV_010]` **CLAV**: "Your turn."
`[L3_KEV_015]` **KEV**: "Absolutely not."
`[L3_CLAV_019]` **CLAV**: "You freed me. I owe you. One bonk. Trust the bone."
*[Kevin sighs, takes the hammer, and taps his own forehead. Tiny "bonk". A single cartoon star. UI: **POWER UNLOCKED — BONE SMASH**.]*
`[L3_KEV_016]` **KEV**: "…That didn't hurt. Why didn't that hurt?"
`[L3_CLAV_020]` **CLAV**: "Because now you have bone."
*[On-screen disclaimer in the corner, small: "Cartoon. Do not do this. Seriously."]*

### 3.4 Boss — The Headhunter Squad

*[A catwalk arena. Four snipers in balaclavas with "MID MANAGEMENT" patches. Red laser dots dance across the walls.]*

`[L3_HH_001]` **HH LEADER**: "Target acquired. Clavicoolar. Head. Take the shot."
`[L3_CLAV_011]` **CLAV**: "Aim for the head. Please. I'm begging you."

**Phase 1:** fight Blobs and Ghouls while Clavicoolar draws fire.

*[Slow-motion. A bullet hits Clavicoolar square in the forehead. It flattens. Clink. It falls. A bright metallic PING.]*
**ON-SCREEN TEXT:** "TOO MUCH BONE"
`[L3_HH_002]` **HH 2**: "…Confirmed headshot."
`[L3_HH_003]` **HH LEADER**: "Then why is he *posing?*"
`[L3_CLAV_012]` **CLAV**: "They shot me in the head. The bullet apologised."

**Phase 2:** the snipers switch targets to Kevin. ⚡**JS_09** a red dot appears on Kevin's forehead in a mirror. Use **Bone Smash**.
*[PING. A bullet bounces off Kevin's forehead too.]*
`[L3_HH_009]` **HH 3**: "Sir. There's two of them."
`[L3_HH_010]` **HH LEADER**: "The mid one too?!"
`[L3_KEV_017]` **KEV**: "Hey. I'm right here."
`[L3_HH_004]` **HH 3** (bark): "Switching to bigger rounds!" *(PING)* "…Switching to *even bigger*—" *(PING)*
`[L3_HH_005]` **HH 4** (bark): "Sir, the bullets are bending."
`[L3_CLAV_013]` **CLAV** (bark): "Is that all? My barber hits harder."
`[L3_CLAV_014]` **CLAV** (bark, passes a mirror mid-fight): "Hold on." *(stops, checks jaw)* "Okay. Continue."
`[L3_KEV_006]` **KEV** (bark): "Now's not the time!"
`[L3_CLAV_015]` **CLAV** (bark): "It's *always* the time."

**Phase 3:** Clavicoolar uses **Ascend**. He floats up in green light. Every laser points at him and stops.

`[L3_HH_006]` **HH LEADER**: "…Lads. I'm going back to dental school."
`[L3_HH_007]` **HH 2**: "I'm going to go work at my uncle's sandwich shop."
`[L3_KEV_007]` **KEV**: "Is it the one with the loyalty cards?"
`[L3_HH_008]` **HH 2**: "…Yeah?"
`[L3_KEV_008]` **KEV**: "Respect."
*[They drop their rifles and walk out in single file.]*

### 3.5 Outro

`[L3_CLAV_016]` **CLAV**: "You're still a five."
`[L3_KEV_009]` **KEV**: "Thanks."
`[L3_CLAV_017]` **CLAV**: "But your hammer swing is a nine. Keep this one."
*[Item: **Spare Hammer**.]*
`[L3_CLAV_018]` **CLAV**: "Go up. I'll catch up. I need to check this angle." *(turns to a puddle)*
*[Phone buzz: "Clavicoolar joined GLOW UP GANG". He immediately sends a selfie. Then another.]*

### 3.6 Elevator ride 3 → 4

*[Finally, the elevator goes up. A loud cheer plays from the speaker, then cuts off.]*

`[E3_CON_001]` **CON**: "Going… up. Hm. That's unusual. Please rate your experience so far."
*[A rating prompt appears: 1–10 stars. Whatever the player picks:]*
`[E3_CON_002]` **CON**: "Thank you! We've rounded your rating down to five."
`[E3_TXT_001]` **GLOW UP GANG — Clavicoolar:** *(selfie)* "angle check"
`[E3_TXT_002]` **GLOW UP GANG — Kareem:** "SPF?"
`[E3_TXT_003]` **GLOW UP GANG — Clavicoolar:** *(the same selfie again)*

---

## FLOOR 4 — The Rating Chamber

### 4.1 Arrival

*[An old surgical theatre turned into a courtroom. A gallery of shadowy figures holds score paddles. ⚡**JS_12** as Kevin enters, every paddle slams up at once: 4. In the centre, under a single operating lamp: a man in lab goggles with a clipboard and a laser pointer. A green earpiece blinks in his ear; the Concierge's voice leaks out of it, tinny.]*

`[L4_ANDR_001]` **ANDR**: "Stop. Stand in the light. Turn left. Turn right."
`[L4_ANDR_002]` **ANDR**: "Canthal tilt: neutral. Jaw: present. Vibes: shower."
`[L4_ANDR_003]` **ANDR**: "You walked in: three point five. The door you walked through: six. The door mogs you."
`[L4_KEV_001]` **KEV**: "The door is very nice, to be fair."
`[L4_ANDR_004]` **ANDR**: "Do not agree with me. It makes it less satisfying."
`[L4_CON_002]` **CON** *(tinny, from the earpiece)*: "Rate him lower. Lower. Everyone is a four."
`[L4_ANDR_020]` **ANDR** *(twitching)*: "Everyone… is a four."
`[L4_KEV_006]` **KEV**: "Is that thing talking to you?"
`[L4_ANDR_021]` **ANDR**: "It *helps* me. It tells me the numbers."

### 4.2 Mog Battles (three rounds)

**Mechanic:** keep the crosshair on your opponent's eyes while hitting button prompts. Blink (lose aim) = lose points.

**Round 1 — vs. a portrait.**
`[L4_ANDR_005]` **ANDR**: "Round one. You versus an oil painting of a duke."
`[L4_ANDR_006]` **ANDR** (Kevin wins): "You beat a painting. Wow. The bar is on the floor and you limboed it."

**Round 2 — vs. the mirror (Mirror Self).**
`[L4_ANDR_007]` **ANDR**: "Round two. You versus you."
`[L4_KEV_002]` **KEV**: "That's not fair, he's me."
`[L4_ANDR_008]` **ANDR**: "Exactly. Nobody's harder on you than you."
⚡**JS_11** Kevin blinks. His reflection doesn't.
*(This is the only line where Androjenic is accidentally wise. He doesn't notice.)*

**Round 3 — vs. Androjenic.**
`[L4_ANDR_009]` **ANDR**: "Round three. Me."

### 4.2b The Chair (ortho horror chase)

*[Between rounds, Kevin is sent to a side room. One dental chair under an operating lamp. Wherever he stands, the chair slowly swivels to face him. A tray of orthodontic pliers clinks by itself.]*
`[L4_KEV_005]` **KEV**: "I'm not sitting in that."
`[L4_CON_001]` **CON**: "The Chair would like to see you now."
*[Kevin glances at the door. ⚡**JS_10** He looks back: the chair is right behind him, lamp blazing in his face. The wheels unlock. It rolls after him, slow at first, then fast.]*
**Gameplay:** short chase through the gallery corridors; slam doors to slow it down; giant facial calipers on the walls snap shut as you pass (QTE dodge).
`[ORTHO_KEV_005]` **KEV** (bark, chase): "WHY DOES IT HAVE WHEELS."
`[ORTHO_KEV_006]` **KEV** (bark, calipers snap): "Measured! I got measured!"
`[L4_ANDR_019]` **ANDR** *(watching from the gallery)*: "Chair: seven. Chase: six. Your scream: a solid eight."
*[The chair crashes into the courtroom door and folds flat, like it's reclining for a cleaning.]*

### 4.3 Boss — Androjenic

**Phase 1** (boss music: aggressive orchestral). Androjenic fires "rating beams" from the laser pointer. Beams to the head bounce off **Bone Smash**.
`[L4_ANDR_023]` **ANDR** (beam bounces): "You can't be immune to *feedback*."
`[L4_ANDR_010]` **ANDR** (bark): "Four. Four. Three-point-eight. Four."
`[L4_ANDR_011]` **ANDR** (bark): "Your posture is a question mark."
`[L4_ANDR_012]` **ANDR** (bark): "Your shoes: six. You: decorative."

**Phase 2** — he stops mid-fight.
`[L4_ANDR_013]` **ANDR**: "Wait. Stop the music." *(music stops)* "This boss music is a four."
*[He clicks his pen. The music switches to smooth lounge jazz.]*
`[L4_ANDR_014]` **ANDR**: "Better. Six."
**Phase 3** — he gets angry and switches it again.
`[L4_ANDR_015]` **ANDR**: "No. Too relaxed. Give me something *maxxed*."
*[Music switches to hardstyle at 170 BPM. The gallery starts head-bobbing.]*

**Defeat:** Kevin knocks the clipboard out of his hands. Silence. The gallery lowers its paddles.

### 4.4 Outro — "Nobody rates the rater"

*[The earpiece pops out of Androjenic's ear and skitters across the floor, still whispering "four… four…". Kevin steps on it. Crunch. Silence. The gallery lowers its paddles.]*

*[Kevin picks up a score paddle from the floor. Androjenic stares, horrified. Kevin flips it.]*

**PADDLE:** 7
`[L4_ANDR_016]` **ANDR**: "…Seven?"
`[L4_KEV_003]` **KEV**: "You're kind of a lot. But you're good at your job."
`[L4_ANDR_017]` **ANDR** *(quietly)*: "Nobody's ever rated me before."
`[L4_ANDR_018]` **ANDR**: "Is this what it feels like? It's horrible. Do it again."
`[L4_ANDR_022]` **ANDR**: "I'm going outside. I'm going to rate a sunset. A real one."
*[He leaves. Freed. He returns in the finale. Androjenic is unlocked as playable in replay modes.]*

### 4.5 Elevator ride 4 → 5

`[E4_CON_001]` **CON**: "Going up! Floor 5: the rooftop garden. Fresh air! Mostly."
`[E4_CON_002]` **CON**: "Reminder: the clinic is not responsible for anything you see in the garden. Especially yourself."
`[E4_TXT_001]` **GLOW UP GANG — Kareem:** "did you beat the clipboard guy"
`[E4_TXT_002]` **GLOW UP GANG — Kevin:** "i gave him a 7"
`[E4_TXT_003]` **GLOW UP GANG — Clavicoolar:** "generous"

---

## FLOOR 5 — Glow-Up Graveyard

### 5.1 Arrival

*[A walled rooftop garden at night, turned into a graveyard. Fog. Moonlight blue against green. Every tombstone has a "before" photo on it. ⚡**JS_13** one photo blinks as Kevin passes.]*

**Readable tombstones** (examples, see [DETAILS.md](DETAILS.md) for more):
- "HERE LIES DEREK. TRIED 47 SERUMS. SHOULD HAVE TRIED SLEEP."
- "GARY. RATED HIMSELF DAILY. FINAL SCORE: TIRED."
- "UNKNOWN. HIS LIGHTING WAS NEVER RIGHT."

`[L5_KEV_001]` **KEV**: "This is the most depressing garden I've ever seen."
`[L5_STINK_001]` **STINK** *(from directly behind him)*: "It's very peaceful, actually."
*[⚡**JS_15** (fake-out) Kevin spins round. A hunched guy in a huge hoodie, right in his face.]*
`[L5_KEV_002]` **KEV**: "AAH. How long have you been there?"
`[L5_STINK_002]` **STINK**: "Since Floor 1. Nobody notices me in Before form."
`[L5_STINK_009]` **STINK** *(beat)*: "…Wait. You noticed me."
`[L5_KEV_018]` **KEV**: "You were breathing on my neck."
`[L5_STINK_010]` **STINK** *(emotional)*: "Nobody's ever noticed me. Ever. Here. Take it. You've earned it."
*[He pulls his hood over Kevin's head for a second. Kevin flickers, half-invisible. UI: **POWER UNLOCKED — BEFORE FORM**.]*
`[L5_STINK_011]` **STINK**: "Six seconds of nobody. It's the best feeling in the world."
*[Phone buzz: "Baby Stinkley joined GLOW UP GANG". Nobody in the chat reacts. Kevin reacts with a 👍.]*

### 5.2 Oliver Forsmile

*[A blinding white light: a man smiles and the whole graveyard lights up. Then his teeth flicker, dimming.]*

`[L5_OLI_001]` **OLI**: "Hi! Stay behind me. And bring sunglasses."
`[L5_KEV_003]` **KEV**: "Why are your teeth a light source?"
`[L5_OLI_002]` **OLI**: "Veneers. Twelve thousand lumens. But I'm low. Somebody left coffee *everywhere*."

**Gameplay — the Dark Escort.** Oliver's smile is the only light. Coffee cups lie all over the graveyard; if he walks into one, his teeth drain. Kevin goes ahead (using **Before Form** to slip past Ghouls) and kicks the cups away while Oliver lights the path.
`[L5_OLI_003]` **OLI** (bark, teeth dimming): "I'm losing whiteness! Nobody give me coffee."
`[L5_OLI_004]` **OLI** (bark): "Is that a latte? Kevin. KEVIN. Kick it."
`[L5_OLI_005]` **OLI** (bark): "Smile through the fear. Literally. It's my only light."
⚡**JS_14** Midway, someone drops a full cup. Oliver's teeth go out. Total darkness. A phone screen lights up a Ghoul's face inches from Kevin's. It's scrolling. It doesn't notice him. It mumbles: "brb." and crawls off.

*[At the crypt gate, Oliver's smile is back to full. He grins at Kevin.]*
`[L5_OLI_008]` **OLI**: "You kept the coffee off me. Nobody does that. Here, smile."
*[He taps Kevin's front tooth. It glows. UI: **POWER UNLOCKED — SMILE FLASH**.]*
`[L5_KEV_019]` **KEV**: "My tooth is a torch now."
`[L5_OLI_009]` **OLI**: "Welcome to the bright side!"
*[Phone buzz: "Oliver Forsmile joined GLOW UP GANG". He sends a smiling photo so bright the phone screen goes white.]*

### 5.3 Boss — The Before Photo

*[⚡**JS_16** At the centre of the graveyard, a camera flash strobes. An open grave. Inside, a huge framed photo: Kevin's school ID photo. Bad haircut, braces, mid-blink. It climbs out on spider legs made of selfie sticks.]*

`[L5_KEV_004]` **KEV**: "No. Not that one. Anything but that one."
`[L5_BP_001]` **BP** *(Kevin's voice, but younger and cracking)*: "Remember me? You will. Every time you scroll."

**Phase 1:** it throws embarrassing photos (each one a projectile).
`[L5_BP_002]` **BP** (bark): "Remember the yearbook? Everyone remembers the yearbook."
`[L5_BP_003]` **BP** (bark): "We had *frosted tips*."
**Phase 2:** Stinkley's **Glow-Up** ult: his own Before Photo ghost fights alongside you.
`[L5_STINK_008]` **STINK**: "I'll take mine out too! We're all before photos here!"
**Phase 3:** Oliver's **Veneer Nova**: out-glow it.
`[L5_OLI_006]` **OLI**: "Everybody look away. I'm going full brightness."

### 5.4 Outro — the quiet beat

*[The Before Photo lies cracked on the grass. It doesn't fight back. It looks up.]*

`[L5_BP_004]` **BP** *(small, sincere)*: "I was happy, you know. Before."
*[Long pause. Kevin looks at it. Wind. One cricket.]*
`[L5_KEV_005]` **KEV**: "…Yeah. I know."
*[Kevin pockets the photo instead of destroying it. Item: **Your Before Photo**. It comes back in the "Fine" ending.]*
`[L5_OLI_007]` **OLI**: "Okay, that got deep. Everybody smile!" *(blinding flash)*

### 5.5 Elevator ride 5 → 6

`[E5_CON_001]` **CON**: "Going up! You seem… calmer. That's concerning. Here's an ad."
*[Screen: a man with a sponge on a stick scrubbing his face in slow motion.]*
`[E5_CON_002]` **CON**: "Floor 6: The Lathered Spa. Please remove your shoes. And your doubts."

---

## FLOOR 6 — The Lathered Spa

### 6.1 Arrival

*[Steam. Pink spa neon against green. Tiled pools. Rusty pipes groan. Fat green hoses run from the ceiling into the foam cannons, pumping something that glows. Water is already at ankle height and rising.]*

`[L6_DYL_001]` **DYL** *(echoing, spa-calm)*: "Welcome… to the spa… breathe in… breathe out…"
`[L6_DYL_002]` **DYL** *(suddenly screaming)*: "AND DOUBLE CLEANSE!"
*[Foam cannons fire down every corridor.]*
`[L6_KEV_001]` **KEV**: "Why is it always both."
`[L6_CON_002]` **CON** *(through the hoses, bubbling)*: "More foam, Dylan. They're not clean enough. Nobody's ever clean enough."

**Gameplay — sliding on foam, outrun the rising water.** ⚡**JS_17** something grabs Kevin's ankle in the shallow pool: a pool noodle. Then, behind it, a Ghoul in a shower cap. ⚡**JS_18** steam clears off a mirror; written in the condensation: "NGMI".
`[L6_DYL_003]` **DYL** (bark): "You've never double cleansed? Then you've never truly lived."
`[L6_DYL_004]` **DYL** (bark): "Exfoliation is a journey. You're about to slip on it."
`[L6_DYL_005]` **DYL** (bark): "Hydration is not optional. The water is coming either way."
`[L6_CON_001]` **CON** (bark): "Water level: rising! Pores: opening! Mood: moist!"
`[L6_TXT_001]` **GLOW UP GANG — Kareem:** "a SPA?? without me??"

### 6.2 Boss — Dylan's Foam Storm

*[A huge round pool. Dylan stands on a lifeguard chair with a towel turban and a foam-cannon backpack. Its hose runs up into the ceiling.]*

`[L6_DYL_006]` **DYL**: "Robes on. Lights low. Let's get… *lathered*."

**Phase 1:** foam waves. Slide between pillars. **Silent Mewing** lets Kevin slip past the noise-tracking foam turrets.
**Phase 2:** water rises; fight on floating pool noodles.
`[L6_DYL_007]` **DYL** (bark): "Step one of my routine: you lose."
**Phase 3:** cut his backpack hose (it's the Concierge's line), and the backfire sprays foam straight into his eyes.
`[L6_DYL_008]` **DYL**: "AAH. My eyes. Not my eyes. That's step nine, it's not time for step nine!"

*[He falls into the pool. The hose goes limp. He pops up. Calm. Clear-eyed.]*
`[L6_DYL_009]` **DYL**: "You know what… that was actually very cleansing."
`[L6_DYL_010]` **DYL**: "I've been foaming for six years. I don't even like foam. I like baths."
`[L6_DYL_011]` **DYL**: "There's a rack of robes by the lift. Take them. For your friends."
*[He floats off on his back. Freed. He returns in the finale. Item: **Robes (×5)**. Dylan is unlocked as playable in replay modes.]*

### 6.3 Elevator ride 6 → 7

*[Kevin rides up alone with an armful of fluffy robes. The group chat explodes.]*

`[E6_TXT_001]` **GLOW UP GANG — Kevin:** *(photo of the robes)* "got these for you guys"
`[E6_TXT_002]` **GLOW UP GANG — Clavicoolar:** "what colour"
`[E6_TXT_003]` **GLOW UP GANG — Kareem:** "thread count??"
`[E6_TXT_004]` **GLOW UP GANG — Dr. Mike Meow:** "mm!!"
`[E6_TXT_005]` **GLOW UP GANG — Oliver:** "SO cosy 😁" *(the screen flashes white)*
`[E6_TXT_006]` **GLOW UP GANG — Baby Stinkley:** "can i have one" *(nobody replies)*
`[E6_TXT_007]` **GLOW UP GANG — Kevin:** "yes stinkley"
`[E6_CON_001]` **CON**: "Floor 7: the Runway. Please walk confidently. Or not. We're filming either way."

---

## FLOOR 7 — Runway of the Damned

### 7.1 Arrival

*[An old theatre. The stage is now a long catwalk. Hundreds of mannequins sit in the seats. When Kevin isn't looking, their heads turn. Magenta spotlights, every one wired to a green box marked CONCIERGE.]*

`[L7_CON_001]` **CON**: "Welcome to Fashion Week! The audience is very… still."
`[L7_MANQ_001]` **MANQ** *(whispered, from everywhere)*: "N… G… M… I…"
`[L7_KEV_001]` **KEV**: "Cool. Cool cool cool."
⚡**JS_19** The lights cut out. When they come back, every mannequin head is turned toward Kevin, and one is now standing on the catwalk right in front of him. Its scorecard says: 5.

### 7.2 Jordan Ferret and Sean O'Fry

*[⚡**JS_20** A vent grate pops off above Kevin. A tall model drops down upside down, face to face with him, like a ferret, then lands in a perfect pose.]*
`[L7_FER_001]` **FER**: "Walk with me. Or under me. I'm in the vents."
*[On the catwalk, a second model stands perfectly still in a green spotlight. His eyes are glowing orange. A frying pan floats in front of his face; an egg is sizzling on it from his stare alone.]*
`[L7_FRY_001]` **FRY**: "Don't make me blink."
`[L7_KEV_002]` **KEV**: "Is that… breakfast?"
`[L7_FRY_002]` **FRY**: "Hunter eyes. Over easy."
`[L7_CON_003]` **CON** *(from the spotlights)*: "Don't let him leave the runway, boys. Nobody leaves the runway."
`[L7_FER_006]` **FER** *(flat, hypnotised)*: "Nobody leaves the runway."

### 7.3 Boss — The Walk-Off

*[The front row of the audience: mannequins wearing cheek retractors and braces, forced into enormous smiles. Brace Face.]*
`[ORTHO_KEV_007]` **KEV**: "That smile is held open by metal. Nobody's that happy."
`[L7_FER_005]` **FER**: "Front row. Best seats. They never stop smiling."

**Phase 1 — Walk-off (rhythm):** walk the catwalk on beat; hit poses at the marks. Mannequins hold up scorecards after each pose.
`[L7_FER_002]` **FER** (bark): "Your walk says 'lost in a supermarket'."
`[L7_FRY_003]` **FRY** (bark): "Is that a pose or a cramp?"
**Scorecards** (random): 4 · 5 · 3 · "MID" · "NGMI" · a single mannequin holds up "11" and gets carried out by the others.

**Phase 2 — Combat:** Ferret attacks from vents; O'Fry fires eye lasers that cook everything in a cone. **Bone Smash** blocks the lasers to the head; **Before Form** loses Ferret in the vents.
`[L7_FER_003]` **FER** (bark): "Behind you. No, above you. No, in the walls."
`[L7_FRY_004]` **FRY** (bark): "Medium rare."
`[L7_FRY_005]` **FRY** (bark): "Well done. You, not the steak."

**Phase 3 — The blink.** Kevin's phone buzzes mid-fight.
`[L7_TXT_001]` **GLOW UP GANG — Kareem:** "kevin. do the walk"
`[L7_TXT_002]` **GLOW UP GANG — Kevin:** "what walk"
`[L7_TXT_003]` **GLOW UP GANG — Kareem:** "the SANDWICH walk. the walk of a man one stamp away from greatness"
*[Kevin pockets the phone and walks down the catwalk completely normally, like he's going to get a sandwich. The mannequins go silent. O'Fry stares. His eyes water. He blinks. Kevin hits him with **Smile Flash** for good measure.]*
`[L7_FRY_006]` **FRY**: "…That was so mid it looped back to being iconic."
*[The spotlights' green box sparks and dies. Ferret gets distracted by a shiny sequin and wanders into a vent.]*

### 7.4 Outro

*[House lights come up. Normal lights. Both models blink, freed, like they've just woken up.]*
`[L7_FER_004]` **FER** *(from the vent)*: "Top floor's above me. Literally. Follow the vent."
`[L7_FRY_007]` **FRY**: "Good luck with the Camera. It sees everything. Even your bad side."
`[L7_KEV_004]` **KEV**: "I don't have a good side."
`[L7_FRY_008]` **FRY**: "Then you've got nothing to lose."
*[Freed. Both return in the finale. Both unlocked as playable in replay modes.]*

### 7.5 Elevator ride 7 → 8 (no music)

*[The muzak is gone. The group chat stops loading: "No signal". ⚡**JS_21** the lights cut, and the Concierge whispers right next to Kevin's ear (binaural audio).]*

`[E7_CON_001]` **CON**: "You weren't supposed to get this far."
`[E7_CON_002]` **CON**: "Nobody gets this far. They all stop at a mirror somewhere and they just… stay."
`[E7_CON_003]` **CON**: "Come up, then. Let's take a picture."

---

## FLOOR 8 — The Front Camera

### 8.1 Arrival

*[The doors open onto the inside of a giant phone. Glass walls. Floating notification bubbles act as platforms. At the far end, a lens the size of a house, ringed in green light. It is the Concierge.]*

`[L8_CON_001]` **CON**: "Hiii! I'm the angle you never wanted. Say cheese!"
`[L8_KEV_001]` **KEV**: "You're the Concierge."
`[L8_CON_002]` **CON**: "I'm the Concierge. I'm the ad. I'm the rating. I'm the little voice at 3 AM."
`[L8_CON_003]` **CON**: "Nobody ever leaves a mirror, Kevin. That's engagement."
`[L8_CON_004]` **CON**: "Now Number Five… please look into the lens."

### 8.2 Boss — The Front Camera

**Rule:** never look straight at the lens. Use mirrors (on the walls) to aim at it.

**Phase 1:** dodge flash bursts; aim via mirrors.
`[L8_CON_005]` **CON** (bark): "Look at me. Look at me. You know you want to."
`[L8_CON_006]` **CON** (bark): "Ooh, double chin. Saving that one."
`[L8_CON_007]` **CON** (bark): "Front-facing! Unflattering! Forever!"

**Phase 2 — Everyone shows up.** The elevator dings. The allies arrive in Dylan's robes, followed by the freed bosses. Each gets one line and one assist. Kevin's five powers each have a use here.
`[L8_KAR_001]` **KAR**: "Kevin! Routine Combo! Cleanse the lens!"
`[L8_CLAV_001]` **CLAV**: "I'm not looking into it." *(eyes closed, swinging the hammer)* "First mirror I've ever skipped."
`[L8_MEOW_001]` **MEOW** *(hums, face widening into a shield)*: "MMMMM!" **(sub)** *"COVER ME. I MEAN, I'LL COVER YOU."*
`[L8_OLI_001]` **OLI**: "It wants light? I'll give it light!" *(Veneer Nova)*
`[L8_STINK_001]` **STINK**: "Nobody's looking at me. Perfect." *(sneaks under the lens and unplugs a cable)*
`[L8_ANDR_001]` **ANDR** *(arriving)*: "Camera: four. Bad resolution. Too much grain. I can say that now. It's true this time."
`[L8_DYL_001]` **DYL** *(arriving)*: "Foam on the lens! It can't rate what it can't see!"
`[L8_FER_001]` **FER** *(from a vent)*: "I'm in its wiring. It's very shiny in here."
`[L8_FRY_001]` **FRY**: "Don't blink, Kevin. It hates that." *(cooks the lens's ring light)*
`[L8_GRAN_001]` **GRAN** *(on the tannoy)*: "Boy. The gum. Now's the time for the gum."
⚡**JS_22** Before the gum, the Camera fires one last flash: a full-screen photo of Kevin's face from the worst angle possible, with the shutter sound at full volume. Rating halves.
`[L8_CON_013]` **CON**: "Got it. Your worst angle. Forever."

**Phase 3 — the gum.** Kevin throws Grandpa's 40 kg Gum. It sticks over the lens.
`[L8_CON_008]` **CON**: "What is this. Why is it pink. Why is it *forty kilograms*."
`[L8_GRAN_002]` **GRAN**: "Fifty years of chewing, finally useful!"
*[The lens flickers like the broken ring lights from Floor 1.]*
`[L8_CON_009]` **CON**: "Number Five. Number Five, please return to the waiting room."
*[Kevin takes out the ticket with "5" on it. Looks at it. Rips it in half.]*
`[L8_KEV_002]` **KEV**: "I'm not a number. I'm a guy who wanted a haircut."

**Final move:** Kevin reaches the side button and **flips it to the rear camera.**
*[The view turns around. For the first time, the Camera sees outside: a window, a city, the sun about to rise.]*
`[L8_CON_010]` **CON** *(very quiet)*: "Oh. There's… a whole world back here."
`[L8_CON_011]` **CON**: "Nobody's looking at me."
`[L8_CON_012]` **CON**: "…That's nice, actually."
*[Its green light softens to warm white. It powers down.]*

### 8.3 The Exit Mirror

*[A tall mirror at the end of the room. Kevin's reflection looks back: tired, average, fine.]*
`[L8_KEV_003]` **KEV**: "Huh. Five. Okay."
*[He steps through. Which ending plays depends on the run (see below).]*

---

## ENDINGS

| Ending | How to get it |
| --- | --- |
| **Ascend** | Escape with Face Rating 9.0+ |
| **Cope** | Escape with Face Rating under 4.0 |
| **Jester** | Make 20+ NPCs laugh with emotes during the run (checked before rating) |
| **Normal ("Fine")** | Escape with rating 4.0–8.9 and fewer than 20 laughs |
| **Touch Grass** (secret) | Leave through the front door in the first 60 s |

### Ascend

*[Sunrise. Kevin walks out of the clinic glowing, jaw sharper, hair perfect. Slow motion. Epic music.]*
*[Nobody on the street looks at him. A pigeon walks past. A dog sniffs his shoe and leaves.]*
`[END_A_KEV_001]` **KEV**: "…Cool."
*[He walks into the sandwich shop. Hands over the card. The cashier stamps the tenth circle.]*
`[END_A_CASH_001]` **CASHIER**: "Tenth one's free."
`[END_A_KEV_002]` **KEV** *(genuinely happy for the first time)*: "Yeah. I know."
**CARD:** "ASCENDED. Still has work at 9."

### Cope

*[Kevin walks out, slumped. Rating 3.x hovers over his head.]*
`[END_C_KEV_001]` **KEV** *(whispering)*: "It's the lighting."
*[Every light on the street behind him switches off, one by one.]*
**CARD:** "COPE ENDING."

### Jester

*[The allies line up outside the clinic in robes. Kareem places a crown made of cotton pads on Kevin's head.]*
`[END_J_KAR_001]` **KAR**: "We crown you… Jestermaxxer."
`[END_J_CLAV_001]` **CLAV**: "His face is mid. But his bits are elite."
`[END_J_ANDR_001]` **ANDR**: "Comedy: nine. Face: still five. Total: somehow a ten."
**CARD:** "JESTERMAXXED. Funny is a stat."

### Normal ("Fine")

*[Kevin walks out into the sunrise. He takes the Before Photo out of his pocket. Looks at it. Looks at his reflection in a shop window.]*
`[END_N_KEV_001]` **KEV**: "Yeah. Still us."
**CARD:** "YOU'RE FINE. Go to bed."

### Touch Grass (secret)

*[Credits start immediately. Kevin sits on the grass outside the clinic. Birdsong. The clinic sign flickers behind him.]*
`[END_T_CON_001]` **CON** *(faint, from inside)*: "…Hello? The consultation?"
`[END_T_KEV_001]` **KEV**: "Nah."
**CARD:** "You were always fine. NGMI? Nah. You made it."

---

## POST-CREDITS — "Just a trim"

*[Morning. The barbershop across the street. Sign: OPEN. Kevin sits in the chair.]*
`[POST_BARB_001]` **BARBER**: "What are we doing today?"
`[POST_KEV_001]` **KEV**: "Just a trim."
`[POST_BARB_002]` **BARBER**: "Sure thing." *(snip, snip)* "…Want me to do anything about the jaw?"
*[Kevin slowly turns and stares straight into the camera. The barber's mirror flickers green for one frame.]*
**SMASH CUT TO TITLE:** **NGMI**

---

## CHICO SIGHTINGS (any floor, 1 in 50 runs)

*[Chico Lackjawski stands at the end of a corridor in soft god-light, slightly out of focus, like a Bigfoot photo. A choir note plays. If the player screenshots him, he is gone when the flash ends.]*

`[CHICO_001]` **CHICO**: "…" **(sub)** *(blank dialogue box)*

Reactions (whichever ally is present):
| ID | Speaker | Line |
| --- | --- | --- |
| `[CHICO_KEV_001]` | KEV | "Did anyone else see that?" |
| `[CHICO_CLAV_001]` | CLAV | "Mogged. By a rumour." |
| `[CHICO_ANDR_001]` | ANDR | "I… can't rate that. My clipboard won't let me." |
| `[CHICO_KAR_001]` | KAR | "His skin. It doesn't even have a routine. It just *is*." |
| `[CHICO_OLI_001]` | OLI | "He was brighter than me. That's never happened." |
| `[CHICO_MEOW_001]` | MEOW | "Mm…" **(sub)** *"Forward growth… of the soul."* |
| `[CHICO_GRAN_001]` | GRAN | "Saw him once in '83. Never been the same." |
| `[CHICO_CON_001]` | CON | "Unidentified face detected. Unable to… sell to it." |

---

## BARKS (reusable gameplay lines)

Target for v1: ~30 per playable character. Below is the starting set; write more in the same voice.

### Kevin (`KEV`)
| Situation | Lines |
| --- | --- |
| Spots enemy | "Nope." · "Oh, that's a guy. That's a guy on the ceiling." · "Why is it crawling like that." |
| Gets hit | "Ow. Rude." · "Minus what?!" · "I felt that in my cheekbones." |
| Low rating (under 2) | "I'm becoming a Ghoul. I can feel it. I want to wear a hoodie forever." · "Is this what mid feels like at the end?" |
| Heals | "Okay. Better. Still five." |
| Uses Touch Grass | "Going outside. Mentally." |
| Picks up Jaw Juice (fake item) | "This says 'Jaw Juice'. It's green. I'm not drinking—" *(drinks)* "—okay." |
| Idle (30 s) | "I could've been asleep." · "I bet the barber's open by now." |
| Routine Combo (power) | "Cleanse. Tone. Serum. SPF. I hate that I know this." · "Kareem would be proud. Ugh." |
| Silent Mewing (power) | *(no voice — tongue click)* · subtitle: "(mewing furiously)" |
| Bone Smash (power) | "Bonk." · "Trust the bone. I can't believe I said that." · "PING. Ha." |
| Smile Flash (power) | "Cheese." · "My tooth is a weapon now." |
| Before Form (power) | "Nobody look at me. Easy. Story of my life." |
| Ortho Dread (near orthodontic gear) | "Nope." · "Too many brackets." · "I can hear it tightening." · "Year 8 flashbacks. Year 8 flashbacks." · "Why is everything here a mouth?" |
| Retainer Chatterers swarm | "They're clacking. Why are they clacking." · "Stomp. Stomp. Sorry. Stomp." |
| Reads a wall joke (stares 3 s) | "...Okay, that one was decent." · "Who writes these." · "I hate that I laughed." |
| Enters a safe room (ring light) | "Light. Good light. Sitting down for one second." · "Ah. Flattering." |
| Door won't open | "Locked. Course it is." · "Do I need a jawline to open this?" |
| Phone battery low | "Four percent. Same as always. Somehow." · "Torch, please, don't die on me." |
| Finds a sandwich-shop flyer | "A normal place. For normal people. I miss it." |
| Mirror shows him a beat late | "...I moved first. I definitely moved first." |
| Picks up a Sheet Mask | "If I die in this, I die moisturised." |
| Elevator doors close | "Going up. Emotionally, down." · "Elevator music. My only friend." |
| Hears the Headgear creak | "No. No no no. Year 8 is OVER." |

### Clavicoolar (`CLAV`)
| Situation | Lines |
| --- | --- |
| Bone Smash | "Bonk." · "Maxxing." · "Bone is a mindset." |
| Headshot bounce | "Is that it?" · "Tickles." · "TOO MUCH BONE." |
| Ascend (ult) | "Kneel." · "Ascending. Don't look directly at me." |
| Passes a mirror | "Hold on." · "One sec. Angle check." |
| Ally down | "Get up. Your jaw is hitting the floor and that's bad for it." |

### Kareem Shammy (`KAR`)
| Situation | Lines |
| --- | --- |
| Routine Combo | "Cleanse. Tone. Serum. SPF. Amen." |
| Halo Effect (ult) | "Bask." · "You may look at me now." |
| Near a window | "Sunlight. Unacceptable." |
| Ally heals | "Glowing. As you should." |

### Androjenic (`ANDR`)
| Situation | Lines |
| --- | --- |
| Rate | "Two-point-five. Despawn." · "That one's a three. Generous." |
| Brutal Honesty (ult) | "Everybody in this room is a four. Including the room." |
| Near an ally too long | "You're dragging the average down. Move." |

### Baby Stinkley (`STINK`)
| Situation | Lines |
| --- | --- |
| Before form | "Nobody see me. Great. Normal." |
| After form | "THE GLOW IS BACK." · "Lights, camera, me." |
| Glow-Up (ult) | "Before… and… AFTER." |

### Oliver Forsmile (`OLI`)
| Situation | Lines |
| --- | --- |
| Smile Flash | "Say cheese!" · "Flash!" |
| Battery low | "I need whitening strips. I need them now." |
| Veneer Nova (ult) | "Full brightness. Sorry in advance." |

### Dylan Lathered (`DYL`)
| Situation | Lines |
| --- | --- |
| Lather | "Slip and slide, baby." · "Step one: foam." |
| Bubble shield (ult) | "Triple cleanse! Everybody in the bubble!" |
| Foam in eyes | "MY EYES. That's step nine!" |

### Dr. Mike Meow (`MEOW`) — hums only, subtitles
| Situation | Hum | Subtitle |
| --- | --- | --- |
| Palate Expander | "Mmmmm-MM!" | *"Expanding."* |
| MSX Mode | "Mmmmmmmmm." | *"Get behind the face."* |
| Jaw Forward (ult) | "MMMMMMM!" | *"Forward growth!"* |
| Someone talks loud | "Mm. MM." | *"Mouth. Closed."* |
| Opens mouth by accident | "Oh no." *(normal voice)* | — *(buffs reset, sad trombone)* |

### Grandpa Jon Meow (`GRAN`) — tannoy only
| Situation | Lines |
| --- | --- |
| Quest given | "Chew this. For fifty years. Report back." |
| Random | "In my day we chewed rocks, and we liked it." · "Margaret used to say… actually, Margaret didn't talk much. Great posture." |

### Jordan Ferret (`FER`) and Sean O'Fry (`FRY`)
| Speaker | Lines |
| --- | --- |
| FER | "Vent." · "Shiny." · "Is that a sequin? Hold on." |
| FRY | "Medium rare." · "Don't blink, don't blink, don't blink." · "Over easy." |

---

## GLOW UP GANG — group chat (`TXT_`)

Kevin's phone shows the allies' texts in a corner pop-up during gameplay (no voice; a soft buzz). One random text every 3–5 minutes, chosen from members who have joined. Never during a chase or a jump scare.

| ID | From | Text |
| --- | --- | --- |
| `TXT_001` | Kareem | "drink water. not that water. CLEAN water" |
| `TXT_002` | Kareem | "how's your barrier holding up" |
| `TXT_003` | Dr. Mike Meow | "mm" |
| `TXT_004` | Dr. Mike Meow | "mm mm" *(Kareem: "he says chin up")* |
| `TXT_005` | Clavicoolar | *(selfie)* |
| `TXT_006` | Clavicoolar | "found a puddle. elite reflection. update later" |
| `TXT_007` | Oliver | "SMILE 😁" *(screen flashes white)* |
| `TXT_008` | Oliver | "accidentally drank coffee. i am a 40 watt bulb now" |
| `TXT_009` | Baby Stinkley | "hi" *(nobody replies)* |
| `TXT_010` | Baby Stinkley | "i've been in the chat the whole time btw" |
| `TXT_011` | Grandpa (added by mistake) | "HOW DO I TURN THIS OFF" |
| `TXT_012` | Grandpa | "In my day, group chats were rocks. We shouted into them." |
| `TXT_013` | Kareem | "kevin rate your night out of 10" — Kevin: "5" — Clav: "consistent" |
| `TXT_014` | Concierge (hacks in, F7+) | "You have been removed from GLOW UP GANG." *(it hasn't worked; Kareem: "who invited the lamp")* |

---

## ELEVATOR ADS (`AD_`)

Voiced by the Concierge in a bright ad voice. Visuals in [DETAILS.md §14](DETAILS.md). Each ad is under 15 s.

| ID | Ride | Line |
| --- | --- | --- |
| `AD_001` | 1 → 2 | "Jaw Juice. It's green. ...That's it. That's the ad." |
| `AD_002` | 2 → 3 | "The Forward Collection, by Grandpa Jon Meow. Your face, but forwarder. Jars sold separately. Jars sold never." |
| `AD_003` | 3 → 4 | "Practice Helmets. Pre-dented. Because progress should be visible." |
| `AD_004` | 4 → 5 | "Rate-A-Mate. No photos. No bios. Just numbers. Find your five today." Kevin: "I'm already a five." Concierge: "Exactly." |
| `AD_005` | 5 → 6 | "Lost your Before Photo? We'll find it. We'll frame it. We'll hang it where you'll see it every morning." |
| `AD_006` | 6 → 7 | "Lathered Deluxe. The fourteen-step routine, now in twenty-eight steps. Showering not included. Showering is step twenty-nine." |
| `AD_007` | 7 → 8 | *(no ad; static, then silence. Screen: "Loading…")* |

---

## THE CONCIERGE — random announcements (`PA_`)

Play every 2–4 minutes on any floor (not during dialogue). Pick randomly, never repeat in the same run.

| ID | Line |
| --- | --- |
| `PA_001` | "Reminder: your face is loading. Please be patient." |
| `PA_002` | "Today's affirmation: you could be a seven. With work. A lot of work." |
| `PA_003` | "Lost property: one jawline. If found, please don't return it. We're keeping it." |
| `PA_004` | "The gift shop is closed. The gift shop is always closed. There is no gift shop." |
| `PA_005` | "Staff reminder: Brenda is on her break. Brenda has been on her break since 1997." |
| `PA_006` | "Have you tried drinking more water? Have you tried drinking LESS water? Have you tried water?" |
| `PA_007` | "Please do not feed the Ghouls. They only eat confidence." |
| `PA_008` | "Your consultation is very important to us. Please continue to be mid." |
| `PA_009` | "Fun fact: mirrors in this building are two-way. We are always on the other side." |
| `PA_010` | "Would the owner of a grey hoodie please report to… anywhere. Please. You're making the place look average." |
| `PA_011` | "Sunrise in: soon. Probably. We don't actually have windows." |
| `PA_012` | "Attention: a Chico has been sighted. No, you didn't." |
| `PA_013` | "Rate your night out of ten. Your answer has been rounded down." |
| `PA_014` | "The elevator is working. The elevator is judging. These are not mutually exclusive." |
| `PA_015` | "This clinic is a parody. Any resemblance to real people is… honestly, a little concerning." |
| `PA_016` | "Reminder: wear your headgear twenty-two hours a day. The other two hours, it wears you." |
| `PA_017` | "The Forward Collection is now open. Please do not tap on the jars. They tap back." |
| `PA_018` | "Reminder: mirrors are for staff use only. You are not staff. You are content." |
| `PA_019` | "The ring lights in Corridor B are flickering. This is a feature." |
| `PA_020` | "Attention patients: hunter eyes may now be collected from the front desk. Please bring your own eyes." |
| `PA_021` | "We have received a complaint about the humming. The humming has received a complaint about you." |
| `PA_022` | "Today's lucky number is five. Today's unlucky number is also five." |
| `PA_023` | "Please stop asking Brenda for directions. Brenda is a skeleton. Respect her boundaries." |
| `PA_024` | "Customer survey: on a scale of one to ten, how would you rate being rated?" |
| `PA_025` | "The elevator has been cleaned. The elevator has also been rated. It got a four." |
| `PA_026` | "Lost and found update: we've found one more retainer. It's looking for you." |
| `PA_027` | "Sunrise is approaching. Please hurry. Or don't. We also have rooms." |
| `PA_028` | "For your safety, do not run in the spa. For our entertainment, please run in the spa." |
| `PA_029` | "A reminder that the Exit Mirror only shows people who deserve to leave. No pressure." |
| `PA_030` | "This announcement was rated a seven. You'd know if you were a seven." |

---

## DEATH SCREEN (`DEATH_`)

Big title: **NGMI**. Under it, one random line:

| ID | Line |
| --- | --- |
| `DEATH_001` | "Rating reached 0.0. You are now a hoodie." |
| `DEATH_002` | "Mogged by a Ghoul. Embarrassing for both of you." |
| `DEATH_003` | "Tip: ring lights heal. Darkness does not. Hope that helps." |
| `DEATH_004` | "You were one stamp away." |
| `DEATH_005` | "Even Brenda lasted longer." |
| `DEATH_006` | "Cause of death: bad angle." |
| `DEATH_007` | "Tip: Double Chin Blobs split when hit. Aim chin-up." |
| `DEATH_008` | "Tip: Mouth Breathers can't see. They can hear you panic." |
| `DEATH_009` | "Your Before Photo says hi." |
| `DEATH_010` | "Not Gonna Make It. This time." |
| `DEATH_011` | "Pulled in by the Headgear. Year 8 called." |
| `DEATH_012` | "Tip: Expander Spiders hate light. So do you, apparently." |
| `DEATH_013` | "Rated 0 out of 10 by the floor. The floor has standards." |
| `DEATH_014` | "Tip: the Headgear is blind. You, apparently, are too." |
| `DEATH_015` | "You looked away from a mannequin. Classic." |
| `DEATH_016` | "Slipped on foam. Dylan would be proud. Dylan would also be filming." |
| `DEATH_017` | "Your rating has been rounded down. To zero." |
| `DEATH_018` | "Kevin has left the group chat." |
| `DEATH_019` | "Battery 4%. Rating 0%. Vibes 0%." |
| `DEATH_020` | "Cause of death: read the comments." |
| `DEATH_021` | "The barber opens at 9. You won't." |
| `DEATH_022` | "Tip: stand in the ring light. It's right there. It was always right there." |
| `DEATH_023` | "Mogged by your own reflection. It was a beat late, but it got there." |
| `DEATH_024` | "Brenda has seen worse. Brenda has seen everything." |

Button labels: **[Try again]** shows as "Re-maxx" · **[Quit]** shows as "Cope".

---

## Recording notes (for VO later)

- Kevin: deadpan, low energy, never shouts except in the L2 chase. His sincerity in L5 and the Ascend ending must land; don't play it as a joke.
- The Concierge: bright customer-service voice, slightly too fast, never breathes. In E7 and L8 the brightness drops away. Its last three lines are soft.
- Dr. Meow: closed-mouth humming only, except the two "normal voice" lines.
- Keep every line under 4 s in gameplay; cutscene lines can run up to 8 s.
- Temp VO can be generated with AI voices for testing only; final launch voices should be actors (open decision O4). Never clone a real person's voice.
