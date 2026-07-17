def build_dashboard(results):
    return {
        "summary": results["portfolio_summary"],
        "risk": results["risk_metrics"],
        "macro": results["macro_risk"],
        "rebalance": results["rebalance"]
    }
