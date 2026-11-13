#!/usr/bin/env python3
"""Export an assembled limitation-of-liability section to DOCX, PDF or PPTX,
on a minimalistic HHL-branded template.

Usage:
    python export.py <input.md> <output.docx|output.pdf|output.pptx>

Input is the plain-text/Markdown section the skill assembled in Step 3,
including its closing note. Supports the Markdown subset the skill actually
produces: #/##/### headings, blank-line-separated paragraphs, "> " clause
quotes, "- " bullets, and **bold** / *italic* inline emphasis. This is a
purpose-built renderer for this skill's own output, not a general Markdown
converter.

DOCX and PPTX are written directly (python-docx / python-pptx), with the
HHL logo bundled at assets/hhl_logo.png (long logo, black/yellow, light
background) so the export works standalone, without depending on the
hhl-branding skill being installed. PDF is produced by writing the DOCX
first, then converting it with LibreOffice (`soffice --headless
--convert-to pdf`), which must be on PATH; if it isn't, the script reports
that plainly rather than crashing or silently falling back.

Branding is deliberately minimal: HHL yellow (#FAAA00) as a single accent
(a rule under the title, a thin frame on slides), black text, Verdana (the
official Office-theme fallback font — safe on a machine without the
corporate Gotham font installed).
"""
import re
import sys
import os
import subprocess
import tempfile

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
LOGO_PATH = os.path.join(ASSETS_DIR, "hhl_logo.png")
LOGO_ASPECT = 2400 / 395  # width / height of the bundled long logo

HHL_YELLOW = "FAAA00"
HHL_BLACK = "000000"
FONT = "Verdana"

BOLD_ITALIC = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")


# --------------------------------------------------------------- Markdown parsing

def parse_blocks(md_text):
    """Turn the skill's Markdown subset into a flat list of typed blocks:
    {"type": "h1"|"h2"|"h3"|"para"|"quote"|"bullet", "text": str}."""
    blocks = []
    for raw_line in md_text.splitlines():
        line = raw_line.rstrip()
        if not line.strip() or line.startswith("---"):
            continue
        if line.startswith("### "):
            blocks.append({"type": "h3", "text": line[4:].strip()})
        elif line.startswith("## "):
            blocks.append({"type": "h2", "text": line[3:].strip()})
        elif line.startswith("# "):
            blocks.append({"type": "h1", "text": line[2:].strip()})
        elif line.startswith("> "):
            blocks.append({"type": "quote", "text": line[2:].strip()})
        elif line.lstrip().startswith("- "):
            blocks.append({"type": "bullet", "text": line.lstrip()[2:].strip()})
        else:
            blocks.append({"type": "para", "text": line.strip()})
    return blocks


# --------------------------------------------------------------- DOCX

def _docx_add_runs(paragraph, text):
    for part in BOLD_ITALIC.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("*") and part.endswith("*"):
            run = paragraph.add_run(part[1:-1])
            run.italic = True
        else:
            paragraph.add_run(part)


