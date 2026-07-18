import numpy as np

def simulate_portfolio(initial, mean, vol, years=10, paths=5000):
    results = []
    for _ in range(paths):
        value = initial
        for _ in range(years):
            value *= np.exp(np.random.normal(mean, vol))
        results.append(value)
    return {
        "median": float(np.median(results)),
        "worst_5pct": float(np.percentile(results, 5)),
        "best_95pct": float(np.percentile(results, 95))
    }
