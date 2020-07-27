# GriceTurrble's Django 3 site template

A [`cookiecutter`][1] template for a basic Django 3.0 site, with some helpful base abstract models, [Bootstrap 4][2], [FontAwesome 5][3] Free, and some starter templates.

## Requirements

- **Python 3.6+** ([required by Django 3][12], and for type hinting and f-string support)
- [`cookiecutter`][1] (install with Pip using the command in the **Installation** instructions below.
- An amazing new project idea you want to bring to life quickly.

## Installation

1. Run `pip install cookiecutter` to be able to copy this project template.
2. Run `cookiecutter https://github.com/GriceTurrble/django3-site-template.git` to build the project. Follow the prompts to set up the project to your liking (prompts defined in `cookiecutter.json`).
3. Create a new virtual environment:
   1. Use `python -m venv <name>` to generate the environment.
   2. Activate your new venv.
   3. (Optional, but recommended) Run `python -m pip install --upgrade pip` to upgrade the venv's Pip version
4. With your venv activated, navigate to the project directory, then run `pip install -r requirements.txt` to install project requirements.
5. Navigate to the project directory containing `manage.py` and run the following:
   1. `python manage.py migrate` to populate the initial database (which is defaulted to SQLite in `settings.py`; feel free to change this for your needs before migrating models).
   2. `python manage.py createsuperuser` to make your superuser account, for access to the Django Admin.
   3. `python manage.py runserver` to start up the development server.
      - By default, this will run the server on port `8000`
      - You can change this using `python manage.py runserver 0.0.0.0:<port>`.
6. Open `localhost:8000` in your browser and check out the new project!

## Usage

Once started up, you can use this project like any other basic Django installation: start up apps, write models, create templates, add static files, and go from there.

What this project template provides is some starting points and working examples you can follow, based on my personal experience with the Django framework and what I would consider best practice. You are more than welcome to disagree with these opinions and take the project in a different direction, of course. :)

Here are some details on what this project template contains:

### The `base_objects` app and `ProjectBaseModel`

The `base_objects` app is a standard Django app included with the site template. This app is intended to contain [abstract models][4], utility methods, and other "common" objects you may use elsewhere in your site. Think of it as a root directory for custom Django objects.

This app contains a single abstract model, `ProjectBaseModel`, with a custom QuerySet used as its model manager, `ProjectBaseQuerySet`. You may subclass `ProjectBaseModel` for each model in your application, instead of the standard `models.Model`:

```python
# my_app/models.py

from base_objects.models import ProjectBaseModel

class MyModel(ProjectBaseModel):
    ...
```

Any model in your application that subclasses `ProjectBaseModel` will automatically include the fields defined in `ProjectBaseModel` and the queryset methods defined in `ProjectBaseQuerySet`, allowing them to share common logic and data without needing to rewrite them for each model.

For starters, this means the time-tracking fields `time_created` and `time_modified`, as well as these command-style QuerySet methods:

| Method                      | Usage                                                                                                                                                                  |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `created_before(dt)`        | Model instances created (via `time_created`) before `dt` (a `datetime.datetime` or `datetime.date` object), inclusive (will return instances of `dt == time_created`). |
| `created_after(dt)`         | Instances created after `dt`.                                                                                                                                          |
| `created_on_date(dt)`       | Instances created on the date of `dt`. Uses Django's [date field lookup][5]. `dt` is coerced to a `datetime.date` object before being used in the query.               |
| `created_between(dt1, dt2)` | Instances created between `dt1` and `dt2`, inclusive. Uses Django's [range field lookup][6] (Note the warnings in their documentation for edge cases).                 |
| `modified_before(dt)`       | Same as `created_before`, for `time_modified` field.                                                                                                                   |
| `modified_after(dt)`        | Same as `created_after`, for `time_modified` field.                                                                                                                    |
| `modified_on_date(dt)`      | Same as `created_on_date`, for `time_modified` field.                                                                                                                  |
| `modified_between(dt)`      | Same as `created_between`, for `time_modified` field.                                                                                                                  |

Each of these methods returns a QuerySet and can be chained like many other QuerySet methods:

```python
MyModel.objects.filter(...).created_before(...).exclude(...)
# and so on.
```

#### Extending `ProjectBaseModel` and `ProjectBaseQuerySet`

`ProjectBaseModel` serves as a hook for functionality that is shared by all models within a project. Rather than updating each model in your project individually, you can add fields to the base model to ensure that all other models get updated automatically, and ensure that the same baseline functionality is available in any future model you use.

The same goes for `ProjectBaseQuerySet` when you add new fields to `ProjectBaseModel` and want to use custom filtering, similar to those used for `time_created` and `time_modified`. Simply add new methods to this QuerySet and they'll become available to every model that subclasses `ProjectBaseModel` and _uses its same QuerySet manager_.

Note that last part: that's where it can get tricky.

#### Subclassing `ProjectBaseQuerySet`

