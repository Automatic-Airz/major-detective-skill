# 大学专业侦探 Skill 下载与安装

> 高考专业选择不是让 AI 替你填志愿，而是让 Agent 帮你把专业、学校、家长期待和官方核验步骤拆清楚。

## 这是什么

「大学专业侦探」是一个 AI Agent Skill，用来辅助高考生和家长做专业调查。

它可以帮你：

- 分析一个专业真实学什么。
- 对比相邻专业的学习内容和就业路径。
- 生成给家长看的沟通版。
- 生成官方核验清单。
- 生成院校-专业候选池表格。
- 生成招办/学长学姐提问清单。
- 生成可打印 PDF 报告。

它的使用体验是：

- 如果你只说了一个专业名，它会先做基础调查，并追问少量关键信息。
- 如果你的情况已经说得比较完整，它会主动给出交付物菜单，让你选择继续生成家长沟通版、核验清单、候选池表格、提问清单或可打印报告。
- 可打印报告优先生成 `report.md` / `report.html` / `report.pdf`；如果环境不支持直接生成 PDF，也可以用 HTML 打印成 PDF。

它不会：

- 替你填志愿。
- 预测录取概率。
- 承诺就业稳定。
- 编造分数线、位次、计划数、排名、经费或网评。
- 模仿或蒸馏任何教育博主/名人。

## 下载

GitHub Release ZIP 直链：

```text
https://github.com/Automatic-Airz/major-detective-skill/releases/download/v0.1.0/major-detective-skill-v0.1.0.zip
```

GitHub 仓库：

```text
https://github.com/Automatic-Airz/major-detective-skill
```

Gitee 镜像：

```text
https://gitee.com/AutoAirz/major-detective-skill
```

推荐优先下载：

```text
major-detective-skill-v0.1.0.zip
```

如果 GitHub 打不开，可以使用当前 Gitee 页面右上角或页面中的“克隆/下载”获取源码包。

## 安装到 Codex

解压后，打开终端，进入解压目录，运行：

```bash
mkdir -p "$HOME/.codex/skills"
cp -R major-detective "$HOME/.codex/skills/major-detective"
```

检查：

```bash
ls "$HOME/.codex/skills/major-detective/SKILL.md"
```

然后重启 Codex。

## 安装到 Claude Code

解压后，打开终端，进入解压目录，运行：

```bash
mkdir -p "$HOME/.claude/skills"
cp -R major-detective "$HOME/.claude/skills/major-detective"
```

检查：

```bash
ls "$HOME/.claude/skills/major-detective/SKILL.md"
```

然后重启 Claude Code。

Claude Code 中也可以直接用：

```text
/major-detective 我是山东物化生，家里建议医学/生物相关，我喜欢实验但不想读博，帮我分析专业方向。
```

## 示例 Prompt

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

如果你不知道怎么说，可以直接问：

```text
使用大学专业侦探 Skill。我想看看医学检验技术怎么样，但我现在也不知道该说什么。
```

## 示例产物

这个 Skill 不只是输出一段聊天回答，它可以把结果整理成可交付材料，例如：

- 三专业真实路径对比表
- 给家长看的沟通版
- 官方核验清单
- 院校-专业候选池表格
- 招办/学长学姐提问清单
- 可打印 PDF 报告

示例 PDF 报告内容包括：

- 用户画像
- 一句话判断
- 三专业对比
- 风险雷达
- 官方核验清单
- 家长沟通版
- 下一步行动

![示例 PDF 报告预览](major-detective/examples/pdf-proof/rendered/report.pdf.png)

## 生成 PDF 报告

如果你的环境有 Python 和 ReportLab，可以运行：

```bash
python3 major-detective/scripts/render_pdf_report.py --output-dir output/pdf-demo
```

在 Codex 桌面环境中，推荐使用：

```bash
/Users/air/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 major-detective/scripts/render_pdf_report.py --output-dir output/pdf-demo
```

生成结果：

```text
output/pdf-demo/report.md
output/pdf-demo/report.pdf
```

如果 PDF 生成失败，可以先让 Agent 生成 `report.html`，再用浏览器打印为 PDF。

## 适合场景

- 高考后不知道该怎么选专业。
- 家里建议一个专业，但你不确定适不适合自己。
- 想比较几个相近专业。
- 想和家长一起核验信息，而不是凭印象争论。

## 安全声明

本 Skill 不是官方志愿填报建议，也不是录取预测工具。所有招生计划、投档位次、选科要求、体检要求、培养方案和就业信息，都应以省级教育招生考试院和高校官方发布为准。

院校-专业候选池如果标注为“待核验搜索种子”，意思是：它只是下一步该查什么，不是推荐你填什么。

网评只能作为问题线索，不能替代官方培养方案、就业报告和在校生多方核验。

科研项目多说明学科活跃，但不等于本科体验一定好，也不等于就业一定好。

## 作者

Automatic-Airz

## License

MIT License. See [LICENSE](./LICENSE).
