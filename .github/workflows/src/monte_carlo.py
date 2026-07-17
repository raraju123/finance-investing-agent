import numpy as np

def monte_carlo_simulation(initial, mean, vol, runs=5000):
    results = [
        initial * np.exp(np.random.normal(mean, vol))
        for _ in range(runs)
    ]
    return {
        "median_outcome": float(np.median(results)),
        "worst_case": float(np.percentile(results, 5)),
        "best_case": float(np.percentile(results, 95))
    }
