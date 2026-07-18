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
