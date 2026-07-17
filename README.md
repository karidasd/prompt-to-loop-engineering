![Loop Engineering Banner](docs/assets/banner.png)

# ⚡ From Prompt Engineering to Loop Engineering

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Advanced-red?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/karidasd/prompt-to-loop-engineering?style=for-the-badge)

---

## Η Ιστορία: Πώς Φτάσαμε Εδώ

Όλα ξεκίνησαν με **ένα απλό κουτί κειμένου.**

Το 2022, το ChatGPT έδωσε σε εκατομμύρια ανθρώπους πρόσβαση σε ένα γλωσσικό μοντέλο για πρώτη φορά. Η αντίδραση ήταν προβλέψιμη: "Πώς το ρωτάω σωστά για να μου δώσει καλύτερη απάντηση;" — και έτσι γεννήθηκε το **Prompt Engineering**.

### Η Εποχή του Prompt Engineering (2022–2024)

Το Prompt Engineering ήταν η τέχνη του **να διατυπώνεις σωστά την ερώτησή σου.** Μάθαμε να:
- Γράφουμε λεπτομερείς οδηγίες (`"Act as a senior engineer..."`)
- Δίνουμε παραδείγματα πριν το ερώτημα (few-shot)
- Ζητάμε από το μοντέλο να "σκεφτεί βήμα-βήμα" (chain-of-thought)

Αυτό δούλεψε — μέχρι ενός σημείου.

### Το Πρόβλημα

Όσο και να βελτιώνεις ένα prompt, **υπάρχει ένα φράγμα που δεν μπορείς να περάσεις:**

```
Εσύ  →  [Prompt]  →  Μοντέλο  →  Απάντηση  →  ΤΕΛΟΣ
```

Αυτή η αρχιτεκτονική είναι **one-shot**: ένα ερώτημα, μία απάντηση, τέλος. Δεν μπορείς να κάνεις το μοντέλο να:
- ❌ Ελέγξει αν η απάντησή του είναι σωστή
- ❌ Τραβήξει δεδομένα από το internet ή βάσεις δεδομένων
- ❌ Δοκιμάσει ξανά αν κάτι δεν δούλεψε
- ❌ Συντονίσει με άλλα μοντέλα για πολύπλοκες εργασίες

### Η Λύση: Loop Engineering (2025–2026)

Αντί για ένα prompt → μία απάντηση, οι μηχανικοί άρχισαν να χτίζουν **κλειστούς βρόχους (loops):**

```
Εσύ  →  [Task]  →  Agent  →  Σκέψη  →  Ενέργεια  →  Παρατήρηση
                      ↑                                      |
                      └─────────── Επαναλαμβάνεται ──────────┘
                                   μέχρι το έργο να τελειώσει
```

Τώρα το μοντέλο δεν απαντάει απλώς — **δουλεύει.** Χρησιμοποιεί εργαλεία, ελέγχει τη δουλειά του, διορθώνει λάθη, και σταματάει μόνο όταν το αποτέλεσμα πληροί ποιοτικά κριτήρια.

**Αυτή είναι η διαφορά μεταξύ ενός chatbot και ενός AI agent.**

---

## Το Πλήρες Spectrum: 7 Επίπεδα

```
ΕΠΙΠΕΔΟ 1          ΕΠΙΠΕΔΟ 2          ΕΠΙΠΕΔΟ 3
Zero-Shot     →    Few-Shot      →    Chain-of-Thought
"Ρώτα απλά"       "Δώσε παράδειγμα"  "Σκέψου βήμα-βήμα"

     ▼ ΤΟ ΦΡΑΓΜΑ ΤΟΥ PROMPT ENGINEERING ▼

ΕΠΙΠΕΔΟ 4          ΕΠΙΠΕΔΟ 5          ΕΠΙΠΕΔΟ 6          ΕΠΙΠΕΔΟ 7
Tool Use      →    ReAct Loop    →    Self-Correction →   Multi-Agent
"Πρόσβαση σε       "Σκέψη +           "Παράγε →          "Πολλοί agents
 εξωτερικά          Ενέργεια +          Κριτίκαρε →        συνεργάζονται
 εργαλεία"          επανάληψη"          Διόρθωσε"           με orchestrator"
```

---

## 📂 Δομή Αρχείων

### Part 1 — Prompt Engineering (Levels 1-3)
| Level | Αρχείο | Τι μαθαίνεις |
|---|---|---|
| 1 | [`01_zero_shot.py`](01_prompt_engineering/01_zero_shot.py) | Το baseline. Μία οδηγία, μία απάντηση. Καταλαβαίνεις γρήγορα τους περιορισμούς. |
| 2 | [`02_few_shot.py`](01_prompt_engineering/02_few_shot.py) | Παραδείγματα αγκυρώνουν τη συμπεριφορά. Η έξοδος γίνεται προβλέψιμη. |
| 3 | [`03_chain_of_thought.py`](01_prompt_engineering/03_chain_of_thought.py) | Αναγκάζεις το μοντέλο να σκεφτεί φωναχτά. Το ανώτατο επίπεδο single-pass thinking. |

