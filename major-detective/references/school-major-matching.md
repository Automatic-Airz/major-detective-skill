# School-Major Matching

Use this reference when the user asks to match their score/rank with possible universities, university-major combinations, school quality, major strength, research funding, or student reviews.

## Positioning

This is not admission prediction. Treat it as:

```text
基于往年投档/录取数据生成「院校-专业候选池」和核验清单。
```

Never say "稳录", "一定能上", "保底一定安全", or "录取概率 X%". Use:

- 冲 / 稳 / 保候选池
- 需核验
- 往年位次参考
- 风险缓冲
- 数据年份和来源
- 今年招生计划、选科、批次、专业组变化可能改变结果

## Required Inputs

Ask for these before generating a candidate pool:

1. Province / exam region
2. Subject combination or文理
3. Score and rank if available. If rank is unavailable, ask for estimated level and wait for rank before finalizing.
4. Target major families or excluded major families
5. City/region preference
6. Whether the user prioritizes school, major, city, stability, cost, or postgraduate path
7. Acceptable school types: public/private, Sino-foreign, local/nonlocal, medical/agriculture/normal universities, etc.

If rank is unavailable, generate only a pre-screening plan and tell the user to re-run after rank is released.

## Rank-Missing Mode

When the user has only a score estimate, special-control-line delta, or rough level, do not produce a true冲稳保 list. Use this shape:

```text
当前缺失：正式全省位次。
现在能做：专业池预筛、地域/学校类型预筛、官方数据源清单、候选池表格模板。
现在不能做：录取概率、稳录判断、真实冲稳保档位、具体保底结论。
位次出来后请补充：省份、选科/文理、正式位次、目标专业、地域偏好、是否接受民办/中外合作/省外/读研。
```

End rank-missing answers with a copyable table template instead of school recommendations unless the user explicitly asks for search seeds.

## Source Hierarchy

Use sources in this priority order.

### Tier 1: Official Admission And Policy Sources

- Provincial exam authority投档情况表 / 录取情况表, such as 山东省教育招生考试院.
- Current-year招生计划 and志愿填报指南.
- Target university招生章程,招生计划, and official admissions website.
- Ministry of Education / 阳光高考 platform for official school and major information.

### Tier 2: Official Or Semi-Official Quality Signals

- 教育部学位中心学科评估 where applicable. Note that学科评估 is graduate-discipline-level, not always undergraduate-major-level.
- 国家级/省级一流本科专业建设点 if available from official school/MOE pages.
- Professional accreditation, such as medical, engineering education, teacher education, when relevant.
- University-published employment quality reports and college graduate destinations.

### Tier 3: Third-Party Reference Signals

- Soft-ranking style lists such as 软科专业排名, only as one reference signal.
- Alumni/student reviews from Zhihu, forums, Bilibili, Xiaohongshu, Tieba, etc., only as qualitative sentiment and issue discovery.

Do not treat third-party rankings or social reviews as final authority.

## Data Dimensions

For each university-major candidate, collect:

- Institution name
- Major name / major group / track
- Province and batch
- Year(s) of data
- Minimum score
- Minimum rank
- 招生计划 count if available
- Subject requirements
- Tuition and Sino-foreign/private flags if relevant
- City
- School type and level
- Major-strength signal
- Employment/graduate-school signal
- Review sentiment summary
- Key risks and verification items

## Candidate Bands

Use rank-based bands, not only score. Suggested framing:

- 冲: historical minimum rank is better than the user's rank, but within a controlled stretch range.
- 稳: historical minimum rank is close to or slightly below the user's rank with reasonable buffer.
- 保: historical minimum rank is below the user's rank with larger buffer.

Do not hard-code universal thresholds. Explain that band thresholds vary by province, score segment, major popularity, 招生计划 changes, and risk tolerance.

If the user lacks rank:

```text
你现在只有分数/估分，我可以先做专业和院校类型预筛；等一分一段表和位次出来后，再按位次生成冲稳保候选池。
```

If historical rank data has not been retrieved or filled, do not label rows as final "冲/稳/保". Use:

- 预筛倾向
- 高位次压力候选
- 接近位次候选
- 保守核验候选
- 待核验搜索种子

Add this warning above any institution table without verified historical rank values:

```text
注意：以下不是推荐名单，也不是最终志愿档位，只是待核验搜索种子。必须填入近三年官方投档位次、当年招生计划、选科要求和招生章程后，才能判断是否进入冲稳保候选池。
```

## Major Quality Signals

