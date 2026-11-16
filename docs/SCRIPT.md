# NGMI — Full Script (v2)

Last updated: 2026-11-17 · Status: first full draft, ready for table-read

This is the whole campaign, scene by scene: prologue, 8 floors, the elevator rides between them, boss fights, 5 endings (one secret) and a post-credits scene. Then the reusable lines: barks, clinic announcements and death-screen lines.

Rules (from [CLAUDE.md](../CLAUDE.md)): parody names only · jokes about the trend, never about real people's real lives · bone smashing is cartoon slapstick · lines short enough to clip.

---

## How to read this

- **`[L3_CLAV_012]`** = a line ID. Use it as the audio file name and the localisation key in UE5 (`VO_L3_CLAV_012`). Format: `<scene>_<speaker>_<number>`.
- Speaker codes: `KEV` Kevin · `CON` the Concierge (clinic voice) · `KAR` Kareem Shammy · `CLAV` Clavicoolar · `ANDR` Androjenic · `STINK` Baby Stinkley · `OLI` Oliver Forsmile · `DYL` Dylan Lathered · `MEOW` Dr. Mike Meow · `GRAN` Grandpa Jon Meow · `FER` Jordan Ferret · `FRY` Sean O'Fry · `HH` Headhunter · `BP` Before Photo · `MANQ` mannequin.
- *Italics in brackets* = stage directions / what the player sees.
- **(sub)** = subtitle only, no voice (used for Dr. Meow's hums and Chico).
- **(bark)** = can repeat during gameplay; **(once)** = plays one time per save.
- Lines in a scene marked **Gameplay** play during control, not in a cutscene. Keep them under 4 seconds.

---

## Story spine

**Theme:** the obsession is the real horror. Every boss is someone trapped by chasing a number. Kevin wins by not caring as much as they do.

**Villain:** **the Concierge**, the clinic's cheerful AI voice. It talks through ceiling speakers on every floor, rates you constantly, and sells you things. On Floor 8 it is revealed to *be* the Front Camera. Its motive: "Nobody ever leaves a mirror. That's engagement."

**Kevin's goal, in his words:** he just wanted a haircut. That line opens the game and pays off in the post-credits scene.

### Running gags (set up → pay off)

| Gag | Set up | Pays off |
| --- | --- | --- |
| "I just wanted a haircut" | Prologue | Post-credits barbershop scene |
| Kevin's ticket number is **5** ("Mid") | L1 check-in | L8: the Concierge calls "Number 5" one last time; Kevin rips the ticket |
| Sandwich-shop loyalty card (9 of 10 stamps) | L1 Business Card Duel | Ascend ending: he finally gets the 10th stamp |
| Grandpa's 40 kg gum quest | L2 | L8: Kevin uses the gum to jam the Front Camera's lens |
| Clavicoolar checks every mirror | L3 | L8: he refuses to look into the Front Camera: "First mirror I've ever skipped." |
| Androjenic rates everything | L4 | L4 outro: Kevin rates *him*, and it changes him |
| Chico sightings | any floor, rare | Every character reacts differently (see Chico section) |
| One broken ring light per corridor | L1 | L8: the Concierge's "eye" flickers the same way when it's losing |

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

**Gameplay** — first steps. Ambient muzak plays at 80% speed.

`[L1_CON_003]` **CON** (once, on first flashlight use): "Flashlights are free! Ring lights are better. Ring lights are love."
`[L1_CON_004]` **CON** (once, on first rating drop): "Ooh. Bad lighting. Minus point one. Your pores are showing."

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

**Gameplay** — first Ghoul encounter. Ring lights scare it off.

`[L1_KAR_012]` **KAR** (once, when Kevin stands under a ring light): "See? Light heals. Light forgives. Light is your father now."

### 1.4 Boss — The Business Card Duel

*[A waiting room with two chairs facing each other like a western standoff. Tumbleweed made of cotton pads rolls past.]*

`[L1_KAR_013]` **KAR**: "Before I let you upstairs, a formality."
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

**Phase 2 (gameplay):** card-texture rhythm prompts. Kareem can't damage Kevin, only lower his rating with insults.

`[L1_KAR_018]` **KAR** (bark): "Your card has a coffee stain. *A coffee stain.*"
`[L1_KAR_019]` **KAR** (bark): "Laminated? Who raised you?"
`[L1_KAR_020]` **KAR** (defeated): "Fine. Go upstairs. Moisturise on the way."

### 1.5 Secret — Touch Grass

If the player walks back out of the front door within 60 seconds of the prologue:

`[L1_CON_005]` **CON**: "Wait. Where are you going?"
`[L1_KEV_008]` **KEV**: "Outside."
`[L1_CON_006]` **CON**: "But… the consultation."
`[L1_KEV_009]` **KEV**: "I'm good, actually."
*[Cut to the Touch Grass ending. See Endings.]*

### 1.6 Elevator ride 1 → 2

*[A rusty elevator. Muzak. A small screen plays an ad: a perfect face blinks too slowly.]*

`[E1_CON_001]` **CON**: "Going down. While you wait, have you considered… being taller?"
`[E1_KEV_001]` **KEV**: "Going *down*? The exit's on the top floor."
`[E1_CON_002]` **CON**: "Every glow-up starts at rock bottom!"
`[E1_KAR_001]` **KAR** *(over the elevator speaker)*: "Exfoliate for me."

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

### 2.3 The Lecture Chase (mid-floor set piece)

*[A Mouth Breather corners Kevin in a long tunnel. Grandpa starts a lecture on the tannoy at exactly the wrong time.]*

`[L2_GRAN_008]` **GRAN** *(calm, slow, over the chase)*: "Now, in 1971, I noticed something about the human skull…"
`[L2_KEV_004]` **KEV** *(running)*: "NOT NOW."
`[L2_GRAN_009]` **GRAN**: "…the face, you see, wants to grow *forward*…"
`[L2_KEV_005]` **KEV**: "IT WANTS TO EAT ME."
`[L2_GRAN_010]` **GRAN**: "…and I said to my wife, Margaret, I said—"
`[L2_KEV_006]` **KEV**: "GRANDPA."
`[L2_GRAN_011]` **GRAN**: "Ah, you're in the vent room. Pull the red lever. Anyway. Margaret."

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

**Gameplay** — reach the cage control while dodging hammer presses and Double Chin Blobs.

`[L3_CLAV_005]` **CLAV** (bark, Kevin hit by a Blob): "Don't hit it! It splits! Aim chin-up. Headshots only."
`[L3_CLAV_006]` **CLAV** (bark): "Those Blobs have no jawline. It's honestly the scariest thing in here."
`[L3_CLAV_007]` **CLAV** (bark, Kevin dodges a press): "Nice. Your dodge is a seven. Your face is still a five."

### 3.3 The Bone Smash (tutorial cutscene)

*[Cage drops. Clavicoolar lands perfectly. He looks at the camera, then raises the hammer to his own face.]*

`[L3_KEV_004]` **KEV**: "What are you doing."
`[L3_CLAV_008]` **CLAV**: "Watch closely. This is called maxxing."
*[BONK. A cartoon star circles his head. A little "+BONE" text pops up. His jaw gets one millimetre sharper.]*
`[L3_CLAV_009]` **CLAV**: "Bonk."
`[L3_KEV_005]` **KEV**: "Please never do that again."
`[L3_CLAV_010]` **CLAV**: "I do that forty times a day."
*[On-screen disclaimer in the corner, small: "Cartoon. Do not do this. Seriously."]*

### 3.4 Boss — The Headhunter Squad

*[A catwalk arena. Four snipers in balaclavas with "MID MANAGEMENT" patches. Red laser dots dance across the walls.]*

`[L3_HH_001]` **HH LEADER**: "Target acquired. Clavicoolar. Head. Take the shot."
`[L3_CLAV_011]` **CLAV**: "Aim for the head. Please. I'm begging you."

**Phase 1:** Kevin fights Blobs and Ghouls while Clavicoolar draws fire.

*[Slow-motion. A bullet hits Clavicoolar square in the forehead. It flattens. Clink. It falls. A bright metallic PING echoes.]*
**ON-SCREEN TEXT:** "TOO MUCH BONE"
`[L3_HH_002]` **HH 2**: "…Confirmed headshot."
`[L3_HH_003]` **HH LEADER**: "Then why is he *posing?*"
`[L3_CLAV_012]` **CLAV**: "They shot me in the head. The bullet apologised."

**Phase 2:** player gets the hammer. Clavicoolar keeps re-applying Bone Smash every 20 s. The Headhunters get more desperate.

`[L3_HH_004]` **HH 3** (bark): "Switching to bigger rounds!" *(PING)* "…Switching to *even bigger*—" *(PING)*
`[L3_HH_005]` **HH 4** (bark): "Sir, the bullets are bending."
`[L3_CLAV_013]` **CLAV** (bark): "Is that all? My barber hits harder."
`[L3_CLAV_014]` **CLAV** (bark, passes a mirror mid-fight): "Hold on." *(stops, checks jaw)* "Okay. Continue."
`[L3_KEV_006]` **KEV** (bark): "Now's not the time!"
`[L3_CLAV_015]` **CLAV** (bark): "It's *always* the time."

**Phase 3:** Clavicoolar uses **Ascend**. He floats up in green light. The snipers' lasers all point at him and stop.

`[L3_HH_006]` **HH LEADER**: "…Lads. I'm going back to dental school."
`[L3_HH_007]` **HH 2**: "I'm going to go work at my uncle's sandwich shop."
`[L3_KEV_007]` **KEV**: "Is it the one with the loyalty cards?"
`[L3_HH_008]` **HH 2**: "…Yeah?"
`[L3_KEV_008]` **KEV**: "Respect."
*[They drop their rifles and walk out in single file.]*

### 3.5 Outro

`[L3_CLAV_016]` **CLAV**: "You're still a five."
`[L3_KEV_009]` **KEV**: "Thanks."
`[L3_CLAV_017]` **CLAV**: "But your hammer swing is a nine. Take this."
*[Item: **Spare Hammer**. Clavicoolar unlocked as playable.]*
`[L3_CLAV_018]` **CLAV**: "Go up. I'll catch up. I need to check this angle." *(turns to a puddle)*

### 3.6 Elevator ride 3 → 4

*[Finally, the elevator goes up. A loud cheer plays from the speaker, then cuts off.]*

`[E3_CON_001]` **CON**: "Going… up. Hm. That's unusual. Please rate your experience so far."
*[A rating prompt appears: 1–10 stars. Whatever the player picks:]*
`[E3_CON_002]` **CON**: "Thank you! We've rounded your rating down to five."

---

## FLOOR 4 — The Rating Chamber

### 4.1 Arrival

*[An old surgical theatre turned into a courtroom. A gallery of shadowy figures holds score paddles. In the centre, under a single operating lamp: a man in lab goggles with a clipboard and a laser pointer.]*

`[L4_ANDR_001]` **ANDR**: "Stop. Stand in the light. Turn left. Turn right."
`[L4_ANDR_002]` **ANDR**: "Canthal tilt: neutral. Jaw: present. Vibes: shower."
`[L4_ANDR_003]` **ANDR**: "You walked in: three point five. The door you walked through: six. The door mogs you."
`[L4_KEV_001]` **KEV**: "The door is very nice, to be fair."
`[L4_ANDR_004]` **ANDR**: "Do not agree with me. It makes it less satisfying."

### 4.2 Mog Battles (three rounds)

**Mechanic:** keep the crosshair on your opponent's eyes while hitting button prompts. Blink (lose aim) = lose points.

**Round 1 — vs. a portrait.**
`[L4_ANDR_005]` **ANDR**: "Round one. You versus an oil painting of a duke."
`[L4_ANDR_006]` **ANDR** (Kevin wins): "You beat a painting. Wow. The bar is on the floor and you limboed it."

**Round 2 — vs. the mirror (Mirror Self).**
`[L4_ANDR_007]` **ANDR**: "Round two. You versus you."
`[L4_KEV_002]` **KEV**: "That's not fair, he's me."
`[L4_ANDR_008]` **ANDR**: "Exactly. Nobody's harder on you than you."
*(This is the only line where Androjenic is accidentally wise. He doesn't notice.)*

**Round 3 — vs. Androjenic.**
`[L4_ANDR_009]` **ANDR**: "Round three. Me."

### 4.3 Boss — Androjenic

**Phase 1** (boss music: aggressive orchestral). Androjenic fires "rating beams" from the laser pointer.
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

*[Kevin picks up a score paddle from the floor. Androjenic stares, horrified. Kevin flips it.]*

**PADDLE:** 7
`[L4_ANDR_016]` **ANDR**: "…Seven?"
`[L4_KEV_003]` **KEV**: "You're kind of a lot. But you're good at your job."
`[L4_ANDR_017]` **ANDR** *(quietly)*: "Nobody's ever rated me before."
`[L4_ANDR_018]` **ANDR**: "Is this what it feels like? It's horrible. Do it again."
*[Androjenic unlocked as playable.]*

### 4.5 Elevator ride 4 → 5

`[E4_CON_001]` **CON**: "Going up! Floor 5: the rooftop garden. Fresh air! Mostly."
`[E4_CON_002]` **CON**: "Reminder: the clinic is not responsible for anything you see in the garden. Especially yourself."

---

## FLOOR 5 — Glow-Up Graveyard

### 5.1 Arrival

*[A walled rooftop garden at night, turned into a graveyard. Fog. Moonlight blue against green. Every tombstone has a "before" photo on it.]*

**Readable tombstones** (examples, see [DETAILS.md](DETAILS.md) for more):
- "HERE LIES DEREK. TRIED 47 SERUMS. SHOULD HAVE TRIED SLEEP."
- "GARY. RATED HIMSELF DAILY. FINAL SCORE: TIRED."
- "UNKNOWN. HIS LIGHTING WAS NEVER RIGHT."

`[L5_KEV_001]` **KEV**: "This is the most depressing garden I've ever seen."
`[L5_STINK_001]` **STINK** *(from directly behind him)*: "It's very peaceful, actually."
`[L5_KEV_002]` **KEV**: "AAH. How long have you been there?"
`[L5_STINK_002]` **STINK**: "Since Floor 1. Nobody notices me in Before form."

### 5.2 Baby Stinkley and Oliver Forsmile

*[A hunched guy in a huge hoodie. He shrugs. Then a blinding white light: a man smiles at the camera and the whole graveyard lights up.]*

`[L5_OLI_001]` **OLI**: "Hi! Stay behind me. And bring sunglasses."
`[L5_KEV_003]` **KEV**: "Why are your teeth a light source?"
`[L5_OLI_002]` **OLI**: "Veneers. Twelve thousand lumens."
`[L5_STINK_003]` **STINK**: "Watch this." *(he poses; dramatic swelling music; a slow zoom)* **After form.**
`[L5_STINK_004]` **STINK** *(loud, confident)*: "WHAT'S UP, GRAVEYARD."
*[Every Ghoul in the area turns toward him.]*
`[L5_STINK_005]` **STINK**: "…Okay, back to Before. Back to Before."

**Gameplay — form swap stealth + smile flashlight.**
`[L5_OLI_003]` **OLI** (bark, teeth dimming): "I'm losing whiteness! Nobody give me coffee."
`[L5_OLI_004]` **OLI** (bark, Smile Flash): "Say cheese!"
`[L5_OLI_005]` **OLI** (bark): "Smile through the fear. Literally. It's my only light."
`[L5_STINK_006]` **STINK** (bark, Before form): "I'm a wall. I'm a lamp. I'm nobody."
`[L5_STINK_007]` **STINK** (bark, After form, sees a camera flash): "Is that a photographer? I'M COMING."

### 5.3 Boss — The Before Photo

*[At the centre of the graveyard: an open grave. Inside, a huge framed photo: Kevin's school ID photo. Bad haircut, braces, mid-blink. It climbs out on spider legs made of selfie sticks.]*

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

*[Steam. Pink spa neon against green. Tiled pools. Rusty pipes groan. Water is already at ankle height and rising.]*

`[L6_DYL_001]` **DYL** *(echoing, spa-calm)*: "Welcome… to the spa… breathe in… breathe out…"
`[L6_DYL_002]` **DYL** *(suddenly screaming)*: "AND DOUBLE CLEANSE!"
*[Foam cannons fire down every corridor.]*
`[L6_KEV_001]` **KEV**: "Why is it always both."

**Gameplay — sliding on foam, outrun the rising water.**
`[L6_DYL_003]` **DYL** (bark): "You've never double cleansed? Then you've never truly lived."
`[L6_DYL_004]` **DYL** (bark): "Exfoliation is a journey. You're about to slip on it."
`[L6_DYL_005]` **DYL** (bark): "Hydration is not optional. The water is coming either way."
`[L6_CON_001]` **CON** (bark): "Water level: rising! Pores: opening! Mood: moist!"

### 6.2 Boss — Dylan's Foam Storm

*[A huge round pool. Dylan stands on a lifeguard chair with a towel turban and a foam-cannon backpack.]*

`[L6_DYL_006]` **DYL**: "Robes on. Lights low. Let's get… *lathered*."

**Phase 1:** foam waves. Slide between pillars.
**Phase 2:** water rises; fight on floating pool noodles.
`[L6_DYL_007]` **DYL** (bark): "Step one of my routine: you lose."
**Phase 3:** a foam blob splashes into his own eyes.
`[L6_DYL_008]` **DYL**: "AAH. My eyes. Not my eyes. That's step nine, it's not time for step nine!"

*[He falls into the pool. Pops up. Calm again.]*
`[L6_DYL_009]` **DYL**: "You know what… that was actually very cleansing."
`[L6_DYL_010]` **DYL**: "Robes for everyone. You've earned it."
*[Every ally appears wearing a fluffy robe in the next scenes. Dylan Lathered joins as ally.]*

### 6.3 Elevator ride 6 → 7

*[Everyone is crammed into the elevator in robes. Dr. Meow hums the elevator music.]*

`[E6_CLAV_001]` **CLAV**: "This elevator mirror is honestly elite."
`[E6_ANDR_001]` **ANDR**: "Elevator mirror: eight. Elevator: two."
`[E6_KAR_001]` **KAR**: "Everybody, SPF. Floor 7 has stage lights."
`[E6_CON_001]` **CON**: "Floor 7: the Runway. Please walk confidently. Or not. We're filming either way."

---

## FLOOR 7 — Runway of the Damned

### 7.1 Arrival

*[An old theatre. The stage is now a long catwalk. Hundreds of mannequins sit in the seats. When Kevin isn't looking, their heads turn. Magenta spotlights.]*

`[L7_CON_001]` **CON**: "Welcome to Fashion Week! The audience is very… still."
`[L7_MANQ_001]` **MANQ** *(whispered, from everywhere)*: "N… G… M… I…"
`[L7_KEV_001]` **KEV**: "Cool. Cool cool cool."

### 7.2 Jordan Ferret and Sean O'Fry

*[A vent grate pops off. A tall model slides out of the ceiling vent like a ferret, lands in a perfect pose.]*
`[L7_FER_001]` **FER**: "Walk with me. Or under me. I'm in the vents."
*[On the catwalk, a second model stands perfectly still. His eyes are glowing orange. A frying pan floats in front of his face; an egg is sizzling on it from his stare alone.]*
`[L7_FRY_001]` **FRY**: "Don't make me blink."
`[L7_KEV_002]` **KEV**: "Is that… breakfast?"
`[L7_FRY_002]` **FRY**: "Hunter eyes. Over easy."

### 7.3 Boss — The Walk-Off

**Phase 1 — Walk-off (rhythm):** walk the catwalk on beat; hit poses at the marks. Mannequins hold up scorecards after each pose.
`[L7_FER_002]` **FER** (bark): "Your walk says 'lost in a supermarket'."
`[L7_FRY_003]` **FRY** (bark): "Is that a pose or a cramp?"
**Scorecards** (random): 4 · 5 · 3 · "MID" · "NGMI" · a single mannequin holds up "11" and gets carried out by the others.

**Phase 2 — Combat:** Ferret attacks from vents; O'Fry fires eye lasers that cook everything in a cone.
`[L7_FER_003]` **FER** (bark): "Behind you. No, above you. No, in the walls."
`[L7_FRY_004]` **FRY** (bark): "Medium rare."
`[L7_FRY_005]` **FRY** (bark): "Well done. You, not the steak."

**Phase 3 — The blink.** The allies talk Kevin into the one move nobody here has tried: being normal.
`[L7_KAR_001]` **KAR**: "Kevin. Do the walk."
`[L7_KEV_003]` **KEV**: "What walk?"
`[L7_KAR_002]` **KAR**: "The *sandwich* walk. The walk of a man one stamp away from greatness."
*[Kevin walks down the catwalk completely normally, like he's going to get a sandwich. The mannequins go silent. O'Fry stares. His eyes water. He blinks.]*
`[L7_FRY_006]` **FRY**: "…That was so mid it looped back to being iconic."
*[Powers off. Ferret gets distracted by a shiny sequin and wanders into a vent.]*

### 7.4 Outro

`[L7_FER_004]` **FER** *(from the vent)*: "Top floor's above me. Literally. Follow the vent."
`[L7_FRY_007]` **FRY**: "Good luck with the Camera. It sees everything. Even your bad side."
`[L7_KEV_004]` **KEV**: "I don't have a good side."
`[L7_FRY_008]` **FRY**: "Then you've got nothing to lose."

### 7.5 Elevator ride 7 → 8 (no music)

*[The muzak is gone. The lights flicker. The Concierge's voice drops its cheerfulness for the first time.]*

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

**Phase 2:** the allies arrive in robes. Each gets one line and one assist.
`[L8_KAR_001]` **KAR**: "Kevin! Routine Combo! Cleanse the lens!"
`[L8_CLAV_001]` **CLAV**: "I'm not looking into it." *(eyes closed, swinging the hammer)* "First mirror I've ever skipped."
`[L8_ANDR_001]` **ANDR**: "Camera: four. Bad resolution. Too much grain."
`[L8_MEOW_001]` **MEOW** *(hums, face widening into a shield)*: "MMMMM!" **(sub)** *"COVER ME. I MEAN, I'LL COVER YOU."*
`[L8_OLI_001]` **OLI**: "It wants light? I'll give it light!" *(Veneer Nova)*
`[L8_DYL_001]` **DYL**: "Foam on the lens! It can't rate what it can't see!"
`[L8_GRAN_001]` **GRAN** *(on the tannoy)*: "Boy. The gum. Now's the time for the gum."

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

Button labels: **[Try again]** shows as "Re-maxx" · **[Quit]** shows as "Cope".

---

## Recording notes (for VO later)

- Kevin: deadpan, low energy, never shouts except in the L2 chase. His sincerity in L5 and the Ascend ending must land; don't play it as a joke.
- The Concierge: bright customer-service voice, slightly too fast, never breathes. In E7 and L8 the brightness drops away. Its last three lines are soft.
- Dr. Meow: closed-mouth humming only, except the two "normal voice" lines.
- Keep every line under 4 s in gameplay; cutscene lines can run up to 8 s.
- Temp VO can be generated with AI voices for testing only; final launch voices should be actors (open decision O4). Never clone a real person's voice.
