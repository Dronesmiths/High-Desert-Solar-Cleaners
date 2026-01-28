# How to Port This "Website Factory" to a New Project

**Goal**: Move the "Brain" of this project to a new client repository instantly.

## The Transfer Kit
To start a new V3 site, you only need to copy two folders from this repository:
1.  **`_factory_resources/`** (The Strategy & Documentation)
2.  **`scripts/`** (The Automation Tools)

## Quickstart Instructions

### 1. Run the Scaffolder
From inside the `Workflow-Factory` repository, run:
```bash
./scripts/scaffold_new_site.sh
```

### 2. Follow the Prompts
1.  Enter the name of your new project (e.g., `Diaz_Landscaping`).
2.  The script will create the folder, init Git, and copy all resources.
3.  Navigate to the new directory.

### 3. Verify
```bash
cd ../[New_Project_Name]
ls -la
```

### 3. The "Day 0" Setup
Before asking the AI to do anything, update the *Identity* of the new project:
1.  Open **`_factory_resources/CLIENT_INTAKE.md`**.
2.  Fill in the **Business Name**, **Phone**, **City**, and **New S3 Bucket Name**.
3.  (Optional) Update `COMPETITIVE_ADVANTAGE.md` with the new client's top 5 selling points.

### 4. Activate the Agent
Paste this command to your AI Agent:
> "Initiate Website Factory Workflow: Run Step 0 of `_factory_resources/DEPLOYMENT_ORDER.md`."

The agent will read your updated intake file and start the rebranding process automatically.

---
**Note on Scripts**: The scripts in `scripts/` (like `generate_blog_batch.py`) are robust but may contain "All Clean" strings. The Agent's first task in **Step 2** will be to sanitize these scripts for the new client.
