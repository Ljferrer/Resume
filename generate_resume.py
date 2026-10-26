"""Build the current resume. Requires ReportLab; fonts ship with ReportLab."""

from pathlib import Path
from shutil import copyfile

import reportlab
from reportlab.graphics import renderPDF
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output/pdf/LukasJoseFerrer_Resume_October2026.pdf"
WAR = "https://github.com/Ljferrer/WorkAuditRefine"
DEMO = "https://youtu.be/6LXrfWtKSlg?si=guy4gEUdLSzJRNSj"
LINKEDIN = "https://www.linkedin.com/in/lukasferrer/"
INK = HexColor("#192B35")
MUTED = HexColor("#52626B")
ACCENT = HexColor("#14645D")
PALE = HexColor("#F0F6F4")
RULE = HexColor("#CDDBD7")
LEFT, WIDTH = 42, 528

font_dir = Path(reportlab.__file__).parent / "fonts"
for name, filename in [("Vera", "Vera.ttf"), ("Vera-Bold", "VeraBd.ttf"),
                       ("Vera-Italic", "VeraIt.ttf")]:
    pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
pdfmetrics.registerFontFamily("Vera", normal="Vera", bold="Vera-Bold", italic="Vera-Italic")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
c = Canvas(str(OUTPUT), pagesize=(612, 792), pageCompression=1)
c.setTitle("Lukas José Ferrer | ML & AI Systems Engineer | October 2026")
c.setAuthor("Lukas José Ferrer")
c.setSubject("Production AI, self-hosted inference, and WAR agent orchestration")


def paragraph(text, y, x=LEFT, width=WIDTH, size=10, leading=14, color=INK, bold=False):
    style = ParagraphStyle("text", fontName="Vera-Bold" if bold else "Vera",
                           fontSize=size, leading=leading, textColor=color,
                           spaceBefore=0, spaceAfter=0, allowWidows=0, allowOrphans=0)
    p = Paragraph(text, style)
    _, height = p.wrap(width, 792)
    if y - height < 43:
        raise ValueError(f"Content overflows page {c.getPageNumber()}: {text[:70]}")
    p.drawOn(c, x, y - height)
    return y - height


def bullet(text, y, size=9.7, leading=13.6, gap=5, x=LEFT, width=WIDTH):
    c.setFillColor(ACCENT)
    c.circle(x + 2, y - 6.6, 1.5, stroke=0, fill=1)
    return paragraph(text, y, x=x + 12, width=width - 12, size=size, leading=leading) - gap


def section(title, y):
    bottom = paragraph(title.upper(), y, size=9.2, leading=12, color=ACCENT, bold=True)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.6)
    c.line(LEFT, bottom - 6, LEFT + WIDTH, bottom - 6)
    return bottom - 19


def role(title, company, dates, y):
    y = paragraph(f"<b>{title}</b> | {company}", y, size=11, leading=15)
    return paragraph(dates, y - 3, size=8.7, leading=12, color=MUTED) - 9


def qr(url, label, x, y, size=64):
    widget = QrCodeWidget(url, barLevel="M", barBorder=4, barFillColor=black)
    bounds = widget.getBounds()
    scale = size / (bounds[2] - bounds[0])
    drawing = Drawing(size, size, transform=[scale, 0, 0, scale, 0, 0])
    drawing.add(widget)
    c.setFillColor(white)
    c.rect(x, y, size, size, stroke=0, fill=1)
    renderPDF.draw(drawing, c, x, y)
    c.linkURL(url, (x, y - 14, x + size, y + size), relative=0, thickness=0)
    c.setFont("Vera-Bold", 7)
    c.setFillColor(ACCENT)
    c.drawCentredString(x + size / 2, y - 10, label)


def footer(page):
    c.setStrokeColor(RULE)
    c.line(LEFT, 34, LEFT + WIDTH, 34)
    c.setFillColor(MUTED)
    c.setFont("Vera", 7.4)
    c.drawString(LEFT, 22, "Lukas José Ferrer  |  October 2026")
    c.drawRightString(LEFT + WIDTH, 22, f"{page} / 2")


