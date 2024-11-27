from fastapi import BackgroundTasks, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from langserve import add_routes  # type: ignore

from db.db import airbnb_db
from db.fetch_sample_data import fetch_sample_data
from graph.graph import compiled_graph
from models.graph_models import InputModel, OutputModel

tags_metadata = [
    {"name": "DB endpoints", "description": "Interact with the database"},
]


def lifespan(app: FastAPI):
    airbnb_db.connect()
    yield
    airbnb_db.disconnect()


app = FastAPI(
    title="LangChain agent",
    version="1.0",
    description="",
    lifespan=lifespan,  # type: ignore
    openapi_tags=tags_metadata,
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
    compiled_graph.with_types(input_type=InputModel, output_type=OutputModel),
)


@app.get(path="/get_the_number_of_docs", tags=["DB endpoints"])
async def get_the_number_of_docs() -> JSONResponse:
    """
    Get the number of documents in the db collection.

    Returns:
        JSONResponse: Response from the db.
    """
    return JSONResponse(
        content=f"The number of docs in the db is: {airbnb_db.get_the_number_of_docs()}",
        status_code=status.HTTP_200_OK,
    )


@app.post(path="/refresh_data", tags=["DB endpoints"])
async def refresh_data(background_task: BackgroundTasks) -> JSONResponse:
    """
    Fetch the data from the sample database.

    Returns:
        JSONResponse: whether the creation of task was successful.
    """
    background_task.add_task(fetch_sample_data)
    return JSONResponse(content="Job created", status_code=status.HTTP_200_OK)
