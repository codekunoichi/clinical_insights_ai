
![image](https://github.com/user-attachments/assets/e305c847-373c-4892-a450-d6cb2b7e4db0)

# Clinical Insights AI

This project provides AI-powered insights into patient visit notes, generating medical summaries, CPT and ICD codes, and lab result summaries, while also maintaining HIPAA-compliant patient communication.

## Features

- Summarize patient visit notes.
- Generates appropriate CPT codes for medical billing.
- Recommends ICD-10 diagnosis codes.
- Creates patient-friendly emails summarizing lab results with trends.
- Facilitates healthcare providers by delivering quick, concise insights into patient histories.

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

After purchasing credits, set the following environment variables for your API keys:
```
export OPENAI_API_KEY="your-openai-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

### Required Libraries

Ensure the following libraries are installed:
- `fastapi`
- `uvicorn`
- `jinja2`
- `openai`
- `anthropic`

Install them using:
```bash
pip install fastapi uvicorn jinja2 openai anthropic
```

### Running the FastAPI Server

To run the FastAPI server for your application:
```bash
uvicorn app.app:app --reload
```

Access the app at `http://localhost:8000` in your browser.

---

## Prompter Types

This project includes several types of prompt generators:

### 1. **CPT Code Prompter**
   - Extracts CPT codes from patient visit summaries.
   - Recommends appropriate CPT codes based on performed procedures, referrals, or specific diagnoses.

### 2. **ICD-10 Code Prompter**
   - Identifies ICD-10 codes relevant to patient visits.
   - Focuses on diagnoses mentioned in the visit notes with specific sections for HCC and SDOH codes.

### 3. **Chart Summary Prompter**
   - Summarizes the key points of the patient’s chart, providing a concise and professional overview for healthcare providers.

### 4. **Lab Result Email Prompter**
   - Generates patient-friendly summaries of lab results, highlighting trends without sharing specific values, protecting patient privacy in email communication.

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
