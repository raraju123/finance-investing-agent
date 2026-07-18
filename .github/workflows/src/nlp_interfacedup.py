def answer_query(query, results):
    q = query.lower()
    if "risk" in q:
        return results["risk_metrics"]
    if "macro" in q:
        return results["macro_risk"]
    return {"answer": "Query not recognized"}
