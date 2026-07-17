"""
LEVEL 5: ReAct Loop (Reasoning + Acting)
The model alternates between THINKING and DOING in a loop.
Thought → Action → Observation → Thought → Action → ...
This is where prompt engineering ends and loop engineering begins.

Paper: "ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al., 2022)
"""

import os
import json
import math
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# --- Tools ---
def search_wikipedia(query: str) -> str:
    """Simulated Wikipedia search."""
    mock_db = {
        "Poisson distribution": "A discrete probability distribution expressing the probability of a given number of events occurring in a fixed interval of time. Parameter: lambda (average rate).",
        "Monte Carlo simulation": "A computational algorithm that uses repeated random sampling to obtain numerical results. Used in physics, finance, and AI.",
        "gradient descent": "An optimization algorithm that iteratively moves in the direction of steepest descent of a loss function to find a local minimum.",
    }
    for key, val in mock_db.items():
        if key.lower() in query.lower():
            return val
    return f"No results found for '{query}'."

def calculate(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}, "math": math, "sqrt": math.sqrt, "log": math.log})
        return str(result)
    except Exception as e:
        return f"Error: {e}"

TOOLS = [
    {"type": "function", "function": {
        "name": "search_wikipedia",
        "description": "Search Wikipedia for information about a topic.",
        "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}
    }},
    {"type": "function", "function": {
        "name": "calculate",
        "description": "Evaluate a mathematical expression. Use Python syntax. math module available.",
        "parameters": {"type": "object", "properties": {"expression": {"type": "string"}}, "required": ["expression"]}
    }}
]

TOOL_MAP = {"search_wikipedia": search_wikipedia, "calculate": calculate}

SYSTEM = """You are a research agent. Solve tasks by thinking step-by-step and using tools.
Follow this pattern:
  Thought: what do I need to figure out?
  Action: call a tool
  Observation: read the result
  Thought: what do I know now?
  ... repeat until you have the final answer.
When done, write: FINAL ANSWER: <your answer>"""

def react_loop(task: str, max_steps: int = 8) -> str:
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": task}
    ]

    print(f"\nTASK: {task}\n{'='*60}")

    for step in range(max_steps):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )

        msg = response.choices[0].message
        print(f"\n[Step {step+1}]")

        # Check if we reached the final answer
        if msg.content and "FINAL ANSWER:" in msg.content:
            print(msg.content)
            return msg.content.split("FINAL ANSWER:")[-1].strip()

        # If the model wants to call a tool
        if msg.tool_calls:
            messages.append(msg)
            for tc in msg.tool_calls:
                fn = tc.function.name
                args = json.loads(tc.function.arguments)
                print(f"  Action: {fn}({args})")
                result = TOOL_MAP[fn](**args)
                print(f"  Observation: {result}")
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result
                })
        elif msg.content:
            print(f"  Thought: {msg.content}")
            messages.append({"role": "assistant", "content": msg.content})

    return "Max steps reached without final answer."

# Example
answer = react_loop(
    "What is the Poisson distribution? If lambda=3, what is the probability of exactly 5 events? Use math."
)
print(f"\nFINAL: {answer}")

"""
THE LOOP DIFFERENCE:
- The model iterates — it doesn't commit to one answer immediately
- Each observation can change the next thought
- It can recover from wrong paths by searching again
- This is qualitatively different from prompt engineering — it's a runtime loop
"""
