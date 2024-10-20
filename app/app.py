from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from app.model_orchestrator import ModelOrchestrator
from app.visit_summary import VisitSummary, visit_1, visit_3, visit_2, visit_4, sdoh_visit, diagnosis_visit_note, lab_result
from flask import render_template

import os
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Landing page
@app.get("/", response_class=HTMLResponse)
async def get_landing_page(request: Request):
    print("Current working directory:", os.getcwd())  # Debugging
    return templates.TemplateResponse("index.html", {"request": request})

# Create the absolute path for the static directory
static_dir = Path(__file__).parent / "templates/static"

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
    result = orchestrator.process_pretty(visit_summary)

    return templates.TemplateResponse("form.html", {"request": request, "visit_note": visit_note, "prompter_type":prompter_type, "result": result})

@app.route('/')
def index():
    return render_template('form.html', visit_1=visit_1, visit_2=visit_2, visit_3=visit_3, visit_4=visit_4, sdoh_visit=sdoh_visit, diagnosis_visit_note=diagnosis_visit_note, lab_result=lab_result)