def build_docx(blocks, out_path):
    from docx import Document
    from docx.shared import Pt, Inches, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    doc = Document()

    # Page geometry — python-docx's built-in default (1in/2.54cm margins, a
    # 0.5in header distance) reads as cramped once a logo sits in the header
    # and crowded next to the yellow rule. Use clean, consistent HHL
    # Working-Paper-style margins instead.
    section = doc.sections[0]
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
    section.header_distance = Cm(1.25)
    section.footer_distance = Cm(1.25)

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(10)
    normal.font.color.rgb = RGBColor.from_string(HHL_BLACK)
    normal.paragraph_format.space_after = Pt(8)
    normal.paragraph_format.line_spacing = 1.15

    heading_specs = {"Title": (20, 4, 12), "Heading 1": (15, 18, 6), "Heading 2": (12, 12, 4)}
    for level, (size, before, after) in heading_specs.items():
        s = doc.styles[level]
        s.font.name = FONT
        s.font.size = Pt(size)
        s.font.bold = True
        s.font.color.rgb = RGBColor.from_string(HHL_BLACK)
        s.paragraph_format.space_before = Pt(before)
        s.paragraph_format.space_after = Pt(after)

    if os.path.exists(LOGO_PATH):
        header_par = doc.sections[0].header.paragraphs[0]
        header_par.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        header_par.paragraph_format.space_after = Pt(0)
        run = header_par.add_run()
        width_cm = 4.0
        run.add_picture(LOGO_PATH, width=Cm(width_cm), height=Cm(width_cm / LOGO_ASPECT))

    # Thin yellow rule under the title block (signature HHL element)
    rule_par = doc.add_paragraph()
    rule_par.paragraph_format.space_after = Pt(14)
    pPr = rule_par._p.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "18")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), HHL_YELLOW)
    borders.append(bottom)
    pPr.append(borders)

    for b in blocks:
        if b["type"] == "h1":
            doc.add_heading(b["text"], level=1)
        elif b["type"] == "h2":
            doc.add_heading(b["text"], level=1)
        elif b["type"] == "h3":
            doc.add_heading(b["text"], level=2)
        elif b["type"] == "quote":
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1.0)
            p.paragraph_format.right_indent = Cm(1.0)
            p.paragraph_format.space_after = Pt(10)
            _docx_add_runs(p, b["text"])
        elif b["type"] == "bullet":
            p = doc.add_paragraph(style="List Bullet")
            _docx_add_runs(p, b["text"])
        else:
            p = doc.add_paragraph()
            _docx_add_runs(p, b["text"])

    doc.save(out_path)


# --------------------------------------------------------------- PPTX

def _pptx_frame(slide, prs):
    from pptx.util import Inches
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.dml.color import RGBColor
    w = Inches(0.08)
    sw, sh = prs.slide_width, prs.slide_height
    for left, top, width, height in [(0, 0, sw, w), (0, sh - w, sw, w),
                                      (0, 0, w, sh), (sw - w, 0, w, sh)]:
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        bar.fill.solid()
        bar.fill.fore_color.rgb = RGBColor.from_string(HHL_YELLOW)
        bar.line.fill.background()
        bar.shadow.inherit = False


def _pptx_style(text_frame, size_pt):
    """Apply brand font/size/color to every run, without touching bold/italic
    flags a caller may already have set per-run."""
    from pptx.util import Pt
    from pptx.dml.color import RGBColor
    for para in text_frame.paragraphs:
        for run in para.runs:
            run.font.name = FONT
            run.font.size = Pt(size_pt)
            run.font.color.rgb = RGBColor.from_string(HHL_BLACK)


def _pptx_add_runs(paragraph, text):
    """Add text to a paragraph, honoring **bold** and *italic* spans."""
    for part in BOLD_ITALIC.split(text):
        if not part:
            continue
        run = paragraph.add_run()
        if part.startswith("**") and part.endswith("**"):
            run.text = part[2:-2]
            run.font.bold = True
        elif part.startswith("*") and part.endswith("*"):
            run.text = part[1:-1]
            run.font.italic = True
        else:
            run.text = part


def _pptx_add_body_line(tf, text, size_pt=14, first=False, bold=False):
    para = tf.paragraphs[0] if first else tf.add_paragraph()
    _pptx_add_runs(para, text)
    _pptx_style(tf, size_pt)
    if bold:
        for run in para.runs:
            run.font.bold = True
    return para


