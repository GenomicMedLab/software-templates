"""Define models for internal data and API responses."""

from typing import Literal
from pydantic import BaseModel

from . import __version__


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
    version: Literal["1.0.0"] = "1.0.0"


class ServiceInfo(BaseModel):
    """Define response structure for GA4GH service_info endpoint."""

    name: Literal["{{ cookiecutter.project_slug }}"] = "{{ cookiecutter.project_slug }}"
    id: Literal["org.genomicmedlab.{{ cookiecutter.project_slug }}"] = "org.genomicmedlab.{{ cookiecutter.project_slug }}"
    description: Literal["{{ cookiecutter.description }}"] = "{{ cookiecutter.description }}"
    type: ServiceType
    organization: ServiceOrganization
    version: Literal[__version__] = __version__
    contact_url: Literal["Alex.Wagner@nationwidechildrens.org"] = (
        "Alex.Wagner@nationwidechildrens.org"
    )
    createdAt: Literal["{% now 'utc', '%Y-%m-%dT%H:%M:%S+00:00' %}"] = "{% now 'utc', '%Y-%m-%dT%H:%M:%S+00:00' %}"  # noqa: N815
    updatedAt: str | None = None  # noqa: N815
