#!/usr/bin/env python3
"""Export an assembled limitation-of-liability section to DOCX or PDF.

Usage:
    python export.py <input.md> <output.docx|output.pdf>

Input is the plain-text/Markdown section the skill assembled in Step 3,
including its closing note. Supports the Markdown subset the skill actually
produces: #/##/### headings, blank-line-separated paragraphs, "> " clause
quotes, "- " bullets, and **bold** / *italic* inline emphasis. This is a
purpose-built renderer for this skill's own output, not a general Markdown
converter.

DOCX is written directly with python-docx. PDF is produced by writing the
DOCX first, then converting it with LibreOffice (`soffice --headless
--convert-to pdf`), which must be on PATH. If LibreOffice isn't available,
the script writes the DOCX and reports that PDF needs it.
"""
import re
import sys
import os
import subprocess
import tempfile

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

BOLD_ITALIC = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")


def add_runs(paragraph, text):
    """Add text to a paragraph, honoring **bold** and *italic* spans."""
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


def build_docx(md_text, out_path):
    doc = Document()

    style = doc.styles["Normal"]
    style.font.name = "Arial"
    style.font.size = Pt(11)
    for level, size in [("Title", 20), ("Heading 1", 16), ("Heading 2", 13)]:
        s = doc.styles[level]
        s.font.name = "Arial"
        s.font.size = Pt(size)
        s.font.bold = True

    for raw_line in md_text.splitlines():
        line = raw_line.rstrip()

        if not line.strip():
            continue

        if line.startswith("---"):
            continue

        if line.startswith("### "):
            doc.add_heading(line[4:].strip(), level=2)
            continue
        if line.startswith("## "):
            doc.add_heading(line[3:].strip(), level=1)
            continue
        if line.startswith("# "):
            doc.add_heading(line[2:].strip(), level=0)
            continue

        if line.startswith("> "):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            add_runs(p, line[2:].strip())
            continue

        if line.lstrip().startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            add_runs(p, line.lstrip()[2:].strip())
            continue

        p = doc.add_paragraph()
        add_runs(p, line.strip())

    doc.save(out_path)


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


def main():
    if len(sys.argv) != 3:
        print("Usage: python export.py <input.md> <output.docx|output.pdf>", file=sys.stderr)
        sys.exit(2)

    input_path, output_path = sys.argv[1], sys.argv[2]
    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    ext = os.path.splitext(output_path)[1].lower()

    if ext == ".docx":
        build_docx(md_text, output_path)
        print(f"Wrote {output_path}")
    elif ext == ".pdf":
        try:
            with tempfile.TemporaryDirectory() as tmp:
                tmp_docx = os.path.join(tmp, "export.docx")
                build_docx(md_text, tmp_docx)
                convert_to_pdf(tmp_docx, output_path)
        except RuntimeError as e:
            print(str(e), file=sys.stderr)
            sys.exit(1)
        print(f"Wrote {output_path}")
    else:
        print(f"Unsupported output format: {ext}. Use .docx or .pdf.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
