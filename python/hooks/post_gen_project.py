"""Provide hooks to run after project is generated."""

from pathlib import Path
import shutil


if not {{ cookiecutter.add_docs }}:
    shutil.rmtree("docs")
    Path(".readthedocs.yaml").unlink()


if not {{ cookiecutter.add_fastapi }}:
    Path("tests/test_api.py").unlink()
    Path("src/{{ cookiecutter.project_slug }}/api.py").unlink()
    Path("src/{{ cookiecutter.project_slug }}/models.py").unlink()
    Path("src/{{ cookiecutter.project_slug }}/logging.py").unlink()
