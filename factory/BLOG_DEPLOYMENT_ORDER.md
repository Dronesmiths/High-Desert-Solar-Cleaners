# AI Pilots: Blog Deployment Order

Follow these steps for every new blog post to ensure 100% SEO parity and tracking.

### Step 1: Content Generation
- [ ] **Draft**: Generate the 800-2,000 word article based on [BLOG_STRATEGY.md](BLOG_STRATEGY.md).
- [ ] **Imagery**: Generate a high-quality WebP hero image for the post.
- [ ] **Interlinking**: Add links to at least 2 Service Pages and 1 Cornerstone Pillar.

### Step 2: Technical Build
- [ ] **HTML**: Create `/blog/[slug]/index.html` using the standard template.
- [ ] **SEO**: Implement unique Meta Title, Description, and `BlogPosting` Schema.
- [ ] **Listings**: Add a preview card to the Blog Hub or Newsletter Hub (`/news/index.html`).

### Step 3: Production Sync & Verification (Dry Run Mandate)
- [ ] **Identity Check**: Verify `s3://[BUCKET-NAME]` and `[DIST-ID]` in [CLIENT_INTAKE.md](CLIENT_INTAKE.md) before pushing.
- [ ] **Dry Run**: `aws s3 sync . s3://[BUCKET-NAME] --exclude ".git/*" --profile mediusa --dryrun`
- [ ] **Git Push**: `git add . && git commit -m "feat: deploy blog - [Topic]" && git push`
- [ ] **AWS Sync**: `aws s3 sync . s3://[BUCKET-NAME] --exclude ".git/*" --profile mediusa`
- [ ] **Invalidate**: `aws cloudfront create-invalidation --distribution-id [DIST-ID] --paths "/blog/*" "/news/*" --profile mediusa`
- [ ] **Audit**: Run `python3 scripts/preflight_audit.py` and ensure a Pass result.
- [ ] **Verify**: Check the live URL on mobile and desktop.

### Step 4: Master Tracking
- [ ] **Check Off**: Mark the post as `[x]` in the [CONTENT_QUEUE.md](CONTENT_QUEUE.md).

> [!TIP]
> **Next Strategic Step**: Proceed to [COMPETITIVE_ADVANTAGE.md](COMPETITIVE_ADVANTAGE.md) to define the brand's "Unfair Advantages."
