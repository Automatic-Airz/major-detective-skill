# Release Notes

## v0.1.0

Initial public release of 大学专业侦探 Skill.

### Included

- Major investigation workflow for Chinese gaokao major selection.
- Guided intake for students who do not know how to describe their situation.
- Parent-facing communication mode.
- School-major matching workflow with historical rank-data safety boundaries.
- Candidate-pool table templates.
- Official verification checklist workflow.
- Online-review and research-funding safeguards.
- Printable report guidance.
- Direct PDF prototype script: `major-detective/scripts/render_pdf_report.py`.

### Demo scenario

Recommended first demo:

```text
山东，物化生，位次先假设 75000。家里希望医学/生物稳定；学生喜欢实验、生命健康、检测分析，但不想走临床医学长周期，也不想读博。重点看医学检验技术、药学、卫生检验与检疫，山东优先，其次华东，公办优先。
```

### Known limitations

- This is not a志愿填报 replacement.
- It does not include a full national score-line database.
- It should not invent admission ranks, scores, plan counts, rankings, funding, or online reviews.
- Direct PDF generation requires Python + ReportLab + Chinese-capable font. Otherwise use HTML export as fallback.

### Recommended install locations

Codex:

```text
~/.codex/skills/major-detective
```

Claude Code:

```text
~/.claude/skills/major-detective
```
