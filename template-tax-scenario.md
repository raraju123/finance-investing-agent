# Tax Scenario Modeling Template

Use this template when the user requests tax scenario modeling for a position.

## Instructions
Ask the user for: position details (shares, cost basis, current price, holding period), tax brackets (federal ordinary, federal LTCG, state, NIIT applicability), account type, and any gains or losses elsewhere for TLH context.

---

## EXECUTIVE SUMMARY
[2-3 sentences on the tax impact of selling now vs. holding, and the key variables that change the outcome.]

---

## 1. POSITION DETAILS

| Field | Value |
|-------|-------|
| Ticker | [___________] |
| Shares | [____] |
| Cost basis per share | $[____] |
| Total cost basis | $[____] |
| Current price per share | $[____] |
| Total current value | $[____] |
| Unrealized gain/(loss) | $[____] |
| Holding period | [ ] Short-term (<1 year) / [ ] Long-term (>=1 year) |
| Account type | [ ] Taxable / [ ] Tax-advantaged (IRA/401k) |

---

## 2. SCENARIO COMPARISON

| Scenario | Gain/Loss | Tax Rate | Tax Owed | After-Tax Proceeds | Notes |
|----------|-----------|----------|----------|-------------------|-------|
| Sell now (ST) | $[____] | [____]% | $[____] | $[____] | [Short-term capital gains tax at ordinary income rates] |
| Hold 1+ year then sell (LT) | $[____] | [____]% | $[____] | $[____] | [Long-term capital gains tax at LTCG rates] |
| Hold 5 years (assume [X]% annual return) | $[____] | [____]% | $[____] | $[____] | [Deferred tax, compounding benefit] |
| Hold indefinitely | $0 now | N/A | $0 | $[____] (current value) | [Tax deferral + step-up in basis at death] |
| Tax-loss harvest (if losses available) | $[____] net gain | [____]% | $[____] | $[____] | [Offsets gains with losses from other positions] |

Formulas:
- Gain = (Current price - Cost basis) x Shares
- Tax owed = Gain x (applicable federal + state + NIIT if applicable)
- After-tax proceeds = (Current price x Shares) - Tax owed
- Opportunity cost of deferring = After-tax sale proceeds x (1 + return rate)^years - current value

---

## 3. TAX-LOSS HARVESTING INTEGRATION

If you have unrealized losses elsewhere:

| Loss Position | Unrealized Loss | Can Offset This Gain? |
|---------------|-----------------|----------------------|
| [Ticker 1] | $[____] | [ ] Yes / [ ] No |
| [Ticker 2] | $[____] | [ ] Yes / [ ] No |
| TOTAL | $[____] | Remaining loss up to $3,000/year offsets ordinary income; excess carries forward |

Wash sale warning:
- Cannot buy "substantially identical" security within 30 days before or after sale
- Options on the stock also trigger wash sale rules
- Acceptable substitutions vary by asset class

---

## 4. KEY DECISIONS

| Decision | Considerations |
|----------|---------------|
| Sell now | Immediate capital, tax cost, opportunity cost |
| Wait for LTCG | Time cost, price risk, tax savings |
| Hold indefinitely | Deferral benefit, step-up in basis, concentration risk |
| Harvest losses | Tax benefit, wash sale constraints, market exposure maintenance |

Disclaimers:
This analysis is educational. It is not personalized investment advice. Consult a qualified financial professional before implementing any strategy.
