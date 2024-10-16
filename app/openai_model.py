from openai import OpenAI
import os
from app.ai_model import AIModel


client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

class OpenAIModel(AIModel):
    def get_summary(self, system_prompt, user_prompt) -> str:
        # The logic that was originally in openai_utils.py for calling OpenAI
        # Example of calling OpenAI API
        # Format the messages for the ChatCompletion API
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        # Use the gpt-3.5-turbo model for chat-based completion
        response = client.chat.completions.create(
            model= "gpt-4-turbo", #"gpt-4o-mini" ,
            messages=messages,
            temperature=0.5,
            max_tokens=500,
            n=1
        )

        # Extract the response text
        summary = response.choices[0].message.content.strip()
        return summary