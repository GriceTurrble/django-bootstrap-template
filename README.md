# Django 3 site template

A [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) template for a basic Django 3.0 site, with some helpful base abstract models, [Bootstrap 4](https://getbootstrap.com/), [FontAwesome 5](https://fontawesome.com/) Free, and some starter templates.

## Requirements

* Python 3.6+ (as required by Django 3, and for type hinting and f-string support)
* `cookiecutter` (linked above; install with Pip using the command in the **Installation** instructions below.
* An amazing new project idea you want to bring to life quickly.

## Installation

1. Run `pip install cookiecutter` to be able to copy this project template.
2. Run `cookiecutter https://github.com/GriceTurrble/django3-site-template.git` to build the project. Follow the prompts to set up the project to your liking.
3. Create a new virtual environment using `python -m venv <name>`. Run its activate script, consider running `python -m pip install -U pip` to upgrade the venv's Pip, then `cd` to the project directory.
4. Run `pip install -r requirements.txt` for all project requirements, which are fairly basic (Django and some development packages, such as [Black](https://github.com/psf/black) and [pylint](https://github.com/PyCQA/pylint) with [pylint-django](https://github.com/PyCQA/pylint-django) plugin).
    * Remember to run `pylint` with `--load-plugins pylint_django` to enable the plugin for Django projects.
    * This can be enabled in VS Code automatically by adding the setting:

```json
"python.linting.pylintArgs": [
    "--load-plugins",
    "pylint_django"
]
```

5. Navigate to the directory containing `manage.py`, then run:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

6. Open `localhost:8000` in a browser and check out the new project!
