# AWS S3 & CloudFront Deployment Guide

This guide provides the standardized steps to deploy your website factory project to AWS S3 and CloudFront.

## 1. Prerequisites
- AWS CLI installed and configured.
- Valid AWS Profile (default: `mediusa`).
- Repository hygiene checked with `preflight_audit.py`.

## 2. Infrastructure "Seek" Protocol
If you do not have your IDs, use these commands to locate them:

### A. List S3 Buckets
```bash
aws s3 ls --profile mediusa
```

### B. List CloudFront Distributions
```bash
aws cloudfront list-distributions --profile mediusa --query "DistributionList.Items[*].{Id:Id,Domain:DomainName,Comment:Comment}" --output table
```

## 3. Deployment Workflow

### Step 1: Pre-Flight Audit (MANDATORY)
```bash
python3 factory/scripts/preflight_audit.py
```

### Step 2: Sync to S3
Replace `[BUCKET_NAME]` with your target bucket.
```bash
aws s3 sync . s3://[BUCKET_NAME] \
    --delete \
    --exclude ".git/*" \
    --exclude ".github/*" \
    --exclude "factory/*" \
    --exclude ".DS_Store" \
    --profile mediusa
```

### Step 3: Invalidate CloudFront Cache
Replace `[DISTRIBUTION_ID]` with your distribution ID.
```bash
aws cloudfront create-invalidation \
    --distribution-id [DISTRIBUTION_ID] \
    --paths "/*" \
    --profile mediusa
```

## 4. Verification
After deployment, verify the changes at the CloudFront URL or custom domain.
- Check title tags and meta descriptions.
- Verify phone number and email consistency.
- Ensure all images (logo/hero) are loading correctly.
