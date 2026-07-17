"""
LEVEL 4: Tool Use (Function Calling)
The model can now reach outside itself.
It decides WHEN to call a tool and WHAT arguments to pass.
This is the first step beyond pure text — the model interacts with the real world.
"""

import os
import json
import requests
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# --- Define real tools the model can call ---

def get_weather(city: str) -> dict:
    """Simulated weather tool (replace with real API in production)."""
    mock_data = {
        "Athens": {"temp_c": 34, "condition": "Sunny", "humidity": 45},
        "London": {"temp_c": 18, "condition": "Cloudy", "humidity": 80},
        "New York": {"temp_c": 28, "condition": "Partly Cloudy", "humidity": 60},
    }
    return mock_data.get(city, {"error": f"No data for {city}"})

def calculate(expression: str) -> dict:
    """Safe math evaluator."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

# --- Tool schema (what the model sees) ---
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"}
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Math expression to evaluate"}
                },
                "required": ["expression"]
            }
        }
    }
]

TOOL_MAP = {"get_weather": get_weather, "calculate": calculate}

def run_with_tools(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]

    # First call: model decides if/which tool to use
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )

    msg = response.choices[0].message

    # If the model called a tool, execute it and feed result back
    if msg.tool_calls:
        messages.append(msg)  # add assistant's tool call to history

        for tool_call in msg.tool_calls:
            fn_name = tool_call.function.name
            fn_args = json.loads(tool_call.function.arguments)

            print(f"  [TOOL CALL] {fn_name}({fn_args})")
            result = TOOL_MAP[fn_name](**fn_args)
            print(f"  [TOOL RESULT] {result}")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })

        # Second call: model synthesizes tool results into final answer
        final = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return final.choices[0].message.content

    return msg.content

# Examples
print(run_with_tools("What's the weather in Athens and how many degrees Fahrenheit is that?"))
print(run_with_tools("If I work 7.5 hours a day for 22 working days, how many hours is that?"))

"""
THE LEAP:
- The model now has agency over external systems
- It decides what to call, when, and with what arguments
- The result is fed back in — the model synthesizes real-world data

STILL NOT A LOOP:
- It calls tools and stops. One pass.
- It cannot retry if a tool fails
- It cannot plan sequences of tool calls dynamically
- It cannot evaluate its own output quality
"""
