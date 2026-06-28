from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from graph.workflow import app_graph


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
class QueryRequest(BaseModel):
    query: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
)

@app.post("/ask")
def ask(request: QueryRequest):

    result = app_graph.invoke(
        {
            "query": request.query
        }
    )

    return result

@app.get("/health")
def health():
    return {"status": "ok"}