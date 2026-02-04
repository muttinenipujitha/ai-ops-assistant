from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent

app = FastAPI()
templates = Jinja2Templates(directory="templates")

planner = PlannerAgent()
executor = ExecutorAgent()
verifier = VerifierAgent()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/run")
def run_task(task: str):
    plan = planner.plan(task)
    executed = executor.execute(plan["steps"])
    return verifier.verify(executed)

