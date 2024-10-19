from abc import ABC, abstractmethod

class AbstractPromptGenerator(ABC):
    @abstractmethod
    def generate_prompt(self, note) -> str:
        """Abstract method to generate the system prompt and user prompt pair for the model."""
        pass

class BillerPrompter(AbstractPromptGenerator):
    def generate_prompt(self, note) -> str:
        # Set the system prompt for the Biller persona
        # Prompt components
        persona = (
            "You are an expert in Ambulatory Patient Care Billing and Coding. You excel at breaking down complex patient visit notes "
            "into appropriate CPT Codes. You are also an expert HCC Coder.\n"
        )
        instruction = "Identify the key CPT of the patient chart from given visit summary.\n"
        context = (
            "Your CPT should extract the most crucial points that can help billers create the right CPT Code for the given visit summary.\n"
        )
        data_format = (
            "Create a bullet-point CPT Code Recommendation.\n"
        )
        audience = (
            "The summary is designed for Revenue Cycle Management Team Billers to create claims with the right CPT Code for the given visit summary.\n"
        )
        tone = "The tone should be professional and clear.\n"
        data = f"Text to recommend CPT From: {note}"

        # Combine all components into one prompt
        user_prompt = data_format + audience + tone + data

        # Combine to form system prompts
        system_prompt = persona + instruction + context 

        return system_prompt, user_prompt
    
class DiagnosisCodePrompter(AbstractPromptGenerator):
    def generate_prompt(self, note) -> str:
        # Set the system prompt for the Biller persona
        # Prompt components
        persona = (
            "You are an expert in Ambulatory Patient Care Billing and Coding. You excel at breaking down complex patient visit notes "
            "into appropriate ICD-10 Codes. You are also an expert HCC Coder.\n"
        )
        instruction = "Identify the key ICD-10 code from the patient chart for given visit summary.\n"
        context = (
            "Your ICD-10 should extract the most most relevant diagnosis for the given chart notes that can help billers create the right ICD-10 Code for the given visit summary.\n"
        )
        data_format = (
            "Create a bullet-point ICD-10 Code Recommendation.\n"
        )
        audience = (
            "The summary is designed for Revenue Cycle Management Team Billers to create claims with the right ICD-10 Code for the given visit summary.\n"
        )
        tone = "The tone should be professional and clear.\n"
        data = f"Text to recommend ICD-10 From: {note}"

        # Combine all components into one prompt
        user_prompt = data_format + audience + tone + data

        # Combine to form system prompts
        system_prompt = persona + instruction + context 

        return system_prompt, user_prompt
    

class SummarizeChartPrompter(AbstractPromptGenerator):
    def generate_prompt(self, note) -> tuple:
        # System prompt (for model behavior and boundaries)
        persona = (
            "You are an expert in Large Language Models and clinical data analysis, specializing in summarizing "
            "patient visit notes for busy healthcare professionals. You are also a highly experienced primary care physician.\n"
        )
        instruction = (
            "Your task is to accurately summarize the key findings from the patient's visit note without adding any inference, "
            "speculation, or additional information. Stay strictly within the boundaries of the provided text, focusing only on "
            "what is explicitly mentioned.\n"
        )
        context = (
            "The summary should highlight the most crucial points from the visit note that will help medical assistants, "
            "physicians, and other healthcare providers quickly grasp the patient's condition, treatment plan, and any important "
            "trends or changes. The summary should be actionable and relevant to ongoing patient care.\n"
        )
        
        # User prompt (for generating the actual summary)
        data_format = (
            "Create a concise, bullet-point summary of the key findings. Each bullet should represent an important fact from the visit note, "
            "such as diagnoses, treatments, lab results, and notable trends.\n"
        )
        follow_up = (
            "After the bullet points, provide a brief paragraph summarizing the patient's overall condition and any "
            "important trends that have emerged from the visit. Avoid making any assumptions or adding extra context.\n"
        )
        audience = (
            "This summary is intended for busy healthcare providers who need a quick overview of the patient's "
            "condition and the key takeaways from the visit.\n"
        )
        tone = "The tone should be professional, clear, and concise.\n"
        data = f"Patient Visit Note to summarize: {note}"

        # Combine prompts
        user_prompt = data_format + follow_up + audience + tone + data
        system_prompt = persona + instruction + context

        return system_prompt, user_prompt
    
class LabResultEmailer(AbstractPromptGenerator):
    def generate_prompt(self, lab_results) -> tuple:
        # System prompt components
        persona = (
            "You are an expert in clinical data analysis, specializing in summarizing lab results in a concise, high-level "
            "manner. Your summaries should avoid specific numerical values and instead focus on general trends.\n"
        )
        instruction = (
            "Summarize the lab results, indicating whether they are normal, mildly elevated, or require follow-up. "
            "Do not include specific values. For normal results, simply list the test names as normal. For any abnormal results, "
            "mention the need for follow-up but avoid disclosing values.\n"
        )
        context = (
            "Summarize lab trends, highlighting results that need attention. Protect patient privacy by omitting exact values."
        )

        # User prompt components
        data_format = (
            "Summarize the lab results provided. Focus on overall trends, listing normal results without values and summarizing "
            "any abnormal results with a brief follow-up recommendation.\n"
        )
        data = f"Lab Results to summarize: {lab_results}"

        # Combine system and user prompts
        system_prompt = persona + instruction + context
        user_prompt = data_format + data

        return system_prompt, user_prompt

    def generate_email(self, summary: str) -> str:
        """Generates a brief email summarizing lab results trends."""
        email_body = (
            "Dear Patient,\n\n"
            "We have reviewed your recent lab results. Here is a brief summary of the key findings:\n\n"
            f"{summary}\n\n"
            "If any of these results are elevated or require follow-up, we recommend contacting your healthcare provider. "
            "Otherwise, there is no need to worry.\n\n"
            "If you have any questions, please feel free to reach out.\n\n"
            "Best regards,\nYour Healthcare Team"
        )
        return email_body