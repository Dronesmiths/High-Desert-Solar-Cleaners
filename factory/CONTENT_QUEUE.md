# AI Pilots: Content & Newsletter Queue

Use this checklist to track the rollout of the 50 high-authority content pieces. Mark as `[x]` only after the page is live and CloudFront cache is invalidated.

## Phase 1: The Authority Foundation (1-10)
- [ ] **01: Cornerstone Guide** - The Ultimate Guide to Pool Maintenance in the Antelope Valley
- [ ] **02: Locality Anchor** - Why AV Pool Bros is Palmdale's Top Rated Pool Service
- [ ] **03: Service Deep Dive** - Chemical Balancing: The Science of Crystal Clear Water
- [ ] **04: Project Spotlight** - Green-to-Clean Success in West Lancaster: A Before & After
- [ ] **05: PAA Capture** - How much does monthly pool cleaning cost in Palmdale?
- [ ] **06: Service Deep Dive** - Filter Cleaning: DE vs Cartridge maintenance in the High Desert
- [ ] **07: Pro Tip** - 5 Things to Do to Keep Your Pool Safe During Wind Storms
- [ ] **08: Project Spotlight** - New Pump Installation for Antelope Valley Pool Efficiency
- [ ] **09: PAA Capture** - Why is my pool turning green even with chlorine?
- [ ] **10: Locality Anchor** - Quartz Hill Pool Care: Special Considerations for the Westside

## Phase 2: Strategic Expansion (11-30)
- [ ] **11: Locality Anchor** - Wind-Resistant Pool Care in Rosamond
- [ ] **12: PAA Capture** - When should I drain and refill my pool?
- [ ] **13: Service Deep Dive** - Commercial Pool Care: Keeping AV Facilities Safe
- [ ] **14: Project Spotlight** - Tile Calcium Removal Success Story
- [ ] **15: Cornerstone Pillar** - The 2026 Homeowner's Guide to Energy Efficient Pool Equipment
- [ ] **16-30:** ...

## Phase 3: Domain Dominance (31-50)
- [ ] **31:** ...
- [ ] **50:** ...

> [!IMPORTANT]
> **Deployment Rule**: Every time a checkbox is marked `[x]`, you must:
> 1. Sync the repo: `git add . && git commit -m "feat: deploy content piece #[XX]" && git push`
> 2. Sync S3: `aws s3 sync . s3://[BUCKET] --profile mediusa`
> 3. Invalidate: `aws cloudfront create-invalidation --distribution-id [ID] --paths "/news/*" "/blog/*"`
