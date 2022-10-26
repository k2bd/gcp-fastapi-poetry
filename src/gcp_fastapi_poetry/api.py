import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gcp_fastapi_poetry.types import ExampleResponse

if os.environ.get("K_SERVICE"):
    # Setup logging if we're in a cloud run environment
    from google.cloud.logging import Client as LoggingClient

    logging_client = LoggingClient()
    logging_client.setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/example/{exampleValue}", response_model=ExampleResponse)
async def say_hello(exampleValue: str):
    logger.info(f"GET /example/{exampleValue}")
    return ExampleResponse(response_value=exampleValue.upper())
