#!/bin/bash

# Configuration
PROFILE="mediusa"
REGION="us-east-1"
BUCKET_PREFIX="high-desert-solar-cleaners"
TIMESTAMP=$(date +%s)
BUCKET_NAME="${BUCKET_PREFIX}-${TIMESTAMP}"
CONFIG_FILE="../aws_config.json"

# Colors
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}Starting Infrastructure Provisioning for High Desert Solar Cleaners...${NC}"

# 1. Create S3 Bucket
echo "Creating S3 Bucket: $BUCKET_NAME..."
aws s3 mb "s3://$BUCKET_NAME" --region "$REGION" --profile "$PROFILE"

# Enable Static Website Hosting
echo "Enabling Static Website Hosting..."
aws s3 website "s3://$BUCKET_NAME" --index-document index.html --error-document index.html --region "$REGION" --profile "$PROFILE"

# Public Access Block (Off for public read, or specific policy)
# For CloudFront OAC/OAI, we typically block all public access and use a policy.
# For simple static hosting + CloudFront without OAC (legacy but simple), we might open it.
# Let's go with the standard modern approach: Block Public Access and use Bucket Policy for CloudFront (or OAC).
# SIMPLIFIED APPROACH for Quick Deploy: Public Read Bucket restricted by bucket policy later or standard website hosting.
# The user asked for "new s3 new bucket- new cloudfront".
# We will disable Block Public Access to allow the bucket policy to grant public read (standard static site pattern) or CloudFront access.
echo "Disabling Block Public Access..."
aws s3api put-public-access-block \
    --bucket "$BUCKET_NAME" \
    --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false" \
    --profile "$PROFILE" --region "$REGION"

# Create Bucket Policy for Public Read (Standard S3 Website) - valid for CloudFront custom origin or direct access
# We will rely on CloudFront mostly, but S3 Website endpoint is robust.
POLICY_JSON='{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::'"$BUCKET_NAME"'/*"
        }
    ]
}'
echo "Applying Bucket Policy..."
aws s3api put-bucket-policy --bucket "$BUCKET_NAME" --policy "$POLICY_JSON" --profile "$PROFILE" --region "$REGION"

# 2. Create CloudFront Distribution
echo "Creating CloudFront Distribution..."
# We use the S3 Website Endpoint as the origin to allow for clean URLs (directory indexes) if needed, 
# although index.html handling is done.
# S3 Website Endpoint format: http://<bucket>.s3-website-<region>.amazonaws.com
ORIGIN_DOMAIN="${BUCKET_NAME}.s3-website-${REGION}.amazonaws.com"

# Create Distribution
# Note: CallerReference ensures idempotency
CALLER_REF="high-desert-${TIMESTAMP}"

DIST_CONFIG='{
    "CallerReference": "'"$CALLER_REF"'",
    "Aliases": {
        "Quantity": 0
    },
    "DefaultRootObject": "index.html",
    "Origins": {
        "Quantity": 1,
        "Items": [
            {
                "Id": "S3-Website",
                "DomainName": "'"$ORIGIN_DOMAIN"'",
                "CustomOriginConfig": {
                    "HTTPPort": 80,
                    "HTTPSPort": 443,
                    "OriginProtocolPolicy": "http-only",
                    "OriginSslProtocols": {
                        "Quantity": 1,
                        "Items": ["TLSv1.2"]
                    }
                }
            }
        ]
    },
    "DefaultCacheBehavior": {
        "TargetOriginId": "S3-Website",
        "ViewerProtocolPolicy": "redirect-to-https",
        "AllowedMethods": {
            "Quantity": 2,
            "Items": ["HEAD", "GET"],
            "CachedMethods": {
                "Quantity": 2,
                "Items": ["HEAD", "GET"]
            }
        },
        "ForwardedValues": {
            "QueryString": false,
            "Cookies": {
                "Forward": "none"
            }
        },
        "MinTTL": 0,
        "DefaultTTL": 86400,
        "MaxTTL": 31536000,
        "Compress": true
    },
    "CacheBehaviors": {
       "Quantity": 0
    },
    "Enabled": true,
    "Comment": "High Desert Solar Cleaners"
}'

# We need to write the config to a temp file because CLI argument parsing for JSON is tricky
echo "$DIST_CONFIG" > dist_config.json

DIST_RESULT=$(aws cloudfront create-distribution --distribution-config file://dist_config.json --profile "$PROFILE")
DIST_ID=$(echo "$DIST_RESULT" | grep -o '"Id": "[^"]*' | cut -d'"' -f4)
DIST_DOMAIN=$(echo "$DIST_RESULT" | grep -o '"DomainName": "[^"]*' | cut -d'"' -f4)

# Cleanup temp file
rm dist_config.json

echo -e "${GREEN}Resource Creation Complete!${NC}"
echo "Bucket Name: $BUCKET_NAME"
echo "Distribution ID: $DIST_ID"
echo "CloudFront Domain: $DIST_DOMAIN"

# Save Config
echo "{\"bucket_name\": \"$BUCKET_NAME\", \"distribution_id\": \"$DIST_ID\", \"domain\": \"$DIST_DOMAIN\"}" > "$CONFIG_FILE"
echo "Config saved to $CONFIG_FILE"
