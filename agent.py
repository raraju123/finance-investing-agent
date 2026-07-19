import pandas as pd
import numpy as np
import json
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# ---------- DATA LOADING ----------

def find_data_file():
    excel_files = glob.glob("*.xlsx") + glob.glob("*.xls")
    csv_files = glob.glob("*.csv")
    if excel_files:
        return excel_files[0]
    if csv_files:
        return csv_files[0]
    return None

def load_data():
    data_path = find_data_file()
    if data_path is None:
        return None, {"error": "No data file found"}
    print(f"📄 Using data file: {data_path}")
    try:
        if data_path.endswith(".csv"):
            df = pd.read_csv(data_path)
        else:
            df = pd.read_excel(data_path)
    except Exception as e:
        return None, {"error": "Failed to load data", "details": str(e)}
    return df, None

# ---------- VALIDATION ----------

def validate_data(df):
    issues = []
    required_cols = ["Asset", "Value", "Return"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        issues.append({"type": "missing_columns", "missing": missing})
    if "Value" in df.columns:
        if not np.issubdtype(df["Value"].dtype, np.number):
            issues.append({"type": "value_not_numeric"})
        if (df["Value"] < 0).any():
            issues.append({"type": "negative_values_in_value"})
    if "Return" in df.columns:
        if not np.issubdtype(df["Return"].dtype, np.number):
            issues.append({"type": "return_not_numeric"})
    if df.duplicated(subset=["Asset"]).any():
        issues.append({"type": "duplicate_assets"})
    empty_rows = df.isna().all(axis=1).sum()
    if empty_rows > 0:
        issues.append({"type": "empty_rows", "count": int(empty_rows)})
    return issues

# ---------- PORTFOLIO SUMMARY ----------

def analyze_portfolio(df):
    total_value = float(df["Value"].sum())
    avg_return = float(df["Return"].mean())
    max_row = df.loc[df["Value"].idxmax()]
    min_row = df.loc[df["Value"].idxmin()]
    return {
        "total_value": total_value,
        "avg_return": avg_return,
        "max_position": str(max_row["Asset"]),
        "min_position": str(min_row["Asset"]),
    }

# ---------- RISK METRICS ----------

def compute_risk_metrics(df):
    returns = df["Return"].astype(float)
    volatility = float(returns.std())
    sharpe = float(returns.mean() / (returns.std() + 1e-9))
    return {
        "volatility": volatility,
        "sharpe_ratio": sharpe,
    }

# ---------- AUTO-DETECT TICKERS ----------

def detect_valid_tickers(df):
    tickers = []
    for asset in df["Asset"]:
        try:
            info = yf.Ticker(asset).history(period="1mo")
            if len(info) > 0:
                tickers.append(asset)
        except Exception:
            continue
    return tickers

# ---------- LIVE MARKET DATA ----------

def fetch_live_market_data(tickers):
    market_data = {}
    for t in tickers:
        try:
            info = yf.Ticker(t).history(period="1y")
            if len(info) == 0:
                continue
            returns = info["Close"].pct_change().dropna()
            market_data[t] = {
                "ticker": t,
                "live_price": float(info["Close"].iloc[-1]),
                "annual_return": float(returns.mean() * 252),
                "annual_volatility": float(returns.std() * np.sqrt(252)),
            }
        except Exception:
            continue
    return market_data

# ---------- PORTFOLIO OPTIMIZATION (MPT) ----------

def optimize_portfolio(market_data):
    if len(market_data) < 2:
        return {"info": "Need at least 2 valid tickers for optimization"}
    assets = list(market_data.keys())
    returns = np.array([market_data[a]["annual_return"] for a in assets])
    vols = np.array([market_data[a]["annual_volatility"] for a in assets])
    sims = 5000
    best_sharpe = -999
    best_weights = None
    for _ in range(sims):
        w = np.random.random(len(assets))
        w /= w.sum()
        portfolio_return = np.sum(w * returns)
        portfolio_vol = np.sqrt(np.sum((w * vols) ** 2))
        sharpe = portfolio_return / (portfolio_vol + 1e-9)
        if sharpe > best_sharpe:
            best_sharpe = sharpe
            best_weights = w
    return {
        "assets": assets,
        "weights": {assets[i]: float(best_weights[i]) for i in range(len(assets))},
        "optimized_sharpe": float(best_sharpe),
    }

# ---------- CHARTS ----------

def generate_charts(df):
    charts = []
    plt.figure(figsize=(8, 4))
    sns.barplot(x="Asset", y="Value", data=df)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("chart_asset_values.png")
    plt.close()
    charts.append({"type": "asset_values", "file": "chart_asset_values.png"})
    plt.figure(figsize=(6, 4))
    sns.histplot(df["Return"], kde=True)
    plt.tight_layout()
    plt.savefig("chart_return_distribution.png")
    plt.close()
    charts.append({"type": "return_distribution", "file": "chart_return_distribution.png"})
    return charts

# ---------- MAIN ----------

def main():
    print("📊 Python Financial Agent Starting...")
    df, load_error = load_data()
    if load_error:
        print(json.dumps(load_error, indent=2))
        return
    validation = validate_data(df)
    summary = analyze_portfolio(df)
    risk = compute_risk_metrics(df)
    charts = generate_charts(df)
    tickers = detect_valid_tickers(df)
    market_data = fetch_live_market_data(tickers)
    optimization = optimize_portfolio(market_data)
    dashboard = {
        "validation": validation,
        "portfolio_summary": summary,
        "risk_metrics": risk,
        "charts": charts,
        "market_data": market_data,
        "optimization": optimization,
    }
    print(json.dumps(dashboard, indent=2))

if __name__ == "__main__":
    main()
