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
4. Run `pip install -r requirements.txt` for all project requirements (which is really just Django itself).
5. Navigate to the directory containing `manage.py`.
    1. Run `python manage.py migrate` to populate the initial database (which is defaulted to SQLite in `settings.py`; feel free to change this for your needs before migrating models).
    2. Run `python manage.py createsuperuser` to make your superuser account, for access to the Django Admin.
6. Run `python manage.py runserver` to start up the development server. By default, this will listen on port 8000; you can change this using `runserver 0.0.0.0:<port>`.
7. Open `localhost:8000` in your browser and check out the new project!

## Usage

*Updating soon...*
