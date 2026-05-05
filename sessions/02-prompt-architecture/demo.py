from dotenv import load_dotenv
load_dotenv()

import anthropic

client = anthropic.Anthropic()

# --- Demo 1: No system prompt ---
response_basic = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=512,
    messages=[
        {"role": "user", "content": "Review this code: def add(a,b): return a+b"}
    ]
)

# --- Demo 2: With system prompt + XML structure ---
response_engineered = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=512,
    system="You are a senior Python engineer. Review code for correctness, \
performance, and Pythonic style. Flag issues with line numbers. \
Return feedback as a numbered list with severity ratings.",
    messages=[
        {"role": "user", "content": """
<code>
def add(a,b): return a+b
</code>

<task>
Review this code and identify any issues or improvements.
</task>
"""}
    ]
)

print("=== BASIC (no system prompt) ===")
print(response_basic.content[0].text)
print(f"\nTokens — in: {response_basic.usage.input_tokens} out: {response_basic.usage.output_tokens}")

print("\n=== ENGINEERED (system prompt + XML) ===")
print(response_engineered.content[0].text)
print(f"\nTokens — in: {response_engineered.usage.input_tokens} out: {response_engineered.usage.output_tokens}")
