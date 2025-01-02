"""Test FastAPI endpoint function."""

import re

from fastapi.testclient import TestClient
import pytest

from {{ cookiecutter.project_slug }}.api import app
from {{ cookiecutter.project_slug }}.models import ServiceEnvironment


@pytest.fixture(scope="module")
def api_client():
    return TestClient(app)


def test_service_info(api_client: TestClient):
    response = api_client.get("/service_info")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"] == "org.genomicmedlab.{{ cookiecutter.project_slug }}"
    assert response_json["name"] == "{{ cookiecutter.project_slug }}"
    assert response_json["type"]["group"] == "org.genomicmedlab"
    assert response_json["type"]["artifact"] == "{{ cookiecutter.project_slug }} API"
    assert re.match(r"\d\.\d\.\d\.", response_json["type"]["version"])
    assert response_json["description"] == "{{ cookiecutter.description }}"
    assert response_json["organization"] == {
        "name": "Genomic Medicine Lab at Nationwide Children's Hospital",
        "url": "https://www.nationwidechildrens.org/specialties/institute-for-genomic-medicine/research-labs/wagner-lab"
    }
    assert response_json["contactUrl"] == "Alex.Wagner@nationwidechildrens.org"
    assert response_json["documentationUrl"] == "https://github.com/{{ cookiecutter.org }}/{{ cookiecutter.repo }}"
    assert ServiceEnvironment(response_json["environment"])
    assert re.match(r"\d\.\d\.\d\.", response_json["version"])
