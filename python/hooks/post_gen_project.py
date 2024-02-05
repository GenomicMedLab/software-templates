"""Provide hooks to run after project is generated."""
from pathlib import Path
import shutil


if not {{ cookiecutter.add_docs }}:
    shutil.rmtree("docs")
    Path(".readthedocs.yaml").unlink()
