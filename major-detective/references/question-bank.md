# Question Bank

Use these questions to guide users without interrogating them. Ask only what is needed for the current intent.

## Core Questions

1. 你想调查的是哪个专业，还是想比较几个专业？
2. 你所在省份/地区是哪里？选科或文理是什么？
3. 你大概的分数、位次或目标批次是什么？不确定可以跳过。
4. 你更看重稳定、收入上限、城市选择、兴趣匹配，还是升学空间？
5. 你是否接受读研、读博、长学制或长期资格考试？

## Guided Intake Script

Use when the user says "不知道怎么说", "引导我填写", or gives only a vague concern.

```text
我先问 5 个问题，回答不完整也没关系：
1. 你想调查/比较哪些专业？
2. 你所在省份和选科/文理是什么？
3. 你大概的分数、位次或目标学校层次是什么？不确定可以写「不确定」。
4. 你更看重：稳定、收入、城市、兴趣、考公考编、升学空间中的哪几个？
5. 你明确排斥什么：读研/读博、强数学、强代码、强背诵、实验、长期熬夜、频繁社交？
```

After the user answers, summarize the profile and say what can be generated next.

## Interest And Aversion

- 你喜欢或能接受：数学、编程、实验、写作、背诵、沟通、画图、医学、商业分析、教育陪伴、动手制作中的哪些？
- 你明确排斥：长期熬夜、频繁社交、强记忆、强数学、强代码、强实验、体力工作、长期深造、异地求学中的哪些？
- 你更喜欢确定性任务，还是开放式探索？

## Family Constraints

- 家里更看重稳定、收入、城市、学校名气，还是专业名气？
- 家里是否能接受读研/读博带来的时间和经济成本？
- 家里是否倾向体制内、教师、医生、国企、大厂、自由职业等路径？
- 是否有明确不能接受的城市、行业或工作形态？

## Major Comparison

When comparing majors, ask:

- 这几个专业中，你目前最偏向哪一个？为什么？
- 你最担心哪一点：就业、学习难度、家长反对、读研压力、城市选择，还是未来转行？
- 你希望比较结果更偏「现实就业」还是「个人适配」？

## Unsupported Or Less-Known Majors

When users ask about a less-known or unsupported major, ask:

- 你是在哪个学校或招生计划里看到这个专业的？
- 你以为这个专业主要学什么？这个理解可能需要先核验。
- 你能接受工程数学、代码、实验、野外/现场环境、长期实习或行业地域限制吗？
- 你更在意就业确定性、专业兴趣、城市选择，还是未来转向空间？
- 是否有相邻专业可以一起比较，例如传统工科、计算机、自动化、资源类、环境类、管理类？

Use these questions to avoid fabricating details while still giving the user a useful investigation path.

## Parent Version

For parent-facing output, ask:

- 父母最担心的问题是什么？
- 父母目前支持哪个专业，反对哪个专业？
- 你希望这份内容是「说服父母」还是「和父母一起冷静讨论」？

## Next-Step Checklist

For student/family action planning, ask:

- 你现在最需要核验的是学校培养方案、就业去向、转专业政策，还是家长沟通？
- 你有目标学校名单吗？如果有，需要逐个查培养方案和招生计划。
- 你希望下一步是做专业对比、查学校信息，还是整理一页给家长看的简报？

## School-Major Matching

For university-major candidate pool generation, ask:

- 你的省份、选科/文理、分数和位次是什么？如果位次没出，可以先做预筛。
- 想看哪些专业或专业方向？有没有明确排除的专业？
- 城市偏好是什么：本省、周边、全国都可，还是指定城市？
- 公办/民办/中外合作/医学类/师范类/农林类等学校类型有没有限制？
- 你更优先学校层次、专业强度、城市、稳定就业、读研空间，还是学费成本？

If rank is missing, say:

```text
位次没出前，我不建议做冲稳保结论。可以先做专业和学校类型预筛；等一分一段表和位次出来后，再按往年位次生成候选池。
```

## Creator-Facing Content Demo

Use only when the user explicitly asks for投稿、运营、图文、短视频、or demo communication. For short-video/demo output, ask:

- 目标平台是抖音图文、口播视频，还是网页 Demo？
- 想展示哪个专业或学生场景？
- 想要偏理性、反差、避坑、温和陪伴，还是家长沟通？
