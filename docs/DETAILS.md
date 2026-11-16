# NGMI — Little details

Small touches that make the game feel alive, funny, and worth clipping. None of them are required to finish the game; together they're what people remember.

Last updated: 2026-11-17

**Cost** = rough effort in UE5: **S** (under a day), **M** (a few days), **L** (a week+).
**Priority**: ★★★ do in the vertical slice · ★★ before demo · ★ nice to have.

Every detail follows [CLAUDE.md](../CLAUDE.md) rules: parody names only, jokes about the trend, no real people's real lives.

---

## Top 15 (if you only do these)

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

---

## How to add a detail

1. Add a row to the right table: what it is, where, cost, priority.
2. If it has dialogue, add the line to [SCRIPT.md](SCRIPT.md) with a line ID.
3. If it changes a rule or a locked decision, ask the owner first.
