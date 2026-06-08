# 安装教程

下面按“小白版”写。你不需要懂代码，只要会复制文件和重启工具。

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

### 方法一：命令行安装

打开终端，进入解压后的目录，然后运行：

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

### 方法二：手动复制

1. 打开用户主目录。
2. 找到或创建 `.codex/skills/` 文件夹。
3. 把 `major-detective` 整个文件夹复制进去。
4. 重启 Codex。

macOS Finder 默认不显示点号开头的隐藏文件夹，可以按：

```text
Command + Shift + .
```

显示隐藏文件。

## 安装到 Claude Code

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

### 2. 它会不会替我填志愿？

不会。它只做专业调查、风险提示、核验清单和候选池整理。最终填报必须以官方数据和家庭决策为准。

### 3. 它为什么不给具体录取概率？

因为录取受当年招生计划、位次分布、专业热度、选科要求等影响。没有完整官方数据时，给概率会误导用户。

### 4. 它能联网查数据吗？

取决于你使用的 Agent 环境。如果不能联网，它会给你核验步骤和表格模板，不会编数据。
