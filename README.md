# Finance & Investing AI Agent

Structured financial analysis, portfolio construction, tax modeling, scenario projections, and investment decision frameworks for stocks, ETFs, bonds, and asset allocation. No personalized advice — this skill provides frameworks, scenarios, comparisons, and insights only.

Built for [Hermes Agent](https://github.com/NousResearch/hermes-agent).

## What it does

- Portfolio audit with concentration and diversification checks
- Single stock analysis with financial health, valuation, and scenario modeling
- Tax scenario modeling (ST/LT, tax-loss harvesting, wash sale rules)
- Stress testing and drawdown projections
- Concept explanations (ROIC, PEG, factor investing, drawdown math, etc.)
- Asset allocation frameworks

## Install

```bash
hermes skills install https://raw.githubusercontent.com/<your-username>/finance-investing-agent/main/SKILL.md
```

## Usage

Load the skill, then use natural language:

- "Audit my portfolio"
- "Model tax-loss harvesting for my holdings"
- "Analyze [ticker]: current price $X, cost $Y, held Z months"
- "Stress test my portfolio against a 30% crash"
- "Explain drawdown math with examples"

## Disclaimer

This skill provides educational analysis only. It is not personalized investment advice. Always consult a qualified financial professional before making financial decisions.

## Folder Structure

```
finance-investing-agent/
  SKILL.md
  README.md
  references/
    template-portfolio-audit.md
    template-single-stock-analysis.md
    template-tax-scenario.md
    template-stress-test.md
    template-pre-decision-checklist.md
```

The skill entry point is `SKILL.md` at the repo root. Template files live in `references/`.

## License

MIT
