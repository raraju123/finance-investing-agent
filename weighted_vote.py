def weighted_vote(decisions, weights):
    score = {}
    for agent, vote in decisions.items():
        score[vote] = score.get(vote, 0) + weights.get(agent, 1)
    consensus = max(score, key=score.get)
    return {"scores": score, "consensus": consensus}
