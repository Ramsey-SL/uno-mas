# Cloudinary DAM Audit — 2026-08-26

**First complete audit of the library.** Run through the Composio Cloudinary connection
(the claude.ai connector was never authorized; Composio had an active connection all along).
Read-only — nothing was uploaded, renamed, retagged or deleted.

---

## 🔴 Finding 1 — 61% of assets tagged `channel:print` are not printable

**105 assets carry `channel:print`. 64 of them are ≤2048px on the long edge.**

This is the expensive one. Someone reaching for a "print-ready" asset gets a low-res file **three
times in five**. The tag actively asserts something false, which is worse than no tag at all —
an untagged asset makes you check; a wrongly-tagged one tells you not to bother.

Examples: `20260618_UM_FOOD_BowlTrio_v2` (1536×2048) · `20260618_UM_FOOD_Quesadilla_v7`
(2048×1536) · `20260623_UM_FOOD_CarneAsadaParrillada` (1536×2048) · `20260623_UM_EVENT_ShrimpTowerSpread02`

## 🔴 Finding 2 — the print gate covers 11% of what it should

| | |
|---|---|
| Images ≤2048px long edge | **786** (59% of all images) |
| Images **exactly** 2048px — the shared-album signature | **710** |
| Tagged `needs-hires-swap` | **89** |
| **Low-res but NOT tagged** | **699** |
| Tagged but actually print-capable (false positives) | 0 |

The gate has no false positives — everything tagged is genuinely low-res. It just **misses 699 of
788**. The registry's "~141 assets" figure counted images *and* videos; on the image side it's 89.

## Finding 3 — `hero-approved` and `print-ok` do not exist

Confirmed: zero assets carry either tag. **415 assets qualify as hero candidates** (≥2400px, real
photography, carrying an approval tag, excluding icons/logos/submissions):

| Folder | Candidates |
|---|---|
| photos/food | 115 |
| photos/promo | 74 |
| photos/brunch | 74 |
| photos/building | 73 |
| photos/cocktails | 46 |
| photos/venue | 25 |
| photos/events | 6 |
| photos/team | 2 |

**415 is too many to be useful** — a shortlist that big is the same search problem in a new hat.
The curation pass should cut this to 25–40. But the machine-verifiable half (resolution, format,
not-an-icon) is now done, so the human pass is a review of 415, not a hunt through 1,324.

## Finding 4 — two tag conventions are running at once

**718 distinct tags** across 1,486 assets. Roughly half colon-style (`channel:web`, `type:food-photo`,
`mood:vibrant` — 569 distinct), half flat/hyphen (`category-food`, `approved`, `website` — 149 distinct).

They overlap and disagree:

| | |
|---|---|
| `category-food` 405 | vs `category:food` 22 |
| `category-venue` 36 | vs `type:venue` 46 |
| `approved` 511 | vs `approved:yes` 779 (and `approved-assets` 526) |

**Three different tags mean "approved" and none of them agrees with the others.** Any search
filtered on one convention silently misses assets tagged with the other. The operating guide
documents only the hyphen style, so it describes about half the library.

## Finding 5 — naming violations are 466, not 31

466 of 1,486 assets (31%) don't match `YYYYMMDD_UM_<CATEGORY>_<Subject>`. The registry records 31;
the live-site audit found 44. The real number is **466**. Resolution is unchanged — **tag, don't
rename**, because public_ids are the delivery URLs — but the scale was understated by 15×.

## Finding 6 — the plan is wrong in every doc

| | Documented | **Actual** |
|---|---|---|
| Plan | FREE | **Plus** |
| Credits | 25/month | **225/month**, 34.96 used (15.5%) |
| Max image size | 10 MB | **20 MB** |
| Max video size | 100 MB | **2 GB** |

**This removes the constraint the whole MediaFlows assessment was built on.** The "if flows are
metered, build Flow 1 only" caution assumed a 25-credit budget. At 225 credits with 84% unused,
automation is affordable and the plan should be reconsidered on merit, not on cost.

Storage 5.33 GB · 1,487 resources · 3,797 derived · 160,424 requests · 5,284 objects.

## Library shape

1,324 images + 162 videos = **1,486**. The "~1,350" figure was right; the "154" figure in
`cloudinary-gpt-action-setup.md` was wrong — that scope expression
(`asset_folder:uno-mas/* OR public_id:uno-mas/*`) **misses everything with an empty `asset_folder`
and a bare public_id**, which is most of the library. **That GPT Action has been searching a
tenth of the library this whole time.**

34 folders. 680 assets — 46% of everything — sit in `approved-assets/photos/food`. 3 assets are in
`<Home>` with no folder. 5 assets have no tags at all.

---

## Recommended fixes, in order

1. **Strip `channel:print` from the 64 assets that aren't print-capable.** Highest value, smallest
   blast radius, and it stops a tag that is actively lying.
2. **Tag the 699 untagged low-res images `needs-hires-swap`.** Makes the print gate real.
3. **Add `print-ok` to everything ≥2400px.** Turns the gate positive instead of relying on absence.
4. **Pick one tag convention and migrate.** Colon-style is more used and more expressive; flat tags
   are older. This is the one that needs a decision before any work.
5. **Curate `hero-approved` down from the 415 candidates** to 25–40.
6. **Fix the GPT Action scope expression** — it is searching ~10% of the library.
7. **Reassess MediaFlows on merit.** The credit objection was based on a plan we're not on.
