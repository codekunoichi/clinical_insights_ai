from abc import ABC, abstractmethod
from app.prompt_generator import AbstractPromptGenerator

class AIModel(ABC):
    def __init__(self, prompter: AbstractPromptGenerator):
        self.prompter = prompter

    def call_model(self, text_to_run) -> str:
        system_prompt, user_prompt = self.prompter.generate_prompt(text_to_run)
        return self.get_summary(system_prompt, user_prompt)
    
    def call_model_and_scrub(self, text_to_run) -> str:
        system_prompt, user_prompt = self.prompter.generate_prompt(text_to_run)
        return self.convert_to_ascii(self.get_summary(system_prompt, user_prompt))

    @abstractmethod
    def get_summary(self, system_prompt, user_prompt) -> str:
        """Abstract method to call the AI model with a specific prompt."""
        pass

    # Function to convert to ASCII-friendly output (removes Markdown-like syntax)
    def convert_to_ascii(self, text):
        # Replace bold markdown (**text**) with dashes
        text = text.replace('**', '')
        
        # Replace bullet points (-) with dashes (--)
        #text = text.replace('- ', '-- ')
        
        # Return the converted text
        return text