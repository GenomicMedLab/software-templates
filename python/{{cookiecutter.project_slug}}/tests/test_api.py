"""Test FastAPI endpoint function."""

from pathlib import Path

import jsonschema
import pytest
import yaml
from fastapi.testclient import TestClient

from {{ cookiecutter.project_slug }}.api import app


@pytest.fixture(scope="module")
def api_client():
    return TestClient(app)


def test_service_info(api_client: TestClient, test_data_dir: Path):
    response = api_client.get("/service-info")
    response.raise_for_status()

    with (test_data_dir / "service_info_openapi.yaml").open() as f:
        spec = yaml.safe_load(f)

    resp_schema = spec["paths"]["/service-info"]["get"]["responses"]["200"]["content"][
        "application/json"
    ]["schema"]

    resolver = jsonschema.RefResolver.from_schema(spec)
    data = response.json()
    jsonschema.validate(instance=data, schema=resp_schema, resolver=resolver)
