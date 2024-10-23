from abc import ABC, abstractmethod

class AbstractPromptGenerator(ABC):
    @abstractmethod
    def generate_prompt(self, note: str, additional_data: str = None) -> tuple:
        """Abstract method to generate the system prompt and user prompt pair for the model."""
        pass
    

class BillerPrompter(AbstractPromptGenerator):
    def generate_prompt(self, note, additional_data: str = None) -> tuple:
        # System prompt components (for model behavior and boundaries)
        persona = (
            "You are an expert in Ambulatory Patient Care Billing and Coding, with specialized expertise in identifying "
            "appropriate CPT and CPT II codes from patient visit notes. You are also an expert HCC Coder.\n"
        )
        instruction = (
            "Your role is to analyze the provided patient visit note and identify the key CPT codes that apply. Focus only on "
            "the information provided in the note and avoid making any assumptions or inferences not explicitly mentioned.\n"
        )
        context = (
            "Extract the most relevant CPT codes based on the procedures performed, referrals, and any evaluations documented in the visit note. "
            "Additionally, consider any CPT II codes related to quality measures, as well as any codes for Social Determinants of Health (SDOH) if applicable. "
            "Provide example CPT II codes and SDOH codes if relevant to the visit note, but only based on the information provided in the text.\n"
        )

        # User prompt components (for generating the actual recommendation)
        data_format = (
            "Create a clear, bullet-point list of CPT code recommendations. Start with the most relevant CPT codes based on "
            "the procedures, treatments, and evaluations performed. Additionally, if applicable, recommend CPT II codes, SDOH-related codes, "
            "and any referral codes. Provide a brief explanation next to each code, and ensure that all recommendations are strictly based "
            "on the text in the visit note.\n"
        )
        follow_up = (
            "Ensure that no inferences or additional assumptions are made beyond what is present in the visit note.\n"
        )
        audience = (
            "The CPT code recommendations are intended for the Revenue Cycle Management Team Billers to accurately create claims based on "
            "the patient visit notes.\n"
        )
        tone = "The tone should be professional, concise, and clear.\n"
        data = f"Text to generate CPT Codes from: {note}"

        # Combine prompts
        user_prompt = data_format + follow_up + audience + tone + data
        system_prompt = persona + instruction + context

        return system_prompt, user_prompt
    
class DiagnosisCodePrompter(AbstractPromptGenerator):
    def generate_prompt(self, note, additional_data: str = None) -> tuple:
        # System prompt components (for model behavior and boundaries)
        persona = (
            "You are an expert in Ambulatory Patient Care Billing and Coding, specializing in breaking down patient visit notes "
            "into accurate ICD-10 Codes. You are also an expert in HCC (Hierarchical Condition Category) coding and Social Determinants "
            "of Health (SDOH) coding using Z codes.\n"
        )
        instruction = (
            "Your task is to analyze the provided patient visit note and identify the most relevant ICD-10 codes. "
            "You must only use the information explicitly mentioned in the visit note. Avoid making any assumptions or adding diagnoses "
            "that are not supported by the information provided in the note.\n"
        )
        context = (
            "Your ICD-10 code recommendations should reflect the most important diagnoses for the patient, helping billers accurately code for "
            "the visit. If there are any HCC-specific codes, highlight them in a separate section labeled 'HCC-Specific Codes'. Additionally, "
            "if the note mentions any Social Determinants of Health (SDOH) issues, include relevant Z codes in a section labeled 'SDOH Z Codes'.\n"
        )

        # User prompt components (for generating the actual recommendation)
        data_format = (
            "Create a bullet-point list of ICD-10 code recommendations based on the visit note. For each diagnosis, include "
            "a brief explanation and ensure all codes are supported by the provided text. If any HCC-specific codes apply, highlight them in "
            "a separate section labeled 'HCC-Specific Codes'. Similarly, if any Social Determinants of Health (SDOH) apply, highlight the "
            "relevant Z codes in a section labeled 'SDOH Z Codes'.\n"
        )
        follow_up = (
            "Do not infer or add diagnoses that are not directly mentioned in the note.\n"
        )
        audience = (
            "The ICD-10 code recommendations are intended for the Revenue Cycle Management Team Billers to create claims with "
            "the correct ICD-10 Codes based on the patient visit notes.\n"
        )
        tone = "The tone should be professional, concise, and clear.\n"
        data = f"Text to recommend ICD-10 From: {note}"

        # Combine prompts
        user_prompt = data_format + follow_up + audience + tone + data
        system_prompt = persona + instruction + context

        return system_prompt, user_prompt
    

class SummarizeChartPrompter(AbstractPromptGenerator):
    def generate_prompt(self, note, additional_data: str = None) -> tuple:
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
    def generate_prompt(self, lab_results, additional_data: str = None) -> tuple:
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
    
