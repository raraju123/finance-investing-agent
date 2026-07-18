def rebalance(df, target_weight=0.10):
    total = float(df["Value"].sum())
    df = df.with_columns((df["Value"] / total).alias("weight"))
    actions = []
    for row in df.iter_rows(named=True):
        if row["weight"] > target_weight:
            actions.append({"asset": row["Asset"], "action": "trim"})
        elif row["weight"] < target_weight:
            actions.append({"asset": row["Asset"], "action": "add"})
    return {"rebalance_actions": actions}
