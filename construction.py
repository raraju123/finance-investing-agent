def risk_parity(df):
    return [1 / len(df)] * len(df)

def black_litterman(df, market_return=0.07):
    r = df["Return"].to_numpy()
    blended = (r + market_return) / 2
    weights = blended / blended.sum()
    return weights.tolist()
