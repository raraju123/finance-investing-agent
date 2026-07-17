def generate_alerts(risk, macro_live, market):
    alerts = []
    if risk["volatility"] > 0.25:
        alerts.append("High volatility")
    return alerts
