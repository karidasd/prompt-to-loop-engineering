"""
LEVEL 3: Chain-of-Thought (CoT) Prompting
Force the model to reason step by step before giving the final answer.
Dramatically improves accuracy on complex tasks.
The key insight: the model's "thinking" is itself part of the prompt context.
"""

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def chain_of_thought(problem: str) -> dict:
    """
    Returns both the reasoning chain and the final answer.
    Structured output makes the reasoning auditable.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """Solve problems step by step.
First, write your reasoning under <thinking>.
Then write your final answer under <answer>.
Be explicit about every step."""
            },
            {"role": "user", "content": problem}
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    # Parse the structured output
    thinking = content.split("<thinking>")[-1].split("</thinking>")[0].strip() if "<thinking>" in content else ""
    answer = content.split("<answer>")[-1].split("</answer>")[0].strip() if "<answer>" in content else content

    return {"thinking": thinking, "answer": answer}

# Example: a problem that zero-shot often gets wrong
problem = """
A team of 5 engineers works on a codebase.
Each engineer opens 3 PRs per week.
Each PR takes 2 other engineers 45 minutes to review.
How many hours per week does the team spend on code review in total?
"""

result = chain_of_thought(problem)
print("REASONING:\n", result["thinking"])
print("\nFINAL ANSWER:\n", result["answer"])

"""
WHY THIS MATTERS:
- Accuracy on multi-step problems increases dramatically
- The reasoning chain is auditable — you can catch wrong assumptions
- Foundation for self-correction: if the reasoning is wrong, you can catch it

THE WALL:
- Still a single call. The model reasons once and commits.
- If the reasoning goes wrong in step 2, steps 3-10 are all wrong.
- No way to verify intermediate steps with external tools or data.
- This is the ceiling of pure prompt engineering.
"""
