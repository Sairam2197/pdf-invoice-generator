import pandas as pd
import glob

filepath = glob.glob("Invoices/*xlsx")

for files in filepath:
    csv_data = pd.read_excel(files, sheet_name="Sheet 1")
    print(csv_data)
