# UE5 production and validation plan

## First gate

Engine candidate: UE 5.8.4, provisional pending both developers installing the same available stable patch and successfully importing/packaging a project. [Epic hotfix announcement](https://forums.unrealengine.com/t/5-8-4-hotfix-released/2842775). Choose target machine before locking settings. Existing 1080p/60 target on GTX 1660/RX 5600-class hardware is a hypothesis; benchmark actual packaged builds and offer lower reflection/GI presets. Do not equate editor FPS with shipping FPS.

Create Game/NGMI.uproject from the First Person Blueprint template. Follow the existing Content/NGMI naming convention. Use discrete chapter maps and a reusable elevator transition first; add streaming only when measured necessary. Git LFS for permitted binary content; never add raw marketplace assets to a public repository. Keep saved/generated/intermediate caches untracked.

## Reusable systems

| ID | System | Implementation and acceptance |
|---|---|---|
| SYS01 | Movement/input | Enhanced Input actions/context; packaged crouch/sprint/interact/pause and remap |
| SYS02 | Interaction | BPI_Interactable + player component, trace/focus/range; door/bell/pickup share contract |
| SYS03 | Face Rating | One component owns clamp 0–10, damage categories, timed effects and death event; equal elapsed-time results at 30/60 fps |
| SYS04 | Light/Dread | Authored volumes and state flags, not rendered pixel brightness; same logic on every preset |
| SYS05 | Powers | Data rows for five earned powers plus ultimate; stable gift IDs, cooldown/active state; Before Form invisibility without attacks; Touch Grass full-heal once per run, safe return |
| SYS06 | Save/checkpoint | Versioned SaveGame payload, previous valid slot, stable chapter/item/gate/event IDs; atomic rating/power/effect/ultimate state |
| SYS07 | Chapter/boss | Named states with explicit enter/exit/reset; clean boot and retries cannot desynchronize |
| SYS08 | Scares/story | Stable IDs, prerequisite and consumed flags, Full/Reduced/Off variants preserve progression |
| SYS09 | Enemy behavior | Base AI, Blackboard/Behavior Tree, hearing noise events for footsteps/throws/doors; search, chase and disengage |
| SYS10 | Dialogue/chat | Existing line IDs, subtitles and localization, source voice refs; prioritize essential information and avoid duplicated saved messages |
| SYS11 | Sound/rhythm | Attenuation, spatial warnings, limited MetaSounds, Quartz clock where needed; test rhythm at 30/60 fps |
| SYS12 | Accessibility | UMG/settings; FOV, motion, flicker, audio, subtitles and remaps; persistent settings and usable controller navigation |
| SYS13 | Mirrors | Staged double or bounded capture; world-visible Kevin body; gameplay targeting independent of reflection preset |
| SYS14 | Loading | Compact maps + elevator loading/recap; clean boot/resume and packaged dependencies checked |

Technical sources: [First Person template](https://dev.epicgames.com/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine), [Blueprint best practices](https://dev.epicgames.com/documentation/unreal-engine/blueprint-best-practices-in-unreal-engine), [Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/input-overview-in-unreal-engine), [SaveGame](https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine), [AI Perception](https://dev.epicgames.com/documentation/en-us/unreal-engine/ai-perception-in-unreal-engine), [Quartz](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-quartz-in-unreal-engine), [Lumen performance](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine), [Level streaming](https://dev.epicgames.com/documentation/unreal-engine/level-streaming-in-unreal-engine).

## Backlog (all proposed)

| ID | Priority | Task | Dependencies | Done when |
|---|---|---|---|---|
| C01 | P0 | Reconcile scope | none | Owner-approved baseline and distinction between Touch Grass ultimate and secret |
| C02 | P0 | Pin engine and test machine | C01 | Packaged template |
| C03 | P0 | Import L3 props | C02 | Hydrated source, scale, materials, pivots, collision checked |
| C04 | P0 | Movement/interact/objective | C02 | Packaged controller, doors, switches, prompts |
| C05 | P0 | Rating/safe rings | C04 | Deterministic heal/damage and recovery caps; ultimate test |
| C06 | P0 | Checkpoint/restart | C05 | Atomic restore of rating, effects, keys, powers, props, flags and ultimate |
| C07 | P0 | L3 greybox and press | C04 | Vista, lower loop, control, shortcut, upper arena playable |
| C08 | P0 | Ghoul and capped Blob | C05,C07 | Readable threat, capped splitting, precise counter |
| C09 | P0 | Rescue and Bone Smash | C06,C07 | Gift survives reload; only intended damage class blocked |
| C10 | P0 | Headhunter encounter | C08,C09 | Warning, cover, readable PING gag |
| C11 | P0 | L3 art/audio/accessibility | C03,C10 | Green/orange composition, silhouettes, captions, reduced effects |
| C12 | P0 | Blind slice test and profile | C11 | 3–5 first-time tests and packaged target-machine measurements |
| C13 | P0 | Reusable chapter/event/dialogue | C12 | IDs link triggers, text, save flags and rewards |
| C14 | P0 | L1 tutorial and Brenda | C13 | Bell solution and secret trigger readable |
| C15 | P0 | L2 stealth/persistent Gum | C14 | No-mic route, retryable walk, key items cannot softlock |
| C16 | P0 | L4 observation/rhythm/Chair | C13 | Reusable timing, assist, known chase route |
| C17 | P0 | L5 escort and emotion | C15,C16 | Two powers, bounded escort, protected resolution |
| C18 | P0 | L6 flooding/sliding | C17 | Dry refuges, reset and motion assistance |
| C19 | P0 | L7 theatre/duo | C16,C18 | Rhythm/observation reuse, timing assist |
| C20 | P0 | L8 convergence/ending | C15,C17,C19 | Guaranteed Gum, fair flash, ending tests with ultimate used/available |
| C21 | P0 | Prologue/exterior | C12 | Eight-minute authored route and spatial triggers |
| C22 | P0 | Full campaign test | C20,C21 | Blind timing, all checkpoints/endings |
| C23 | P1 | Final original characters/VO | C22 | Reusable rigs, rights and final lines |
| C24 | P0 | Cohesion/performance/package | C23 | Lowest settings readable; all cooked dependencies |
| C25 | P2 | Optional local mic | C22 | Explicit opt-in, local amplitude only, no voice storage/upload, input equivalent |
| C26 | P2 | Rating Card/chapter replay | C22 | Separate campaign/replay state |
| C27 | Deferred | Co-op/procedural/heroes/chat | C24 | Separate approved scope |

## Tests that must happen early

- L3: press warning, collision at motion extremes, control activated once, cage rescue, power grant, boss finish and checkpoint resume. Prototype the immunity as clearly fictional gameplay with cartoon presentation.
- Reload during or after a gift, death during a timed effect, quit mid-rescue, resume boss surrender, repeat a consumed trigger, check a missing key. No duplicate grants or irreversible locks.
- Mirrors: movement, crouching, off-screen actor, power effect, reload, low graphics. Medium may rely on SSR; a puzzle must not depend on pixels from an unavailable reflection.
- Timing: rhythm input with varied frame rates; count real active play separately from pauses/retries.
- Perf: packaged cold start, worst arena, fog and movable light costs, frame-time spikes, VRAM and shader/PSO hitches. Measure before optimizing. Record machine, resolution, preset and engine patch.
- All accessibility variants must preserve gameplay cues. PA/chat cannot drown out hazard warnings or important dialogue.
- Use one working original humanoid rig with idle, walk, run, crouch, reaction and one authored pose before building the full cast.

## Learning exercises (each leaves a testable artifact)

Package a room; reusable door; remapped controls; persistent pickup; hearing AI; snapped/colliding catwalk; neutral + green/orange lighting; working mirror on low settings; spatial sound warning; rhythm interaction; Unreal Insights capture; clean chapter transition. Read only enough documentation to complete the corresponding exercise. Keep logs/screenshots locally and record pass/fail evidence in the backlog.
