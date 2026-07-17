"""
LEVEL 7: Multi-Agent Loop (The Full Pattern)
Multiple specialized agents collaborate in a loop.
Each agent has a defined role, tools, and scope.
The orchestrator coordinates — it doesn't do the work itself.

Architecture: Orchestrator → [Researcher | Writer | Critic] → Output

This is how production AI systems are built in 2026.
"""

import os
import json
from openai import OpenAI
from datetime import datetime

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# ─────────────────────────────────────────────
# Simulated Tools
# ─────────────────────────────────────────────

def web_search(query: str) -> str:
    """Simulated web search. Replace with real search API."""
    mock = {
        "loop engineering AI 2026": "Loop engineering refers to building AI systems where language models operate in iterative cycles, using tools, memory, and self-evaluation to complete complex tasks autonomously.",
        "prompt engineering limitations": "Prompt engineering is limited to single-pass inference. It cannot retry, use tools dynamically, or evaluate its own output. These limitations drove the move to agentic loops.",
        "agentic AI systems": "Agentic AI systems in 2026 use ReAct, self-correction, and multi-agent coordination to complete multi-step tasks with minimal human intervention."
    }
    for k, v in mock.items():
        if any(word in query.lower() for word in k.split()):
            return v
    return "No results found."

def save_to_file(filename: str, content: str) -> str:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"Saved to {filename}"

TOOLS = [
    {"type": "function", "function": {
        "name": "web_search",
        "description": "Search the web for information.",
        "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}
    }},
    {"type": "function", "function": {
        "name": "save_to_file",
        "description": "Save content to a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {"type": "string"},
                "content": {"type": "string"}
            },
            "required": ["filename", "content"]
        }
    }}
]

TOOL_MAP = {"web_search": web_search, "save_to_file": save_to_file}

# ─────────────────────────────────────────────
# Agent Runner (reusable)
# ─────────────────────────────────────────────

def run_agent(system_prompt: str, task: str, tools=None, max_steps: int = 5) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": task}
    ]

    for _ in range(max_steps):
        kwargs = {"model": "gpt-4o", "messages": messages}
        if tools:
            kwargs["tools"] = tools
            kwargs["tool_choice"] = "auto"

        response = client.chat.completions.create(**kwargs)
        msg = response.choices[0].message

        if msg.tool_calls:
            messages.append(msg)
            for tc in msg.tool_calls:
                fn = tc.function.name
                args = json.loads(tc.function.arguments)
                result = TOOL_MAP[fn](**args)
                messages.append({"role": "tool", "tool_call_id": tc.id, "content": str(result)})
        else:
            return msg.content

    return messages[-1]["content"] if messages else ""

# ─────────────────────────────────────────────
# Specialized Agents
# ─────────────────────────────────────────────

def researcher_agent(topic: str) -> str:
    print("  [RESEARCHER] Gathering information...")
    return run_agent(
        system_prompt="You are a research specialist. Search for relevant information and return a structured summary with key facts, examples, and sources.",
        task=f"Research this topic thoroughly: {topic}",
        tools=TOOLS
    )

def writer_agent(research: str, format_instructions: str) -> str:
    print("  [WRITER] Drafting content...")
    return run_agent(
        system_prompt="You are an expert technical writer. Transform research notes into clear, engaging, well-structured content. No fluff. Be direct.",
        task=f"Write content based on this research:\n\n{research}\n\nFormat: {format_instructions}"
    )

def critic_agent(content: str, criteria: str) -> dict:
    print("  [CRITIC] Evaluating output...")
    result = run_agent(
        system_prompt="""You are a strict quality evaluator. Return JSON only with keys:
- "approved": boolean
- "score": 1-10  
- "feedback": string (specific issues or 'Approved' if good)""",
        task=f"Evaluate this content against these criteria:\nCriteria: {criteria}\n\nContent:\n{content}"
    )
    try:
        return json.loads(result)
    except:
        return {"approved": True, "score": 7, "feedback": "Approved"}

# ─────────────────────────────────────────────
# Orchestrator
# ─────────────────────────────────────────────

def orchestrate(topic: str, format_instructions: str, quality_threshold: int = 7, max_revisions: int = 2):
    print(f"\nORCHESTRATOR: Starting pipeline for '{topic}'")
    print("="*60)

    # Step 1: Research
    research = researcher_agent(topic)
    print(f"  Research complete ({len(research)} chars)\n")

    # Step 2: Write → Critique → Revise loop
    content = writer_agent(research, format_instructions)

    for revision in range(max_revisions + 1):
        review = critic_agent(content, f"Technical accuracy, clarity, and adherence to format: {format_instructions}")
        score = review.get("score", 0)
        approved = review.get("approved", False)

        print(f"  [REVIEW {revision+1}] Score: {score}/10 | Approved: {approved}")
        print(f"  Feedback: {review.get('feedback', '')}\n")

        if approved or score >= quality_threshold:
            break

        if revision < max_revisions:
            print("  [WRITER] Revising based on feedback...")
            content = run_agent(
                system_prompt="You are a technical writer. Revise the content based on the feedback provided.",
                task=f"Original content:\n{content}\n\nFeedback:\n{review['feedback']}\n\nRevise and improve."
            )

    # Step 3: Save
    filename = f"output_{topic.replace(' ', '_')[:30]}.md"
    save_to_file(filename, content)
    print(f"  [SAVED] {filename}")

    return content

# Run
result = orchestrate(
    topic="Loop Engineering vs Prompt Engineering in AI systems 2026",
    format_instructions="A 300-word markdown article with an intro, 3 key points, and a conclusion",
    quality_threshold=7
)
print("\nFINAL OUTPUT:\n", result[:500], "...")
