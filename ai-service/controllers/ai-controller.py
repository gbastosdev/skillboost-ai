from openai import OpenAI
import os

client = OpenAI(
	base_url="https://api-inference.huggingface.co/v1/",
	api_key= os.environ['HF_KEY']
)

messages = [
	{
		"role": "user",
		"content": "Create basic python backend small challenge for practicing."
	}
]

completion = client.chat.completions.create(
    model="Qwen/QwQ-32B-Preview", 
	messages=messages, 
	max_tokens=500
)

print(completion.choices[0].message.content)