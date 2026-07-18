def debate_scenarios(risk, macro, stress):
    arguments = []
    if risk["sharpe_ratio"] < 1:
        arguments.append("Weak risk-adjusted returns")
    if macro["combined_macro_risk"] < 0:
        arguments.append("Macro pressure rising")
    return {"arguments": arguments, "consensus": arguments[0] if arguments else "stable"}
