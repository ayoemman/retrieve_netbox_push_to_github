import json
import sys
import pandas as pd

def convert_json_to_xlsx(json_file, xlsx_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    writer = pd.ExcelWriter(xlsx_file, engine='xlsxwriter')

    for key, value in data.items():
        df = pd.json_normalize(value)
        df.to_excel(writer, sheet_name=key, index=False)

    writer.save()

if __name__ == "__main__":
    json_file = sys.argv[1]
    xlsx_file = sys.argv[2]
    convert_json_to_xlsx(json_file, xlsx_file)
