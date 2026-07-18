# =========================================
# src/market_data.py
# =========================================
import yfinance as yf

def get_price(ticker: str):
    try:
        data = yf.Ticker(ticker).history(period="1y")
        return {
            "ticker": ticker,
            "last_price": float(data["Close"].iloc[-1]),
            "one_year_return": float((data["Close"].iloc[-1] / data["Close"].iloc[0]) - 1),
        }
    except Exception as e:
        return {"ticker": ticker, "error": str(e)}


# =========================================
# src/optimizer_advanced.py
# =========================================
import numpy as np
import polars as pl

def optimize(df: pl.DataFrame):
    returns = df["Return"].to_numpy()
    if len(returns) < 2:
        return {
            "equal_weight_volatility": 0.0,
            "max_return_asset": None,
            "min_return_asset": None,
        }

    cov = np.cov(returns)
    weights = np.ones(len(returns)) / len(returns)
    portfolio_vol = float(np.sqrt(weights.T @ cov @ weights))

    return {
        "equal_weight_volatility": portfolio_vol,
        "max_return_asset": df.sort("Return", descending=True)[0]["Asset"],
        "min_return_asset": df.sort("Return")[0]["Asset"],
    }


# =========================================
# src/risk_model.py
# =========================================
import numpy as np
import polars as pl

def compute_risk_metrics(df: pl.DataFrame):
    returns = df["Return"].to_numpy()
    if len(returns) == 0:
        return {"volatility": 0.0, "sharpe_ratio": 0.0}

    volatility = float(np.std(returns))
    sharpe = float(np.mean(returns) / volatility) if volatility > 0 else 0.0

    return {
        "volatility": volatility,
        "sharpe_ratio": sharpe,
    }


# =========================================
# src/tax_engine.py
# =========================================
def tax_projection(total_value: float, tax_rate: float = 0.15):
    return {
        "tax_rate": tax_rate,
        "estimated_tax": float(total_value * tax_rate),
    }


# =========================================
# src/stress_test.py
# =========================================
import polars as pl

def stress_test(df: pl.DataFrame, shock: float = -0.20):
    total_value = float(df["Value"].sum())
    post_shock = total_value * (1 + shock)
    return {
        "shock": shock,
        "post_shock_value": post_shock,
    }


# =========================================
# src/monte_carlo.py
# =========================================
import numpy as np

def monte_carlo_simulation(initial_value: float, mean_return: float, volatility: float, runs: int = 5000):
    if volatility <= 0:
        return {
            "median_outcome": initial_value,
            "worst_case": initial_value,
            "best_case": initial_value,
        }

    results = []
    for _ in range(runs):
        simulated = initial_value * np.exp(np.random.normal(mean_return, volatility))
        results.append(simulated)

    return {
        "median_outcome": float(np.median(results)),
        "worst_case": float(np.percentile(results, 5)),
        "best_case": float(np.percentile(results, 95)),
    }


# =========================================
# src/sector_rotation.py
# =========================================
import polars as pl

def sector_rotation(df: pl.DataFrame):
    if "Sector" not in df.columns:
        return {
            "best_sector": None,
            "worst_sector": None,
            "sector_scores": {},
        }

    sectors = df.group_by("Sector").agg([
        pl.col("Return").mean().alias("avg_return"),
        pl.col("Value").sum().alias("total_value"),
    ])

    best_sector = sectors.sort("avg_return", descending=True)[0]["Sector"]
    worst_sector = sectors.sort("avg_return")[0]["Sector"]

    return {
        "best_sector": best_sector,
        "worst_sector": worst_sector,
        "sector_scores": sectors.to_dict(as_series=False),
    }


# =========================================
# src/factors.py
# =========================================
import polars as pl

