# Proposed 180-minute campaign

## Direction

Authored first-person horror-comedy, with sound/observation stealth, environmental puzzles, defensive powers and brief action set pieces. The institution is frightening and sincerely absurd; jokes release tension rather than replacing dread. Keep Kevin's deadpan role, the Concierge, the eight named chapters, existing parody names, five earned abilities and the separate Touch Grass ultimate/secret ending. Do not turn the story into a three-hour procedural grind.

Reference: [GDD](../../GAME_DESIGN.md), [Levels](../../LEVELS.md), [newer script](https://github.com/devspideyy/NGMI/blob/16b37cb74df664ba6950c3f612684579785674ca/docs/SCRIPT.md), [scare map](https://github.com/devspideyy/NGMI/blob/16b37cb74df664ba6950c3f612684579785674ca/docs/JUMPSCARES.md).

## Runtime

Target: representative blind normal-mode completion including short exploration and dialogue; excludes long pauses, retries, completionist detours and secret early exit. All values are hypotheses.

| Segment | Minutes | Cumulative | Beats (minutes) |
|---|---:|---:|---|
| Arrival | 8 | 8 | Notification .75; road 3.25; gate 1; car park 2; scan 1 |
| L1 Waiting Room | 17 | 25 | Reception 3; routine 3; light lesson 3; card duel 2; Brenda 4; resolution 2 |
| Elevator 1–2 | 1 | 26 | Dialogue/ad, recap |
| L2 Mewing Catacombs | 21 | 47 | Sound 3; gallery 5; lecture chase 2; Silent Walk 4; boss 5; handoff 2 |
| Elevator 2–3 | 1 | 48 | Recovery |
| L3 Bone Smash Basement | 23 | 71 | Vista 3; press route 5; control 4; rescue/power 3; arena 6; outro 2 |
| Elevator 3–4 | 1 | 72 | Rating prompt |
| L4 Rating Chamber | 20 | 92 | Arrival 3; trial loop 6; Chair 3; boss 6; outro 2 |
| Elevator 4–5 | 1 | 93 | Transition |
| L5 Glow-Up Graveyard | 24 | 117 | Landmark 3; Stinkley 4; escort 8; boss 6; quiet resolution 3 |
| Elevator 5–6 | 1 | 118 | Transition |
| L6 Lathered Spa | 18 | 136 | Arrival 2; practice 3; flood loop 5; boss 6; outro 2 |
| Elevator 6–7 | 1 | 137 | Robes/chat |
| L7 Runway of the Damned | 21 | 158 | Arrival 3; backstage 5; walk-off 4; duo 7; outro 2 |
| Elevator 7–8 | 1 | 159 | Signal loss and silence |
| L8 Front Camera | 17 | 176 | Reveal 2; mirror lesson 3; convergence 7; gum/flip 4; exit 1 |
| Ending and coda | 4 | 180 | Outcome, exterior, coda |
| **Total** | **180** | | 161 floors + 19 transitions/arrival/ending |

## Room-by-room proposals

**Arrival:** constrained spline drive, not a full driving simulation. Headlights reveal billboards by position, not a timer; use one distant building silhouette then real near geometry. Gate, compact car park, guard booth, inspection clues, front-door scan. Preserve the car and Sam/location callbacks. Anchor the secret exit window to the scan/check-in rather than the start of the drive.

**L1:** reception hub -> sink loop -> light safety encounter -> card duel -> return behind desk -> bell resolution -> elevator. Show the bell and locked lift early. A repeated space should change after the player learns the institution's rules.

**L2:** wet entry -> sound tutorial -> expander gallery -> dry service loop / wet shortcut -> visible vent room -> lecture chase -> Silent Walk nest -> cistern boss. Teach the noise rule safely first, then test it. Use nearby retries; no real microphone required. Keep the gum and scissors recoverable.

**L3:** entry overlook sees cage/furnace and control station -> timed press corridor -> lower machinery loop -> control -> cage rescue -> opened shortcut -> safe power practice -> upper catwalk arena -> exit. Build a smaller 12–15 minute representative version first. Use safe ring-light refuges and nonlethal introductory trap cue. Original props should drive the layout, not vice versa.

**L4:** courtroom hub -> portrait/mirror trial -> gallery loop -> dental Chair chase through known corridor -> final timed stare/rating battle -> resolution. Use one reusable timing controller, and a quality-independent cue for the reflection puzzle.

**L5:** walled garden, crypt/dead tree landmark, two loops and bounded escort legs. Teach Before Form and Smile Flash separately, then combine them. Oliver waits at defined anchors. Let darkness establish suspense, not merely a black screen. Protect the Before Photo emotional resolution from random jokes and PA.

**L6:** dry perimeter route and shallow practice bay -> wet channels -> staged flood -> pool arena -> hose interaction -> lift. Prefer authored water heights and explicit collision to simulated fluid flooding; offer motion reduction and reliable retry. The chapter is a deliberate breather.

**L7:** entrance, backstage loop, vent previews, stage wings, short walk-off and duo encounter. Distant mannequins can be static instanced dressing, near judges separate head/rig. Reuse L4 prompt controller. Sandwich walk should be an ordinary player-controlled payoff.

**L8:** one readable giant-camera arena, broad notification walkways, cover islands, protected mirror station, return loop. Powers each get a recognizable purpose; allies can arrive as staged assists. Guaranteed gum, reachable side control, final exit. The ending should reflect player choices rather than a forced last-second score collapse.

## Horror pacing

Use orientation -> evidence -> anticipation -> action/encounter -> recovery -> payoff. Use ambient cues before loud stingers, and visible or audible warnings before consequential threats. Keep existing JS_00–JS_22 (23 events), distinguishing big scares, creeps and fake-outs. Preserve the final silent lift exception. Reuse observation/changed-return-room techniques instead of adding more jump scares. Test player control and navigation at low brightness and reduced effects.

Read [Frictional's horror lessons](https://frictionalgames.com/2019-10-9-years-9-lessons-on-horror/) and [The Level Design Book blockout](https://book.leveldesignbook.com/process/blockout), then test [with first-time players](https://book.leveldesignbook.com/process/blockout/playtesting). Each room needs a goal, initial sightline, warning, choice, recovery, changed return state and save contract.

## Decisions requiring reconciliation

| Current risk | Proposal / test |
|---|---|
| D6 says ~2 hours | Owner decision before updating canonical design |
| Death ends a solo run | Checkpoints in authored story; keep run-based replay separate |
| 6-minute drive description vs 7.5-minute component sum and four billboards every two minutes | 8-minute arrival, spatial triggers; test skip/resume |
| Face Rating heal/drain overlaps and repeatable recovery | Explicit stacking, caps, cooldowns and pause semantics |
| Final JS_22 halves rating before Ascend requires 9+ | Taught counter or non-damaging presentation; prove all endings |
| Touch Grass heals fully once per run | Persist used/available state and test ending balance; distinct from secret early exit |
| Gum is throwaway and finale key | Guarantee persistent/recoverable key state |
| One active ability vs multiple earned powers | Remappable selection model, test gamepad and keyboard |
| Jaw Juice values differ across docs | Pick one data-table value after review |
| Clock ends at 6 AM | Decide whether deadline is narrative/checkpoint-based or real timer; avoid punishing accessibility/reading |
| 22 scares in older docs | Reconcile to 23 after newer branch is adopted |

Acceptance: first-time tests record time by segment, confusion, retries, scare response and mechanic comprehension. Target meaningful play, not enforced duration. No canon changes are made by this research.
