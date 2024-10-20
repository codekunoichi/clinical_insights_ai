
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
