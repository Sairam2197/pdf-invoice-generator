import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepath = glob.glob("Invoices/*xlsx")

for files in filepath:

    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(files).stem
    invoice_no = filename.split("-")[0]
    date = filename.split("-")[1]

    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=10, h=10, txt=f"Invoice No.{invoice_no}",ln=1)
    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=10, h=10, txt=f"Date.{date}", ln=1)

    csv_data = pd.read_excel(files, sheet_name="Sheet 1")

# add header
    column = csv_data.columns
    column = [item.replace("_", " ").title() for item in column]
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=30, h=8, txt=column[0], border=1)
    pdf.cell(w=60, h=8, txt=column[1], border=1)
    pdf.cell(w=40, h=8, txt=column[2], border=1)
    pdf.cell(w=30, h=8, txt=column[3], border=1)
    pdf.cell(w=30, h=8, txt=column[4], border=1, ln=1)

#added rows
    for index,row in csv_data.iterrows():
        pdf.set_font(family="Times", style="B", size=14)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1,ln=1)

    pdf.output(f"PDFs/{filename}.pdf")

