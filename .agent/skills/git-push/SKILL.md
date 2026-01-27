---
name: git-push
description: "Workflow to auto-export slides, update index, and sync to git. Use when user says 'Git Push' or asks to sync slides."
---

# Git Push Workflow

This skill automates the process of updating the course materials and syncing them to the repository.

## Workflow Status

- **Trigger**: "Git Push", "Update and Push", "Sync Slides"
- **Action**:
  0.  **Generate Maps**: Calls `slide` skill's `generate_map.py` to update course maps (respects `MapLock`).
  1.  **Export Slides**: Calls `slide` skill's `export.py` to convert all `.md` files to PDF.
  2.  **Update Index**: The export script automatically regenerates `display/index.html` with correct paths/names.
  3.  **Git Sync**: Adds all files, commits with "Auto update", and pushes to remote.

## Usage

Run the following command in the project root:

```bash
python .agent/skills/git-push/scripts/push.py
```

## Dependencies

- Requires `.agent/skills/slide/scripts/export.py` to exist.
- Requires `git` to be configured.
