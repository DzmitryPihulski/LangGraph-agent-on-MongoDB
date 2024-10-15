from fastapi import FastAPI
from graph.graph import compiled_graph
from langserve import add_routes
import uvicorn

app = FastAPI(
    title="LangChain agent",
    version="1.0",
    description="",
)

add_routes(
    app,
    compiled_graph,
)

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=1234)
