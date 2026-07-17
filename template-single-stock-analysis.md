# Single Stock Analysis Template

Use this template when the user requests analysis of an individual stock.

## Instructions
Ask the user for: ticker, current price, cost basis, holding period, tax brackets, and account type. If the ticker is not verifiable, immediately flag that and request confirmation on SEC EDGAR before proceeding with valuation.

---

## EXECUTIVE SUMMARY
[2-3 sentences on the stock's key characteristics, current valuation snapshot, and whether it seems to fit the user's portfolio within concentration limits.]

---

## 1. BASIC INFO

| Field | Value |
|-------|-------|
| Ticker | [___________] |
| Company name | [___________] |
| Sector | [___________] |
| Current price | $[____] |
| Cost basis | $[____] |
| Unrealized gain/(loss) | $[____] per share |
| Holding period | [ ] Short-term (<1 year) / [ ] Long-term (>=1 year) |
| Date of analysis | [___________] |
| User thesis | [1-2 sentences on why they own / want to own it] |

---

## 2. BUSINESS MODEL CHECK

| Check | Pass/Fail | Notes |
|-------|-----------|-------|
| Can explain how company makes money in 3 sentences | [ ] Yes / [ ] No | |
| Revenue streams are understandable | [ ] Yes / [ ] No | |
| No excessive related-party transactions | [ ] Yes / [ ] No | |
| Competitive moat (network effects, patents, scale, switching costs) | [ ] Yes / [ ] No / [ ] Partial | [Describe] |
| Management insider ownership alignment | [ ] Good / [ ] Mixed / [ ] Bad | [____]% |
| Capital allocation track record | [ ] Prudent / [ ] Mixed / [ ] Poor | |

Red flags spotted:
- [ ] Yes: [list]
- [ ] No

---

## 3. FINANCIAL HEALTH METRICS

| Metric | 1 Year Ago | 3 Years Ago | 5 Years Ago | Rule of Thumb | Pass/Fail |
|--------|------------|------------|------------|--------------|-----------|
| Revenue growth YoY | [____]% | [____]% | [____]% | Stable or growing | [ ] |
| Operating margin | [____]% | [____]% | [____]% | Stable or expanding | [ ] |
| ROIC | [____]% | [____]% | [____]% | >15% excellent | [ ] |
| ROE | [____]% | [____]% | [____]% | >15% good (watch leverage) | [ ] |
| Debt/Equity | [____]x | [____]x | [____]x | <0.5 conservative | [ ] |
| Interest coverage | [____]x | [____]x | [____]x | >5.0x strong | [ ] |
| Current ratio | [____]x | [____]x | [____]x | 1.2-2.0 healthy | [ ] |
| OCF / Net income | [____]x | [____]x | [____]x | >=1.0x healthy | [ ] |
| Free cash flow | $[____]M | $[____]M | $[____]M | Positive and growing | [ ] |
| Dividend payout ratio | [____]% | [____]% | [____]% | <80% sustainable | [ ] |

Notes:
- If metrics are unavailable, state that and recommend checking 10-K/10-Q before sizing.
- Compare trends over time, not just single-year snapshot.

---

## 4. VALUATION

| Metric | Current Value | 5-Year Low | 5-Year High | Sector Average | Assessment |
|--------|---------------|------------|------------|---------------|------------|
| Trailing P/E | [____]x | [____]x | [____]x | [____]x | [Cheap / Fair / Expensive] |
| Forward P/E | [____]x | N/A | N/A | [____]x | [Cheap / Fair / Expensive] |
| P/FCF | [____]x | [____]x | [____]x | [____]x | [Cheap / Fair / Expensive] |
| EV/EBITDA | [____]x | [____]x | [____]x | [____]x | [Cheap / Fair / Expensive] |
| Dividend yield | [____]% | [____]% | [____]% | [____]% | [High / Fair / Low] |
| PEG ratio | [____]x | N/A | N/A | N/A | <1 cheap, >2 expensive |

Implied growth rate (reverse DCF, if calculable): [____]%
Your estimated fair value range: $[____] to $[____]
Upside to fair value (if current price is $[____]): [____]%
Downside to 50% of fair value: [____]%

---

## 5. PORTFOLIO FIT

| Check | Value | Limit | Result |
|-------|-------|-------|--------|
| Current share of total portfolio | [____]% | 5-10% | [ ] Pass / [ ] Fail |
| Current share of equity allocation | [____]% | 20-25% max per stock | [ ] Pass / [ ] Fail |
| Sector share of equity allocation | [____]% | 20-25% | [ ] Pass / [ ] Fail |
| After buying [X] more shares | [____]% | 5-10% | [ ] Pass / [ ] Fail |

Additional notes:
- Correlation to existing holdings: [High / Moderate / Low]
- Redundant exposure: [Yes/No — describe overlap with other holdings]

---

## 6. TAX CONSIDERATIONS

| Scenario | Gain/Loss | Tax Rate | Tax Owed | After-Tax Proceeds | Effective Tax Rate |
|----------|-----------|----------|----------|-------------------|-------------------|
| Sell now (ST) | $[____] | [____]% | $[____] | $[____] | [____]% |
| Sell after 1+ year (LT) | $[____] | [____]% | $[____] | $[____] | [____]% |
| Hold indefinitely | $0 now | N/A | $0 | $[____] (current value) | 0% deferred |

Tax-loss harvest opportunity:
- If sold at a loss: offsets [____] of gains dollar-for-dollar
- Excess up to $[3,000]/year offsets ordinary income
- Remaining carries forward indefinitely
- Wash sale window: 30 days before/after sale

---

## 7. SCENARIO OUTCOMES

| Scenario | Probability | Price Target | Position Value (X shares) | Portfolio Impact |
|----------|------------|--------------|---------------------------|------------------|
| Bear (thesis fails) | [25]% | $[____] | $[____] | [____]% of portfolio |
| Base (fair value) | [50]% | $[____] | $[____] | [____]% of portfolio |
| Bull (thesis plays out) | [25]% | $[____] | $[____] | [____]% of portfolio |

---

## 8. EXIT CRITERIA

I will sell if:
1. [Quantitative metric fails: e.g., ROIC falls below 10% for 2 consecutive quarters]
2. [Valuation trigger: e.g., forward P/E exceeds 35x]
3. [Portfolio limit: e.g., position exceeds 10% of total portfolio]
4. [Thesis invalidation: e.g., competitive moat erodes]
5. [Better opportunity: e.g., same risk profile with higher expected return]

---

## 9. QUESTIONS TO ANSWER

Before making a decision:
1. Can I explain the business model in 3 sentences?
2. Have I reviewed the latest 10-K / 10-Q?
3. Does this position exceed my concentration limit?
4. What is my maximum tolerable drawdown on this position?
5. Am I buying/selling because of research or recent price movement?
6. What is the opportunity cost of this capital?

Disclaimers:
This analysis is educational. It is not personalized investment advice. Consult a qualified financial professional before implementing any strategy.
