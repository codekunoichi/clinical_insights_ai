
![image](https://github.com/user-attachments/assets/e305c847-373c-4892-a450-d6cb2b7e4db0)

# Clinical Insights AI

A comprehensive AI-powered healthcare automation platform that transforms patient visit notes into actionable clinical insights. The application supports medical billing & coding, clinical decision support, patient care coordination, and multilingual patient communication using both OpenAI and Anthropic AI models.

## Features

- **Clinical Documentation & Summaries**: Generate professional chart summaries and patient visit notes
- **Medical Billing & Coding**: Extract CPT codes, recommend ICD-10 diagnosis codes, HCC coding, and SDOH Z-codes
- **Lab Result Communication**: Create patient-friendly emails summarizing lab results with trends
- **Clinical Decision Support**: Analyze drug interactions, contraindications, and identify care gaps
- **Patient Care Coordination**: Track follow-up appointments, medication adherence, and pre-visit planning
- **Multilingual Patient Communication**: Generate patient visit summaries in English, Spanish, Mandarin, Korean, Arabic, and Bengali
- **HIPAA-Compliant**: Secure basic authentication for all protected health information
- **AI-Powered**: Supports both OpenAI and Anthropic models for flexible AI processing

---

## Setup


### Environment Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/codekunoichi/clinical_insights_ai.git
    cd clinical_insights_ai
    ```

2. Set up the virtual environment and install the required libraries:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set the proper file path for running the app:
    ```bash
    export PYTHONPATH=$(pwd)
    ```
4. Token Credits and API Key Setup

Before running the application, you need to purchase token credits for OpenAI and/or Anthropic if required.

- OpenAI Credits: Purchase token credits from OpenAI.
- Anthropic Credits: Purchase token credits from Anthropic.

After purchasing credits, create a `.env` file in the project root with the following environment variables:
```bash
# AI API Keys
OPENAI_API_KEY="your-openai-api-key"
ANTHROPIC_API_KEY="your-anthropic-api-key"

# Basic Authentication (for HIPAA compliance)
BASIC_AUTH_USERNAME="your-username"
BASIC_AUTH_PASSWORD="your-secure-password"
```

Alternatively, you can export them directly:
```bash
export OPENAI_API_KEY="your-openai-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
export BASIC_AUTH_USERNAME="your-username"
export BASIC_AUTH_PASSWORD="your-secure-password"
```

### Required Libraries

The following libraries are required (see `requirements.txt`):
- `fastapi==0.85.0` - Web framework
- `uvicorn==0.19.0` - ASGI server
- `jinja2==3.0.1` - Template engine
- `openai==1.51.2` - OpenAI API client
- `anthropic==0.36.1` - Anthropic API client
- `python-dotenv` - Environment variable management
- `python-multipart` - Form data parsing
- `Flask==2.1.1` - Additional web framework components
- `Werkzeug==2.0` - WSGI utilities
- `gunicorn` - Production WSGI server

All dependencies are installed via:
```bash
pip install -r requirements.txt
```

### Running the FastAPI Server

To run the FastAPI server for your application:
```bash
uvicorn app.app:app --reload
```

Access the app at `http://localhost:8000` in your browser.

**Note**: The application uses HTTP Basic Authentication. You'll be prompted to enter the username and password you configured in your environment variables (`BASIC_AUTH_USERNAME` and `BASIC_AUTH_PASSWORD`).

### Available Web Interfaces

The application provides multiple web interfaces for different medical workflows:

- **`/`** - Landing page with links to all available tools and API key status
- **`/form`** - Main interface for billing, coding, summaries, and patient communication
- **`/clinical_decision_support`** - Clinical decision support analysis (drug interactions, contraindications, care gaps)
- **`/followup_asst`** - Post-visit follow-up appointment tracking
- **`/visit_summary`** - Visit summary generation
- **`/chinese_summary`** - Mandarin Chinese patient summary generation

### API Endpoints

- **POST `/process`** - Main processing endpoint for most prompter types
- **POST `/clinical_decision_support`** - Clinical decision support with medication analysis
- **POST `/process_followup`** - Follow-up appointment processing
- **GET `/get_visit_note`** - Retrieves sample visit notes for testing

---

## Quick Start Guide

1. **Set up environment** (see Setup section above)
2. **Start the server**: `uvicorn app.app:app --reload`
3. **Navigate to** `http://localhost:8000`
4. **Log in** with your configured username and password
5. **Choose a workflow** from the landing page:
   - Medical billing/coding
   - Clinical decision support
   - Patient communication
   - Multilingual summaries
6. **Select a model**: OpenAI or Anthropic (ensure API key is configured)
7. **Choose a sample visit note** or paste your own
8. **Select the prompter type** for your desired analysis
9. **Click process** and review the AI-generated results

---

## Prompter Types

This project includes 18+ specialized prompt generators organized by clinical workflow:

### Medical Billing & Coding
- **biller** (`CPTCodePrompter`): Extracts CPT codes and E&M level recommendations from patient visit summaries
- **diagnosis** (`DiagnosisCodePrompter`): Identifies ICD-10 diagnosis codes relevant to patient visits
- **hcc_coder** (`HCCPrompter`): Hierarchical Condition Category coding for risk adjustment
- **sdoh_coder** (`SDOHPrompter`): Social Determinants of Health Z-code identification

### Clinical Documentation
- **summarizer** (`SummarizeChartPrompter`): Creates professional chart summaries for healthcare providers
- **clinical_decision_support** (`ClinicalDecisionSupportPrompter`): Analyzes drug interactions, contraindications, and identifies care gaps

### Patient Care Coordination
- **follow_up** (`FollowUpPrompter`): Tracks follow-up appointments and recommended services
- **medication_adherance** (`MedicationAdherencePrompter`): Generates patient medication compliance messages
- **previsit_planner** (`PreVisitPlanningPrompter`): Pre-visit planning with EHR data analysis
- **previsit_planner_2** (`PreVisitPlanningPrompter_Alternate`): Alternative pre-visit workflow with huddle notes

### Lab & Communication
- **lab_result_emailer** (`LabResultEmailer`): Patient-friendly lab result summaries with trend analysis

### Multilingual Patient Summaries
- **english_summary** (`VisitSummaryPrompterEnglish`): Patient visit summary in English
- **spanish_summary** (`VisitSummaryPrompterSpanish`): Patient visit summary in Spanish
- **mandarin_summary** (`VisitSummaryPrompterMandarin`): Patient visit summary in Mandarin Chinese
- **korean_summary** (`VisitSummaryPrompterKorean`): Patient visit summary in Korean
- **arabic_summary** (`VisitSummaryPrompterArabic`): Patient visit summary in Arabic
- **bengali_summary** (`VisitSummaryPrompterBengali`): Patient visit summary in Bengali

All multilingual summaries include diagnosis information, treatment plans, medications, and pharmacy pickup details.

---

## Architecture & Technology Stack

### Design Patterns
- **Strategy Pattern**: Flexible prompter and model selection
- **Factory Pattern**: `ModelOrchestrator` creates appropriate prompter/model combinations
- **Abstract Factory Pattern**: `AbstractPromptGenerator` base class for all prompters

### Technology Stack
- **Backend**: FastAPI (Python 3.9) with Jinja2 templating
- **AI Models**: OpenAI GPT and Anthropic Claude
- **Authentication**: HTTP Basic Auth with `secrets` module
- **Deployment**: Heroku with Gunicorn + Uvicorn workers
- **Configuration**: python-dotenv for environment management

### Application Layers
1. **Presentation Layer**: FastAPI routes and Jinja2 templates
2. **Orchestration Layer**: `ModelOrchestrator` coordinates models and prompters
3. **Processing Layer**: AI models with specialized prompt generators

---

## Security & HIPAA Compliance

The application implements the following security measures:

- **HTTP Basic Authentication**: All protected routes require username/password authentication
- **Environment Variable Security**: API keys and credentials stored in `.env` file (never commit this file!)
- **Cache Prevention**: Headers configured to prevent credential caching
- **Secure Credential Comparison**: Uses `secrets.compare_digest()` for timing-attack resistant authentication

**Important**:
- Always use HTTPS in production and ensure strong passwords for basic authentication
- Never commit your `.env` file to version control (add it to `.gitignore`)
- Rotate API keys and credentials regularly
- Follow HIPAA guidelines for handling protected health information (PHI)

---

## Sample Visit Notes

The application includes built-in sample visit notes for testing different workflows:

- `visit_1`, `visit_2`, `visit_3`, `visit_4` - General patient visits
- `sdoh_visit` - Social Determinants of Health scenario
- `diagnosis_visit_note` - Diagnosis-focused visit
- `lab_result` - Laboratory result sample
- `follow_up` - Follow-up appointment scenario
- `medication_adherance` - Medication compliance tracking
- `previsit_planner` - Pre-visit planning data
- `previsit_huddle` - Pre-visit huddle notes

These are accessible via the `/get_visit_note` endpoint or through the web interface dropdowns.

---

## Example Visit Summary

```plaintext
Visit 1: October 1, 2024
Subjective:
    • The patient reports an increase in hip pain, especially when lying down.
    • ... [visit details truncated]
Objective:
    • Vitals: BP 130/85 mmHg, HR 72 bpm, Temp 98.6°F, BMI 28.
    • ... [physical exam details]
Assessment:
    • ICD-10 Codes: M25.551, M25.552, M54.5
    • CPT Codes: 99214, 72148
Plan:
    • Medications: Ibuprofen, Cyclobenzaprine
    • Continue physical therapy and follow-up in 4 weeks.
```


## Heroku Deployment Setup

To deploy the Clinical Insights AI application to Heroku and integrate it with GitHub for continuous deployment, follow these steps:

### Prerequisites

- Create a Heroku account
- Install the Heroku CLI on your local machine
- Ensure your application code is version-controlled with Git and accessible on GitHub

#### MacOS

    ```brew tap heroku/brew && brew install heroku```

#### Step 1: Create a Heroku App

- Log in to Heroku via the CLI:

```heroku login```


- In your terminal, navigate to the project directory and create a new Heroku app:

```heroku create <your-app-name>```

Replace <your-app-name> with a unique name for your app.

#### Step 2: Set Up Environment Variables

- Go to the Heroku dashboard, navigate to your app, and open Settings.
- Under Config Vars, click Reveal Config Vars and add the necessary environment variables:
  - OPENAI_API_KEY
  - ANTHROPIC_API_KEY
  - BASIC_AUTH_USERNAME
  - BASIC_AUTH_PASSWORD

#### Step 3: Configure GitHub Integration for Continuous Deployment

- In the Heroku dashboard for your app, go to the Deploy tab.
- Under Deployment method, select GitHub.
- Connect to your GitHub account and select the repository with the Clinical Insights AI code.
- Enable Automatic Deploys to deploy each time you push a new commit to the main branch.

#### Step 4: Specify the Heroku Runtime and Procfile

Ensure your repository contains:

- A `runtime.txt` specifying the Python version:
  ```
  python-3.9
  ```

- A `Procfile` in the root directory with the following line:
  ```
  web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.app:app --bind 0.0.0.0:$PORT
  ```

  Note: Heroku automatically sets the `$PORT` environment variable.



#### Step 5: Deploy the App

- Once GitHub integration is set, Heroku will automatically deploy the app when changes are pushed to the linked branch.
- Alternatively, you can manually trigger a deployment from the Deploy tab in the Heroku dashboard by clicking Deploy Branch.

#### Step 6: View Logs for Troubleshooting

To view logs for debugging:

```heroku logs --tail --app <your-app-name>```

You can now access the deployed application via the Heroku app URL provided in your dashboard.


## Lets Experiment!

We encourage you to dive into this repository and experiment with the tools and AI models. Consider investing a small amount in token credits:

- OpenAI Credits: $10 for nearly 1 million tokens, enough for a proof of concept.
- Anthropic Credits: $25 to get started.

Instead of spending on that daily coffee, invest in yourself and your future. Learn prompt engineering, develop AI skills, and experiment freely!


For pricing details, check out:
- [OpenAI Pricing](https://openai.com/api/pricing/)
- [Anthropic Pricing](https://www.anthropic.com/pricing#anthropic-api)

Following is the actual spend thus far, its not a lot, be brave and purchase! (Yes that is daily spend of 70 cents on OpenAI, for running and re-running this experiment and iterating.)

![image](https://github.com/user-attachments/assets/1b53162f-7227-480e-9bdb-94676c936bc6)

[For Heroku App Deployments](https://www.heroku.com/pricing?)
The eco pricing is $5/month you get 999 eco dyno hours.

Following is the actual spend thus far for last two days of 24 X 7 running with few clicks of experiments here and there.
<img width="1597" alt="image" src="https://github.com/user-attachments/assets/cd17e8b5-33a9-4543-9399-95b1e74ef5b3">


[Eco Dyno Hours](https://devcenter.heroku.com/articles/eco-dyno-hours)
