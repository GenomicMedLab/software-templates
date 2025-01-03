"""Provide hooks to run after project is generated."""
from pathlib import Path
import shutil


if not {{ cookiecutter.add_docs }}:
    shutil.rmtree("docs")
    Path(".readthedocs.yaml").unlink()

if not {{ cookiecutter.add_cli }}:
    Path("./src/{{ cookiecutter.project_slug }}/cli.py").unlink()
    Path("./src/{{ cookiecutter.project_slug }}/logging.py").unlink()
    Path("./docs/source/cli_reference.rst").unlink()
