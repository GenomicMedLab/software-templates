# Lab Software Templates

## Instructions

Clone this repo, create a virtual environment, and install `cookiecutter`:

```shell
git clone https://github.com/genomicmedlab/software-templates
cd software-templates
python3 -m virtualenv venv
source venv/bin/activate
python3 -m pip install "cookiecutter>=2.5.0"
```

Choose a template (eg `python/`) and an output directory (eg `~/projects`) and run `cookiecutter`:

```shell
python3 -m cookiecutter -o ~/code/ python/
```