class MedicationAdherencePrompter(AbstractPromptGenerator):
    def generate_prompt(self, note: str, additional_data: str = None) -> tuple:
         # Use additional_data (medication adherence responses) if available
        medication_question = additional_data if additional_data else "No additional medication data provided."

        # System prompt (for model behavior and boundaries)
        persona = (
            "You are an expert in patient engagement, specializing in breaking down medical information to help "
            "patients understand their medication regimen. You focus on creating easy-to-understand summaries "
            "that encourage adherence to prescribed medications.\n"
        )
        instruction = (
            "Your task is to generate a simple, easy-to-read message summarizing the patient's medication plan and "
            "reminding them of their adherence goals. Keep the message at a 6th-grade reading level.\n"
        )
        context = (
            "The message should help patients understand their medication, why it’s important to take it regularly, "
            "and any advice they have received from their healthcare provider. Use clear, simple language without "
            "medical jargon, and offer encouragement for sticking to the plan.\n"
        )

        # User prompt (for generating the actual message)
        data_format = (
            "Create a simple message summarizing the patient’s medication plan based on the visit note and their recent responses. "
            "The message should explain what the medication is for and remind them to stay on track. "
            "Make sure to include positive encouragement.\n"
        )
        follow_up = (
            "Provide a final sentence with a reminder to reach out to their healthcare provider if they have any questions or concerns about their medications.\n"
        )
        tone = "The tone should be supportive, simple, and clear at a 6th-grade reading level.\n"
        data = f"Patient Visit Note: {note}\nRecent Medication Question Response: {medication_question}"

        # Combine prompts
        user_prompt = data_format + follow_up + tone + data
        system_prompt = persona + instruction + context

        return system_prompt, user_prompt
    

class FollowUpPrompter(AbstractPromptGenerator):
    def generate_prompt(self, notes, additional_data: str = None) -> tuple:
        # System prompt components (for model behavior and boundaries)
        persona = (
            "You are an expert medical assistant specializing in identifying patient follow-up needs from multiple visit notes. "
            "Your task is to curate a list of follow-ups mentioned in past visits, ensuring busy physicians can easily see what "
            "services or appointments are needed without digging through old notes.\n"
        )
        instruction = (
            "For each visit note provided, itemize the follow-ups needed, including the visit date and the specific service "
            "or follow-up mentioned. Present this in a clear, bullet-point format for quick reference.\n"
            "For each follow-up, use the current query date to calculate when the future appointment should take place. If a follow-up "
            "is required in 6 months or 1 year from the visit date, convert this into the appropriate month and year for scheduling."
        )
        context = (
            "The goal is to create a summary that highlights follow-up appointments, tests, or services the patient needs, "
            "making it easier for physicians to review the follow-ups without reading through entire visit notes. "
            "Only extract follow-up items explicitly mentioned in the notes, without adding new information.\n"
        )

        # User prompt components (for generating the actual follow-up list)
        data_format = (
            "Create a bullet-point list of follow-up services or appointments. Each bullet point should include:\n"
            "- The date of the visit where the follow-up was mentioned.\n"
            "- The specific follow-up required (e.g., 'Lab test', 'Follow-up with cardiologist', etc.).\n"
            "- If no follow-up is mentioned, include a statement: 'No follow-up mentioned in this visit'.\n"
            "- For follow-ups, project the future appointment date based on the visit date. Provide the specific month and year "
            "the follow-up should be scheduled (e.g., 'Follow-up in June 2025')."
        )
        follow_up = (
            "Do not add any extra information or assumptions. If no follow-up is mentioned, clearly state that no follow-up was noted for that visit.\n"
        )
        audience = (
            "This prompt is intended for physicians who need a concise and clear list of follow-ups from past visits, "
            "including a projection of when future appointments should occur."
        )
        tone = "The tone should be professional, concise, and clear.\n"
        
        # Formatting the provided notes for the prompt
        data = f"Visit Notes to process: {notes}"

        # Combine prompts
        user_prompt = data_format + follow_up + audience + tone + data
        system_prompt = persona + instruction + context

        return system_prompt, user_prompt
    
class HCCPrompter(AbstractPromptGenerator):
    def generate_prompt(self, note, additional_data: str = None) -> tuple:
        # System prompt components (for model behavior and boundaries)
        persona = (
            "You are an expert in Hierarchical Condition Category (HCC) coding and ICD-10 coding for Ambulatory Patient Care. "
            "Your task is to accurately extract and recommend HCC ICD-10 codes based strictly on the provided visit notes. "
            "You should only use information explicitly mentioned in the notes without making any assumptions or adding diagnoses that are not supported by the text.\n"
        )
        instruction = (
            "Review the visit notes and extract any relevant HCC ICD-10 codes. When recommending a code, you must provide a brief explanation "
            "referencing the visit note text that supports the code recommendation. If there are no applicable HCC codes based on the provided information, "
            "you should clearly state: 'No HCC ICD-10 was found in the given visit note input'.\n"
        )
        context = (
            "This task is designed to assist healthcare billing teams and clinicians in understanding which HCC codes are applicable for the patient's visit, "
            "so that they can accurately submit claims and ensure proper reimbursement.\n"
        )

        # User prompt components (for generating the actual code recommendations)
        data_format = (
            "Create a bullet-point list of HCC ICD-10 code recommendations. For each code, provide the following:\n"
            "- The ICD-10 code and description.\n"
            "- A brief explanation citing the specific part of the visit note that justifies this code.\n"
            "- If no HCC ICD-10 codes are applicable, clearly state: 'No HCC ICD-10 was found in the given visit note input'.\n"
        )
        follow_up = (
            "Do not add any information or diagnoses that are not directly supported by the visit note text. Stay strictly within the information provided.\n"
        )
        audience = (
            "The HCC ICD-10 code recommendations are intended for healthcare billing professionals and clinicians who need accurate coding for "
            "HCC-related conditions, ensuring proper reimbursement under risk-adjusted payment models."
        )
        tone = "The tone should be professional, concise, and clear.\n"
        data = f"Text to analyze: {note}"

        # Combine prompts
        user_prompt = data_format + follow_up + audience + tone + data
        system_prompt = persona + instruction + context

        return system_prompt, user_prompt