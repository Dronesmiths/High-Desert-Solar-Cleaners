#!/bin/bash

# Configuration
PROFILE="mediusa"
CONFIG_FILE="aws_config.json"

# Check if config exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: $CONFIG_FILE not found. Run infrastructure/create_resources.sh first."
    exit 1
fi

# Load Config (Simple parsing since jq might not be available)
BUCKET_NAME=$(grep -o '"bucket_name": "[^"]*' "$CONFIG_FILE" | cut -d'"' -f4)
DIST_ID=$(grep -o '"distribution_id": "[^"]*' "$CONFIG_FILE" | cut -d'"' -f4)

echo "Deploying to Bucket: $BUCKET_NAME"
echo "CloudFront Dist ID: $DIST_ID"

# Sync Files
# Exclude infrastructure, git, and DS_Store
aws s3 sync . "s3://$BUCKET_NAME" \
    --exclude ".git/*" \
    --exclude "infrastructure/*" \
    --exclude "aws_config.json" \
    --exclude ".DS_Store" \
    --exclude "*.sh" \
    --delete \
    --profile "$PROFILE"

# Invalidate Cache
echo "Invalidating CloudFront Cache..."
aws cloudfront create-invalidation --distribution-id "$DIST_ID" --paths "/*" --profile "$PROFILE"

echo "Deployment Complete!"
