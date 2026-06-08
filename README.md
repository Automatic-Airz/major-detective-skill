# 大学专业侦探 Skill

一个面向高考专业选择的 AI Agent Skill。它不替你填志愿，也不预测录取概率，而是帮助学生和家长把专业、学校、位次、培养方案、就业去向和家庭期待拆开核验。

## 它能做什么

- 引导学生补充关键信息：省份、选科、位次、兴趣、排斥项、家庭期待。
- 分析大学专业的真实学习内容、常见误解、适合条件和风险点。
- 对比相邻专业，例如医学检验技术、药学、卫生检验与检疫。
- 生成给家长看的沟通版，强调共同核验而不是对立说服。
- 生成官方核验清单：省考试院投档表、招生计划、招生章程、培养方案、就业报告。
- 生成院校-专业候选池表格，数据不足时明确标注为“待核验搜索种子”。
- 生成 Markdown / PDF 报告样例。

## 适合谁

- 刚高考完、不知道怎么选专业的学生。
- 想和家长讨论专业选择，但不知道如何组织信息的学生。
- 想快速了解某个专业是否适合自己的家庭。
- 想用 Agent Skill 做结构化专业调查的 AI 用户。

## 不适合什么

本 Skill 不是：

- 官方志愿填报服务。
- 录取概率预测器。
- 分数线数据库。
- 保证就业或升学的工具。
- 某位教育博主或名人的模仿版。

## 快速开始

安装后可以直接问：

```text
使用大学专业侦探 Skill。

我是山东考生，物化生，位次先假设 75000。家里希望我报医学/生物相关，觉得稳定、体面、离家近。我喜欢实验、生命健康、检测分析，但不想走临床医学长周期，也不想读到博士。

我重点考虑：医学检验技术、药学、卫生检验与检疫。

请你帮我生成：
1. 三个专业的真实路径对比表
2. 给家长看的沟通版
3. 官方核验清单
4. 院校-专业候选池表格，数据不足时只标为待核验搜索种子
5. 可打印报告
```

如果你不知道怎么说，也可以问：

```text
使用大学专业侦探 Skill。我想看看医学检验技术怎么样，但我现在也不知道该说什么。
```

## 安装

详见 [INSTALL.md](./INSTALL.md)。

下载 ZIP：

```text
https://github.com/Automatic-Airz/major-detective-skill/releases/download/v0.1.0/major-detective-skill-v0.1.0.zip
```

## 示例产物

Skill 内置了 PDF 报告生成脚本：

```bash
python3 major-detective/scripts/render_pdf_report.py --output-dir output/pdf-demo
```

在 Codex 桌面环境里，推荐使用 bundled Python：

```bash
/Users/air/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 major-detective/scripts/render_pdf_report.py --output-dir output/pdf-demo
```

样例输出：

```text
report.md
report.pdf
```

## 安全边界

使用时请记住：

- 所有招生计划、投档位次、选科要求，以省级教育招生考试院和高校官方信息为准。
- 院校-专业候选池不是推荐名单，数据未核验时只作为搜索种子。
- 网评只能作为问题线索，不能替代培养方案、就业报告和在校生多方核验。
- 科研项目多说明学科活跃，不等于本科体验一定好，也不等于就业一定好。

## 作者

Automatic-Airz

## License

MIT License. See [LICENSE](./LICENSE).
