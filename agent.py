import pandas as pd
import json
import glob

def find_data_file():
    """
    Detects the first available data file in the folder.
    Supports: .xlsx, .xls, .csv
    Priority: Excel first, then CSV
    """
    excel_files = glob.glob("*.xlsx") + glob.glob("*.xls")
    csv_files = glob.glob("*.csv")

    if excel_files:
        return excel_files[0]
    if csv_files:
        return csv_files[0]

    return None

def load_data():
    """
    Loads the detected data file into a pandas DataFrame.
    """
    data_path = find_data_file()
    if data_path is None:
        return None

    print(f"📄 Using data file: {data_path}")

    if data_path.endswith(".csv"):
        return pd.read_csv(data_path)
    else:
        return pd.read_excel(data_path)

def analyze_portfolio(df):
    """
    Performs basic portfolio analysis.
    Requires columns: Asset, Value, Return
    """
    if df is None:
        return {"error": "No data file found"}

    required_columns = {"Asset", "Value", "Return"}
    if not required_columns.issubset(df.columns):
        return {
            "error": "Missing required columns",
            "required": list(required_columns),
            "found": list(df.columns)
        }

    summary = {
        "total_value": float(df["Value"].sum()),
        "avg_return": float(df["Return"].mean()),
        "max_position": str(df.loc[df["Value"].idxmax(), "Asset"]),
        "min_position": str(df.loc[df["Value"].idxmin(), "Asset"]),
    }
    return summary

def main():
    print("📊 Python Financial Agent Starting...")
    df = load_data()
    results = analyze_portfolio(df)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
