import pandas as pd
import json
import os
import glob

def find_excel_file():
    # Look for any .xlsx or .xls file in the current folder
    excel_files = glob.glob("*.xlsx") + glob.glob("*.xls")

    if not excel_files:
        return None

    # Use the first Excel file found
    return excel_files[0]

def load_excel():
    excel_path = find_excel_file()
    if excel_path is None:
        return None

    print(f"📄 Using Excel file: {excel_path}")
    return pd.read_excel(excel_path)

def analyze_portfolio(df):
    if df is None:
        return {"error": "No Excel file found"}

    summary = {
        "total_value": df["Value"].sum(),
        "avg_return": df["Return"].mean(),
        "max_position": df.loc[df["Value"].idxmax(), "Asset"],
        "min_position": df.loc[df["Value"].idxmin(), "Asset"],
    }
    return summary

def main():
    print("📊 Python Financial Agent Starting...")
    df = load_excel()
    results = analyze_portfolio(df)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