def build_pptx(blocks, out_path, title=None, subtitle=""):
    from pptx import Presentation
    from pptx.util import Inches

    # The skill's own output has exactly one h1/h2 at the top (the overall
    # section title) and then one h3 per sub-clause (10.1 Scope, 10.2
    # Periods, ...). Pull that first heading out as the document title, and
    # split the remaining slides on h3, not h2, so a slide holds one
    # sub-clause rather than the whole section.
    doc_title = title
    seen_doc_title = False
    sections = []
    current = None
    for b in blocks:
        if not seen_doc_title and b["type"] in ("h1", "h2"):
            seen_doc_title = True
            if doc_title is None:
                doc_title = b["text"]
            continue
        if b["type"] in ("h1", "h2", "h3"):
            if current is not None:
                sections.append(current)
            current = {"title": b["text"], "body": []}
        else:
            if current is None:
                current = {"title": doc_title or "Clause", "body": []}
            prefix = "- " if b["type"] == "bullet" else ""
            current["body"].append(prefix + b["text"])
    if current is not None:
        sections.append(current)
    if not sections:
        sections = [{"title": doc_title or "Clause", "body": []}]
    doc_title = doc_title or "Limitation of Liability"

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    def new_slide():
        slide = prs.slides.add_slide(blank)
        _pptx_frame(slide, prs)
        if os.path.exists(LOGO_PATH):
            w = Inches(1.6)
            slide.shapes.add_picture(
                LOGO_PATH, prs.slide_width - w - Inches(0.35), Inches(0.3),
                width=w, height=Inches(1.6 / LOGO_ASPECT))
        return slide

    # Title slide
    slide = new_slide()
    box = slide.shapes.add_textbox(Inches(0.6), Inches(2.6), Inches(9.5), Inches(2.0))
    tf = box.text_frame
    tf.word_wrap = True
    _pptx_add_body_line(tf, doc_title, size_pt=32, first=True, bold=True)
    if subtitle:
        _pptx_add_body_line(tf, subtitle, size_pt=16)

    for sec in sections:
        slide = new_slide()
        title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.5), Inches(10.5), Inches(0.9))
        ttf = title_box.text_frame
        _pptx_add_body_line(ttf, sec["title"], size_pt=22, first=True, bold=True)

        body_box = slide.shapes.add_textbox(Inches(0.6), Inches(1.5), Inches(11.8), Inches(5.5))
        btf = body_box.text_frame
        btf.word_wrap = True
        lines = sec["body"] or [""]
        for i, line in enumerate(lines):
            _pptx_add_body_line(btf, line, size_pt=13, first=(i == 0))

    prs.save(out_path)


# --------------------------------------------------------------- PDF (via DOCX)

def convert_to_pdf(docx_path, pdf_path):
    out_dir = os.path.dirname(os.path.abspath(pdf_path)) or "."
    try:
        result = subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", "--outdir", out_dir, docx_path],
            capture_output=True, text=True, timeout=60,
        )
    except FileNotFoundError:
        raise RuntimeError(
            "PDF export needs LibreOffice ('soffice'), which isn't installed or isn't "
            "on PATH in this environment. Export as .docx instead, or install LibreOffice."
        )
    if result.returncode != 0:
        raise RuntimeError(
            "LibreOffice (soffice) conversion failed.\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )
    produced = os.path.join(
        out_dir, os.path.splitext(os.path.basename(docx_path))[0] + ".pdf"
    )
    if produced != pdf_path:
        os.replace(produced, pdf_path)


# --------------------------------------------------------------- CLI

def main():
    if len(sys.argv) != 3:
        print("Usage: python export.py <input.md> <output.docx|output.pdf|output.pptx>",
              file=sys.stderr)
        sys.exit(2)

    input_path, output_path = sys.argv[1], sys.argv[2]
    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()
    blocks = parse_blocks(md_text)

    ext = os.path.splitext(output_path)[1].lower()

    if ext == ".docx":
        build_docx(blocks, output_path)
        print(f"Wrote {output_path}")
    elif ext == ".pptx":
        build_pptx(blocks, output_path)
        print(f"Wrote {output_path}")
    elif ext == ".pdf":
        try:
            with tempfile.TemporaryDirectory() as tmp:
                tmp_docx = os.path.join(tmp, "export.docx")
                build_docx(blocks, tmp_docx)
                convert_to_pdf(tmp_docx, output_path)
        except RuntimeError as e:
            print(str(e), file=sys.stderr)
            sys.exit(1)
        print(f"Wrote {output_path}")
    else:
        print(f"Unsupported output format: {ext}. Use .docx, .pdf or .pptx.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
