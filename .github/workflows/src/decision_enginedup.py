def autonomous_decision(risk, macro, stress, rebalance):
    votes = []
    if risk["sharpe_ratio"] < 1:
        votes.append("increase_quality_assets")
    if macro["combined_macro_risk"] < 0:
        votes.append("reduce_growth_exposure")
    return {"votes": votes, "consensus_action": votes[0] if votes else "hold"}
