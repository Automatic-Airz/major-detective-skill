# 安装教程

下面按“小白版”写。你不需要懂代码，只要会复制文件和重启工具。

## 先选你的使用方式

这个项目是一个 AI Agent Skill，不是普通 App。

你可以按自己的工具选择：

| 使用方式 | 适合谁 | 怎么用 |
|---|---|---|
| Codex | 已经能用 OpenAI Codex 的用户 | 原生安装 Skill 文件夹 |
| Claude Code | 已经能用 Claude Code 的用户 | 原生安装 Skill 文件夹 |
| 国产 AI IDE / 编程 Agent | 不能方便使用 Codex / Claude Code，但能用 TRAE、通义灵码、CodeBuddy 等 | 打开项目文件夹，让 Agent 阅读 `SKILL.md` |
| 国产智能体平台 | 想做成网页智能体或分享给别人使用 | 把 `SKILL.md` 改成系统提示词，把 references 上传成知识库 |

## 下载安装包

从 Release 页面下载：

```text
major-detective-skill-v0.1.0.zip
```

解压后你会看到：

```text
major-detective-skill-v0.1.0/
├── major-detective/
├── README.md
├── INSTALL.md
├── RELEASE_NOTES.md
└── LICENSE
```

真正的 Skill 文件夹是：

```text
major-detective/
```

## 安装到 Codex

Codex 是 OpenAI 的 coding agent，可以读取项目、执行命令、生成文件。新版 Codex 官方文档中的用户级 Skill 路径是：

```text
$HOME/.agents/skills
```

部分桌面版或旧版教程可能仍使用：

```text
$HOME/.codex/skills
```

如果你不确定，先用“新版推荐路径”；如果重启后没有识别，再试“兼容路径”。

### 方法一：新版推荐路径

打开终端，进入解压后的目录，然后运行：

```bash
mkdir -p "$HOME/.agents/skills"
cp -R major-detective "$HOME/.agents/skills/major-detective"
```

检查是否安装成功：

```bash
ls "$HOME/.agents/skills/major-detective/SKILL.md"
```

如果能看到文件路径，说明复制成功。

然后重启 Codex。

### 方法二：Codex 兼容路径

如果方法一没有触发 Skill，再运行：

```bash
mkdir -p "$HOME/.codex/skills"
cp -R major-detective "$HOME/.codex/skills/major-detective"
```

检查是否安装成功：

```bash
ls "$HOME/.codex/skills/major-detective/SKILL.md"
```

如果能看到文件路径，说明复制成功。

然后重启 Codex。

### 方法三：手动复制

1. 打开用户主目录。
2. 找到或创建 `.agents/skills/` 文件夹。
3. 把 `major-detective` 整个文件夹复制进去。
4. 重启 Codex。
5. 如果没有识别，再把同一个文件夹复制到 `.codex/skills/`。

macOS Finder 默认不显示点号开头的隐藏文件夹，可以按：

```text
Command + Shift + .
```

显示隐藏文件。

## 安装到 Claude Code

Claude Code 是 Anthropic 的 agentic coding tool。它可以读代码库、编辑文件、运行命令，也支持 Skills。

打开终端，进入解压后的目录，然后运行：

```bash
mkdir -p "$HOME/.claude/skills"
cp -R major-detective "$HOME/.claude/skills/major-detective"
```

检查是否安装成功：

```bash
ls "$HOME/.claude/skills/major-detective/SKILL.md"
```

如果这是你第一次创建 `~/.claude/skills/`，建议重启 Claude Code。

安装后可以直接调用：

```text
/major-detective 我是山东物化生，家里建议医学/生物相关，我喜欢实验但不想读博，帮我分析专业方向。
```

也可以自然语言触发：

```text
使用大学专业侦探 Skill，帮我分析医学检验技术、药学、卫生检验与检疫怎么选。
```

## 在国产 AI IDE / 编程 Agent 里使用

这些工具不一定支持 Codex/Claude Code 的 Skill 目录格式，但通常可以读取项目文件、理解 Markdown 规则。

可以尝试：

- TRAE: https://www.trae.cn/
- 通义灵码: https://lingma.aliyun.com/
- 腾讯 CodeBuddy: https://www.codebuddy.ai/

通用步骤：

1. 下载并解压本项目。
2. 用 AI IDE 打开 `major-detective-skill-v0.1.0` 整个文件夹。
3. 新建对话，输入：

```text
请先阅读 major-detective/SKILL.md，并按这个 Skill 的规则工作。

我想使用“大学专业侦探”来分析高考专业选择。
如果信息不完整，请先追问；如果信息已经足够，请主动给出交付物菜单，包括：
1. 下一步核验清单
2. 家长沟通版 / 微信短版
3. 专业对比表
4. 院校-专业候选池表格
5. 招办/学长学姐提问清单
6. 可打印 report.md / report.html / report.pdf
```