def factor_exposure(df: pl.DataFrame):
    # These columns are optional; handle missing gracefully
    pe = df["PE"] if "PE" in df.columns else None
    rev = df["RevenueGrowth"] if "RevenueGrowth" in df.columns else None
    roe = df["ROE"] if "ROE" in df.columns else None

    value_exp = float((1 / pe).mean()) if pe is not None else 0.0
    growth_exp = float(rev.mean()) if rev is not None else 0.0
    momentum_exp = float(df["Return"].tail(3).mean()) if len(df) >= 3 else float(df["Return"].mean())
    quality_exp = float(roe.mean()) if roe is not None else 0.0
    overall = float(df["Return"].mean())

    return {
        "value_exposure": value_exp,
        "growth_exposure": growth_exp,
        "momentum_exposure": momentum_exp,
        "quality_exposure": quality_exp,
        "overall_factor_score": overall,
    }


# =========================================
# src/macro_model.py
# =========================================
import polars as pl

def macro_risk(df: pl.DataFrame, rate_shock: float = -0.01, inflation_shock: float = 0.02):
    total_value = float(df["Value"].sum())
    return {
        "rate_shock_impact": float(total_value * rate_shock),
        "inflation_shock_impact": float(total_value * inflation_shock),
        "combined_macro_risk": float(total_value * (rate_shock + inflation_shock)),
    }


# =========================================
# src/rebalance.py
# =========================================
import polars as pl

def rebalance(df: pl.DataFrame, target_weight: float = 0.10):
    total_value = float(df["Value"].sum())
    df = df.with_columns((pl.col("Value") / total_value).alias("weight"))

    actions = []
    for row in df.iter_rows(named=True):
        if row["weight"] > target_weight:
            actions.append({"asset": row["Asset"], "action": "trim"})
        elif row["weight"] < target_weight:
            actions.append({"asset": row["Asset"], "action": "add"})

    return {"rebalance_actions": actions}


# =========================================
# src/macro_feed.py
# =========================================
import requests

def get_fed_rates(api_key: str | None = None):
    if api_key is None:
        return None
    try:
        r = requests.get(
            "https://api.stlouisfed.org/fred/series/observations",
            params={
                "series_id": "FEDFUNDS",
                "api_key": api_key,
                "file_type": "json",
            },
            timeout=5,
        )
        data = r.json()["observations"]
        return float(data[-1]["value"])
    except Exception:
        return None

def get_cpi():
    return None  # placeholder, requires BLS API key

def get_unemployment():
    return None  # placeholder, requires BLS API key


# =========================================
# src/debate.py
# =========================================
def debate_scenarios(risk: dict, macro: dict, stress: dict):
    arguments = []

    if risk.get("sharpe_ratio", 0) < 1:
        arguments.append("Risk-adjusted returns are weak — consider rebalancing.")
    if macro.get("combined_macro_risk", 0) < 0:
        arguments.append("Macro risk is rising — defensive positioning recommended.")
    if stress.get("post_shock_value", 0) < 0:
        arguments.append("Stress test shows vulnerability to shocks.")

    return {
        "arguments": arguments,
        "consensus": arguments[0] if arguments else "No major risks detected.",
    }


# =========================================
# src/construction.py
# =========================================
import numpy as np
import polars as pl

def risk_parity(df: pl.DataFrame):
    vol = df["Return"].std()
    if vol == 0:
        return [1.0] * len(df)
    weights = 1 / vol
    return [float(weights)] * len(df)

def black_litterman(df: pl.DataFrame, market_return: float = 0.07):
    returns = df["Return"].to_numpy()
    if len(returns) == 0:
        return []
    blended = (returns + market_return) / 2
    weights = blended / blended.sum()
    return [float(w) for w in weights]


# =========================================
# src/dashboard.py
# =========================================
def build_dashboard(results: dict):
    return {
        "summary": results.get("portfolio_summary"),
        "risk": results.get("risk_metrics"),
        "macro": results.get("macro_risk"),
        "factors": results.get("factor_exposure"),
        "sector": results.get("sector_rotation"),
        "rebalance": results.get("rebalance"),
        "forecast": results.get("monte_carlo"),
        "market": results.get("market_data"),
    }


