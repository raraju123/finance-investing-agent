import numpy as np

def optimize(df):
    r = df["Return"].to_numpy()
    if len(r) < 2:
        return {"equal_weight_volatility": 0.0}
    cov = np.cov(r)
    w = np.ones(len(r)) / len(r)
    vol = float(np.sqrt(w.T @ cov @ w))
    return {"equal_weight_volatility": vol}
