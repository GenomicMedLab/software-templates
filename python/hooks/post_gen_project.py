"""Provide hooks to run after project is generated."""
import shutil


if not {{ cookiecutter.add_docs }}:
    shutil.rmtree("docs")
