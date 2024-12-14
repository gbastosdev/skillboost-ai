from openai import OpenAI
from fastapi import status
from fastapi.responses import JSONResponse
import os

class AIController():
	ai_session = None
	def __init__(self):
		self.ai_session = OpenAI(
			base_url="https://api-inference.huggingface.co/v1/",
			api_key= os.environ['HF_KEY'])

	def ai_response(self, message):
		try:

			messages = [{
				"role": "user",
				"content": message
			}]

			completion = self.ai_session.chat.completions.create(
				model="Qwen/QwQ-32B-Preview", 
				messages=messages, 
				max_tokens=500
			)
		except Exception as e:
			raise JSONResponse(content=f'Error occurred: {e}', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

		return JSONResponse(content=completion.choices[0].message.content, status_code=status.HTTP_200_OK)
	