#!/bin/bash

# Workflow-Factory V3 Scaffolder
# Usage: ./factory/scaffold_new_site.sh

# 1. Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Workflow Factory V3 Scaffolder ===${NC}"

# Step 0: Input
echo -e "\n${BLUE}[Step 0] Initializing...${NC}"
read -p "Enter New Project Name (e.g. 'Diaz_Landscaping'): " PROJECT_NAME
if [ -z "$PROJECT_NAME" ]; then
    echo "Project Name is required."
    exit 1
fi

# Path Setup
FACTORY_ROOT=$(dirname "$0")
SOURCE_ROOT=$(pwd)
PARENT_DIR="$(dirname "$SOURCE_ROOT")"
NEW_PROJECT_PATH="$PARENT_DIR/$PROJECT_NAME"

echo "Targeting: $NEW_PROJECT_PATH"

if [ -d "$NEW_PROJECT_PATH" ]; then
    echo "Directory already exists. Aborting."
    exit 1
fi

# Step 1: Create Directory
echo -e "\n${BLUE}[Step 1] Creating Directory Structure...${NC}"
mkdir -p "$NEW_PROJECT_PATH"
echo "Created: $NEW_PROJECT_PATH"

# Step 2: Copy Public Site
echo -e "\n${BLUE}[Step 2] Cloning Gold Master Public Site...${NC}"
cp -r "$SOURCE_ROOT/about" "$SOURCE_ROOT/blog" "$SOURCE_ROOT/contact" "$SOURCE_ROOT/css" "$SOURCE_ROOT/images" "$SOURCE_ROOT/js" "$SOURCE_ROOT/privacy" "$SOURCE_ROOT/services" "$SOURCE_ROOT/terms" "$NEW_PROJECT_PATH/"
cp "$SOURCE_ROOT/index.html" "$SOURCE_ROOT/robots.txt" "$SOURCE_ROOT/sitemap.xml" "$SOURCE_ROOT/.gitignore" "$NEW_PROJECT_PATH/"
echo "Public site assets copied."

# Step 3: Copy Factory Engine
echo -e "\n${BLUE}[Step 3] Injecting Factory Engine...${NC}"
cp -r "$SOURCE_ROOT/factory" "$NEW_PROJECT_PATH/"
echo "Factory toolbox injected."

# Step 4: Git Initialization
echo -e "\n${BLUE}[Step 4] Initializing Git Repository...${NC}"
cd "$NEW_PROJECT_PATH"
git init
git checkout -b main
echo "Git repository initialized at: $(pwd)"

echo -e "\n${GREEN}=== Scaffolding Complete ===${NC}"
echo "1. Go to directory: cd $NEW_PROJECT_PATH"
echo "2. Edit Config: nano factory/factory_config.json"
echo "3. Review Plan: code factory/DEPLOYMENT_ORDER.md"
echo "4. Run Audit: python3 factory/scripts/preflight_audit.py"
