#!/usr/bin/env python3
"""Build aaryan-samanta-resume.pdf from the same verified facts as index.html.

    pip install -r tools/requirements.txt
    python3 tools/build_resume.py

The PDF is written to the repository root (same filename, so old links keep working).
Fonts are the site's own Newsreader and Hanken Grotesk, instantiated from the
variable woff2 files in assets/fonts/. No phone number, no reference contact
details: keep it that way.

Content rule: only completed results are stated as results. Update this file
and index.html together, then bump the dates (see docs/CONTENT-GUIDE.md).
"""
import os
import sys
import tempfile

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont as RLFont
from reportlab.platypus import (BaseDocTemplate, Frame, HRFlowable, KeepTogether,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts")
OUT = os.path.join(ROOT, "aaryan-samanta-resume.pdf")

INK, MUTED, SIGNAL, RULE = HexColor("#101b33"), HexColor("#46516b"), HexColor("#2545e6"), HexColor("#c9cfdb")

# ---------------------------------------------------------------- fonts
def make_fonts(tmp):
    def inst(src, axes, name):
        f = TTFont(os.path.join(FONTS, src))
        tags = {a.axisTag for a in f["fvar"].axes}
        g = instancer.instantiateVariableFont(f, {k: v for k, v in axes.items() if k in tags})
        g.flavor = None
        # reportlab de-duplicates embedded fonts by PostScript name, so every instance needs a unique one.
        for nid, val in ((1, name), (4, name), (6, name.replace(" ", ""))):
            g["name"].setName(val, nid, 3, 1, 0x409)
            g["name"].setName(val, nid, 1, 0, 0)
        path = os.path.join(tmp, name + ".ttf")
        g.save(path)
        pdfmetrics.registerFont(RLFont(name, path))

    inst("newsreader-latin-normal.woff2", {"wght": 400, "opsz": 10}, "News")
    inst("newsreader-latin-normal.woff2", {"wght": 620, "opsz": 10}, "News-Semi")
    inst("newsreader-latin-italic.woff2", {"wght": 400, "opsz": 10}, "News-Italic")
    inst("newsreader-latin-normal.woff2", {"wght": 380, "opsz": 60}, "News-Display")
    inst("hanken-grotesk-latin.woff2", {"wght": 400}, "Hank")
    inst("hanken-grotesk-latin.woff2", {"wght": 600}, "Hank-Semi")
    inst("hanken-grotesk-latin.woff2", {"wght": 700}, "Hank-Bold")
    pdfmetrics.registerFontFamily("News", normal="News", bold="News-Semi", italic="News-Italic", boldItalic="News-Semi")
    pdfmetrics.registerFontFamily("Hank", normal="Hank", bold="Hank-Bold", italic="Hank", boldItalic="Hank-Bold")


# ---------------------------------------------------------------- styles
def styles():
    base = dict(textColor=INK, alignment=TA_LEFT)
    return {
        "name": ParagraphStyle("name", fontName="News-Display", fontSize=27, leading=30, **base),
        "contact": ParagraphStyle("contact", fontName="Hank", fontSize=8.6, leading=12, textColor=MUTED),
        "h": ParagraphStyle("h", fontName="Hank-Bold", fontSize=9.4, leading=12, spaceBefore=10, spaceAfter=2, **base),
        "body": ParagraphStyle("body", fontName="News", fontSize=9.7, leading=12.4, **base),
        "title": ParagraphStyle("title", fontName="News-Semi", fontSize=10.2, leading=12.6, **base),
        "meta": ParagraphStyle("meta", fontName="Hank", fontSize=8.3, leading=11, textColor=MUTED),
        "date": ParagraphStyle("date", fontName="Hank", fontSize=8.3, leading=12.6, textColor=MUTED, alignment=2),
        "bullet": ParagraphStyle("bullet", fontName="News", fontSize=9.7, leading=12.4, leftIndent=10, bulletIndent=0, **base),
    }


S = None
W = letter[0] - 1.3 * inch  # text width


def link(text, url):
    return f'<a href="{url}" color="#2545e6">{text}</a>'


def heading(text):
    return [Paragraph(text, S["h"]), HRFlowable(width="100%", thickness=0.8, color=INK, spaceAfter=4)]


def entry(title, date="", meta="", body=None):
    """One resume entry: bold title + right-aligned date, optional meta line and body."""
    head = Table([[Paragraph(title, S["title"]), Paragraph(date, S["date"])]], colWidths=[W - 1.5 * inch, 1.5 * inch])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    parts = [head]
    if meta:
        parts.append(Paragraph(meta, S["meta"]))
    if body:
        parts.append(Paragraph(body, S["body"]))
    parts.append(Spacer(1, 5))
    return KeepTogether(parts)


def line(label, text):
    return Paragraph(f'<font name="Hank-Bold" size="8.6">{label}</font>&nbsp;&nbsp;{text}', S["body"])


# ---------------------------------------------------------------- content
def build_story():
    st = []
    st.append(Paragraph("Aaryan Samanta", S["name"]))
    st.append(Spacer(1, 3))
    st.append(Paragraph(
        "Cupertino, CA &nbsp;|&nbsp; " + link("aaryan.samanta@gmail.com", "mailto:aaryan.samanta@gmail.com")
        + " &nbsp;|&nbsp; " + link("aaryansamanta.github.io", "https://aaryansamanta.github.io/")
        + " &nbsp;|&nbsp; " + link("github.com/aaryansamanta", "https://github.com/aaryansamanta"), S["contact"]))
    st.append(Paragraph(
        link("Google Scholar", "https://scholar.google.com/citations?user=TboJyScAAAAJ") + " &nbsp;|&nbsp; "
        + link("ORCID 0009-0005-6381-4890", "https://orcid.org/0009-0005-6381-4890") + " &nbsp;|&nbsp; "
        + link("aiethos.org", "https://www.aiethos.org") + " &nbsp;|&nbsp; "
        + link("nextgenai.org", "https://www.nextgenai.org"), S["contact"]))
    st.append(Spacer(1, 6))
    st.append(Paragraph(
        "High school researcher applying machine learning to biology and medicine. First author of two peer-reviewed "
        "papers, USACO Platinum, and founder of AI Ethos, Inc., a 501(c)(3) that has reached more than 1,500 students "
        "with AI tutoring.", S["body"]))

    # ---- Education
    st += heading("Education")
    st.append(entry("Legend College Preparatory, Cupertino, CA", "Class of 2028",
                    "GPA 4.8 weighted, 4.0 unweighted. SAT 1570 (800 Math). AP Scholar with Distinction: 9 exams, 4.77 average score.",
                    "NSHSS National Scholar. College Board National Recognition Program, Outstanding Academic Achievement. "
                    "Advanced AI sequence capstones: CNN pneumonia detector, symptom and disease pattern analysis, diabetes-risk "
                    "model comparison (" + link("code", "https://github.com/aaryansamanta/advanced-ai-curriculum") + ")."))

    # ---- Research
    st += heading("Research and publications")
    st.append(entry("First author, IEEE AIAM 2025", "2025",
                    "Quantum-Inspired Hybrid Genetic Algorithm and Graph Neural Network Ensemble for Multimodal Classification. "
                    + link("IEEE Xplore", "https://ieeexplore.ieee.org/abstract/document/11322272"),
                    "Quantum-inspired genetic algorithm fused with a graph neural network, explained with SHAP. F1 0.57 vs 0.55 (Random Forest) and 0.52 (SVM)."))
    st.append(entry("First author, International Journal of High School Research", "2026",
                    "Natural Genetic Variation in Mitochondrial Health-Regulating Genes in the <i>C. elegans</i> Strains CX11314 and EG4725 "
                    "Leads to Increased Mitochondrial Resilience. " + link("doi:10.36838/IJHSR816.1", "https://doi.org/10.36838/IJHSR816.1"),
                    "UC Santa Barbara Summer Research Academy capstone (youngest accepted scholar). 540 isotypes, 609 RNA-seq samples, "
                    "six mitochondrial quality-control genes; expression predictor Spearman 0.959."))
    st.append(entry("Research Scholar, Stanford Medicine, Department of Urology", "Jan 2026 to present",
                    "Mentor: Christos E. Constantinou, Associate Professor of Urology, Emeritus",
                    "Analyze anonymized pelvic-floor ultrasound from 23 subjects; extract displacement, velocity and acceleration during "
                    "voluntary contraction, Valsalva and cough. Preliminary findings; not yet published."))
    st.append(entry("Student Researcher, MIT EECS (mentored)", "2026 to present", None,
                    "Weekly research with an MIT computer science professor applying machine learning to computational linguistics."))
    st.append(entry("Researcher, UCLA COSMOS, Cluster 1: Brain-Inspired Computing", "Summer 2026", None,
                    "InfernoCommand: actor-critic, fire-relative reinforcement learning for wildfire response on a real Los Angeles terrain model. "
                    "Over training, mean reward rose 52% and buildings lost fell 54%. Manuscript submitted. "
                    + link("Code", "https://github.com/aaryansamanta/ai-research-publications/tree/main/ucla-cosmos-2026-c1-infernotactics") + "."))
    st.append(entry("Manuscripts under review and in progress", "2026", None,
                    "<b>Under review:</b> MS-TAGNet, a joint STFT-CWT multi-scale fusion framework for EEG semantic decoding under noisy conditions. "
                    "<b>In progress (not yet accepted):</b> QIWGA-GAT for five-year tumor recurrence prediction, targeting IET Computer Vision; "
                    "a study of how simplified biology diagrams create misconceptions, targeting <i>CBE-Life Sciences Education</i>."))

    # ---- Competitions
    st += heading("Competitions")
    st.append(line("USACO", "Platinum division (2026). Perfect 1000 in Bronze, Silver and Gold, ranked first among 5,137, 2,721 and 1,336 participants. "
                            "2025 US Open: perfect 1000 in Gold and Silver, one of eight students in the U.S."))
    st.append(Spacer(1, 2))
    st.append(line("AMC / AIME", "National 1st place with perfect 150 scores: AMC 8 and 10 (2025); AMC 10 and 12 (2026). AIME qualifier in both years."))
    st.append(Spacer(1, 2))
    st.append(line("USAPhO", "Gold medalist (2026). Second-highest F=ma score in the U.S. (24 of 25)."))
    st.append(Spacer(1, 2))
    st.append(line("USABO", "Semifinalist (2026). 43 of 50 on the Open Exam; Semifinal Recognition of Academic Excellence, top 50 of 573."))
    st.append(Spacer(1, 2))
    st.append(line("Kaggle", "Silver medal, Stanford RNA 3D Folding Part 2 (2026): 92nd of 1,867. "
                             + link("Competition", "https://www.kaggle.com/competitions/stanford-rna-3d-folding-2") + "."))
    st.append(Spacer(1, 2))
    st.append(line("ARML Local", "Team WARML I-5, 2nd of about 250 teams and 1st among U.S. teams (2026)."))

    # ---- Leadership
    st += heading("Leadership and service")
    st.append(entry("Founder, President and CEO, AI Ethos, Inc. (501(c)(3))", "2025 to present", None,
                    "Multilingual, privacy-first AI tutoring for low-income, rural, multilingual and neurodiverse students. More than 1,500 students "
                    "reached; average 22% gain in math scores. IRS approval September 2025."))
    st.append(entry("Founder and President, NextGenAI International", "2025 to present", None,
                    "Student-led AI education organization: bootcamps, mentored projects and exchange, including outreach in Taiwan and Thailand. "
                    "200+ participants across three countries."))
    st.append(entry("Founder and research lead, CogArc", "In development", None,
                    "Wearable and EEG neurofeedback platform testing whether emotion is encoded in how body signals couple. Hypothesis stage."))
    st.append(entry("Co-captain and student coach, Cupertino Junior Olympiad Math/CS Team", "2024 to present", None,
                    "Coached 20+ peers toward AIME qualification and USACO Gold."))
    st.append(entry("Volunteer team leader, VA Palo Alto Health Care System", "2024 to present", None,
                    "Led a student team that audited medical images of 50+ elderly patients and standardized the workflow."))
    st.append(entry("Peer tutoring and STEM outreach", "Ongoing", None,
                    "Tutored 30+ peers in multivariable calculus and graph theory; mentored 20+ elementary students in coding."))

    # ---- Beyond
    st += heading("Beyond the classroom")
    st.append(entry("Track and field, Monta Vista Matadors", "2025 to present", None,
                    "Freshman-year school record, 100 m (11.89); Rookie of the Year. Anchored the winning frosh/soph 4×400 m relay at the Los Gatos "
                    "Top 8 Invitational (3:36.02); ran on the 4×400 m relay that set an all-time stadium record at RustBuster. "
                    "2026 season bests: 200 m 24.35, 400 m 54.53."))
    st.append(entry("Percussion section leader, Monta Vista Concert Band", "Grade 9", None,
                    "Led rehearsals for the first unanimous Superior rating across all Monta Vista ensembles at the CMEA Festival."))

    # ---- Skills
    st += heading("Skills")
    st.append(line("Languages and tools", "Python (PyTorch, TensorFlow, scikit-learn, NumPy, Pandas), Java, JavaScript, MATLAB, Git, LaTeX, Linux."))
    st.append(Spacer(1, 2))
    st.append(line("Spoken", "English; Spanish (AP level); Bengali (beginner)."))
    st.append(Spacer(1, 6))
    st.append(Paragraph("References available on request.", S["meta"]))
    return st


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Hank", 7.6)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.65 * inch, 0.4 * inch, "Aaryan Samanta  |  aaryansamanta.github.io  |  Updated September 2026")
    canvas.drawRightString(letter[0] - 0.65 * inch, 0.4 * inch, f"{doc.page}")
    canvas.restoreState()


def main():
    global S
    with tempfile.TemporaryDirectory() as tmp:
        make_fonts(tmp)
        S = styles()
        doc = BaseDocTemplate(OUT, pagesize=letter, title="Aaryan Samanta, Resume", author="Aaryan Samanta",
                              subject="Resume, September 2026")
        frame = Frame(0.65 * inch, 0.65 * inch, W, letter[1] - 1.2 * inch, id="f",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=footer)])
        doc.build(build_story())
    print("wrote", OUT)


if __name__ == "__main__":
    sys.exit(main())
