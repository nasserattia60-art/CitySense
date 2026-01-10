from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors

def generate_report_pdf(report, file_path):
    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm,
    )

    styles = getSampleStyleSheet()
    styles["Title"].alignment = TA_CENTER

    story = []

    # Title
    story.append(Paragraph("CitySense Location Report", styles["Title"]))
    story.append(Spacer(1, 20))

    # Meta
    story.append(Paragraph(
        f"<b>Address:</b> {report.analysis.location.address}", styles["Normal"]
    ))
    story.append(Paragraph(
        f"<b>Generated for:</b> {report.analysis.user.email}", styles["Normal"]
    ))
    story.append(Paragraph(
        f"<b>Date:</b> {report.created_at.strftime('%Y-%m-%d')}", styles["Normal"]
    ))
    story.append(Spacer(1, 20))

    # Scores Table
    table_data = [
        ["Metric", "Score"],
        ["Safety", report.safety_score],
        ["Noise", report.noise_level],
        ["Rent Index", report.rent_index],
        ["Water Quality", report.water_quality],
        ["Population Density", report.population_density],
        ["AI Score", report.ai_score],
    ]

    table = Table(table_data, colWidths=[8*cm, 4*cm])
    table.setStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 1, colors.grey),
        ("ALIGN", (1,1), (-1,-1), "CENTER"),
    ])

    story.append(table)
    story.append(Spacer(1, 20))

    # Summary
    story.append(Paragraph("<b>Summary</b>", styles["Heading2"]))
    story.append(Paragraph(report.summary, styles["Normal"]))

    doc.build(story)
