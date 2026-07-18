def factor_exposure(df):
    momentum = float(df["Return"].tail(3).mean())
    overall = float(df["Return"].mean())
    return {"momentum_exposure": momentum, "overall_factor_score": overall}
