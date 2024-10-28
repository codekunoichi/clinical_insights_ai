from app.openai_model import OpenAIModel
from app.anthropic_model import AnthropicModel
from app.visit_summary import VisitSummary
from app.prompt_generator import CPTCodePrompter, SummarizeChartPrompter, DiagnosisCodePrompter, LabResultEmailer, MedicationAdherencePrompter, FollowUpPrompter, HCCPrompter, SDOHPrompter, PreVisitPlanningPrompter, VisitSummaryPrompterSpanish, VisitSummaryPrompterMandarin, VisitSummaryPrompterEnglish, VisitSummaryPrompterKorean
class ModelOrchestrator:
    def __init__(self, model_type: str, prompter_type: str):
        print(f"************* Summarization for {model_type} for the persona {prompter_type}")
        if prompter_type == 'biller':
            self.prompter = CPTCodePrompter()
        elif prompter_type == 'summarizer':
            self.prompter = SummarizeChartPrompter()
        elif prompter_type == 'diagnosis':
            self.prompter = DiagnosisCodePrompter()
        elif prompter_type == 'lab_result_emailer':
            self.prompter = LabResultEmailer()
        elif prompter_type == 'medication_adherance':
            self.prompter = MedicationAdherencePrompter()
        elif prompter_type == 'follow_up':
            self.prompter = FollowUpPrompter()
        elif prompter_type == 'hcc_coder':
            self.prompter = HCCPrompter()
        elif prompter_type == 'sdoh_coder':
            self.prompter = SDOHPrompter()
        elif prompter_type == 'previsit_planner':
            self.prompter = PreVisitPlanningPrompter()
        elif prompter_type == 'spanish_summary':
            self.prompter = VisitSummaryPrompterSpanish()
        elif prompter_type == 'mandarin_summary':
            self.prompter = VisitSummaryPrompterMandarin()
        elif prompter_type == 'english_summary':
            self.prompter = VisitSummaryPrompterEnglish()
        elif prompter_type == 'korean_summary':
            self.prompter = VisitSummaryPrompterKorean()
        else:
            raise ValueError(f"{prompter_type} - Invalid prompter type provided.")

        if model_type == 'openai':
            self.model = OpenAIModel(self.prompter)
        elif model_type == 'anthropic':
            self.model = AnthropicModel(self.prompter)
        else:
            raise ValueError("Invalid model type provided. Choose 'openai' or 'anthropic'.")

    def generate_email(self, result: str) -> str:
        if isinstance(self.prompter, LabResultEmailer):
            return self.prompter.generate_email(result)
        else:
            raise AttributeError(f"{self.model_type} prompter cannot generate an email.")
        
    def process(self, visit_summary: VisitSummary, ) -> str:
        # Call the model with the generated prompt
        print(f"Visit Summary: \n\n {visit_summary.get_text()}")
        result = self.model.call_model(visit_summary.get_text())
        return result
    
    # removes the markdown characters returned.
    def process_pretty(self, visit_summary: VisitSummary, ) -> str:
        # Call the model with the generated prompt
        result = self.model.call_model_and_scrub(visit_summary.get_text(), None)
        return result
    
    def process_pretty_with_additional_data(self, visit_summary: VisitSummary, additiona_data) -> str:
        # Call the model with the generated prompt
        result = self.model.call_model_and_scrub(visit_summary.get_text(), additiona_data)
        return result
    
    
    def process_summary_and_email(self, visit_summary: VisitSummary, ) -> tuple:
        # Call the model with the generated prompt
        print(f"Visit Summary: \n\n {visit_summary.get_text()}")
        summary =self.process_pretty(visit_summary)
        email = self.generate_email(summary)
        return summary, email

if __name__ == "__main__":
    # Example usage
    visit_summary = VisitSummary(VisitSummary.get_sample_visits())


    # # Orchestrate with OpenAI model and BillerPrompter
    # orchestrator = ModelOrchestrator(model_type='openai', prompter_type='biller')
    # result = orchestrator.process_pretty(visit_summary)
    # print(result)

    # # Orchestrate with Anthropic model and BillerPrompter
    # orchestrator = ModelOrchestrator(model_type='anthropic', prompter_type='biller')
    # result = orchestrator.process_pretty(visit_summary)
    # print(result)

    # # Orchestrate with OpenAI model and SummarizeChartPrompter
    # orchestrator = ModelOrchestrator(model_type='openai', prompter_type='summarizer')
    # result = orchestrator.process_pretty(visit_summary)
    # print(result)

    # # Orchestrate with Anthropic model and SummarizeChartPrompter
    # orchestrator = ModelOrchestrator(model_type='anthropic', prompter_type='summarizer')
    # result = orchestrator.process_pretty(visit_summary)
    # print(result)

    # # Orchestrate with Anthropic model and DiagnosisCodePrompter
    # orchestrator = ModelOrchestrator(model_type='anthropic', prompter_type='diagnosis')
    # result = orchestrator.process_pretty(visit_summary)
    # print(result)

    # # Orchestrate with OpenAI model and DiagnosisCodePrompter
    # orchestrator = ModelOrchestrator(model_type='openai', prompter_type='diagnosis')
    # result = orchestrator.process_pretty(visit_summary)
    # print(result)

    # # Orchestrate with OpenAI model and LabEmailPrompter
    # orchestrator = ModelOrchestrator(model_type='openai', prompter_type='lab_result_emailer')
    # result, email = orchestrator.process_summary_and_email(VisitSummary(VisitSummary.get_lab_result_samplenote()))
    # print("&&&&&&&&&&&&&&&&&&&& \n\n\nSummary:\n\n")
    # print(result)
    # print("&&&&&&&&&&&&&&&&&&&& \n\n\nEmail:\n\n")
    # print(email)

    # # Orchestrate with OpenAI model and MedicationAdherencePrompter
    # visit_summary = VisitSummary(VisitSummary.get_medication_adherance()[0])
    # orchestrator = ModelOrchestrator(model_type='openai', prompter_type='medication_reminder')
    # result = orchestrator.process_pretty_with_additional_data(visit_summary, VisitSummary.get_medication_adherance()[1])
    # print(result)

    # # Orchestrate with OpenAI model and FollowupPrompter
    # orchestrator = ModelOrchestrator(model_type='openai', prompter_type='follow_up')
    # result = orchestrator.process_pretty(VisitSummary(VisitSummary.get_followup_visit()))
    # print(result)

    # # Orchestrate with OpenAI model and HCCPrompter
    # orchestrator = ModelOrchestrator(model_type='openai', prompter_type='hcc_coder')
    # result = orchestrator.process_pretty(VisitSummary(VisitSummary.get_visit_4()))
    # print(result)

    # # Orchestrate with OpenAI model and SDOHPrompter
    # orchestrator = ModelOrchestrator(model_type='openai', prompter_type='sdoh_coder')
    # result = orchestrator.process_pretty(VisitSummary(VisitSummary.get_sdoh_visit()))
    # print(result)

    # Orchestrate with OpenAI model and SDOHPrompter
    orchestrator = ModelOrchestrator(model_type='openai', prompter_type='previsit_planner')
    result = orchestrator.process_pretty(VisitSummary(VisitSummary.get_previst_planning_visit()))
    print(result)