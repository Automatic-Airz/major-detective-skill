#!/usr/bin/env python3
"""Render a Major Detective report package as Markdown and PDF.

This script intentionally uses ReportLab directly instead of relying on a
browser. It is meant as a portable fallback for Codex environments where
Playwright, Pandoc, or wkhtmltopdf are unavailable.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


FONT_CANDIDATES = [
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]


def find_font() -> str:
    for candidate in FONT_CANDIDATES:
        if Path(candidate).exists():
            return candidate
    raise FileNotFoundError(
        "No Chinese-capable font found. Add a TTF/TTC font path to FONT_CANDIDATES."
    )


def register_fonts() -> str:
    font_path = find_font()
    pdfmetrics.registerFont(TTFont("MajorCJK", font_path))
    return "MajorCJK"


def sample_report() -> dict[str, Any]:
    return {
        "title": "大学专业侦探报告：医学检验技术 / 药学 / 卫生检验与检疫",
        "subtitle": "山东物化生，假设位次 75000，学生与家长共同核验版",
        "profile": {
            "省份": "山东",
            "选科": "物理 / 化学 / 生物",
            "位次": "假设 75000，需替换为官方一分一段位次",
            "偏好": "实验、生命健康、检测分析、山东或华东、公办优先",
            "排斥": "临床长周期、强编程、强物理硬件、必须读博路线",
        },
        "disclaimer": "本报告不是官方志愿填报建议，不预测录取概率，不承诺就业稳定。所有院校-专业结论必须以省考试院投档表、当年招生计划、招生章程和学校官网为准。",
        "one_liner": "当前最适合做的不是直接定专业，而是把医学相关方向拆成专业理解、学校核验、家庭沟通和风险确认四件事。",
        "major_table": [
            ["方向", "家长容易理解的说法", "主要风险", "下一步核验"],
            ["医学检验技术", "医院和医学检测背后的检验技术路线", "不等于医生；岗位看学历、证书、实习资源", "实习医院名单、培养方案、就业去向"],
            ["药学", "围绕药品研发、质控、注册、药房和药企岗位", "本科就业分化，研发路线更看重研究生学历", "药学方向、药企/医院去向、考研比例"],
            ["卫生检验与检疫", "公共卫生、食品环境和疾病防控检测", "岗位口径可能较窄，地区差异明显", "疾控/海关/检测机构资源和岗位需求"],
        ],
        "risk_radar": [
            ["风险项", "等级", "说明"],
            ["位次未核验", "高", "75000 是假设位次，必须替换为官方一分一段位次。"],
            ["专业名称误判", "中", "同名或相近专业在不同学校培养方向差异较大。"],
            ["本科就业确定性", "中", "医学技术和药学类路径常受地区、学历、证书影响。"],
            ["网评误导", "中", "网评只能作为问题线索，不能替代官方培养方案和就业报告。"],
        ],
        "verification": [
            "下载山东省教育招生考试院近三年普通类常规批投档表，按专业+学校查看最低位次。",
            "核验 2026 年招生计划、选科要求、体检限制、校区和学费。",
            "查看目标学校招生章程、专业培养方案、就业质量报告或学院毕业去向。",
            "向招办或学院确认实习医院/药企/疾控/检测机构资源是否面向本科生。",
            "把知乎、小红书、贴吧等网评转成问题：实习弱？校区远？考研压力大？逐项求证。",
        ],
        "parent_brief": "爸妈，我不是排斥医学和生命健康方向，而是想把它查得更具体。医学检验技术、药学、卫生检验与检疫都和稳定、实验、健康相关，但学习内容、就业单位、学历要求和岗位数量不一样。我们可以一起核验每个学校的往年位次、培养方案、实习资源和毕业去向，再判断哪些更适合我，而不是只凭“医学/生物听起来稳定”做决定。",
        "next_actions": [
            "生成院校-专业候选池表格，所有学校先标为待核验搜索种子。",
            "生成 300-500 字微信短版家长沟通说明。",
            "生成招办/学长学姐提问清单。",
            "在正式位次公布后，把近三年最低位次填入候选池并重新排序。",
        ],
    }


def para(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(str(text).replace("\n", "<br/>"), style)


def bullet_list(items: list[str], style: ParagraphStyle) -> ListFlowable:
    return ListFlowable(
        [ListItem(para(item, style), leftIndent=6) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=14,
    )


def as_table(rows: list[list[str]], style: ParagraphStyle, col_widths: list[float]) -> Table:
    data = [[para(cell, style) for cell in row] for row in rows]
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E9F2FF")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#153B66")),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B8C3CF")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def build_styles(font_name: str) -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "MajorTitle",
            parent=base["Title"],
            fontName=font_name,
            fontSize=20,
            leading=26,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#17324D"),
            wordWrap="CJK",
        ),
        "subtitle": ParagraphStyle(
            "MajorSubtitle",
            parent=base["Normal"],
            fontName=font_name,
            fontSize=10.5,
            leading=16,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#526170"),
            wordWrap="CJK",
        ),
        "h2": ParagraphStyle(
            "MajorH2",
            parent=base["Heading2"],
            fontName=font_name,
            fontSize=14,
            leading=20,
            spaceBefore=12,
            spaceAfter=7,
            textColor=colors.HexColor("#17324D"),
            wordWrap="CJK",
        ),
        "body": ParagraphStyle(
            "MajorBody",
            parent=base["BodyText"],
            fontName=font_name,
            fontSize=9.5,
            leading=15,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#24313D"),
            wordWrap="CJK",
        ),
        "small": ParagraphStyle(
            "MajorSmall",
            parent=base["BodyText"],
            fontName=font_name,
            fontSize=8.4,
            leading=12,
            textColor=colors.HexColor("#34495E"),
            wordWrap="CJK",
        ),
        "callout": ParagraphStyle(
            "MajorCallout",
            parent=base["BodyText"],
            fontName=font_name,
            fontSize=9.2,
            leading=14,
            backColor=colors.HexColor("#FFF8E6"),
            borderColor=colors.HexColor("#E9C46A"),
            borderWidth=0.6,
            borderPadding=7,
            textColor=colors.HexColor("#3D3522"),
            wordWrap="CJK",
        ),
    }


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("MajorCJK", 8)
    canvas.setFillColor(colors.HexColor("#667789"))
    canvas.drawCentredString(A4[0] / 2, 12 * mm, f"第 {doc.page} 页")
    canvas.restoreState()


def render_pdf(report: dict[str, Any], pdf_path: Path) -> None:
    font_name = register_fonts()
    styles = build_styles(font_name)
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=15 * mm,
        bottomMargin=18 * mm,
        title=report["title"],
    )

    story: list[Any] = []
    story.append(para(report["title"], styles["title"]))
    story.append(para(report["subtitle"], styles["subtitle"]))
    story.append(Spacer(1, 8))
    story.append(para(report["disclaimer"], styles["callout"]))

    story.append(para("用户画像", styles["h2"]))
    profile_rows = [["字段", "内容"]] + [[key, value] for key, value in report["profile"].items()]
    story.append(as_table(profile_rows, styles["small"], [34 * mm, 128 * mm]))

    story.append(para("一句话判断", styles["h2"]))
    story.append(para(report["one_liner"], styles["body"]))

    story.append(para("三专业对比", styles["h2"]))
    story.append(as_table(report["major_table"], styles["small"], [26 * mm, 48 * mm, 45 * mm, 43 * mm]))

    story.append(para("风险雷达", styles["h2"]))
    story.append(as_table(report["risk_radar"], styles["small"], [38 * mm, 22 * mm, 102 * mm]))

    story.append(PageBreak())
    story.append(para("官方核验清单", styles["h2"]))
    story.append(bullet_list(report["verification"], styles["body"]))

    story.append(para("家长沟通版", styles["h2"]))
    story.append(para(report["parent_brief"], styles["body"]))

    story.append(para("下一步行动", styles["h2"]))
    story.append(bullet_list(report["next_actions"], styles["body"]))

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


def render_markdown(report: dict[str, Any], md_path: Path) -> None:
    lines = [
        f"# {report['title']}",
        "",
        report["subtitle"],
        "",
        f"> {report['disclaimer']}",
        "",
        "## 用户画像",
        "",
    ]
    for key, value in report["profile"].items():
        lines.append(f"- **{key}**：{value}")
    lines.extend(["", "## 一句话判断", "", report["one_liner"], ""])

    lines.extend(["## 三专业对比", ""])
    for row in report["major_table"]:
        lines.append("| " + " | ".join(row) + " |")
        if row == report["major_table"][0]:
            lines.append("|" + "|".join(["---"] * len(row)) + "|")
    lines.extend(["", "## 风险雷达", ""])
    for row in report["risk_radar"]:
        lines.append("| " + " | ".join(row) + " |")
        if row == report["risk_radar"][0]:
            lines.append("|" + "|".join(["---"] * len(row)) + "|")
    lines.extend(["", "## 官方核验清单", ""])
    for item in report["verification"]:
        lines.append(f"- {item}")
    lines.extend(["", "## 家长沟通版", "", report["parent_brief"], "", "## 下一步行动", ""])
    for item in report["next_actions"]:
        lines.append(f"- {item}")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-json", type=Path, help="Optional JSON report data.")
    parser.add_argument("--output-dir", type=Path, default=Path("output/pdf-demo"))
    args = parser.parse_args()

    if args.input_json:
        report = json.loads(args.input_json.read_text(encoding="utf-8"))
    else:
        report = sample_report()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    md_path = args.output_dir / "report.md"
    pdf_path = args.output_dir / "report.pdf"
    render_markdown(report, md_path)
    render_pdf(report, pdf_path)
    print(f"Wrote {md_path}")
    print(f"Wrote {pdf_path}")


if __name__ == "__main__":
    main()
