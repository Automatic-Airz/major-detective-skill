# Deliverables

Use this reference when the user asks for a more productized output than a chat answer, such as a PDF report, report package, printable HTML, parent brief, or short-video script.

## Why Deliverables Matter

Major Detective should be visibly different from a normal answer. A normal answer can be correct, but the Skill should produce repeatable artifacts:

- 专业调查报告
- 家长沟通简报
- 专业对比矩阵
- 院校-专业候选池
- 风险雷达
- 官方核验清单
- 招办/学长学姐提问清单
- 家庭讨论表
- 下一步核验清单
- 短视频/图文脚本（仅作为创作者/投稿辅助交付物）
- 可打印 HTML / PDF 报告包

## Report Package

When asked to package a result, create these outputs:

```text
major-report/
├── report.md       # Full Markdown report
├── report.html     # Print-ready HTML report
└── assets/         # Optional charts, screenshots, or images
```

If direct PDF generation is available in the environment, also create:

```text
report.pdf
```

In this project, direct PDF generation is supported through:

```text
scripts/render_pdf_report.py
```

Use it when the environment has ReportLab and a Chinese-capable font. It can generate `report.md` and `report.pdf` directly from built-in sample data or JSON report data.

If direct PDF generation is unavailable, create `report.html` with print CSS and tell the user it can be exported to PDF from the browser print dialog.

Recommended direct-PDF command in the Codex bundled runtime:

```bash
/Users/air/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 major-detective/scripts/render_pdf_report.py --output-dir major-detective/examples/pdf-proof
```

Validation:

- Use `pypdf` to confirm page count and extractable Chinese text.
- On macOS, Quick Look (`qlmanage`) can render a preview thumbnail for visual inspection.
- If Poppler/PyMuPDF is available, render every page to PNG before final delivery.

## Proactive Offering

Do not wait for the user to know the deliverable names. After a substantial report or reasonably complete consultation, offer:

```text
这版信息已经足够进入交付物阶段。你接下来可以选一个，我直接生成：
1. 生成「下一步核验清单」
2. 生成「家长沟通版 / 微信短版」
3. 生成「专业对比表」
4. 生成「招办/学长学姐提问清单」
5. 生成「可打印报告」：report.md / report.html / report.pdf（若环境支持）
```

If key context is missing, do not offer the full menu yet. Ask focused follow-up questions first, then say what can be generated after the user answers.

For normal student/family answers, do not include creator-facing scripts in this menu unless the user has asked about投稿、运营、图文、短视频、or demo.

For school-major matching answers, include student/family artifacts before generic reports:

```text
你接下来可以选一个：
1. 院校-专业候选池表格
2. 官方数据核验清单
3. 专业质量比较表
4. 家长沟通版 / 微信短版
5. 招办/学长学姐提问清单
6. 可打印报告：report.md / report.html / report.pdf（若环境支持）
```

## Required Report Sections

Use this order:

1. 封面信息：专业、用户画像、生成时间、免责声明
2. 一句话画像
3. 用户真实问题
4. 信息完整度
5. 真实学习内容
6. 常见误解
7. 适合条件
8. 需要谨慎的情况
9. 升学与就业路径
10. 风险雷达
11. 替代专业
12. 家长沟通版
13. 官方核验清单
14. 下一步行动

## Visual Standards

- Use tables for risk radar and major comparisons.
- Keep disclaimers visible but not alarmist.
- Make the first page useful when screenshotted.
- Avoid decorative fluff. The artifact should feel like a report, not a marketing page.

## School-Major Candidate Pool

When packaging a school-major matching output, make uncertainty visible in the artifact:

- Use "待核验搜索种子" until official historical rank data is filled.
- Use "预筛倾向" before final banding; reserve "冲/稳/保候选池" for source-labeled historical rank data plus current-year plan context.
- Include source columns: 省考试院投档表、当年招生计划、招生章程、培养方案、就业报告.
- Include "数据状态": 已核验 / 用户提供 / 待填 / 推断.
- Include "不是录取预测" near the top.

Recommended table columns:

```markdown
| 预筛倾向 | 院校 | 专业/专业类 | 城市 | 数据状态 | 近三年最低位次 | 计划变化 | 专业实力信号 | 就业/升学信号 | 主要风险 | 必查来源 |
|---|---|---|---|---|---|---|---|---|---|---|
```

## Parent Brief

For parent-facing deliverables, default to respectful共同核验 wording. Avoid "说服父母" framing unless the user explicitly asks for persuasion.

Offer two lengths when useful:

- 完整说明版: suitable for a family discussion or report.
- 微信短版: 300-500 Chinese characters, suitable for direct sharing.

Include:

- 家长关心点复述: 稳定、体面、离家近、成本、学校层次.
- 学生偏好 and aversions.
- Why major names are not enough.
- A short comparison of candidate directions.
- A joint verification checklist.

## Differentiation Checklist

A deliverable should make Skill output clearly different from no-Skill chat by including:

- A named report title.
- A structured user profile.
- Information completeness.
- A risk radar table.
- A family communication section.
- A verification checklist.
- A next-step action list.
- A clear final menu that offers the next deliverable instead of making the user invent the prompt.
- A printable report option that names `report.md`, `report.html`, and `report.pdf` when PDF generation is available.

If these are missing, the output may feel too similar to ordinary chat.

## Audience Priority

Default deliverables should serve the student/family workflow:

1. Professional investigation report
2. Parent communication brief
3. Comparison matrix
4. Verification checklist
5. Next-step action list
6. School-major candidate pool when score/rank matching is requested
7. Printable HTML/PDF-ready report

Creator-facing scripts are secondary. Generate them only when the user explicitly needs投稿、运营、图文、短视频、or demo materials.

## Demo Packaging Positioning

For a short-video demo, position the product as a downloadable Skill and Agent workflow, not a standalone website.

The video should demonstrate:

- A student starts with an incomplete question.
- The Skill asks for missing context instead of requiring a perfect prompt.
- The Skill turns anxiety into artifacts: parent brief, verification checklist, candidate-pool table, and printable report.
- The Skill visibly avoids admission prediction and fabricated data.

Minimum demo artifacts before recording:

1. 家长沟通版: respectful共同核验 tone plus optional微信短版.
2. 官方核验清单: what to verify, where to verify, and what would change the conclusion.
3. 院校-专业候选池表格: clearly labeled待核验搜索种子 when data is missing.
4. 可打印报告: `report.md` and `report.html` or PDF-ready HTML.
5. 招办/学长学姐提问清单: converts uncertainty and online-review patterns into questions.

Do not make a webpage demo the product center unless explicitly requested. A local HTML report is acceptable as an exported artifact, not the primary app.
