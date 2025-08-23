# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Environment Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=$(pwd)
```

### Running the Application
- **Local development**: `uvicorn app.app:app --reload`
- **Production (Heroku)**: Uses gunicorn via Procfile: `gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.app:app --bind 0.0.0.0:$PORT`

### Testing and Development
- No formal test suite is currently implemented
- Development testing is done through the web interface at `http://localhost:8000`
- Use different prompter types and model types to test various medical analysis workflows
- Sample visit notes are available through the `VisitSummary` class static methods

### Dependencies
- Python 3.9 runtime
- FastAPI with Jinja2 templates for web interface
- OpenAI and Anthropic APIs for AI model integration
- Basic HTTP authentication for security

## Architecture Overview

### Core Architecture Pattern
The application follows a **Strategy Pattern** with three main layers:
1. **Presentation Layer**: FastAPI routes and Jinja2 templates
2. **Orchestration Layer**: ModelOrchestrator coordinates between models and prompters
3. **Processing Layer**: AI models (OpenAI/Anthropic) with specialized prompt generators

### Core Components

**FastAPI Application** (`app/app.py`):
- Main web server with basic HTTP authentication using `HTTPBasic`
- Multiple HTML template routes for different medical analysis workflows
- RESTful endpoints (`/process`, `/clinical_decision_support`, `/process_followup`)
- Dynamic visit note selection via `/get_visit_note` endpoint

**Model Orchestrator** (`app/model_orchestrator.py`):
- **Factory Pattern** implementation that instantiates correct prompter and model combinations
- Supports 20+ prompter types including multilingual summaries
- Three main processing methods: `process()`, `process_pretty()`, `process_pretty_with_additional_data()`
- Handles special cases like lab result email generation and medication adherence

**Prompt Generator System** (`app/prompt_generator.py`):
- **Abstract Factory Pattern** with `AbstractPromptGenerator` base class
- Each prompter creates system/user prompt pairs optimized for specific medical tasks
- Supports complex prompt engineering with persona, instruction, context, and data formatting
- Specialized prompters for CPT codes, ICD-10 codes, HCC/SDOH coding, and multilingual summaries

**AI Model Implementations**:
- **Abstract base class** `AIModel` (`app/ai_model.py`) defines common interface
- `openai_model.py`: OpenAI GPT integration with conversation history support
- `anthropic_model.py`: Anthropic Claude integration
- Both support markdown scrubbing via `convert_to_ascii()` method
- Models handle both simple prompts and prompts with additional data (medications, adherence responses)

**Visit Summary Data** (`app/visit_summary.py`):
- Container class that wraps text snippets for consistent processing
- Static factory methods provide sample data for different medical scenarios
- Handles complex multi-part data like medication adherence (note + response pairs)

### Template Structure
- Jinja2 templates in `app/templates/` with static assets
- Multiple specialized forms for different medical analysis workflows
- Responsive web interface for healthcare professionals

### Medical Analysis Workflows

**Billing & Coding**:
- `biller`: CPT code extraction and E&M code recommendations
- `diagnosis`: ICD-10 diagnosis code recommendations
- `hcc_coder`: Hierarchical Condition Category coding
- `sdoh_coder`: Social Determinants of Health Z-code identification

**Clinical Documentation**:
- `summarizer`: Professional chart summaries for healthcare providers
- `clinical_decision_support`: Drug interactions, contraindications, and care gaps analysis
- `lab_result_emailer`: Patient-friendly lab result communications

**Patient Care Coordination**:
- `follow_up`: Follow-up appointment and service tracking
- `medication_adherance`: Patient medication compliance messaging
- `previsit_planner`: Pre-visit planning with EHR data analysis
- `previsit_planner_2`: Alternative pre-visit workflow with huddle notes

**Multilingual Patient Communication**:
- `english_summary`, `spanish_summary`, `mandarin_summary`: Patient visit summaries
- `korean_summary`, `arabic_summary`, `bengali_summary`: Additional language support
- Each includes diagnosis, treatment plan, medications, and pharmacy pickup information

## Environment Variables
Required for operation:
- `OPENAI_API_KEY`: OpenAI API access token
- `ANTHROPIC_API_KEY`: Anthropic API access token  
- `BASIC_AUTH_USERNAME`: HTTP basic authentication username
- `BASIC_AUTH_PASSWORD`: HTTP basic authentication password
- `PYTHONPATH`: Should be set to project root for proper module imports
- `PORT`: Heroku deployment port (automatically set in production)

## Key Development Patterns

### Processing Flow
1. **Input**: Visit notes entered via web forms or selected from sample data
2. **Route Selection**: FastAPI routes determine workflow type and model preference
3. **Orchestration**: `ModelOrchestrator` factory creates appropriate prompter + model combination
4. **Prompt Generation**: Prompter creates system/user prompt pairs with medical context
5. **AI Processing**: OpenAI or Anthropic models process prompts with clinical expertise
6. **Output Formatting**: Results rendered through Jinja2 templates with markdown scrubbing

### Authentication & Security
- Basic HTTP authentication required for all protected routes
- Credentials managed via environment variables (`BASIC_AUTH_USERNAME`, `BASIC_AUTH_PASSWORD`)
- Cache-preventing headers on authenticated pages
- HIPAA compliance considerations in all medical data processing

### Adding New Medical Analysis Types
1. Create new prompter class inheriting from `AbstractPromptGenerator`
2. Implement `generate_prompt()` method with system/user prompt logic
3. Add prompter case to `ModelOrchestrator.__init__()`
4. Create corresponding HTML template if needed
5. Add route in `app.py` following existing patterns

### Model Integration
- Both OpenAI and Anthropic models use identical interface through `AIModel` abstract base
- API keys configured via environment variables
- Models support conversation context and additional data parameters
- Markdown output can be scrubbed for plain text presentation