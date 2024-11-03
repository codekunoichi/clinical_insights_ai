from openai import OpenAI
import os
from app.ai_model import AIModel


client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
client.organization = os.getenv('OPENAI_ORG_ID')

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
    
    def get_followup(self, user_prompt) -> str:
        
        # Example of calling OpenAI API
        # Format the messages for the ChatCompletion API
        messages = [
            {"role": "system", "content": "Provide a JSON array where each object includes 'followup_details' and 'due_date' for each item in the patient's 'Next Steps' section. For each item, if a due date is specified, calculate it based on the visit date and include it in 'due_date' in mm/dd/yyyy format. If no specific time frame is given, set 'due_date' to 'n/a'."},
            {"role": "user", "content": user_prompt}
        ]

        # Use the fine tuned followup-assistant-5a model for chat-based completion
        response = client.chat.completions.create(
            model="ft:gpt-4o-mini-2024-07-18:mdland-international:followup-assitance-5a:APTjpmCz",
            messages=messages,
            temperature=0.5,
            n=1,
            #temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response
    
follow_up_note = """
Date of Visit: 01/01/2024
Next steps:
- Return for annual wellness check in 1 year and  3 months.
- Routine CBC Panel check in 90 days.
- Return for blood pressure check in a quarter
- Maintain a healthy weight.
"""
openai_client = OpenAIModel(None)
response = openai_client.get_followup(follow_up_note)
print(response.choices[0].message.content)