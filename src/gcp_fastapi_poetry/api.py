import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gcp_fastapi_poetry.types import ExampleResponse

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
    return ExampleResponse(response_value=exampleValue.upper())
