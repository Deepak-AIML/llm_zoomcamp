from openai import OpenAI

# Initialize the client to connect to your local Ollama instance
# Note the change in port from 11434 to 11435
client = OpenAI(base_url="http://localhost:11435/v1", api_key="ollama")

prompt = "What's the formula for energy?"

response = client.chat.completions.create(
    model="gemma:2b",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.0
)

# Print the response
print(response.choices[0].message.content)

# Print the number of completion tokens
print(f"Completion tokens: {response.usage.completion_tokens}")