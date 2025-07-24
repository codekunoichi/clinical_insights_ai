# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Running the Application
- **Local development**: `uvicorn app.app:app --reload`
- **Production (Heroku)**: Uses gunicorn via Procfile: `gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.app:app --bind 0.0.0.0:$PORT`
- **Environment setup**: 
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  export PYTHONPATH=$(pwd)
  ```

### Dependencies
- Python 3.9 runtime
- FastAPI with Jinja2 templates for web interface
- OpenAI and Anthropic APIs for AI model integration
- Basic HTTP authentication for security

## Architecture Overview

### Core Components

**FastAPI Application** (`app/app.py`):
- Main web server with basic HTTP authentication
- Multiple HTML template routes for different medical analysis types
- RESTful endpoints for processing medical visit notes

**Model Orchestrator** (`app/model_orchestrator.py`):
- Central coordination between AI models (OpenAI/Anthropic) and prompt generators
- Supports multiple medical analysis types: billing codes (CPT), diagnosis codes (ICD-10), chart summaries, lab result emails
- Handles multilingual visit summaries (English, Spanish, Mandarin, Korean, Arabic, Bengali)

**Prompt Generator System** (`app/prompt_generator.py`):
- Abstract base class with specialized prompters for different medical tasks
- Each prompter generates system/user prompt pairs for specific use cases
- Supports advanced medical coding including HCC and SDOH codes

**AI Model Implementations**:
- `openai_model.py`: OpenAI API integration
- `anthropic_model.py`: Anthropic API integration  
- Both models support markdown scrubbing and additional data processing

**Visit Summary Data** (`app/visit_summary.py`):
- Container class for medical visit text snippets
- Static methods providing sample visit data for different scenarios
- Handles complex cases like medication adherence and pre-visit planning

### Template Structure
- Jinja2 templates in `app/templates/` with static assets
- Multiple specialized forms for different medical analysis workflows
- Responsive web interface for healthcare professionals

### Medical Analysis Types
- **CPT Code Analysis**: Billing code extraction from visit notes
- **ICD-10 Diagnosis Coding**: Medical diagnosis code recommendations
- **Chart Summarization**: Clinical summary generation
- **Lab Result Processing**: Patient-friendly lab result emails
- **Medication Adherence**: Patient medication compliance tracking
- **Follow-up Planning**: Automated follow-up scheduling
- **HCC/SDOH Coding**: Advanced healthcare quality metrics
- **Pre-visit Planning**: Clinical preparation workflows
- **Multilingual Summaries**: Patient communication in multiple languages

## Environment Variables
Required API keys:
- `OPENAI_API_KEY`: OpenAI API access
- `ANTHROPIC_API_KEY`: Anthropic API access
- `BASIC_AUTH_USERNAME`: HTTP basic auth username
- `BASIC_AUTH_PASSWORD`: HTTP basic auth password

## Key Patterns
- All medical analysis follows the pattern: Visit Note → Prompt Generator → AI Model → Processed Result
- Authentication is enforced on all routes using FastAPI's HTTPBasic
- The orchestrator pattern allows easy switching between AI providers
- Prompt engineering uses separate system/user prompts for better AI model performance
- Medical data processing emphasizes patient privacy and HIPAA compliance considerations