import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from .env

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain what a transformer architecture is in 3 sentences."}
    ]
)

print(response.content[0].text)
print(f"\n--- Usage ---")
print(f"Input tokens:  {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
