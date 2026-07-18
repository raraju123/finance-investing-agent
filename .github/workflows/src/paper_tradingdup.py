def simulate_trade(action, price):
    if action.startswith("add"):
        return {"trade": "buy", "price": price}
    if action.startswith("trim"):
        return {"trade": "sell", "price": price}
    return {"trade": "hold", "price": price}
