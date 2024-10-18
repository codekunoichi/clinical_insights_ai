from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from app.model_orchestrator import ModelOrchestrator
from app.visit_summary import VisitSummary
import os

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Landing page
@app.get("/", response_class=HTMLResponse)
async def get_landing_page(request: Request):
    print("Current working directory:", os.getcwd())  # Debugging
    return templates.TemplateResponse("index.html", {"request": request})

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
    
    visit_summary = VisitSummary([visit_note])
    result = orchestrator.process_pretty(visit_summary)

    return templates.TemplateResponse("form.html", {"request": request, "result": result})