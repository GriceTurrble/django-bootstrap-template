import random
import os
from pathlib import Path
import re
import fileinput


def remove_open_source_files():
    """Remove files related to open source development.

    Borrowed from cookiecutter-django:
    https://github.com/pydanny/cookiecutter-django
    """
    file_names = ["CONTRIBUTORS.txt", "LICENSE"]
    for file_name in file_names:
        os.remove(file_name)


def remove_gplv3_files():
    """Remove files related to the GPLv3 license.

    Borrowed from cookiecutter-django:
    https://github.com/pydanny/cookiecutter-django
    """
    file_names = ["COPYING"]
    for file_name in file_names:
        os.remove(file_name)


def add_to_env_file(key, val):
    """Add the given key and value to the environment file."""
    env_file_path = Path("{{ cookiecutter.project_slug }}") / ".env"
    with open(env_file_path, "a") as envfile:
        envfile.write(f"{key}={val}\n")


def new_secret_key(length=50):
    """Generate a new key to use for Django's SECRET_KEY setting."""
    choice_set = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_+)"
    )
    return "".join([random.SystemRandom().choice(choice_set) for i in range(length)])


def main():
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_open_source_files()

    if "{{ cookiecutter.open_source_license}}" != "GPLv3":
        remove_gplv3_files()

    # Create environment variables.
    add_to_env_file("DEBUG", "on")
    add_to_env_file("SECRET_KEY", new_secret_key())

    if "{{ cookiecutter.database_backend }}" == "postgres":
        add_to_env_file("POSTGRES_NAME", "mydatabase")
        add_to_env_file("POSTGRES_USER", "mydatabaseuser")
        add_to_env_file("POSTGRES_PASSWORD", "mypassword")
        add_to_env_file("POSTGRES_HOST", "127.0.0.1")
        add_to_env_file("POSTGRES_PORT", "5432")


if __name__ == "__main__":
    main()
