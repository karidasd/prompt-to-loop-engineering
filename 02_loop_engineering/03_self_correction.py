"""
LEVEL 6: Self-Correction Loop
The model generates output, then evaluates its own output, then fixes it.
Generate → Critique → Revise → (repeat until quality passes)

This is the pattern behind Constitutional AI and most RLHF refinement loops.
In production: reduces hallucinations, catches logical errors, improves format compliance.
"""

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

CRITIQUE_PROMPT = """You are a strict technical editor. Review the following output for:
1. Factual accuracy
2. Logical consistency  
3. Missing important caveats
4. Overconfident claims

Return JSON with keys:
- "passed": true/false
- "score": 1-10
- "issues": list of specific problems (empty if passed)
- "suggestion": one-sentence fix instruction (empty if passed)"""

def generate(task: str, context: str = "") -> str:
    messages = [{"role": "user", "content": task}]
    if context:
        messages.insert(0, {"role": "system", "content": context})
    r = client.chat.completions.create(model="gpt-4o", messages=messages)
    return r.choices[0].message.content

def critique(output: str, original_task: str) -> dict:
    import json
    r = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": CRITIQUE_PROMPT},
            {"role": "user", "content": f"TASK: {original_task}\n\nOUTPUT TO REVIEW:\n{output}"}
        ],
        response_format={"type": "json_object"}
    )
    return json.loads(r.choices[0].message.content)

def revise(original_output: str, issues: list, suggestion: str, task: str) -> str:
    issues_str = "\n".join(f"- {i}" for i in issues)
    r = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": f"""Original task: {task}

Your previous response:
{original_output}

Issues found:
{issues_str}

Fix instruction: {suggestion}

Rewrite the response addressing all issues."""
            }
        ]
    )
    return r.choices[0].message.content

def self_correction_loop(task: str, max_iterations: int = 3) -> str:
    print(f"TASK: {task}\n{'='*60}")

    output = generate(task)
    print(f"\n[DRAFT]\n{output}\n")

    for iteration in range(max_iterations):
        review = critique(output, task)
        score = review.get("score", 0)
        passed = review.get("passed", False)

        print(f"[REVIEW {iteration+1}] Score: {score}/10 | Passed: {passed}")

        if passed or score >= 8:
            print("Quality threshold met. Stopping.")
            break

        issues = review.get("issues", [])
        suggestion = review.get("suggestion", "")
        print(f"  Issues: {issues}")
        print(f"  Fix: {suggestion}\n")

        output = revise(output, issues, suggestion, task)
        print(f"[REVISED]\n{output}\n")

    return output

# Example
final = self_correction_loop(
    "Explain why transformers replaced RNNs for sequence modeling tasks."
)
print(f"\nFINAL OUTPUT:\n{final}")

"""
WHY THIS IS LOOP ENGINEERING:
- The system runs multiple inference passes — not one
- Each pass has a defined role: Generator, Critic, Reviser
- The loop terminates on a quality condition, not a fixed count
- Output quality is systematically higher than single-pass generation

PRODUCTION USES:
- Code generation with automatic test-run feedback
- Report generation with fact-checking loops
- Legal/medical text with compliance checking
- Any domain where quality > speed
"""
