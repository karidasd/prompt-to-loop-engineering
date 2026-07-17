"""
LEVEL 8: Memory Loop (Bonus Pattern)
The agent remembers across multiple tasks using a persistent memory store.
Without memory, every loop starts from zero. With memory, the agent improves over time.

Real-world use: customer support agents, coding assistants, research agents.
"""

import os
import json
from datetime import datetime
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# ─────────────────────────────────────────────
# Simple persistent memory store (JSON file)
# In production: replace with vector DB (Chroma, Pinecone, Weaviate)
# ─────────────────────────────────────────────

MEMORY_FILE = "agent_memory.json"

def load_memory() -> list:
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_memory(memories: list):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memories, f, indent=2)

def add_to_memory(task: str, result: str, memories: list) -> list:
    memories.append({
        "timestamp": datetime.now().isoformat(),
        "task": task,
        "result": result
    })
    # Keep last 20 memories to stay within context limits
    return memories[-20:]

def format_memory_context(memories: list) -> str:
    if not memories:
        return "No previous interactions."
    lines = []
    for m in memories[-5:]:  # inject last 5 for context
        lines.append(f"[{m['timestamp'][:10]}] Task: {m['task']}\nResult: {m['result'][:200]}...")
    return "\n\n".join(lines)

# ─────────────────────────────────────────────
# Memory-aware agent
# ─────────────────────────────────────────────

def run_with_memory(task: str) -> str:
    memories = load_memory()
    memory_context = format_memory_context(memories)

    system_prompt = f"""You are a persistent AI assistant with memory of past interactions.

PAST INTERACTIONS:
{memory_context}

Use this context to:
- Avoid repeating mistakes from previous tasks
- Build on previous answers where relevant
- Reference past work when appropriate
- Improve your responses based on what you've learned"""

    print(f"\n[TASK] {task}")
    print(f"[MEMORY] {len(memories)} past interactions loaded")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": task}
        ]
    )

    result = response.choices[0].message.content

    # Save this interaction to memory
    memories = add_to_memory(task, result, memories)
    save_memory(memories)
    print(f"[MEMORY] Saved. Total memories: {len(memories)}")

    return result

# Run multiple tasks — notice how memory accumulates
tasks = [
    "Explain what a ReAct loop is in 2 sentences.",
    "Now compare it to what you just explained — how does self-correction improve on ReAct?",
    "Summarize everything we've discussed so far about AI agent patterns."
]

for task in tasks:
    result = run_with_memory(task)
    print(f"\n[RESULT]\n{result}\n{'─'*60}")

"""
THE MEMORY DIFFERENCE:
- Task 1: No context, fresh start
- Task 2: The agent references its own previous explanation
- Task 3: The agent synthesizes across the full conversation history

WITHOUT MEMORY: Every task is isolated. The agent never gets smarter.
WITH MEMORY:    The agent accumulates context. Answers improve over time.

LIMITATIONS OF THIS PATTERN:
- Memory is text-based (not semantic) — irrelevant memories still use context tokens
- In production, use a vector DB with semantic retrieval
- Shared memory between agents requires careful design to avoid conflicts
"""
