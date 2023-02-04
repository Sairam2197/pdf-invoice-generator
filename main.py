import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepath = glob.glob("Invoices/*xlsx")

for files in filepath:
    csv_data = pd.read_excel(files, sheet_name="Sheet 1")
    print(csv_data)
    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(files).stem
    invoice_no = filename.split("-")[0]
    pdf.set_font(family="Times", style="B", size=10)
    pdf.cell(w=10, h=10, txt=f"Invoice No.{invoice_no}", )
    pdf.output(f"PDFs/{filename}.pdf")