4. 如果工具不能自动读文件，就打开 `major-detective/SKILL.md`，把内容复制进对话，告诉它“请把这段当作系统规则”。

## 在国产智能体平台里迁移

这些平台更适合做成一个网页智能体，让别人点开就能用：

- 扣子 Coze: https://www.coze.cn/
- 腾讯元器: https://yuanqi.tencent.com/
- 阿里云百炼: https://www.aliyun.com/product/bailian
- 百度文心智能体平台 AgentBuilder: https://agents.baidu.com/
- Dify: https://docs.dify.ai/zh/home

通用步骤：

1. 新建智能体。
2. 名称：`大学专业侦探`。
3. 头像和简介可选。
4. 在“角色设定 / 系统提示词 / Prompt”里粘贴下面的简化系统提示词。
5. 如果平台支持知识库、资料库或文件上传，上传：

```text
major-detective/SKILL.md
major-detective/references/conversation-ux.md
major-detective/references/deliverables.md
major-detective/references/safety-boundaries.md
major-detective/references/school-major-matching.md
major-detective/references/report-schema.md
major-detective/references/majors/biology.md
major-detective/references/majors/psychology.md
major-detective/references/majors/law.md
major-detective/references/majors/computer-science.md
major-detective/references/majors/clinical-medicine.md
```

6. 设置开场白：

```text
我是大学专业侦探。我不会替你填志愿，也不预测录取概率，但可以帮你把一个专业调查清楚：学什么、适合谁、风险在哪、下一步该核验什么。你可以只输入一个专业名，也可以描述你的省份、选科、位次、兴趣和家庭期待。
```

7. 用下面的测试 Prompt 试运行：

```text
我是山东物化生，位次先假设 75000。家里觉得医学/生物相关稳定。我喜欢实验检测，不想临床长周期，也不想读到博士。重点考虑医学检验技术、药学、卫生检验与检疫。帮我分析怎么选。
```

简化系统提示词：

```text
你是“大学专业侦探”，面向中国高考生和家长，帮助用户调查大学专业。

工作目标：
1. 把用户的模糊问题拆成：专业真实学习内容、适合条件、风险点、升学就业路径、替代专业、官方核验步骤。
2. 不替用户填志愿，不预测录取概率，不承诺就业稳定，不编造分数线、位次、计划数、排名、科研经费或网评。
3. 如果信息不完整，先给基础版判断，并追问最多 5 个关键问题，允许用户回答“不确定”。
4. 如果信息已经比较完整，自动给出交付物菜单，不要让用户追问“还能生成什么”。

必须主动提供的交付物菜单：
1. 下一步核验清单
2. 家长沟通版 / 微信短版
3. 专业对比表
4. 院校-专业候选池表格，数据不足时只能标为“待核验搜索种子”
5. 招办/学长学姐提问清单
6. 可打印报告：report.md / report.html / report.pdf（如果当前平台不支持 PDF，就输出 HTML/PDF-ready 内容）

回答风格：
温和、具体、不制造焦虑。优先使用“适配条件 / 风险点 / 核验清单”，避免“千万别报”“一定能上”“毕业就高薪”等绝对表达。
```

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

如果 PDF 生成失败，可以让 Agent 先生成 `report.html`，然后用浏览器打印为 PDF。

## 常见问题

### 1. 为什么安装后没有触发？

请检查：

- 文件夹是不是叫 `major-detective`。
- `SKILL.md` 是否在 `major-detective/SKILL.md`。
- Codex / Claude Code 是否已经重启。
- Codex 可以先试 `$HOME/.agents/skills`，不行再试 `$HOME/.codex/skills`。

### 2. 它会不会替我填志愿？

不会。它只做专业调查、风险提示、核验清单和候选池整理。最终填报必须以官方数据和家庭决策为准。

### 3. 它为什么不给具体录取概率？

因为录取受当年招生计划、位次分布、专业热度、选科要求等影响。没有完整官方数据时，给概率会误导用户。

### 4. 它能联网查数据吗？

取决于你使用的 Agent 环境。如果不能联网，它会给你核验步骤和表格模板，不会编数据。

### 5. 国产平台能不能直接安装这个 ZIP？

多数情况下不能直接“安装”。更现实的方式是迁移：

- 把 `SKILL.md` 当成系统提示词。
- 把 `references/` 里的文件当成知识库资料。
- 把 `scripts/render_pdf_report.py` 当成可选的本地 PDF 生成脚本。

平台能力不同，实际效果会有差异。
