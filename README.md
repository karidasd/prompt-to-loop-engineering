![Loop Engineering Banner](docs/assets/banner.png)

# ⚡ From Prompt Engineering to Loop Engineering

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Advanced-red?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/karidasd/prompt-to-loop-engineering?style=for-the-badge)

---

> **Prompt engineering is dead. Long live loop engineering.**
>
> Writing clever prompts was the skill of 2022-2023. It's table stakes now.
> The engineers building serious AI systems in 2026 don't think in prompts — they think in **loops**: iterative, self-correcting, tool-using agents that run until a quality condition is met.
>
> This repository is the complete progression. From zero-shot to multi-agent orchestration. With real, runnable Python code at every step.

---

## The Mental Model Shift

```
PROMPT ENGINEERING (2022-2023)      LOOP ENGINEERING (2025-2026)
─────────────────────────────       ──────────────────────────────
You → Prompt → Model → Answer       You → Task → Agent Loop → Result
                                           ↑                      |
One shot. Commit. Hope.                    └──── Tools / Memory ──┘

Input quality determines output.    The loop runs until quality is met.
You bear the cognitive load.        The system bears the cognitive load.
```

---

## 📂 The Progression (7 Levels)

### Part 1 — Prompt Engineering
| Level | File | Concept |
|---|---|---|
| 1 | [`01_zero_shot.py`](01_prompt_engineering/01_zero_shot.py) | One instruction. One answer. The baseline. |
| 2 | [`02_few_shot.py`](01_prompt_engineering/02_few_shot.py) | Examples anchor the model. Output becomes predictable. |
| 3 | [`03_chain_of_thought.py`](01_prompt_engineering/03_chain_of_thought.py) | Force step-by-step reasoning. The ceiling of single-pass thinking. |

### Part 2 — Loop Engineering
| Level | File | Concept |
|---|---|---|
| 4 | [`01_tool_use.py`](02_loop_engineering/01_tool_use.py) | The model reaches outside itself. Real-world data enters the loop. |
| 5 | [`02_react_loop.py`](02_loop_engineering/02_react_loop.py) | Thought → Action → Observation → repeat. The ReAct pattern. |
| 6 | [`03_self_correction.py`](02_loop_engineering/03_self_correction.py) | Generate → Critique → Revise → repeat until quality passes. |
| 7 | [`04_multi_agent.py`](02_loop_engineering/04_multi_agent.py) | Orchestrator coordinates Researcher + Writer + Critic agents. |

---

## 💣 Why Prompt Engineering Hits a Wall

You can write the perfect prompt. You still can't make it:
- **Retry** when a tool call fails
- **Verify** a factual claim against a live database
- **Evaluate** its own output and improve it
- **Coordinate** multiple specialized models

Prompt engineering optimizes a single forward pass. Loop engineering builds a system that runs until the work is actually done.

---

## The 5 Loop Patterns (Cheat Sheet)

```
1. TOOL LOOP          Model → Tool Call → Observation → Model
2. REACT LOOP         Thought → Action → Observation → Thought → ...
3. SELF-CORRECTION    Generate → Critique → Revise → (repeat)
4. PLAN-EXECUTE       Plan all steps → Execute each → Verify
5. MULTI-AGENT        Orchestrator → [Agent A | Agent B | Agent C] → Merge
```

---

## 🚀 Run the Examples

```bash
git clone https://github.com/karidasd/prompt-to-loop-engineering.git
cd prompt-to-loop-engineering
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here

# Run in order
python 01_prompt_engineering/01_zero_shot.py
python 01_prompt_engineering/02_few_shot.py
python 01_prompt_engineering/03_chain_of_thought.py
python 02_loop_engineering/01_tool_use.py
python 02_loop_engineering/02_react_loop.py
python 02_loop_engineering/03_self_correction.py
python 02_loop_engineering/04_multi_agent.py
```

**Works with any OpenAI-compatible API** (OpenAI, Groq, Ollama, Azure OpenAI, etc.)

---

## 📖 Further Reading

- [ReAct: Synergizing Reasoning and Acting in LLMs](https://arxiv.org/abs/2210.03629)
- [Constitutional AI — Anthropic](https://arxiv.org/abs/2212.08073)
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
- [AutoGPT — Early agentic architecture](https://github.com/Significant-Gravitas/AutoGPT)
- [LangGraph — Production loop orchestration](https://github.com/langchain-ai/langgraph)

---

## 🤝 Contributing

This repo follows the levels. If you have a new pattern that belongs between or after existing levels, open a PR. Each file should:
1. Start with a docstring explaining the concept and its limitations
2. Have a runnable, self-contained example
3. End with a comment block explaining what this pattern still can't do

---

> Built by **[DARKAIS Data Science](https://github.com/karidasd)** · 2026
> If this changed how you think about AI systems — give it a ⭐
