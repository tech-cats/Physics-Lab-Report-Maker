---
name: physics-lab-report
description: Process a university physics experiment folder containing manuals, templates, handwritten measurements, scans, or existing pre-lab pages into a concise post-lab Markdown report with necessary calculations and charts, a post-lab PDF, and an assembled final PDF. Use for repeated 大学物理实验报告 workflows; do not use for generic essays or reports without experimental data.
---

# Physics Lab Report

Produce a submission-ready report from the evidence in the experiment folder.

## Governing principle

**If text could reasonably be included or omitted without losing a requirement, result, reproducibility, or necessary explanation, omit it.** Apply this to prose, headings, tables, charts, captions, caveats, and the final response. State each fact once. Do not add abstracts, introductions, background summaries, generic transitions, repeated conclusions, or decorative content unless the source template requires them.

## Report prose boundary

The manual's report requirements, the report template, and the user's explicit request define the scope. Do not introduce an unrequested quantity, comparison, curve, or analysis merely because it is related to the experiment. If that item is outside scope, omit both the item and any statement that its data are missing or that it cannot be evaluated. For example, when only stopping-voltage versus frequency analysis is required, do not mention the absence of saturation-current measurements or complete current-voltage curves.

Write the submitted report as the student's experiment report, not as an account of the assistant's work. Keep transcription checks, source inventories, confirmation history, file locations, point-count compliance, and quality-control notes in working assets when useful; exclude them from the report.

Do not add defensive statements about what was not fabricated, corrected, fitted, measured, or available. For example, omit “不补造原点数据”, “不能作为完整测量不确定度”, and unsolicited explanations about missing frequency measurements or reference values. Omit the optional analysis that would require such a disclaimer instead. Data integrity remains mandatory: never invent measurements, uncertainties, reference values, or completed experimental steps.

Include a limitation only when removing it would make a retained required result materially false or misleading; attach the shortest necessary qualification to that result. Missing inputs for an explicitly required result belong in a concise user-facing clarification or working note, not an automatic missing-data paragraph in the report. Do not add comparison or uncertainty sections solely to explain why they cannot be calculated.

## Mandatory final prose self-check

Before declaring the report complete, reread every generated paragraph, table note, and figure caption against the actual report requirements. This semantic review is mandatory; a keyword search alone does not satisfy it.

- Look specifically for unsolicited missing-data statements, explanations of analyses that cannot be performed, defensive assurances, assistant workflow commentary, and optional qualifications. Phrases such as “原记录没有……”, “未提供……”, “无法／不能据此……”, “并非新增测量”, and “未计入……” are review cues, not an exhaustive blacklist.
- For each sentence, ask whether deleting it would lose a required answer, a necessary result, an indispensable calculation step, or an essential interpretation. If not, delete it. If an optional analysis exists only with a disclaimer, remove that analysis and its disclaimer together. Preserve the shortest qualification needed to keep a required result accurate.
- Check for the same meaning expressed in different words. Do not replace a deleted caveat with a softer caveat, repeat table values in the conclusion, or add a sentence announcing that the self-check was performed.
- After deletions, regenerate both PDFs and check their final text as well as the Markdown so that an older export cannot retain removed wording. Complete the visual inspection after the final revision. Keep any self-check notes in working assets, outside the submitted report.

## Workflow

1. Inventory the experiment folder. Identify the manual, report template, handwritten data, pre-lab pages, raw-record pages, and any automatic-measurement output. Read the relevant experiment chapter and the template's required post-lab sections.
2. Preserve existing pre-lab and raw-record pages. Do not complete or rewrite them unless explicitly requested. The generated Markdown begins at the first required post-lab section and does not repeat identity fields or preserved material.
3. Transcribe measurements with units and validate expected ranges, step sizes, and row counts. Recheck ambiguous handwriting at high resolution. Leave unreadable or covered values missing; never covertly fabricate or alter measurements.
4. Use only traceable processing needed by the experiment: the required plots, calculations or fits, and interpolation needed to obtain a specified quantity such as an axis intercept. Show raw points whenever smoothing or fitting is used. Exclude incomplete boundary extrema. Include uncertainty, fit quality, or reference comparisons only when required or necessary to interpret the result and supported by the available evidence.
5. Write only the required data processing, conclusion/phenomenon analysis, and discussion answers. If a required comparison lacks quantitative data, provide only the supported answer and resolve any essential missing input outside the report. Never invent data or add a generic paragraph listing unavailable analyses. Apply the report prose boundary before export.
6. Create the Markdown, its local assets, a rendered post-lab PDF, and the final merged PDF. Typeset mathematical expressions using the equation-rendering requirements below. Default order: preserved pre-lab pages, preserved raw-record pages, then post-lab pages. Use [scripts/assemble_report.py](scripts/assemble_report.py) when image/PDF page assembly is needed.
7. Complete the mandatory final prose self-check, then render every final PDF page to images and inspect it. Verify legibility, Chinese fonts, equations, chart labels, table boundaries, page order, page numbering, bookmarks, page count, and agreement among source data, calculations, charts, and conclusions. Do not deliver until both the prose self-check and visual inspection pass.

## Equation rendering

- Keep editable LaTeX math in Markdown: use dollar delimiters for inline expressions and double-dollar delimiters on separate lines for display equations. Preserve backslashes when writing source files; use raw strings or proper escaping in the host language.
- The PDF must contain rendered mathematics, not literal LaTeX, exposed markup such as <super>, or plain-text substitutes such as sqrt(...) and (numerator)/(denominator) for display equations. Typeset fractions, radicals, sums, Greek letters, subscripts and superscripts with a math renderer. Use upright units and italic mathematical variables.
- Prefer a LaTeX-capable document renderer when available. For a ReportLab workflow, render supported LaTeX expressions with Matplotlib MathText using Computer Modern fonts, export SVG paths, and embed them with svglib.svg2rlg. This provides vector mathematics without a full TeX installation; MathText supports a subset of LaTeX, so verify each expression and use a full LaTeX or MathJax renderer when unsupported syntax is needed. Never silently fall back to raw source text.
- Prefer vector equations; if raster output is necessary, render at least 300 dpi at the intended print size. Save reusable equation assets under the report assets folder. Keep equations readable at normal page size; move long expressions to their own lines or split them logically rather than shrinking them excessively.
- Inspect actual rendered pages in both the post-lab and merged PDFs: check fraction bars, radical coverage, sum limits, baseline alignment, glyphs, clipping, line spacing and page breaks. Confirm every symbol and numerical value agrees with the Markdown and calculations. Successful export or text extraction alone is not proof of correct equation rendering.
- For a formula-formatting revision, preserve existing measurements, calculations and approved charts; update equation rendering and necessary spacing only. Recheck pagination and bookmarks after reflow.

## Output defaults

- Work in the experiment folder and name files from the experiment title: `<实验名>_课后报告.md`, `<实验名>_课后报告_assets/`, `<实验名>_课后报告.pdf`, and `<实验名>_完整实验报告.pdf`.
- Keep original files unchanged. Put transcription data in the assets folder when it materially improves auditability.
- Use the fewest figures that prove the result. Prefer a raw curve and one fit/derived chart; add another only when it answers a distinct required question.
- Keep the final response to the result and links to deliverables.
