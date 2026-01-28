---
description: Clean orphan PDFs and rebuild all slides
---

1. Clean orphan PDFs
// turbo
python .agent/skills/slide/scripts/cleanup_pdf.py

2. Export all slides
// turbo
python .agent/skills/slide/scripts/export.py -a
