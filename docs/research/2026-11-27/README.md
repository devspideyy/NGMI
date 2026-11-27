# NGMI production research | 27 November 2026

**Review proposal, not a change to the agreed design.** The existing two-hour D6 decision remains in effect until the owner approves a replacement. This research proposes a 180-minute first blind solo campaign, retaining eight floors, the realistic green palette, fictional characters, existing story beats and earned powers.

## Read in this order

- [Campaign and level design](CAMPAIGN.md): runtime budget, room flow, horror pacing and story consistency.
- [UE5 implementation and acceptance gates](UE5.md): reusable systems, L3 slice, risks, 27-task backlog and practical learning path.
- [Art and acquisition plan](ART.md): original-prop QA, lighting, backgrounds, material pipeline and 2D content.
- [Asset candidate register](ASSETS.csv): 49 source candidates, floors, priorities and acquisition caveats.

## Repository evidence

The current main README still describes pre-production and no Unreal project. The research audit also examined these earlier snapshots (not merged by this PR):
- [Expanded design and detail snapshot, dc23e08](https://github.com/devspideyy/NGMI/tree/dc23e08ccd2507c441e356909e06f99e098abcd4)
- [Drive script snapshot, 3716233](https://github.com/devspideyy/NGMI/tree/3716233d3394d0cb9a72c55564e94d0c0fb8d601)
- [Prop-pack snapshot, 16b37cb](https://github.com/devspideyy/NGMI/tree/16b37cb74df664ba6950c3f612684579785674ca)

The prop snapshot documents 79 manifest entries plus Headgear, 80 FBX and 80 GLB paths, six contact sheets and 77 thumbnails. Five retrieved GLBs (Catwalk, Ring Light, Retainer Chatterer Jaw, Mannequin and Headgear) were inspected; the rest were not individually validated. No UE import, packaged playtest or runtime benchmark has been performed. The audit is a snapshot, not a claim that those branches are already on main.

## Production decisions proposed for owner review

1. Three hours of authored solo play; defer multiplayer, procedural replay, playable hero expansion and chat integrations until the campaign works.
2. Keep the existing L3 milestone and prove it with a 12–15-minute packaged representative slice before expanding to its full chapter.
3. Preserve the story's fictional parody, no real likenesses and no real injury detail. Keep source licensing and local-only optional mic processing rules.
4. Reconcile D6, checkpoint semantics, recovery economy and ending eligibility in the canonical docs only after approval.
5. The repository currently reports public visibility despite its private-only documentation. No raw third-party assets, screenshots from licensed packs, binaries or secrets are included here. Owner should check visibility before importing licensed content.

This PR is an editable, text-first handoff derived from the research dossier and register. It is not the original PDF/XLSX/ZIP or an Unreal implementation; asset downloads and original binary deliverables are not checked in.
