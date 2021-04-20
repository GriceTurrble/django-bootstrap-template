# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

[![Built with Django3 Site Template](https://img.shields.io/badge/Built%20with-Django3%20Site%20Template-blueviolet.svg)](https://github.com/griceturrble/django3-site-template/) [![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

{% if cookiecutter.open_source_license != "Not open source" %}
## License

This project uses the {{ cookiecutter.open_source_license }} license. Please see the [LICENSE](LICENSE) for details.
{% endif %}

## Installation

1. Create a new Python virtual environment.

   - Using `venv` on Linux:

     ```bash
     python3 -m venv .venv --prompt {{ cookiecutter.project_slug }}
     ```

   - Using `venv` on Windows:

     ```bash
     python3 -m venv .venv --prompt {{ cookiecutter.project_slug }}
     ```

   - Or, use whichever style of virtual environment management you prefer!

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
{% if cookiecutter.database_backend == "postgres" %}
1. *PostgreSQL settings*: if not present already create a new `.env` file at `{{ cookiecutter.project_slug }}/core/.env`. This file should be gitignored from the repo, and should contain credentials for connecting to the PostgreSQL database:

   - `POSTGRES_NAME`: database name
   - `POSTGRES_USER`: username
   - `POSTGRES_PASSWORD`: password
   - `POSTGRES_HOST`: host serving the database
   - `POSTGRES_PORT`: port
{% endif %}
1. Migrate models to the database:

   ```bash
   python {{ cookiecutter.project_slug }}/manage.py migrate
   ```

1. Create a superuser:

   ```bash
   python {{ cookiecutter.project_slug }}/manage.py createsuperuser
   ```

1. Run the development server:

   ```bash
   python {{ cookiecutter.project_slug }}/manage.py runserver
   ```

1. Open http://localhost:8000 to view the running site.
