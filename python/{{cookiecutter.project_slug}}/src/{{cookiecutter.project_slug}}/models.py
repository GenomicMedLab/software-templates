"""Define models for internal data and API responses."""

from enum import Enum
from typing import Literal

from pydantic import BaseModel

from . import __version__


class ServiceEnvironment(str, Enum):
    """Define current runtime environment."""

    DEV = "dev"
    PROD = "prod"
    TEST = "test"
    STAGING = "staging"


class ServiceOrganization(BaseModel):
    """Define service_info response for organization field"""

    name: Literal["Genomic Medicine Lab at Nationwide Children's Hospital"] = (
        "Genomic Medicine Lab at Nationwide Children's Hospital"
    )
    url: Literal[
        "https://www.nationwidechildrens.org/specialties/institute-for-genomic-medicine/research-labs/wagner-lab"
    ] = "https://www.nationwidechildrens.org/specialties/institute-for-genomic-medicine/research-labs/wagner-lab"


class ServiceType(BaseModel):
    """Define service_info response for type field"""

    group: Literal["org.genomicmedlab"] = "org.genomicmedlab"
    artifact: Literal["{{ cookiecutter.project_slug }} API"] = "{{ cookiecutter.project_slug }} API"
    version: Literal[__version__] = __version__


class ServiceInfo(BaseModel):
    """Define response structure for GA4GH /service_info endpoint."""

    id: Literal["org.genomicmedlab.{{ cookiecutter.project_slug }}"] = (
        "org.genomicmedlab.{{ cookiecutter.project_slug }}"
    )
    name: Literal["{{ cookiecutter.project_slug }}"] = "{{ cookiecutter.project_slug }}"
    type: ServiceType
    description: Literal["{{ cookiecutter.description }}"] = "{{ cookiecutter.description }}"
    organization: ServiceOrganization
    contactUrl: Literal["Alex.Wagner@nationwidechildrens.org"] = (  # noqa: N815
        "Alex.Wagner@nationwidechildrens.org"
    )
    documentationUrl: Literal["https://github.com/{{ cookiecutter.org }}/{{ cookiecutter.repo }}"] = (  # noqa: N815
        "https://github.com/{{ cookiecutter.org }}/{{ cookiecutter.repo }}"
    )
    createdAt: Literal["{% now 'utc', '%Y-%m-%dT%H:%M:%S+00:00' %}"] = "{% now 'utc', '%Y-%m-%dT%H:%M:%S+00:00' %}"  # noqa: N815
    updatedAt: Literal["{% now 'utc', '%Y-%m-%dT%H:%M:%S+00:00' %}"] = "{% now 'utc', '%Y-%m-%dT%H:%M:%S+00:00' %}"  # noqa: N815
    environment: ServiceEnvironment
    version: Literal[__version__] = __version__
