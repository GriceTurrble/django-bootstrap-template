{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

{{ cookiecutter.description }}

.. image:: https://img.shields.io/badge/Built%20with-Django3%20Site%20Template-blueviolet.svg
     :target: https://github.com/griceturrble/django3-site-template/
     :alt: Built with Django3 Site Template
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style
{% if cookiecutter.open_source_license != "Not open source" %}

:License: {{cookiecutter.open_source_license}}
{% endif %}
