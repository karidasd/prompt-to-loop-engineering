"""
LEVEL 2: Few-Shot Prompting
Give the model examples of what you want. It pattern-matches.
The output becomes predictable. The format becomes consistent.
This was the state of the art in 2022.
"""

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a senior code reviewer. 
Classify code review comments into one of: [BUG, STYLE, PERFORMANCE, SECURITY, NITPICK].
Return only the category. Nothing else."""

EXAMPLES = [
    {"role": "user",      "content": "This SQL query is vulnerable to injection attacks."},
    {"role": "assistant", "content": "SECURITY"},
    {"role": "user",      "content": "You should add a space after the comma here."},
    {"role": "assistant", "content": "STYLE"},
    {"role": "user",      "content": "This O(n²) loop will collapse under production load."},
    {"role": "assistant", "content": "PERFORMANCE"},
]

def few_shot_classify(comment: str) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(EXAMPLES)
    messages.append({"role": "user", "content": comment})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0  # deterministic output
    )
    return response.choices[0].message.content

# Example
comments = [
    "The API key is hardcoded in the config file.",
    "Variable name 'x' is not descriptive.",
    "This recursive call has no base case — it will crash."
]

for c in comments:
    print(f"  Comment: {c}")
    print(f"  Category: {few_shot_classify(c)}\n")

"""
IMPROVEMENT OVER ZERO-SHOT:
+ Consistent output format (always one word)
+ Behavior is anchored to your examples
+ Reproducible across runs (temperature=0)

STILL LIMITED:
- Still a single call — no iteration, no correction
- If a comment is ambiguous, it picks one and moves on
- No tool use, no external data, no memory
"""