# Page 1: portfolio and recent production engineering.
paragraph("Lukas José Ferrer", 753, size=26, leading=32, bold=True, width=450)
paragraph("ML &amp; AI SYSTEMS ENGINEER", 715, size=10.3, leading=14, color=ACCENT, bold=True)
paragraph('<link href="mailto:lukasjferrer@gmail.com">lukasjferrer@gmail.com</link>'
          '  |  310.801.8751  |  Los Angeles, CA', 694, size=8.7, leading=12, width=450)
paragraph(f'<link href="{LINKEDIN}" color="#14645D">linkedin.com/in/lukasferrer</link>'
          '  |  <link href="https://github.com/Ljferrer" color="#14645D">github.com/Ljferrer</link>',
          677, size=8.5, leading=12, width=450)
qr(LINKEDIN, "LinkedIn", 506, 687, size=64)

y = paragraph("ML engineer building clinical AI, self-hosted inference, and developer tools. "
              "Shipped systems processing <b>100M+ medical-record pages</b>; creator of WAR, "
              "an open-source platform for parallel AI coding with independent review and verified integration.",
              647, size=10, leading=14)

card_top = y - 15
card_bottom = card_top - 167
c.setFillColor(PALE)
c.roundRect(LEFT, card_bottom, WIDTH, 167, 5, stroke=0, fill=1)
paragraph("FEATURED OPEN SOURCE", card_top - 12, x=54, width=350,
          size=8, leading=11, color=ACCENT, bold=True)
paragraph(f'<link href="{WAR}"><b>WAR</b> | Work Audit Refine</link>',
          card_top - 30, x=54, width=350, size=15, leading=20)
paragraph("Creator &amp; Maintainer  |  June 2026 - Present", card_top - 54,
          x=54, width=350, size=8.3, leading=12, color=MUTED)
wy = bullet("Built a Claude Code plugin that schedules task DAGs, runs parallel agents in isolated "
            "Git worktrees, and integrates approved changes through a serial merge queue.",
            card_top - 76, x=54, width=350, size=9, leading=12.3, gap=5)
wy = bullet("Designed commit-pinned reviews by 1-5 independent auditors, severity-based blocking, "
            "and test/lint gates; added SQLite FTS5 memory and Git-based crash recovery.",
            wy, x=54, width=350, size=9, leading=12.3, gap=0)
if wy < card_bottom + 8:
    raise ValueError("WAR feature overflows its panel")
qr(WAR, "Explore WAR", 416, card_bottom + 54, size=65)
qr(DEMO, "Watch demo", 493, card_bottom + 54, size=65)

y = section("Experience", card_bottom - 19)
y = role("Lead ML & DevOps Engineer", "Sequoia Port Inc.",
         "Mar 2021 - Present  |  Remote / Los Angeles, CA", y)
for text in [
    "<b>Led the migration of medical-record Activation to self-hosted Qwen 3.6 (27B), "
    "bringing measured AI pipeline cost below $0.01/page</b>: $0.009628 across 110.1K page "
    "activations (Oct 21-26, 2026; excluding chat costs).",
    "Built asynchronous LLM routing across detection, transcription, extraction, classification, "
    "and summarization using Step Functions, SQS/SNS, and DynamoDB, with durable recovery, "
    "validated outputs, and controlled fallback to paid APIs.",
    "Moved seven page and summary compute steps to ECS Fargate and ARM64; added Spot capacity "
    "with on-demand recovery for bulk page processing.",
    "Operationalized hybrid GPU inference using local ECS Anywhere workers and queue-driven "
    "cloud fallback, with Spot/on-demand capacity that scales to zero when idle.",
    "Shipped a Python-native clinical record-summary pipeline with pgvector retrieval, parallel "
    "extraction, shadow comparisons, transactional persistence, and runtime fallback.",
    "Built biomedical translation evaluations and extended extraction/deduplication benchmarks "
    "with degraded scans, clinical-error reports, and paired, blinded model comparisons.",
    "Protected physician edits during reprocessing through database-authoritative record "
    "reconciliation and idempotent persistence.",
]:
    y = bullet(text, y)
