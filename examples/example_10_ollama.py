"""
Documentation: https://github.com/ollama/ollama-python
"""
import ollama

# Use generate() for one-shot prompts
response = ollama.generate(prompt="Hello, world", model="llama3.2")
print(response.response)

# Use chat() for messages w/ context
prompt = "Write a hello world script in python"

messages = [{"role": "user", "content": prompt}]
response: ollama.ChatResponse = ollama.chat(
    model="llama3", messages=messages
)

print(response["message"]["content"])  # Access via keys
print(response.message.content)        # Access via attributes
