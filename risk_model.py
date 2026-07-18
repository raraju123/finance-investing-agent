import numpy as np

def compute_risk_metrics(df):
    r = df["Return"].to_numpy()
    vol = float(np.std(r))
    sharpe = float(np.mean(r) / vol) if vol > 0 else 0
    return {"volatility": vol, "sharpe_ratio": sharpe}
