import pandas as pd
import numpy as np
import json
import glob
import os
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
    if not {"Asset", "Value", "Return"}.issubset(df.columns):
        return {"error": "Missing required columns for portfolio analysis"}

    total_value = float(df["Value"].sum())
    avg_return = float(df["Return"].mean())
    max_row = df.loc[df["Value"].idxmax()]
    min_row = df.loc[df["Value"].idxmin()]

    summary = {
        "total_value": total_value,
        "avg_return": avg_return,
        "max_position": str(max_row["Asset"]),
        "min_position": str(min_row["Asset"]),
    }
    return summary

# ---------- RISK METRICS ----------

def compute_risk_metrics(df):
    if "Return" not in df.columns:
        return {"error": "Return column missing for risk metrics"}

    returns = df["Return"].astype(float)

    volatility = float(returns.std())
    sharpe = float(returns.mean() / (returns.std() + 1e-9))

    metrics = {
        "volatility": volatility,
        "sharpe_ratio": sharpe,
    }
    return metrics

# ---------- LIVE MARKET DATA ----------

def fetch_live_market_data(df):
    tickers = df["Asset"].dropna().tolist()
    market_data = {}

    for t in tickers:
        try:
            info = yf.Ticker(t).history(period="1y")
            if len(info) == 0:
                continue

            returns = info["Close"].pct_change().dropna()

            market_data[t] = {
                "live_price": float(info["Close"].iloc[-1]),
                "annual_return": float(returns.mean() * 252),
                "annual_volatility": float(returns.std() * np.sqrt(252)),
            }
        except Exception:
            continue

    return market_data

# ---------- PORTFOLIO OPTIMIZATION (MPT) ----------

def optimize_portfolio(df, market_data):
    tickers = list(market_data.keys())
    if len(tickers) < 2:
        return {"info": "Need at least 2 tickers for optimization"}

    returns = []
    vols = []
    for t in tickers:
        returns.append(market_data[t]["annual_return"])
        vols.append(market_data[t]["annual_volatility"])

    returns = np.array(returns)
    vols = np.array(vols)

    # Random weight simulation
    sims = 5000
    best_sharpe = -999
    best_weights = None

    for _ in range(sims):
        w = np.random.random(len(tickers))
        w /= w.sum()

        portfolio_return = np.sum(w * returns)
        portfolio_vol = np.sqrt(np.sum((w * vols) ** 2))
        sharpe = portfolio_return / (portfolio_vol + 1e-9)

        if sharpe > best_sharpe:
            best_sharpe = sharpe
            best_weights = w

    optimized = {
        "tickers": tickers,
        "weights": {tickers[i]: float(best_weights[i]) for i in range(len(tickers))},
        "optimized_sharpe": float(best_sharpe),
    }

    return optimized

# ---------- CASHFLOW INSIGHTS ----------

def compute_cashflow(df):
    if not {"Type", "Amount", "Date"}.issubset(df.columns):
        return {"info": "Cashflow columns (Type, Amount, Date) not present"}

    cf = df.copy()
    cf["Date"] = pd.to_datetime(cf["Date"], errors="coerce")
    cf["Month"] = cf["Date"].dt.to_period("M")

    income = cf[cf["Type"] == "Income"].groupby("Month")["Amount"].sum()
    expenses = cf[cf["Type"] == "Expense"].groupby("Month")["Amount"].sum()

    monthly = []
    for m in sorted(set(income.index) | set(expenses.index)):
        inc = float(income.get(m, 0.0))
        exp = float(expenses.get(m, 0.0))
        monthly.append({
            "month": str(m),
            "income": inc,
            "expenses": exp,
            "savings": inc - exp,
        })

    return {
        "monthly_cashflow": monthly,
        "savings_rate_overall": float(
            (income.sum() - expenses.sum()) / (income.sum() + 1e-9)
        ),
    }

# ---------- CHARTS ----------

def generate_charts(df):
    charts = []

    if {"Asset", "Value"}.issubset(df.columns):
        plt.figure(figsize=(8, 4))
        sns.barplot(x="Asset", y="Value", data=df)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        fname = "chart_asset_values.png"
        plt.savefig(fname)
        plt.close()
        charts.append({"type": "asset_values", "file": fname})

    if "Return" in df.columns:
        plt.figure(figsize=(6, 4))
        sns.histplot(df["Return"], kde=True)
        plt.tight_layout()
        fname = "chart_return_distribution.png"
        plt.savefig(fname)
        plt.close()
        charts.append({"type": "return_distribution", "file": fname})

    return charts

# ---------- DASHBOARD ----------

def build_dashboard(df, validation_issues, portfolio_summary, risk_metrics, cashflow, charts, market_data, optimization):
    return {
        "validation": validation_issues,
        "portfolio_summary": portfolio_summary,
        "risk_metrics": risk_metrics,
        "cashflow": cashflow,
        "charts": charts,
        "market_data": market_data,
        "optimization": optimization,
    }

# ---------- MAIN ----------

def main():
    print("📊 Python Financial Agent Starting...")
    df, load_error = load_data()

    if load_error is not None:
        print(json.dumps(load_error, indent=2))
        return

    validation_issues = validate_data(df)
    portfolio_summary = analyze_portfolio(df)
    risk_metrics = compute_risk_metrics(df)
    cashflow = compute_cashflow(df)
    charts = generate_charts(df)

    market_data = fetch_live_market_data(df)
    optimization = optimize_portfolio(df, market_data)

    dashboard = build_dashboard(
        df,
        validation_issues,
        portfolio_summary,
        risk_metrics,
        cashflow,
        charts,
        market_data,
        optimization,
    )

    print(json.dumps(dashboard, indent=2))

if __name__ == "__main__":
    main()
