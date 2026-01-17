from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import red, green, black


def generate_report(file_path, data):
    """
    data = {
        filename,
        final_label,
        confidence,
        risk,
        attack_percentage
    }
    """

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    # ===== TITLE =====
    title = Paragraph(
        "<b><font size=18>Network Traffic Analysis Report</font></b>",
        styles["Title"]
    )
    content.append(title)
    content.append(Spacer(1, 20))

    # ===== FILE INFO =====
    content.append(Paragraph(f"<b>File Name:</b> {data['filename']}", styles["Normal"]))
    content.append(Spacer(1, 10))

    # ===== VERDICT =====
    color = green if data["final_label"] == "normal" else red
    verdict = Paragraph(
        f"<b>Final Verdict:</b> <font color='{color}'>{data['final_label'].upper()}</font>",
        styles["Normal"]
    )
    content.append(verdict)
    content.append(Spacer(1, 10))

    # ===== DETAILS =====
    content.append(Paragraph(f"<b>Confidence:</b> {data['confidence']}%", styles["Normal"]))
    content.append(Paragraph(f"<b>Risk Level:</b> {data['risk']}", styles["Normal"]))
    content.append(Paragraph(f"<b>Attack Percentage:</b> {data['attack_percentage']}%", styles["Normal"]))
    content.append(Spacer(1, 20))

    # ===== EXPLAINABLE AI =====
    content.append(Paragraph("<b>Explainable AI Summary</b>", styles["Heading2"]))
    content.append(Spacer(1, 10))

    if data["final_label"] == "attack":
        content.append(Paragraph(
            "Traffic pattern shows abnormal behavior such as high packet rate or unusual data transfer.",
            styles["Normal"]
        ))
    else:
        content.append(Paragraph(
            "Traffic behavior is within normal limits with no suspicious patterns detected.",
            styles["Normal"]
        ))

    doc.build(content)
