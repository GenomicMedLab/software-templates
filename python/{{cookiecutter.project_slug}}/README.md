# {{ cookiecutter.project_name }}

[![image](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![image](https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![image](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Actions status](https://github.com/{{ cookiecutter.org }}/{{ cookiecutter.project_slug }}/workflows/checks.yaml/badge.svg)](https://github.com/{{ cookiecutter.org }}/{{ cookiecutter.project_slug }}/actions/checks.yaml)

<!-- description -->
{{ cookiecutter.description }}
<!-- /description -->

{% if cookiecutter.add_docs %}---

**[Documentation](https://{{ cookiecutter.project_slug }}.readthedocs.io/stable/)** · [Installation](https://{{ cookiecutter.project_slug }}.readthedocs.io/stable/install.html) · [Usage](https://{{ cookiecutter.project_slug }}.readthedocs.io/stable/usage.html) · [API reference](https://{{ cookiecutter.project_slug }}.readthedocs.io/stable/reference/index.html){% endif %}

---

## Installation

Install from [PyPI](https://pypi.org/project/{{ cookiecutter.project_slug }}/):

```shell
python3 -m pip install {{ cookiecutter.project_slug }}
```

---{% if cookiecutter.add_docs %}

## Feedback and contributing

We welcome bug reports, feature requests, and code contributions from users and interested collaborators. The [documentation](https://{{ cookiecutter.project_slug }}.readthedocs.io/latest/contributing.html) contains guidance for submitting feedback and contributing new code.{% else %}

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
```{% endif %}