footer(1)
c.showPage()

# Page 2: established impact, earlier roles, and technical breadth.
paragraph("Lukas José Ferrer", 750, size=16, leading=21, bold=True)
paragraph("Production AI  /  ML infrastructure  /  Agent orchestration", 724,
          size=9, leading=13, color=MUTED)
y = section("Experience continued", 706)
y = paragraph("<b>Sequoia Port Inc.</b> | Selected earlier impact", y, size=10.3, leading=14) - 9
for text in [
    "Architected a fault-tolerant medical-record NLP pipeline serving Fortune 100 healthcare "
    "customers: <b>100M+ pages processed</b> and <b>5M+ pages/month on 2-4 GPUs</b>.",
    "Built clinical AI products that reduced insurance claim review time by <b>65%</b> and "
    "specialist escalations by <b>40%</b>; automated segmentation of 1,000+ page cases for "
    "physician review in under an hour.",
    "Improved clinical retrieval from <b>87% to 95% Recall@5</b> using a domain ontology and "
    "graph database; built multi-stage case summaries with citation validation and PHI anonymization.",
]:
    y = bullet(text, y)

y = role("Red Team (Contract)", "OpenAI", "Jan 2024 - Jun 2024  |  Remote", y - 7)
y = bullet("Red-teamed GPT-4o for calibrated uncertainty in clinical contexts. Designed synthetic-condition "
           "evaluations that exposed plausible but nonexistent ICD-10 codes and tested ontology-grounded retrieval.", y)

y = role("Regulatory Software Engineer", "Neuralink", "Oct 2020 - Jan 2021  |  Fremont, CA", y - 7)
y = bullet("Supported FDA regulatory preparation for a Class III implantable brain-computer interface; "
           "assessed design-control gaps and proposed remediation aligned with medical-device requirements.", y)

y = role("Research Programmer", "USC Information Sciences Institute",
         "May 2018 - Oct 2020  |  Marina del Rey, CA", y - 7)
for text in [
    "Integrated research Transformer architectures into a neural machine translation training library; "
    "trained thousands of models and improved translation quality across low-resource languages.",
    "Built an ETL pipeline ingesting <b>100,000+ news articles/day</b> for the SAGE geopolitical "
    "forecasting platform, improving relevant-document retrieval by <b>73% (Recall@5)</b>.",
]:
    y = bullet(text, y)

y = section("Technical skills", y - 12)
for text in [
    "<b>AI &amp; ML:</b> PyTorch, Transformers, multimodal models, LoRA, distillation, Qwen, "
    "Anthropic/OpenAI APIs, RAG, pgvector, FAISS, evaluation, citation validation.",
    "<b>Infrastructure:</b> AWS CDK, Lambda, Step Functions, ECS/Fargate, ECS Anywhere, EC2, "
    "SQS/SNS, S3, DynamoDB, PostgreSQL, Docker, Linux, GPU serving, CI/CD.",
    "<b>Development:</b> Python, TypeScript/JavaScript, SQL, Bash, React, Ruby on Rails, "
    "Claude Code, MCP, multi-agent orchestration, Git worktrees, SQLite FTS5.",
    "<b>Domain:</b> Clinical document processing, PHI protection, HIPAA-oriented pipelines, "
    "differential privacy (PATE), medical-device regulatory workflows.",
]:
    y = paragraph(text, y, size=9.1, leading=12.3) - 4

y = section("Education", y - 11)
y = paragraph("<b>M.S. Biomedical Engineering</b> | USC Viterbi School of Engineering | Aug 2017",
              y, size=9.3, leading=13)
y = paragraph("<b>B.S. Biomedical Engineering</b> | USC Viterbi School of Engineering | May 2016",
              y - 5, size=9.3, leading=13)
footer(2)
c.save()
copyfile(OUTPUT, ROOT / "LukasFerrer_Resume.pdf")
print(OUTPUT)
