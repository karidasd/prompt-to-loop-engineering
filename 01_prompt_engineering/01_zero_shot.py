"""
LEVEL 1: Zero-Shot Prompting
The most basic form. One instruction. One response. No context, no examples.
The model relies entirely on its pre-trained knowledge.
"""

import os
from openai import OpenAI  # works with any OpenAI-compatible API

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def zero_shot(task: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": task}]
    )
    return response.choices[0].message.content

# Example
result = zero_shot("Summarize the main risks of deploying ML models in production.")
print(result)

"""
LIMITATIONS:
- No control over output format
- No examples to anchor the model's behavior
- Output quality is unpredictable
- One shot — if it fails, you start over manually
"""