# =========================================
# src/decision_engine.py
# =========================================
def autonomous_decision(risk: dict, macro: dict, stress: dict, rebalance: dict):
    votes = []

    if risk.get("sharpe_ratio", 0) < 1:
        votes.append("increase_quality_assets")
    if macro.get("combined_macro_risk", 0) < 0:
        votes.append("reduce_growth_exposure")
    if stress.get("post_shock_value", 0) < 0:
        votes.append("increase_cash_buffer")

    for action in rebalance.get("rebalance_actions", []):
        votes.append(f"{action['action']}_{action['asset']}")

    if votes:
        from collections import Counter
        consensus = Counter(votes).most_common(1)[0][0]
    else:
        consensus = "hold"

    return {
        "votes": votes,
        "consensus_action": consensus,
    }


# =========================================
# src/memory.py
# =========================================
import json
import os

MEMORY_FILE = "agent_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"history": []}

def save_memory(entry: dict):
    mem = load_memory()
    mem["history"].append(entry)
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)


# =========================================
# src/alerts.py
# =========================================
def generate_alerts(risk: dict, macro_live: dict, market: dict):
    alerts = []

    if risk.get("volatility", 0) > 0.25:
        alerts.append("High volatility detected.")
    if macro_live.get("fed_rate", 0) and macro_live["fed_rate"] > 5:
        alerts.append("Fed rate above 5% — tightening risk.")
    if market.get("one_year_return", 0) < 0:
        alerts.append("Negative 1-year return trend.")

    return alerts


# =========================================
# src/rl_engine.py
# =========================================
import numpy as np

def reward_function(history: list[dict]):
    if len(history) < 2:
        return 0.0
    returns = [h["portfolio_summary"]["avg_return"] for h in history]
    vol = np.std(returns)
    growth = returns[-1] - returns[0]
    reward = growth - (0.5 * vol)
    return float(reward)

def update_policy(memory: dict):
    reward = reward_function(memory.get("history", []))
    policy = {
        "risk_tolerance": float(min(max(0.1 + reward, 0.01), 0.5)),
        "cash_buffer": float(min(max(0.05 - reward, 0.01), 0.3)),
    }
    return policy


# =========================================
# src/weighted_vote.py
# =========================================
def weighted_vote(decisions: dict, weights: dict):
    score = {}
    for agent, vote in decisions.items():
        weight = weights.get(agent, 1)
        score[vote] = score.get(vote, 0) + weight

    consensus = max(score, key=score.get) if score else None
    return {"scores": score, "consensus": consensus}


# =========================================
# src/report_generator.py
# =========================================
import json

def generate_report():
    with open("agent_output.json", "r") as f:
        data = json.load(f)

    report = {
        "summary": data.get("portfolio_summary"),
        "risk": data.get("risk_metrics"),
        "macro": data.get("macro_live"),
        "forecast": data.get("monte_carlo"),
        "decision": data.get("decision"),
        "alerts": data.get("alerts"),
    }
    with open("report.json", "w") as f:
        json.dump(report, f, indent=2)
    return report


# =========================================
# src/simulator.py
# =========================================
import numpy as np

def simulate_portfolio(initial: float, mean: float, vol: float, years: int = 10, paths: int = 5000):
    if vol <= 0:
        return {"median": initial, "worst_5pct": initial, "best_95pct": initial}

    results = []
    for _ in range(paths):
        value = initial
        for _ in range(years):
            value *= np.exp(np.random.normal(mean, vol))
        results.append(value)

    return {
        "median": float(np.median(results)),
        "worst_5pct": float(np.percentile(results, 5)),
        "best_95pct": float(np.percentile(results, 95)),
    }


