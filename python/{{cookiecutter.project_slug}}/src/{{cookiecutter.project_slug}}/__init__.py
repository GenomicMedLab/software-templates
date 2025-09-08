"""{{ cookiecutter.description }}"""

from importlib.metadata import version, PackageNotFoundError


try:
    __version__ = version("{{ cookiecutter.project_slug }}")
except PackageNotFoundError:
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
