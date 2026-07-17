import pandas as pd
import json
import os

def load_excel():
    excel_path = "010126.xlsx"
    if os.path.exists(excel_path):
        return pd.read_excel(excel_path)
    return None

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
