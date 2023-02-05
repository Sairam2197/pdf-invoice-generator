import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepath = glob.glob("Invoices/*xlsx")

for files in filepath:
    csv_data = pd.read_excel(files, sheet_name="Sheet 1")

    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(files).stem
    invoice_no = filename.split("-")[0]
    date = filename.split("-")[1]

    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=10, h=10, txt=f"Invoice No.{invoice_no}",ln=1)
    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=10, h=10, txt=f"Date.{date}")

    pdf.output(f"PDFs/{filename}.pdf")

