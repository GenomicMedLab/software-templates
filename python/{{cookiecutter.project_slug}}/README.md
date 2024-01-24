# {{ cookiecutter.project_name }}

[![image](https://img.shields.io/pypi/v/{{ cookiecutter.repo }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo }})
[![image](https://img.shields.io/pypi/l/{{ cookiecutter.repo }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo }})
[![image](https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.repo }})
[![Actions status](https://github.com/{{ cookiecutter.org }}/{{ cookiecutter.repo }}/workflows/CI/badge.svg)](https://github.com/{{ cookiecutter.org }}/{{ cookiecutter.repo }}/actions)
![{{ cookiecutter.project_slug }}](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/{{ cookiecutter.project_slug }}/main/assets/badge/v2.json)

{{ cookiecutter.description }}

## Installation

Install from [PyPI](https://pypi.org/project/{{ cookiecutter.project_slug }}/):

```shell
python3 -m pip install {{ cookiecutter.project_slug }}
```

## Development

Clone the repo and create a virtual environment:

```shell
git clone https://github.com/{{ cookiecutter.org }}/{{ cookiecutter.repo }}
cd {{ cookiecutter.repo }}
python3 -m virtualenv venv
source venv/bin/activate
```

Install development dependencies and `pre-commit`:

```shell
python3 -m pip install -e '.[dev,tests]'
pre-commit install
```

Check style with `ruff`:

```shell
python3 -m ruff format . && python3 -m ruff check --fix .
```

Run tests with `pytest`:

```shell
pytest
```
