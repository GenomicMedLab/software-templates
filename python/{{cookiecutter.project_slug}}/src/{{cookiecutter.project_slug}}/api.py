"""Define API endpoints."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from enum import Enum

from fastapi import FastAPI

from {{ cookiecutter.project_slug }} import __version__
from {{ cookiecutter.project_slug }}.config import config
from {{ cookiecutter.project_slug }}.logging import initialize_logs
from {{ cookiecutter.project_slug }}.models import ServiceInfo, ServiceOrganization, ServiceType


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """Perform operations that interact with the lifespan of the FastAPI instance.

    See https://fastapi.tiangolo.com/advanced/events/#lifespan.

    :param app: FastAPI instance
    """
    initialize_logs()
    yield


class _Tag(str, Enum):
    """Define tag names for endpoints."""

    META = "Meta"


app = FastAPI(
    title="{{ cookiecutter.project_slug }}",
    description="{{ cookiecutter.description }}",
    version=__version__,
    contact={
        "name": "Alex H. Wagner",
        "email": "Alex.Wagner@nationwidechildrens.org",
        "url": "https://www.nationwidechildrens.org/specialties/institute-for-genomic-medicine/research-labs/wagner-lab",
    },
    license={
        "name": "MIT",
        "url": "https://github.com/{{ cookiecutter.org }}/{{ cookiecutter.repo }}/blob/main/LICENSE",
    },
    docs_url="/docs",
    openapi_url="/openapi.json",
    swagger_ui_parameters={"tryItOutEnabled": True},
)


@app.get(
    "/service_info",
    summary="Get basic service information",
    response_model=ServiceInfo,
    description="Retrieve service metadata, such as versioning and contact info. Structured in conformance with the [GA4GH service info API specification](https://www.ga4gh.org/product/service-info/)",
    tags=[
        _Tag.META,
    ],
)
def service_info() -> ServiceInfo:
    """Provide service info per GA4GH Service Info spec

    :return: conformant service info description
    """
    return ServiceInfo(
        organization=ServiceOrganization(), type=ServiceType(), environment=config.env
    )
