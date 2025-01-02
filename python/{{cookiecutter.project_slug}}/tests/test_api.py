"""Test FastAPI endpoint function."""

import re

import pytest
from fastapi.testclient import TestClient

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
        "url": "https://www.nationwidechildrens.org/specialties/institute-for-genomic-medicine/research-labs/wagner-lab",
    }
    assert response_json["contactUrl"] == "Alex.Wagner@nationwidechildrens.org"
    assert (
        response_json["documentationUrl"]
        == "https://github.com/{{ cookiecutter.org }}/{{ cookiecutter.repo }}"
    )
    assert ServiceEnvironment(response_json["environment"])
    assert re.match(r"\d\.\d\.\d\.", response_json["version"])


def test_service_info_version(api_client: TestClient):
    """Early in development, we expect `__version__` to be None, but it shouldn't be
    once a version tag is made. Therefore, this test is broken out so that it can be easily
    ignored while initial development is ongoing.
    """
    response_json = api_client.get("/service_info").json()
    assert re.match(r"\d\.\d\.\d\.", response_json["type"]["version"])
    assert re.match(r"\d\.\d\.\d\.", response_json["version"])