# =========================================
# src/regime.py
# =========================================
def detect_regime(macro_live: dict):
    rate = macro_live.get("fed_rate")
    cpi = macro_live.get("cpi")
    unemp = macro_live.get("unemployment")

    if None in [rate, cpi, unemp]:
        return "unknown"

    if cpi > 4 and rate > 4:
        return "inflationary_contraction"
    if cpi > 4 and rate < 3:
        return "inflationary_expansion"
    if cpi < 2 and unemp < 4:
        return "disinflationary_expansion"
    if unemp > 6:
        return "recession"

    return "neutral"


# =========================================
# src/conflict.py
# =========================================
def resolve_conflict(weighted_vote_result: dict, regime: str):
    if regime == "recession":
        return "increase_cash_buffer"
    if regime == "inflationary_contraction":
        return "reduce_growth_exposure"
    return weighted_vote_result.get("consensus")


# =========================================
# src/paper_trading.py
# =========================================
def simulate_trade(action: str, market_price: float):
    if not action:
        return {"trade": "hold", "price": market_price}
    if action.startswith("add"):
        return {"trade": "buy", "price": market_price}
    if action.startswith("trim"):
        return {"trade": "sell", "price": market_price}
    return {"trade": "hold", "price": market_price}


# =========================================
# src/personalities.py
# =========================================
def risk_agent_personality():
    return {
        "name": "RiskAgent",
        "style": "cautious",
        "bias": -0.2,
        "priority": ["volatility", "drawdown"],
    }

def macro_agent_personality():
    return {
        "name": "MacroAgent",
        "style": "strategic",
        "bias": 0.1,
        "priority": ["rates", "inflation", "employment"],
    }

def factor_agent_personality():
    return {
        "name": "FactorAgent",
        "style": "analytical",
        "bias": 0.0,
        "priority": ["value", "growth", "momentum", "quality"],
    }


# =========================================
# src/strategy.py
# =========================================
def evolve_strategy(memory: dict, policy: dict):
    history = memory.get("history", [])
    if len(history) < 10:
        return {"strategy": "baseline", "confidence": 0.3}

    avg_return = sum(h["portfolio_summary"]["avg_return"] for h in history[-10:]) / 10
    vol = sum(h["risk_metrics"]["volatility"] for h in history[-10:]) / 10

    if avg_return > 0.05 and vol < 0.15:
        return {"strategy": "growth_bias", "confidence": 0.7}
    if avg_return < 0.02 and vol > 0.25:
        return {"strategy": "defensive_bias", "confidence": 0.8}

    return {"strategy": "neutral", "confidence": 0.5}


# =========================================
# src/themes.py
# =========================================
import polars as pl

def generate_themes(df: pl.DataFrame):
    assets = df["Asset"].to_list()
    themes = {
        "ai_automation": [a for a in assets if "AI" in a or "Tech" in a],
        "energy_transition": [a for a in assets if "Energy" in a or "Clean" in a],
        "healthcare_innovation": [a for a in assets if "Health" in a or "Bio" in a],
        "defensive_income": [a for a in assets if "Dividend" in a or "Income" in a],
    }
    return themes


# =========================================
# src/nlp_interface.py
# =========================================
def answer_query(query: str, results: dict):
    q = query.lower()

    if "risk" in q:
        return results.get("risk_metrics")
    if "sector" in q:
        return results.get("sector_rotation")
    if "macro" in q:
        return results.get("regime")
    if "rebalance" in q:
        return results.get("rebalance")
    if "forecast" in q:
        return results.get("simulation")

    return {"answer": "Query not recognized"}


# =========================================
# agent.py  (in repo root)
# =========================================
import json
import os
import polars as pl

