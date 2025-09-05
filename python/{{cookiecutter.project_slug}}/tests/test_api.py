"""Test FastAPI endpoint function."""

import re
from datetime import datetime
from pathlib import Path

import pytest
import yaml
from fastapi.testclient import TestClient

from {{ cookiecutter.project_slug }}.api import app
from {{ cookiecutter.project_slug }}.models import ServiceEnvironment


@pytest.fixture(scope="module")
def api_client():
    return TestClient(app)


# def test_service_info(api_client: TestClient):
#     response = api_client.get("/service_info")
#     assert response.status_code == 200
#     expected_version_pattern = r"\d\.\d\."  # at minimum, should be something like "0.1"
#     response_json = response.json()
#     assert response_json["id"] == "org.genomicmedlab.{{ cookiecutter.project_slug }}"
#     assert response_json["name"] == "{{ cookiecutter.project_slug }}"
#     assert response_json["type"]["group"] == "org.genomicmedlab"
#     assert response_json["type"]["artifact"] == "{{ cookiecutter.project_slug }} API"
#     assert re.match(expected_version_pattern, response_json["type"]["version"])
#     assert response_json["description"] == "{{ cookiecutter.description }}"
#     assert response_json["organization"] == {
#         "name": "Genomic Medicine Lab at Nationwide Children's Hospital",
#         "url": "https://www.nationwidechildrens.org/specialties/institute-for-genomic-medicine/research-labs/wagner-lab",
#     }
#     assert response_json["contactUrl"] == "Alex.Wagner@nationwidechildrens.org"
#     assert (
#         response_json["documentationUrl"]
#         == "https://github.com/{{ cookiecutter.org }}/{{ cookiecutter.repo }}"
#     )
#     assert datetime.fromisoformat(response_json["createdAt"])
#     assert ServiceEnvironment(response_json["environment"])
#     assert re.match(expected_version_pattern, response_json["version"])


def test_service_info(client: TestClient, test_data_dir: Path):
    response = client.get("/service-info")
    response.raise_for_status()

    with (test_data_dir / "service_info_openapi.yaml").open() as f:
        spec = yaml.safe_load(f)

    resp_schema = spec["paths"]["/service-info"]["get"]["responses"]["200"]["content"][
        "application/json"
    ]["schema"]

    resolver = jsonschema.RefResolver.from_schema(spec)
    data = response.json()
    jsonschema.validate(instance=data, schema=resp_schema, resolver=resolver)
