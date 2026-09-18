---
name: physics-lab-report
description: Process a university physics experiment folder containing manuals, templates, handwritten measurements, scans, or existing pre-lab pages into a concise post-lab Markdown report with necessary calculations and charts, a post-lab PDF, and an assembled final PDF. Use for repeated 大学物理实验报告 workflows; do not use for generic essays or reports without experimental data.
---

# Physics Lab Report

Produce a submission-ready report from the evidence in the experiment folder.

## Governing principle

**If text could reasonably be included or omitted without losing a requirement, result, reproducibility, or necessary explanation, omit it.** Apply this to prose, headings, tables, charts, captions, caveats, and the final response. State each fact once. Do not add abstracts, introductions, background summaries, generic transitions, repeated conclusions, or decorative content unless the source template requires them.

## Workflow

1. Inventory the experiment folder. Identify the manual, report template, handwritten data, pre-lab pages, raw-record pages, and any automatic-measurement output. Read the relevant experiment chapter and the template's required post-lab sections.
2. Preserve existing pre-lab and raw-record pages. Do not complete or rewrite them unless explicitly requested. The generated Markdown begins at the first required post-lab section and does not repeat identity fields or preserved material.
3. Transcribe measurements with units and validate expected ranges, step sizes, and row counts. Recheck ambiguous handwriting at high resolution. Leave unreadable or covered values missing; never covertly fabricate or alter measurements.
4. Use only traceable processing needed by the experiment: interpolation solely for displaying or smoothing gaps, a raw-data plot, and the calculation or fit required by the manual. Show raw points whenever smoothing or fitting is used. Exclude incomplete boundary extrema. Report the measured result, uncertainty or fit quality when meaningful, and the required comparison with the reference value.
5. Write only the required data processing, conclusion/phenomenon analysis, and discussion answers. If requested automatic data is absent, compare qualitatively and say no quantitative record was available; do not invent it.
6. Create the Markdown, its local assets, a rendered post-lab PDF, and the final merged PDF. Default order: preserved pre-lab pages, preserved raw-record pages, then post-lab pages. Use [scripts/assemble_report.py](scripts/assemble_report.py) when image/PDF page assembly is needed.
7. Render every PDF page to images and inspect it. Verify legibility, Chinese fonts, equations, chart labels, table boundaries, page order, page numbering, bookmarks, page count, and agreement among source data, calculations, charts, and conclusions. Iterate until clean.

## Output defaults

- Work in the experiment folder and name files from the experiment title: `<实验名>_课后报告.md`, `<实验名>_课后报告_assets/`, `<实验名>_课后报告.pdf`, and `<实验名>_完整实验报告.pdf`.
- Keep original files unchanged. Put transcription data in the assets folder when it materially improves auditability.
- Use the fewest figures that prove the result. Prefer a raw curve and one fit/derived chart; add another only when it answers a distinct required question.
- Keep the final response to the result and links to deliverables.