from src.market_data import get_price
from src.optimizer_advanced import optimize
from src.risk_model import compute_risk_metrics
from src.tax_engine import tax_projection
from src.stress_test import stress_test
from src.monte_carlo import monte_carlo_simulation
from src.factors import factor_exposure
from src.sector_rotation import sector_rotation
from src.macro_model import macro_risk
from src.rebalance import rebalance
from src.macro_feed import get_fed_rates, get_cpi, get_unemployment
from src.debate import debate_scenarios
from src.construction import risk_parity, black_litterman
from src.dashboard import build_dashboard
from src.decision_engine import autonomous_decision
from src.memory import load_memory, save_memory
from src.alerts import generate_alerts
from src.rl_engine import update_policy
from src.weighted_vote import weighted_vote
from src.report_generator import generate_report
from src.simulator import simulate_portfolio
from src.regime import detect_regime
from src.conflict import resolve_conflict
from src.paper_trading import simulate_trade
from src.personalities import risk_agent_personality, macro_agent_personality, factor_agent_personality
from src.strategy import evolve_strategy
from src.themes import generate_themes
from src.nlp_interface import answer_query

def load_excel():
    excel_path = "010126.xlsx"
    if not os.path.exists(excel_path):
        return None
    return pl.read_excel(excel_path)

def main():
    df = load_excel()
    if df is None:
        print(json.dumps({"error": "Excel file not found"}, indent=2))
        return

    total_value = float(df["Value"].sum())
    mean_return = float(df["Return"].mean())
    volatility = float(df["Return"].std())

    results = {}

    results["portfolio_summary"] = {
        "total_value": total_value,
        "avg_return": mean_return,
    }
    results["optimization"] = optimize(df)
    results["risk_metrics"] = compute_risk_metrics(df)
    results["tax_projection"] = tax_projection(total_value)
    results["stress_test"] = stress_test(df)
    results["monte_carlo"] = monte_carlo_simulation(total_value, mean_return, volatility)
    results["factor_exposure"] = factor_exposure(df)
    results["sector_rotation"] = sector_rotation(df)
    results["macro_risk"] = macro_risk(df)
    results["rebalance"] = rebalance(df)

    macro_live = {
        "fed_rate": get_fed_rates(api_key=None),
        "cpi": get_cpi(),
        "unemployment": get_unemployment(),
    }
    results["macro_live"] = macro_live

    results["market_data"] = get_price("AAPL")

    results["debate"] = debate_scenarios(
        results["risk_metrics"],
        results["macro_risk"],
        results["stress_test"],
    )

    results["construction"] = {
        "risk_parity": risk_parity(df),
        "black_litterman": black_litterman(df),
    }

    results["dashboard"] = build_dashboard(results)

    memory = load_memory()
    results["policy"] = update_policy(memory)

    decision = autonomous_decision(
        results["risk_metrics"],
        results["macro_risk"],
        results["stress_test"],
        results["rebalance"],
    )
    results["decision"] = decision

    results["alerts"] = generate_alerts(
        results["risk_metrics"],
        results["macro_live"],
        results["market_data"],
    )

    results["simulation"] = simulate_portfolio(
        results["portfolio_summary"]["total_value"],
        results["portfolio_summary"]["avg_return"],
        results["risk_metrics"]["volatility"],
    )

    regime = detect_regime(results["macro_live"])
    results["regime"] = regime

    votes = {
        "risk_agent": results["decision"]["consensus_action"],
        "macro_agent": regime,
        "rebalance_agent": results["rebalance"]["rebalance_actions"][0]["action"]
        if results["rebalance"]["rebalance_actions"] else "hold",
    }
    weights = {"risk_agent": 2, "macro_agent": 3, "rebalance_agent": 1}
    results["weighted_vote"] = weighted_vote(votes, weights)

    results["final_decision"] = resolve_conflict(results["weighted_vote"], regime)
    results["paper_trade"] = simulate_trade(
        results["final_decision"],
        results["market_data"].get("last_price", 0.0),
    )

    results["personalities"] = {
        "risk": risk_agent_personality(),
        "macro": macro_agent_personality(),
        "factor": factor_agent_personality(),
    }

    results["strategy_evolution"] = evolve_strategy(memory, results["policy"])
    results["themes"] = generate_themes(df)

    results["nlp_example"] = answer_query("What is my macro regime?", results)

    save_memory(results)

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
