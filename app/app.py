from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from app.model_orchestrator import ModelOrchestrator
from app.visit_summary import VisitSummary, visit_1, visit_3, visit_2, visit_4, sdoh_visit, diagnosis_visit_note, lab_result
from flask import render_template
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.visit_summary import VisitSummary
from typing import Optional
from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os
from starlette.status import HTTP_401_UNAUTHORIZED
import secrets
from dotenv import load_dotenv
from pathlib import Path
from app.openai_model import OpenAIModel

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
# Load environment variables from .env file
load_dotenv()

# Set up basic authentication
security = HTTPBasic()

# Environment variables for basic authentication credentials
USERNAME = os.getenv("BASIC_AUTH_USERNAME")
PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")

# Function to handle basic authentication
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    # Fetch environment variables
    USERNAME = os.getenv("BASIC_AUTH_USERNAME", "").strip()
    PASSWORD = os.getenv("BASIC_AUTH_PASSWORD", "").strip()

    # Debugging statements
    # print(f"Environment username: |{USERNAME}|")
    # print(f"Environment password: |{PASSWORD}|")
    # print(f"Entered username: |{credentials.username.strip()}|")
    # print(f"Entered password: |{credentials.password.strip()}|")

    # Use secrets.compare_digest to compare user input with environment variables
    correct_username = secrets.compare_digest(credentials.username.strip(), USERNAME)
    correct_password = secrets.compare_digest(credentials.password.strip(), PASSWORD)

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials

# Landing page
# Securing the index route with basic authentication
@app.get("/", response_class=HTMLResponse)
async def get_landing_page(request: Request, credentials: HTTPBasicCredentials = Depends(authenticate)):
    # Ensure that Basic Auth credentials are valid
    if not credentials:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    # Define headers to prevent caching of the credentials and page
    headers = {
        "Cache-Control": "no-store",
        "Pragma": "no-cache",
        "Expires": "0",
        "WWW-Authenticate": 'Basic realm="Authentication required"'
    }

    # Check if the API keys are present
    openai_key_present = bool(os.getenv("OPENAI_API_KEY"))
    anthropic_key_present = bool(os.getenv("ANTHROPIC_API_KEY"))

    # Render the template with cache-preventing headers
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "openai_key_present": openai_key_present,
            "anthropic_key_present": anthropic_key_present,
        },
        headers=headers
    )

# Create the absolute path for the static directory
static_dir = Path(__file__).parent / "templates/static"


# Define a new route to get the visit note based on the selected option
@app.get("/get_visit_note")
def get_visit_note(note_id: str):
    print(f"Note ID selected..{note_id}")
    visit_notes = {
        "visit_1": VisitSummary.get_visit_1(),
        "visit_2": VisitSummary.get_visit_2(),
        "visit_3": VisitSummary.get_visit_3(),
        "visit_4": VisitSummary.get_visit_4(),
        "sdoh_visit": VisitSummary.get_sdoh_visit(),
        "diagnosis_visit_note": VisitSummary.get_diagnosis_visit_note(),
        "lab_result": VisitSummary.get_lab_result_samplenote(),
        "follow_up" : VisitSummary.get_followup_visit(),
        "medication_adherance": VisitSummary.get_medication_adherance(),
        "previsit_planner": VisitSummary.get_previst_planning_visit(),
        "previsit_huddle" : VisitSummary.get_previsit_planning_visit_with_huddlenotes()
    }

    # Check if the selected note is 'medication_adherance' which returns both note and response
    if note_id == "medication_adherance":
        note, adherence_response = visit_notes.get(note_id)
        return JSONResponse({"visit_note": note, "adherence_response": adherence_response})
    
    note = visit_notes.get(note_id, "No visit note found.")
    return JSONResponse({"visit_note": note})

# Mount the static directory using the absolute path
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/form", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.get("/visit_summary", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("visit_summary.html", {"request": request})

@app.get("/followup_asst", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("post_visit_summary.html", {"request": request})

@app.get("/chinese_summary", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("chinese_summary.html", {"request": request})

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/process_followup", response_class=HTMLResponse)
async def process_followup(
    request: Request,
    visit_note: str = Form(...),
    model_type: str = Form(...)
):
    print(f"Request received for note:\n\n{visit_note}")
    openai_client = OpenAIModel(None)
    response = openai_client.get_followup(visit_note)
    result = response.choices[0].message.content
    return templates.TemplateResponse("/post_visit_summary.html", {"request": request, "model_type": model_type, "visit_note": visit_note, "result": result})


@app.post("/process", response_class=HTMLResponse)
async def process_note(
    request: Request,
    visit_note: str = Form(...),
    prompter_type: str = Form(...),
    model_type: str = Form(...),
    adherence_response: str = Form(None)
):
    # Initialize orchestrator and process based on prompter_type
    orchestrator = ModelOrchestrator(model_type=model_type, prompter_type=prompter_type)
    print(f"Request received for note:\n\n{visit_note}")
    visit_summary = VisitSummary([visit_note])
    
    if prompter_type == 'lab_result_emailer':
        result, email = orchestrator.process_summary_and_email(visit_summary)
        return templates.TemplateResponse("form.html", {"request": request, "model_type": model_type, "visit_note": visit_note, "prompter_type": prompter_type, "result": result, "email": email})
    elif prompter_type == 'medication_adherance':
        result = orchestrator.process_pretty_with_additional_data(visit_summary, adherence_response)
        return templates.TemplateResponse("form.html", {"request": request, "model_type": model_type, "visit_note": visit_note, "adherence_response": adherence_response, "prompter_type": prompter_type, "result": result})
    else:
        result = orchestrator.process_pretty(visit_summary)
        return templates.TemplateResponse("form.html", {"request": request, "model_type": model_type, "visit_note": visit_note, "prompter_type": prompter_type, "result": result})


@app.route('/')
def index():
    return render_template('form.html', visit_1=visit_1, visit_2=visit_2, visit_3=visit_3, visit_4=visit_4, sdoh_visit=sdoh_visit, diagnosis_visit_note=diagnosis_visit_note, lab_result=lab_result)