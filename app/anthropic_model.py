import os
from anthropic import Anthropic
from app.ai_model import AIModel

# Initialize the Anthropic client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class AnthropicModel(AIModel):
    def get_summary(self, system_prompt, user_prompt) -> str:
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=500,
            temperature=0.5,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )
        
        summary = response.content[0].text
        return summary