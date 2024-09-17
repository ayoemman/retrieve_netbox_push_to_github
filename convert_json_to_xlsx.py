import pandas as pd
import json
import sys

def convert_json_to_xlsx(json_file, xlsx_file):
    try:
        # Load JSON data
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # Normalize JSON data into a flat table
        df = pd.json_normalize(data)

        # Write DataFrame to XLSX file
        with pd.ExcelWriter(xlsx_file, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Data')

        print(f"Successfully converted {json_file} to {xlsx_file}")

    except Exception as e:
        print(f"Failed to convert {json_file} to {xlsx_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 convert_json_to_xlsx.py <input_json_file> <output_xlsx_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    xlsx_file = sys.argv[2]
    convert_json_to_xlsx(json_file, xlsx_file)
