from fastapi import FastAPI
from pydantic import BaseModel

from graph.workflow import app_graph


app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "AI Agent Running"}


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