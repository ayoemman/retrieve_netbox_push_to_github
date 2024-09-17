#import sys
import pandas as pd
import json

def convert_json_to_xlsx(json_file, xlsx_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    writer = pd.ExcelWriter(xlsx_file, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Data')
    writer.save()

if __name__ == "__main__":
    import sys
    json_file = sys.argv[1]
    xlsx_file = sys.argv[2]
    convert_json_to_xlsx(json_file, xlsx_file)
