def sector_rotation(df):
    if "Sector" not in df.columns:
        return {"best_sector": None, "worst_sector": None}
    grouped = df.group_by("Sector").agg(df["Return"].mean().alias("avg_return"))
    best = grouped.sort("avg_return", descending=True)[0]["Sector"]
    worst = grouped.sort("avg_return")[0]["Sector"]
    return {"best_sector": best, "worst_sector": worst}
