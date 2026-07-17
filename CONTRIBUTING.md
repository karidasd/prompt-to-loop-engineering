# Contributing to prompt-to-loop-engineering

Thank you for taking the time to contribute. This repository follows a strict philosophy: **every file must teach something that the previous file cannot do.**

---

## What We Accept

### ✅ New Loop Patterns
If you have a pattern that belongs in the progression (between or after existing levels), open a PR. Examples of patterns we'd like to add:
- **Memory Loop** — agent that remembers across sessions using a vector store
- **Plan-and-Execute** — agent that plans all steps before executing any
- **Debate Loop** — two agents argue opposing positions, third agent decides
- **Reflection Loop** — agent reflects on its own past failures before retrying

### ✅ Better Tool Implementations
Replace simulated tools with real API integrations (Serper, Tavily, Wikipedia API, WolframAlpha).

### ✅ Framework Equivalents
For each vanilla pattern, add a framework equivalent:
- `02_react_loop_langgraph.py` — same ReAct loop, built with LangGraph
- `04_multi_agent_autogen.py` — same multi-agent, built with AutoGen

### ✅ Bug Fixes and Improvements
If a code example has a bug, an unclear comment, or is missing error handling — fix it.

---

## What We Don't Accept

- ❌ Prompt tricks or jailbreaks
- ❌ Examples without the docstring explaining what the pattern **can't** do
- ❌ Untested code (run it before submitting)
- ❌ Wrapper libraries that abstract the actual mechanics (the point is to see the mechanics)

---

## File Structure

Each contribution file must:

```python
"""
LEVEL X: [Pattern Name]
One sentence: what this pattern does.
One sentence: why the previous level wasn't enough.

[Optional: paper reference]
"""

# --- your code ---

"""
WHY THIS IS A STEP FORWARD:
- bullet points

THE REMAINING LIMITATIONS:
- what this pattern still can't do
- this is what motivates the next level
"""
```

---

## PR Process

1. Fork the repo
2. Create a branch: `git checkout -b pattern/memory-loop`
3. Add your file in the correct folder with the correct naming convention
4. Run it and paste the output in the PR description
5. Submit

We review PRs within 48 hours.
