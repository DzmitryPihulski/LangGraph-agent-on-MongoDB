from fastapi import BackgroundTasks, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from langserve import add_routes  # type: ignore

from db.db import airbnb_db
from db.fetch_sample_data import fetch_sample_data
from graph.graph import compiled_graph
from models.graph_models import InputModel


def lifespan(app: FastAPI):
    airbnb_db.connect()
    yield
    airbnb_db.disconnect()


app = FastAPI(
    title="LangChain agent",
    version="1.0",
    description="",
    lifespan=lifespan,
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


@app.post(path="/refresh_data")
async def refresh_data(background_task: BackgroundTasks) -> JSONResponse:
    background_task.add_task(fetch_sample_data)
    return JSONResponse(content="Job created", status_code=status.HTTP_200_OK)
