def stress_test(df, shock=-0.20):
    total = float(df["Value"].sum())
    return {"shock": shock, "post_shock_value": total * (1 + shock)}
