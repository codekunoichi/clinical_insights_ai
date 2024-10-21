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

import os
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Landing page
@app.get("/", response_class=HTMLResponse)
async def get_landing_page(request: Request):
    print("Current working directory:", os.getcwd())  # Debugging
    # Check if the API keys are present
    openai_key_present = bool(os.getenv("OPENAI_API_KEY"))
    anthropic_key_present = bool(os.getenv("ANTHROPIC_API_KEY"))
    return templates.TemplateResponse("index.html", {
        "request": request,
        "openai_key_present": openai_key_present,
        "anthropic_key_present": anthropic_key_present
    })

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
        "lab_result": VisitSummary.get_lab_result_samplenote()
    }
    
    note = visit_notes.get(note_id, "No visit note found.")
    return JSONResponse({"visit_note": note})

# Mount the static directory using the absolute path
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/form", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/process", response_class=HTMLResponse)
async def process_note(request: Request, visit_note: str = Form(...), prompter_type: str = Form(...)):
    # You can invoke the orchestrator here based on the selected prompter
    orchestrator = ModelOrchestrator(model_type='openai', prompter_type=prompter_type)  # Or 'anthropic'
    print(f"Request received for note:\n\n{visit_note}")
    visit_summary = VisitSummary([visit_note])
    if (prompter_type == 'lab_result_emailer'):
        result, email = orchestrator.process_summary_and_email(visit_summary)
        return templates.TemplateResponse("form.html", {"request": request, "visit_note": visit_note, "prompter_type":prompter_type, "result": result, "email": email})
    else:
        result = orchestrator.process_pretty(visit_summary)
        return templates.TemplateResponse("form.html", {"request": request, "visit_note": visit_note, "prompter_type":prompter_type, "result": result})

@app.route('/')
def index():
    return render_template('form.html', visit_1=visit_1, visit_2=visit_2, visit_3=visit_3, visit_4=visit_4, sdoh_visit=sdoh_visit, diagnosis_visit_note=diagnosis_visit_note, lab_result=lab_result)