### Part 2 — Loop Engineering (Levels 4-7)
| Level | Αρχείο | Τι μαθαίνεις |
|---|---|---|
| 4 | [`01_tool_use.py`](02_loop_engineering/01_tool_use.py) | Το μοντέλο αποφασίζει μόνο του πότε και ποιο εργαλείο να καλέσει. Η πρώτη επαφή με τον πραγματικό κόσμο. |
| 5 | [`02_react_loop.py`](02_loop_engineering/02_react_loop.py) | **Thought → Action → Observation → επανάληψη.** Το θεμέλιο κάθε AI agent. |
| 6 | [`03_self_correction.py`](02_loop_engineering/03_self_correction.py) | **Generate → Critique → Revise.** Το μοντέλο αξιολογεί και βελτιώνει τη δική του δουλειά σε loop. |
| 7 | [`04_multi_agent.py`](02_loop_engineering/04_multi_agent.py) | Orchestrator + Researcher + Writer + Critic. Κάθε agent έχει ρόλο. Το αποτέλεσμα είναι ανώτερο από ό,τι μπορεί να κάνει ένας agent μόνος. |

---

## Γιατί Έγινε Αυτή η Αλλαγή;

Τρεις τεχνολογικές αλλαγές το επέτρεψαν:

**1. Τα μοντέλα έγιναν αρκετά έξυπνα για να χρησιμοποιούν εργαλεία αξιόπιστα.**
Το function calling του GPT-4 (2023) έδωσε στα μοντέλα τη δυνατότητα να αλληλεπιδρούν με εξωτερικά APIs με δομημένο τρόπο — ένα πράγμα που τα παλαιότερα μοντέλα δεν μπορούσαν να κάνουν αξιόπιστα.

**2. Το κόστος inference έπεσε δραματικά.**
Το να τρέξεις 10 inference calls για ένα task που παλιά χρειαζόταν 1 έγινε οικονομικά βιώσιμο. Αυτό επέτρεψε τους loops.

**3. Frameworks όπως LangChain, LangGraph, και AutoGen αφαίρεσαν την πολυπλοκότητα.**
Δεν χρειάζεται να χτίσεις τον orchestrator από το μηδέν. Τα frameworks αναλαμβάνουν τη διαχείριση state, memory, και tool routing.

---

## Prompt Engineering vs Loop Engineering — Side by Side

| | Prompt Engineering | Loop Engineering |
|---|---|---|
| **Execution model** | Single forward pass | Iterative loop |
| **Tools** | None (text only) | APIs, databases, code execution |
| **Error handling** | You retry manually | Agent retries automatically |
| **Self-evaluation** | Not possible | Built-in critique step |
| **Memory** | Context window only | Persistent memory store |
| **Multi-step tasks** | Limited by context | Unlimited (loop continues) |
| **Coordination** | Single model | Multi-agent orchestration |
| **Output quality** | Depends on prompt | Improves through iterations |
| **Cost per task** | 1 API call | N API calls (N = loop iterations) |
| **Best for** | Simple Q&A, formatting | Complex tasks, autonomous work |

---

## 🗺️ Roadmap

Patterns we're building next — contributions welcome:

- [ ] **Level 8: Plan-and-Execute** — agent plans all steps before executing any. More efficient than ReAct for deterministic tasks.
- [ ] **Level 9: Debate Loop** — two agents argue opposing positions, a judge agent decides. Used in constitutional AI.
- [ ] **Level 10: Reflection Loop** — agent reviews its own failure history before starting a new task.
- [ ] **Framework equivalents** — LangGraph, AutoGen, and CrewAI versions of each pattern.
- [ ] **Benchmarks** — automated quality metrics for each level vs the previous.

---

## 🎁 Bonus Patterns

Beyond the 7 core levels, the `03_patterns/` directory contains advanced patterns:

| Pattern | File | What It Adds |
|---|---|---|
| Memory Loop | [`memory_loop.py`](03_patterns/memory_loop.py) | Agent remembers across tasks — improves over time |

---



```bash
git clone https://github.com/karidasd/prompt-to-loop-engineering.git
cd prompt-to-loop-engineering
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here

# Τρέξε τα επίπεδα με τη σειρά για να νιώσεις την εξέλιξη
python 01_prompt_engineering/01_zero_shot.py
python 01_prompt_engineering/02_few_shot.py
python 01_prompt_engineering/03_chain_of_thought.py
python 02_loop_engineering/01_tool_use.py
python 02_loop_engineering/02_react_loop.py
python 02_loop_engineering/03_self_correction.py
python 02_loop_engineering/04_multi_agent.py
```

**Συμβατό με κάθε OpenAI-compatible API** — OpenAI, Groq, Ollama, Azure OpenAI.

---

## 📖 Βιβλιογραφία

- [ReAct: Synergizing Reasoning and Acting in LLMs](https://arxiv.org/abs/2210.03629) — η επιστημονική βάση του ReAct loop
- [Constitutional AI — Anthropic](https://arxiv.org/abs/2212.08073) — το θεωρητικό υπόβαθρο του self-correction
- [Toolformer](https://arxiv.org/abs/2302.04761) — πώς τα μοντέλα μαθαίνουν να χρησιμοποιούν εργαλεία
- [LangGraph](https://github.com/langchain-ai/langgraph) — production-grade loop orchestration
- [AutoGen — Microsoft](https://github.com/microsoft/autogen) — multi-agent framework

---

> Built by **[DARKAIS Data Science](https://github.com/karidasd)** · 2026
> Αν αυτό το repo άλλαξε τον τρόπο που σκέφτεσαι για AI systems — δώσε ένα ⭐