When you want to add custom fields to a specific model that subclasses `ProjectBaseModel`, you may be inclined to simply make a new QuerySet and/or Manager class and assign this to the `objects` manager on that model. However, doing so will overwrite `ProjectBaseQuerySet` as a manager of that model, making its methods unavailable.

Django's documentation regarding [Custom managers and model inheritance][7] is quite helpful here. However, their solution revolves around creating multiple managers for a subclassed abstract model with its own base manager, so that you may need to reference a different manager besides `objects`.

Personally, I find it frustrating to use any other manager besides `objects` unless absolutely necessary; and I want to retain the ability to chain all the different custom methods together. My solution and recommendation is to subclass `ProjectBaseQuerySet`, then use the subclass as the new model's manager:

```python
from base_object.managers import ProjectBaseQuerySet

class MyQuerySet(ProjectBaseQuerySet):
    def my_new_method(self):
        ...

class MyModel(ProjectBaseModel):
    objects = MyQuerySet.as_manager()
```

This way, all methods from the base model's QuerySet are still available in the `objects` manager; the new methods can also be found in the `objects` manager; and they can all be chained together:

```python
MyModel.objects.filter(...).my_new_method().created_before(...)
```

All of that, as I said, is a personal opinion: you can do differently as suits your needs.

### Starter templates

The front page you see when you first launch the project is a static template that includes a lot of handy features to get you started in frontend development:

- The page is served by a generic `TemplateView` defined in `<project_name>/urls.py`, right below the standard `admin` path; no extra view code required! If you want to serve some static pages, this is a good example to follow.
- The main template, `homepage.html`, extends a base template from which all other site templates can be built to give a uniform look and feel. Find this at `templates/base.html` to see its code.
- The base template brings in Bootstrap 4 CSS and JS via CDN; FontAwesome 5 free edition via a local copy, served as a deferred script to load SVG icons; and site-specific CSS and JS files, which you'll find in `<project_name>/static/` and that you can edit freely.
- The base template also includes "widget"-style templates for `base_navbar.html` and `base_footer.html`, which inject a Bootstrap navbar in the top of each page and a custom footer, respectively. Separating templates in this way is helpful for compartmentalizing and re-using content: your templates don't need to be one-file monoliths!
  - Note also how `base_navbar.html` adds in a link to the Admin index. See more details on writing Admin URLs [here][8]
- You'll see `homepage.html` has very little code; in fact, all it does is include another "widget"-style template, `welcome_wagon.html`, which contains all the contents of the front page. You can quickly remove the "welome wagon" display by removing the `{% include %}` tag for that template, giving you a blank slate to start from.
  - I would recommend keeping the `welcome_wagon.html` file in your project as a reference.
- One last template, `template_of_templates.html`, contains a basis for new site templates. It includes the `{% extends %}` tag for `base.html` and a copy of each `{% block %}` tag used in that base template. You can easily start up a new page by copying this file, adding the content you need, and removing the blocks you aren't changing.

### Other project contents

- `base_objects` includes a barebones [AppConfig][9], `BaseObjectsConfig`. You can find this in `base_objects/apps.py`.
  - An app's AppConfig is a good place to [connect model signals][10] by importing an app's `signals.py` module in that app's `AppConfig.ready` method. This is typically cleaner than defining signal receivers in `models.py`.
  - It is good practice to explicitly point to an app's config in the `INSTALLED_APPS` setting, instead of the app's name. For instance, `base_objects` is listed by its AppConfig class using `"base_objects.apps.BaseObjectsConfig"`.
- A project-level `static/` directory is available to dump static files that don't fit within an app structure. You can still use app-level static files as needed (and remember to run `collectstatic` in production!), but it's good to have a central spot for site-level static content.
- The project is automatically built with the same MIT license used for the template repo, including your entry for Author Name and the current year.
- The `base_objects` app has some sparse [type hinting][11] built into the methods for `base_objects.managers.ProjectBaseQuerySet`. Running the project in Python <3.5 (which is [technically not supported in Django 3][12]) will cause errors due to these type hints.
  - Since this is a template for a new project, you _should_ be (and I highly recommend) using the latest stable Python release that Django and your other dependencies support.

[1]: https://github.com/cookiecutter/cookiecutter
[2]: https://getbootstrap.com/
[3]: https://fontawesome.com/
[4]: https://docs.djangoproject.com/en/3.0/topics/db/models/#abstract-base-classes
[5]: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#date
[6]: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#range
[7]: https://docs.djangoproject.com/en/3.0/topics/db/managers/#custom-managers-and-model-inheritance
[8]: https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#reversing-admin-urls
[9]: https://docs.djangoproject.com/en/3.0/ref/applications/
[10]: https://docs.djangoproject.com/en/3.0/topics/signals/#connecting-receiver-functions
[11]: https://docs.python.org/3/library/typing.html
[12]: https://docs.djangoproject.com/en/3.0/releases/3.0/
