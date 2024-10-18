import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes

from graph.graph import compiled_graph
from models.graph_models import InputModel

app = FastAPI(
    title="LangChain agent",
    version="1.0",
    description="",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_routes(
    app,
    compiled_graph.with_types(input_type=InputModel),
)

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=1234)
