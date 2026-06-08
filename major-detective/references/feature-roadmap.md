# Feature Roadmap

## Current Core Workflow

1. Guided student intake
2. Major truth report
3. Major comparison
4. Parent communication
5. Next-step verification checklist
6. Printable report package

## New Planned Workflow: School-Major Candidate Pool

After the student has narrowed the major direction and has a score/rank, offer:

```text
要不要继续生成「院校-专业候选池」？
我会基于你的省份、选科、位次、专业方向和城市偏好，整理冲/稳/保候选表。
注意：这不是录取预测，必须以当年招生计划和省考试院投档数据为准。
```

## User Flow

### Step 1: Gather Profile

- Province
- Subject combination
- Score/rank
- Candidate majors
- City preference
- School-type constraints
- Priority: school, major, city, stability, cost, postgraduate path

### Step 2: If Rank Is Missing

Output:

- Major direction pre-screening
- School-type pre-screening
- Data-source checklist
- Table template to fill after rank is released

Do not output冲稳保.

### Step 3: If Rank Exists

Output:

- Historical-data boundary note
- Candidate pool table
- 冲/稳/保 bands
- Major-quality signals
- Verification checklist
- Questions to ask admissions office/current students

### Step 4: Quality Layer

For each candidate, add:

- Major/discipline strength signal
- Undergraduate program signal
- Research platform/funding signal if relevant
- Employment/graduate-school signal
- Online review warning patterns, clearly labeled as anecdotal

## Data Source Principles

Use official admission sources first:

- Provincial exam authority投档/录取表
- Current-year招生计划
- Target university招生章程 and admissions website
- 阳光高考

Use quality signals second:

- 学科评估
- 一流本科专业建设点
- Professional accreditation
- Employment quality reports

Use third-party and social sources last:

- 软科 or similar ranking
- Zhihu/student reviews

Never let social reviews override official data.

## Product Boundary

Allowed:

- Generate candidate pool
- Rank evidence quality
- Produce核验清单
- Flag risky assumptions
- Compare university-major combinations

Not allowed:

- Predict admission probability
- Promise录取
- Invent missing cutoff data
- Treat rankings as final truth
- Treat Zhihu/student reviews as facts
- Say research funding guarantees teaching quality or employment
