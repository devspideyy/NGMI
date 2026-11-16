# NGMI — Little details

Small touches that make the game feel alive, funny, and worth clipping. None of them are required to finish the game; together they're what people remember.

Last updated: 2026-11-17

**Cost** = rough effort in UE5: **S** (under a day), **M** (a few days), **L** (a week+).
**Priority**: ★★★ do in the vertical slice · ★★ before demo · ★ nice to have.

Every detail follows [CLAUDE.md](../CLAUDE.md) rules: parody names only, jokes about the trend, no real people's real lives.

---

## Top picks (if you only do these)

| # | Detail | Where | Cost | Priority |
| --- | --- | --- | --- | --- |
| 1 | Face Rating number **ticks** with a tiny sound on every change (+0.5 "glow" chime, −1.0 "mogged" bass thud) | HUD | S | ★★★ |
| 2 | "TOO MUCH BONE" headshot: 0.3 s slow-mo, metallic PING, bullet flattens and drops, text stamps on screen | L3 | M | ★★★ |
| 3 | Mirrors show Kevin's reflection **one frame late** | All | M | ★★★ |
| 4 | One ring light per corridor is broken and flickers dead (same flicker pattern returns on the Front Camera when it's losing) | All, L8 | S | ★★★ |
| 5 | Death screen: big **NGMI**, random funny line, buttons "Re-maxx" / "Cope" | UI | S | ★★★ |
| 6 | The Concierge's random PA announcements (15 lines in SCRIPT.md) | All | S | ★★★ |
| 7 | Readable tombstones with joke epitaphs | L5 | S | ★★ |
| 8 | Brenda the skeleton receptionist with perfect glowing skin; her chair slowly turns to face you when you're not looking | L1 | S | ★★ |
| 9 | Kevin's ticket "5" visible in the inventory the whole game; ripped in the finale | All, L8 | S | ★★ |
| 10 | Rating Card share image after every run | UI | M | ★★ |
| 11 | Dr. Meow's hums are subtitled with full sentences | L2+ | S | ★★ |
| 12 | Mannequins turn their heads when you look away | L7 | M | ★★ |
| 13 | Elevator rides with ads on a small screen (covers level loading) | Between floors | M | ★★ |
| 14 | Settings menu jokes ("Jawline quality: Ultra") | Menu | S | ★★ |
| 15 | Post-credits barbershop scene | End | M | ★★ |
| 16 | Wall jokes on every floor (section 12) | All | S | ★★★ |
| 17 | Orthodontic horror: Expander Wall, Headgear stalker, The Chair (section 13) | L2, L4 | M | ★★★ |

---

## 1. HUD and UI

| Detail | Cost | Priority |
| --- | --- | --- |
| Face Rating shows as a big number top-left with a tiny face icon that looks more "mid" as it drops (eyebrows lower, mouth flattens) | S | ★★★ |
| Rating pop-ups: "+0.5 GLOW", "−1.0 MOGGED", "−0.1 BAD LIGHTING" in the green UI font | S | ★★★ |
| At rating under 2.0, the screen edges get a grey hoodie-fabric texture creeping in (you're turning into a Ghoul) | M | ★★ |
| Interact prompts are written like a clinic: "[E] Consult", "[E] Exfoliate", "[E] Inspect angle" | S | ★★ |
| Objective text uses clinic language: "Current treatment: Escape" · "Next appointment: Floor 4" | S | ★★ |
| Pause menu title: "Consultation paused" | S | ★ |
| Loading screen is a progress bar labelled "Face loading…" that stalls at 50% for a moment, then jumps | S | ★ |
| Collectibles counter is called "Before Photos found: 12/50" | S | ★ |
| Subtitles have a speaker colour per character (Concierge = green, Kareem = pearl white, Clav = steel, etc.) | S | ★★ |
| Kevin's notes app: an in-game phone shows a to-do list that updates ("☐ haircut ☐ escape haunted clinic ☐ buy milk") | M | ★ |

## 2. Settings and menus

| Detail | Cost | Priority |
| --- | --- | --- |
| Graphics option "Jawline quality: Low / Medium / High / Ultra / Mogging" (it secretly does nothing) | S | ★★ |
| Brightness calibration screen: "Adjust until the Ghoul is *barely* visible. Like your self-esteem." — then a gentler "Adjust until the symbol is barely visible" line in the accessibility version | S | ★★ |
| FOV slider labelled "Field of view (how much of yourself you can stand)" with a normal label in tooltip | S | ★ |
| Difficulty names: "Normie" · "Mid" · "Mogged" · "NGMI" | S | ★★ |
| Credits include "Brenda — Receptionist (since 1997)" and "Parody. Not affiliated with any real person." | S | ★★★ |
| Main menu background: the clinic entrance, rain, the neon sign flickering "NO REFUND" | M | ★★ |
| Quit confirmation: "Leave the clinic? (You'd be surprised how few people do.)" | S | ★ |
| Photosensitivity toggle that reduces flicker everywhere (keeps the joke, removes the strobe) | S | ★★★ |

## 3. Audio

| Detail | Cost | Priority |
| --- | --- | --- |
| Lobby muzak plays at 80% speed; speeds up to normal for one second when you heal | S | ★★ |
| Ring lights hum in a slightly out-of-tune chord; broken ones crackle | S | ★★★ |
| Bone Smash is a cartoon "bonk" plus a tiny xylophone note, never a realistic crunch | S | ★★★ |
| Mouth Breathers' breathing is spatialised; you can locate them by ear with headphones | M | ★★★ |
| The Concierge PA voice comes from the nearest ceiling speaker (positional), so you can find speakers by sound | S | ★★ |
| Elevator music is the same 4-bar loop on every ride; on the last ride it's gone (silence is the scare) | S | ★★ |
| Sad trombone when Dr. Meow opens his mouth | S | ★★ |
| Androjenic's boss music genuinely switches genre mid-fight (orchestral → lounge jazz → hardstyle), synced to his lines | M | ★★ |
| Footsteps change by surface: tile squeak (L1, L6), wet brick (L2), metal grate clank (L3), grass (L5), stage wood (L7), glass (L8) | M | ★★ |
| Oliver's smile makes a soft "ting" sparkle sound every time he uses it | S | ★ |
| A choir note plays for Chico; it's cut off the instant he vanishes | S | ★★ |

## 4. Kevin (player) details

| Detail | Cost | Priority |
| --- | --- | --- |
| First-person hands: bitten nails, cheap digital watch that shows the real in-game time to sunrise | M | ★★ |
| Flashlight is a phone torch; its battery is the phone battery; it buzzes with the Concierge's notifications | M | ★★ |
| When Kevin passes a mirror he never stops (contrast with Clavicoolar) — except once, in L8 | S | ★★ |
| Idle 30 s: Kevin checks his phone; the screen shows "Barbershop: CLOSED · opens 9 AM" | S | ★ |
| Taking damage at low rating: his breathing gets heavier and the camera bob gets sloppier | S | ★★ |
| Kevin's hoodie is visible on his arms; at 0 rating, the hoodie sleeves cover his hands | S | ★ |

## 5. Character micro-details

| Character | Detail | Cost | Priority |
| --- | --- | --- | --- |
| Clavicoolar | Stops at every reflective surface for 3 s, including puddles and the back of a spoon | S | ★★★ |
| Clavicoolar | His hammer has a rubber grip with "MAXX" written on it in marker | S | ★ |
| Kareem Shammy | His sheet mask slowly slips off during the boss fight; he fixes it between phases | S | ★★ |
| Kareem Shammy | Wipes every surface before he touches it | S | ★ |
| Androjenic | Writes on his clipboard constantly; if you get close, you can read "Kevin: 5. Hoodie: 4." | S | ★★ |
| Baby Stinkley | In Before form, NPCs bump into him and say "sorry, didn't see a wall there" | S | ★★ |
| Oliver Forsmile | His smile lights up dust particles in the air like a real flashlight beam | M | ★★ |
| Dylan Lathered | Leaves a trail of foam footprints that slowly fade | S | ★ |
| Dr. Mike Meow | Nods very enthusiastically instead of speaking; jaw visibly 2 cm smaller after he talks | S | ★★ |
| Grandpa Jon Meow | Never seen until L8; his tannoy has a "Margaret" photo taped next to the mic (visible in the L8 window) | S | ★ |
| Jordan Ferret | Leaves vent grates slightly open everywhere he's been; you can follow his route | S | ★ |
| Sean O'Fry | Eggs fried by his gaze are scattered around L7 as pickups (+0.25 rating, "Protein!") | S | ★★ |
| Chico | Always slightly out of focus via depth of field, never sharp, even in screenshots | S | ★★ |

## 6. Environment storytelling

| Detail | Where | Cost | Priority |
| --- | --- | --- | --- |
| Waiting-room TV loops before/after ads where the "after" photo is the same photo with a ring light | L1 | S | ★★ |
| Magazine rack: covers like "Jawline Weekly", "Pore Mechanics", "Is Your Chin Lying To You?" | L1 | S | ★★ |
| Suggestion box overflowing with notes: "more mirrors", "fewer mirrors", "let me out" | L1 | S | ★ |
| Chalk tally marks on the catacomb walls counting "days mewing" | L2 | S | ★★ |
| Grandpa's old posters: diagrams of skulls with arrows saying "FORWARD!" | L2 | S | ★★ |
| Chewed-gum stalactites hanging from the ceiling near Grandpa's tannoy | L2 | S | ★ |
| Hammers hung on a pegboard like a tool shop, labelled by "bone level" | L3 | S | ★★ |
| A dented helmet labelled "Practice" on a shelf | L3 | S | ★ |
| Gallery seats with tiny scorecards still on them; one seat has a 10 that's been crossed out | L4 | S | ★ |
| Tombstone epitaphs: "Here lies Derek. Tried 47 serums. Should have tried sleep." · "Gary. Rated himself daily. Final score: tired." · "Unknown. His lighting was never right." · "Steve. Took 3,000 selfies. Found his angle. Too late." · "Kyle. Went to the gym. Forgot to leave." | L5 | S | ★★★ |
| Fresh flowers on one grave: "Mum. Thought I looked fine." | L5 | S | ★★ |
| Spa price list on the wall where every price is "Your soul" except "Water: $14" | L6 | S | ★ |
| Fluffy robes on hooks; one robe has a name tag "BRENDA" | L6 | S | ★ |
| Backstage mirrors with lightbulbs, notes taped on: "Smile with your eyes." "Don't blink." | L7 | S | ★★ |
| The audience mannequins all wear the same grey hoodie as Kevin | L7 | S | ★★ |
| Notification bubbles you jump on say things like "3 people viewed your profile" and "Your screen time is up 400%" | L8 | M | ★★★ |

## 7. Interactables (press E)

| Detail | Response | Cost | Priority |
| --- | --- | --- | --- |
| Ticket machine | Always prints "5" | S | ★★★ |
| Water cooler | "+0.25. Hydrated. Still mid." | S | ★★ |
| Vending machine | Only sells "Jaw Juice" (fake, green); Kevin: "Of course." | S | ★★ |
| Mirror | Kevin: "Yep. That's me." (once per mirror) | S | ★★ |
| Scale in L1 | Shows "?" and the Concierge says "We don't do numbers here. Except all the other numbers." | S | ★ |
| Phone booth | Rings once; if answered, the Concierge: "Just checking you're still mid." | S | ★ |
| Toilet in L6 | Flushing makes the water level rise faster. Kevin: "Bad call." | S | ★ |
| Piano in L7 | Plays the elevator music | S | ★ |

## 8. Enemies

| Detail | Cost | Priority |
| --- | --- | --- |
| Sub-5 Ghouls all wear the same grey hoodie; when they lose track of you, they sit and scroll an invisible phone | S | ★★★ |
| Ghouls flinch away from ring lights with a little hiss | S | ★★ |
| Double Chin Blobs make a wobbling jelly sound; when they split, each half gets a smaller, squeakier voice | S | ★★ |
| Recessed Chin Crawlers drip water before they drop (warning) | S | ★★★ |
| Mouth Breathers pause and "listen" with their head tilted when you make a sound | S | ★★ |
| Mirror Self copies your emotes, but a beat late | M | ★★ |
| The Front Camera's "eye" shows a loading spinner when it's stunned | S | ★★ |

## 9. Easter eggs

| Detail | Cost | Priority |
| --- | --- | --- |
| Chico sightings (1 in 50 runs); screenshot him 3 times to unlock | M | ★★ |
| A sandwich-shop flyer is hidden on every floor; finding all 8 gives Kevin a golden loyalty card skin | S | ★★ |
| Typing "TOUCHGRASS" on the main menu plays birdsong | S | ★ |
| Brenda appears in a different place on every floor (a portrait, a robe tag, a mannequin) | S | ★★ |
| One Ghoul in L1 is wearing a crown; it's the "Mid King" and drops a cosmetic hat | S | ★ |
| The credits have a hidden final line after 30 s of waiting: "You can go to bed now." | S | ★ |

## 10. Achievements

| Name | Condition |
| --- | --- |
| **Just a Trim** | Finish the game |
| **Touch Grass** | Find the secret ending |
| **TOO MUCH BONE** | Watch 50 bullets bounce off Clavicoolar |
| **Shower Is A Routine** | Fail 10 Routine Combos |
| **Nine Out Of Ten** | Win the Business Card Duel |
| **Mouth Closed** | Finish Floor 2 without making a sound |
| **Rate The Rater** | Give Androjenic a 7 |
| **I Was Happy** | Keep your Before Photo |
| **Double Cleansed** | Beat Dylan without slipping |
| **Sandwich Walk** | Win the walk-off with the default walk |
| **Rear Camera** | Beat the Front Camera |
| **Cryptid Hunter** | Screenshot Chico |
| **Brenda's Friend** | Find Brenda on every floor |
| **Mid Forever** | Finish with exactly 5.0 rating |
| **Jestermaxxed** | Get the Jester ending |

## 11. Accessibility (also make the game better)

| Detail | Cost | Priority |
| --- | --- | --- |
| Subtitles on by default, with speaker names and colours | S | ★★★ |
| Jump-scare intensity slider (full / reduced / off) | M | ★★ |
| Flicker reduction (photosensitivity) | S | ★★★ |
| Mic mode is opt-in, local only, with a clear "mic is listening" icon | S | ★★★ |
| Hold-to-mew can be toggle-to-mew | S | ★★ |
| Colour-blind safe UI; green grade never carries information alone | S | ★★ |

## 12. Wall jokes (signs, posters, graffiti)

Readable text on the walls is the cheapest comedy in the game: one decal each. Place one every ~20 m of corridor, more in safe rooms, fewer in chases. Font style per type: **Sign** = clinic signage (clean, green) · **Poster** = glossy ad · **Graffiti** = scratched/marker · **Notice** = printed A4 taped up.

### Floor 1 — The Waiting Room
| Type | Text |
| --- | --- |
| Sign | "PLEASE TAKE A NUMBER. YOUR NUMBER IS 5." |
| Sign | "Estimated waiting time: until you're a 10." |
| Poster | "BEFORE → AFTER" (both photos identical; the After one has a ring light) |
| Notice | "Employee of the Month: Brenda. (Every month since 1997.)" |
| Sign | "Smile! You're on 400 cameras." |
| Notice | "Have you rated yourself today? ☐ Yes ☐ Also yes" |
| Sign | "Wet floor. Great for your skin." |
| Notice | "Mirrors removed from toilets. They kept staring back." |
| Graffiti | "i came in for a haircut" (Kevin stops and reads it twice) |

### Floor 2 — Mewing Catacombs
| Type | Text |
| --- | --- |
| Sign | "QUIET ZONE. Mouth Breathers on duty." |
| Sign | "Nose breathing only beyond this point." |
| Graffiti | "Day 4,312 of mewing. Still no jaw. Still hope." |
| Graffiti | "Tongue up. Chin up. Rent due." |
| Poster (Grandpa) | "THE FACE WANTS TO GO FORWARD. LET IT." |
| Notice | "LOST: one tongue posture. Last seen 2009. Answers to 'roof'." |
| Poster (ortho) | "Turn the key a quarter turn. Every night. EVERY. NIGHT." |
| Poster (ortho) | "Wear your headgear 22 hours a day." (Kevin flinches) |

### Floor 3 — Bone Smash Basement
| Type | Text |
| --- | --- |
| Sign | "Days since last bonk: 0" (counter resets every time a press slams) |
| Sign | "Hard hats mandatory. Hard faces optional." |
| Sign | "CAUTION: Hammers swing both ways." |
| Sign | "Parking: Mid Management only." |
| Notice | "This machine has no feelings. Neither does Clav." |
| Poster | "Bone is a mindset." (with Clav's silhouette) |
| Graffiti | "the bullets apologised" |

### Floor 4 — The Rating Chamber
| Type | Text |
| --- | --- |
| Sign | "SILENCE IN COURT. ALL RATINGS ARE FINAL." |
| Board | "Today's judge: Androjenic. Today's verdict: four." |
| Scoreboard | "HIGHEST RATING EVER: 6.2 (a door)" |
| Notice | "Please do not rate the jury." |
| Poster (ortho) | "BRACE YOURSELF." (a giant smiling mouth full of braces) |

### Floor 5 — Glow-Up Graveyard
| Type | Text |
| --- | --- |
| Sign | "Keep off the grass. The grass is a 3." |
| Sign | "Visiting hours: Before and After." |
| Notice | "No selfies after midnight. They come back." |
| Tombstones | See section 6 (Derek, Gary, Steve, Kyle, Unknown, Mum) |
| Graffiti (ortho) | "RETAINERS ARE FOREVER" carved into a crypt door |

### Floor 6 — The Lathered Spa
| Type | Text |
| --- | --- |
| Sign | "No running. Sliding is fine." |
| Sign | "Pool depth: deeper than your routine." |
| Notice | "Towels: one per person. Robes: as many as your confidence allows." |
| Price list | Every treatment costs "Your soul" except "Water: $14" |
| Poster | "Shower thoughts welcome. Double-cleanse thoughts mandatory." |

### Floor 7 — Runway of the Damned
| Type | Text |
| --- | --- |
| Sign | "Walk like nobody's watching. (Everyone is watching.)" |
| Notice (backstage) | "NO BLINKING BACKSTAGE." |
| Door sign | "Dressing Room 2: J. Ferret (in the vents)" |
| Notice | "Mannequin Union rule 1: don't look at them. Rule 2: see rule 1." |
| Mirror note | "Smile with your eyes." · "No. Your OTHER eyes." |

### Floor 8 — The Front Camera
| Type | Text |
| --- | --- |
| Notification | "You have 99+ unread insecurities." |
| Notification | "Screen time this week: yes." |
| Notification | "Low battery. Low self-esteem. Charge one." |
| Notification | "3 people viewed your profile. They left." |

### Elevator (every ride)
| Type | Text |
| --- | --- |
| Plaque | "Max capacity: 8 people or 1 ego." |
| Plaque | "In case of fire, check your angles." |
| Plaque (scratched) | "going down again?? why" |

---

## 13. Orthodontic horror

**Kevin's fear.** Kevin had braces *and* headgear in school (his Before Photo on Floor 5 shows the braces). Orthodontic gear is the one thing in the clinic that genuinely scares him. Everyone else in the clinic treats these devices as holy objects. For Kevin, they're a horror movie.

**Rule:** scary through sound, shape and movement, never through injury. No blood, no gums, no teeth being pulled. The joke is that Kevin is terrified of objects everyone else worships.

**Kevin's "Ortho Dread" mechanic (M, ★★):** near any orthodontic horror, a faint wire-tightening creak plays, the screen edges pinch inward slightly, his breathing speeds up, and his rating drains −0.05/s. Moving away stops it. Dr. Meow cranking his expander near Kevin also triggers it ("Please stop cranking it near me").

### Set pieces and props
| Object | Where | What it does | Cost | Priority |
| --- | --- | --- | --- | --- |
| **The Expander Wall** | L2 | A wall of palate expanders (MSE-style) in glass specimen jars, labelled like a museum. When you look away, one turns a quarter turn: *click*. When you look back, they've all turned. | M | ★★★ |
| **Headgear Rack** | L2, L4 | Dozens of reverse-pull face masks hanging like hockey masks in a slasher film. One hook is empty. (The Headgear enemy is the missing one.) | S | ★★★ |
| **Expander Key doors** | L2 | Locked doors with a giant expander keyhole. Kevin has to turn a giant key a quarter turn; each turn makes the whole corridor creak wider. | M | ★★ |
| **Retainer Lost & Found** | L1 | A box of clear retainers behind the desk. When you pass, the lids snap open and shut like clams. | S | ★★ |
| **Rubber Band Dispenser** | L3 | Orthodontic bands stretched across corridors as tripwires; they snap like whips (knockback, −0.25). | S | ★★ |
| **The Chair** | L4 | A dental chair under an operating lamp. It swivels to face you wherever you stand. Mid-floor, it rolls after you by itself (chase). | M | ★★★ |
| **Cheek-retractor mannequins** | L7 | Mannequins wearing cheek retractors, forced into wide smiles. They're the audience's front row. | S | ★★★ |
| **Braces fence** | L5 | The graveyard fence is giant braces wire with brackets as fence posts. | S | ★★ |
| **Giant facial calipers** | L4 | Androjenic's measuring calipers on the wall, two metres tall; they snap shut when you walk between them (QTE dodge). | M | ★★ |
| **Mouth-tape roll** | L2 | Pickup: tape Kevin's mouth for 30 s of total silence (Mouth Breathers can't hear him). Kevin: "This is a trend, apparently." | S | ★★★ |
| **Jaw trainer** | L3 | A chew-block pickup; Clav insists Kevin chews it. Kevin: "It tastes like a phone case." +0.25 rating. | S | ★ |
| **Symmetry grid projector** | L4 | Projects a green face-grid onto every surface, including Kevin's hands. | S | ★★ |

### New enemies
| Enemy | Where | Behaviour | Counter | Rating damage |
| --- | --- | --- | --- | --- |
| **The Headgear** | L2 (intro), L4, L8 cameo | A floating reverse-pull face mask, rubber bands stretched from it to the walls. Blind; follows the creak of your footsteps. If a band touches you, it *pulls* you toward it. Recurring stalker. | Cut its bands with the scissors pickup; hide behind pillars so bands snag | −0.5 + pull |
| **Expander Spiders** | L2, L4 | Small expander-shaped crawlers; the screws are their legs. They click faster as they get closer. If one latches onto your face, your FOV stretches wider and wider (screen-warp) until you shake it off. | Mash to shake off; flashlight makes them scatter | −0.25/s while latched |
| **Retainer Chatterers** | L1, L5 | Clear plastic retainers that chatter like wind-up toy teeth. Harmless alone; a swarm nibbles your rating. Drawn to noise. | Stomp; throw an object away from you to lure them | −0.1 each |
| **Brace Face** | L5, L7 | Mannequins with cheek retractors and braces. Only move when unobserved, like the rest of the mannequins, but their smile *widens* each time they move. | Keep them in view; back away | −0.75 |

### Kevin's lines (see SCRIPT.md, `ORTHO_` IDs)
"I had headgear in Year 8. I'm not going back." · "Is that… an expander? Why is it in a jar? Why is it *moving*?" · "Please stop cranking it near me." · "Nope. Rubber bands. I'm out." · "That smile is held open by metal. Nobody's that happy."

---

## How to add a detail

1. Add a row to the right table: what it is, where, cost, priority.
2. If it has dialogue, add the line to [SCRIPT.md](SCRIPT.md) with a line ID.
3. If it changes a rule or a locked decision, ask the owner first.
