def macro_risk(df, rate_shock=-0.01, inflation_shock=0.02):
    total = float(df["Value"].sum())
    return {
        "rate_shock_impact": total * rate_shock,
        "inflation_shock_impact": total * inflation_shock,
        "combined_macro_risk": total * (rate_shock + inflation_shock)
    }