When evaluating whether "this university's specific major is strong", use a weighted evidence view:

1. Does the school have the relevant college/discipline foundation?
2. Is there a recognized学科评估 result for the related discipline?
3. Is the undergraduate major an一流本科专业建设点 or accredited program?
4. Are there affiliated hospitals, labs, practice bases, teacher-training bases, or industry links relevant to the major?
5. Does the school publish transparent graduate-school/employment destinations?
6. Are there repeated student-review issues that match the user's aversions?

Separate evidence labels when school-specific claims are not fully verified:

- 已核验事实: source-labeled official data.
- 基于公开常识的推断: reasonable but not source-confirmed in the current answer.
- 待核验: must be checked before family decisions.

If using scores or weights, label them as "默认可调整权重", not an official ranking model. Avoid false precision; explain that families can adjust weights based on stability, city, school level, major fit, cost, or graduate-school tolerance.

Prefer "公开可核验的学科建设信号" over unstable claims about unpublished or incomplete evaluation rounds. Do not imply that graduate-discipline evaluation is the same as undergraduate major quality.

## Research Funding Signals

Use research funding carefully. It can indicate discipline activity but does not directly prove undergraduate teaching quality.

Preferred signals:

- National Natural Science Foundation project counts / recent awards for relevant school or discipline, when available.
- University/college official research project summaries.
- Key labs and research platforms.
- Major research centers, affiliated hospitals, or practice bases.

Always explain:

```text
科研项目多说明该学科科研活跃，但不等于本科体验一定好，也不等于就业一定好。
```

Do not invent funding amounts, project counts, or award levels. If no current source is available, create a field for the user to fill and list where to verify it.

## Student Review Signals

Use online reviews as qualitative warning signs only.

Extract patterns, not isolated comments:

- Course difficulty
- Teacher support
- Lab/internship access
- Transfer-major policy
- Dorm/campus split
- City and internship opportunities
- Workload and exam pressure
- Employment and postgraduate atmosphere

Do not quote or rely on a single anonymous review as fact. Say:

```text
网评只能作为问题线索，不能替代官方培养方案、就业报告和在校生多方核验。
```

Convert every review pattern into a verification question. For example, "多人提到实习弱" becomes "请向学院或在校生核验本科实习医院名单、分配方式、近三年实习单位".

## Output Structure

For a school-major matching report, use:

1. Input recap and missing data
2. Data-source disclaimer
3. Candidate pool table
4. 冲/稳/保 band explanation
5. University-major quality notes
6. Major fit with user's profile
7. Key risks and must-check items
8. Questions to ask admissions office / current students
9. Next step after rank is released or after target list is narrowed

## Candidate Pool Table

Use this table:

| 档位 | 院校 | 专业/专业类 | 城市 | 往年最低位次/分数 | 计划变化 | 专业实力信号 | 适配理由 | 主要风险 | 下一步核验 |
|---|---|---|---|---|---|---|---|---|---|

If data has not been retrieved, output a table template and source checklist instead of inventing values.

## Copyable Templates

Use a copyable Markdown table when the user needs to continue manually:

```markdown
| 预筛倾向 | 院校 | 专业/专业类 | 城市 | 数据状态 | 2025最低位次 | 2024最低位次 | 2023最低位次 | 2026计划变化 | 专业实力信号 | 就业/升学信号 | 主要风险 | 必查来源 |
|---|---|---|---|---|---:|---:|---:|---|---|---|---|---|
| 待核验搜索种子 |  |  |  | 待填 |  |  |  |  |  |  |  | 省考试院投档表；招生计划；招生章程；培养方案；就业报告 |
```

For professional-quality comparison:

```markdown
| 学校 | 专业完整名称 | 录取位次压力 | 专业建设信号 | 实践/附属资源 | 就业/升学去向 | 科研活跃度线索 | 网评问题线索 | 待核验问题 | 初步判断 |
|---|---|---|---|---|---|---|---|---|---|
|  |  | 高/中/低 |  |  |  | 不等于本科质量 | 仅作线索 |  | 值得重点核验/暂缓/备选 |
```

## Safety Rules

- Do not fabricate cutoffs, ranks, plan counts, rankings, funding numbers, or reviews.
- If browsing/search is unavailable, create a research plan and data table template.
- Always cite the year and source for admission data.
- Explain that current-year招生计划,选科要求,批次设置, and student preferences may change the interpretation of previous-year data.
- For social reviews, summarize only repeated patterns and label them as anecdotal.
