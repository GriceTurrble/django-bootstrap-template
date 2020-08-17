# 2020-08-14 - Environment variable support, database and license selection, README, `pytest` support, and some bells and whistles

Template updated with some helpful features:

- [`django-environ`][1] has been added as a project requirement, in order to easily inject environment variables to the project settings.
  - `<project>/settings.py` now uses `env(...)` calls to get settings like `DEBUG` and `SECRET_KEY`.
  - These settings and the environment file are automatically generated when the template is run through `cookiecutter`.
- A new cookiecutter option, `database_backend`, provides a selection between `sqlite3` (Django's default, enough for small prototype projects) and `postgres`.
  - When `postgres` is selected as the backend:
    - environment variables are added to the generated `.env` file for `POSTGRES_NAME`, `POSTGRES_USER`, etc.
    - `settings.py` is adjusted to use the postgres backend and the environment variables specified above.
    - `requirements.txt` is updated to include `psycopg2`, which is needed for Python to interact with a Postgres database.
- Another new cookiecutter option, `open_source_license`, allows selection of the type of license to use, instead of forcing the MIT license.
  - This option and code for it borrowed from [`pydanny/cookiecutter-django`][2]
  - Selecting `Not open source` will remove all open-source license files from the project.
- Added `requirements-dev.txt` to template project.
  - Includes `pytest` and `pytest-django` for testing (with a `pytest.ini` file included that should help you get started), and `black` for code formatting (recommended, obviously not required).
  - [See docs for `pytest-django`][3].
  - Tests for the `base_objects` app will be added in a future update.
- `README.rst` added to the template project.
  - Partly borrowed from [`pydanny/cookiecutter-django`][2], adjusted to point to this site template. :)

[1]: https://django-environ.readthedocs.io/en/latest/
[2]: https://github.com/pydanny/cookiecutter-django
[3]: https://pytest-django.readthedocs.io/
