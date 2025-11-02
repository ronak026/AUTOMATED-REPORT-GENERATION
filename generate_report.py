import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Step 1: Read Data
data_file = "data.csv"
df = pd.read_csv(data_file)

# Step 2: Analyze Data
summary = df.describe().round(2)

# Step 3: Generate PDF Report
report_filename = "report.pdf"
doc = SimpleDocTemplate(report_filename, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Add Title
title = Paragraph("Sales Performance Report", styles["Title"])
elements.append(title)
elements.append(Spacer(1, 12))

# Add Summary Table
summary_data = [summary.columns.tolist()] + summary.values.tolist()
table = Table([["Statistic"] + summary.columns.tolist()] + summary.reset_index().values.tolist())

# Style the table
style = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
])
table.setStyle(style)

elements.append(Paragraph("Summary Statistics:", styles["Heading2"]))
elements.append(table)
elements.append(Spacer(1, 12))

# Add Some Custom Insights
avg_sales = df["Sales"].mean()
best_performer = df.loc[df["Sales"].idxmax(), "Name"]
insight_text = f"The average sales figure is {avg_sales:.2f}. The top performer is {best_performer}."
elements.append(Paragraph(insight_text, styles["Normal"]))

# Build PDF
doc.build(elements)

print(f"Report generated successfully: {report_filename}")
