# Django Bootstrap site template

A [cookiecutter] template for a basic [Django] site, with some helpful base abstract models, [Bootstrap], [FontAwesome], and some starter templates.

Includes:

- Django 4.0
- Bootstrap 5.1.3
- FontAwesome 5.15.4 Free edition

## Requirements

- Python 3.8+, as required by Django 4.0. See [Django 4.0 release notes](https://docs.djangoproject.com/en/4.0/releases/4.0/#python-compatibility) for details.
- [cookiecutter] (install with Pip using the command in the **Installation** instructions below.
- An amazing new project idea you want to bring to life quickly.

## Installation

First, install the `cookiecutter` package (in its own virtual environment, preferably) from PyPI:

```bash
pip install cookiecutter
```

Next, use the `cookiecutter` command, providing the link to this repo, like so:

```bash
cookiecutter https://github.com/GriceTurrble/django-bootstrap-template.git
```

Follow the prompts to set up the project to your liking:

```
project_name [My Project]:
project_slug [my_project]:
description [a site that does stuff]:
author_name [Galen Rice]:
version [0.1.0]:
Select database_backend:
1 - sqlite3
2 - postgres
Choose from 1, 2 [1]:
Select open_source_license:
1 - MIT
2 - BSD
3 - GPLv3
4 - Apache Software License 2.0
5 - Not open source
Choose from 1, 2, 3, 4, 5 [1]:
```

Finally, navigate to the new project directory (the same as the `project_slug` setting). The generated README file there will provide custom instructions based on the options you selected above. Follow those instructions to install and start up your new project.

## Extending your templated project

Once the template is created and you start the site for the first time, you can use it like any other basic Django installation: start new apps, write models, create templates, add static files, and go from there.

This template provides some starting points and working examples you can follow, based on my personal experience with the Django framework and what I would consider best practice. You are more than welcome to disagree with these opinions and take the project in a different direction, of course. :)

Here are some details on what this project template contains:

### The `MyBaseModel` abstract model

Your new project's `core` directory contains [abstract models], utility methods, and other "common" objects you may use elsewhere in your site. Think of it as a root directory for custom Django objects.

A single abstract model, `MyBaseModel`, is currently available. This includes a custom QuerySet used as its model manager, `MyBaseQuerySet`. You may subclass `MyBaseModel` for each model in your application, instead of the standard `models.Model`:

```python
# my_app/models.py

from core.models import MyBaseModel

class MyModel(MyBaseModel):
    ...
```

Any model in your project that subclasses `MyBaseModel` will automatically include the fields defined in `MyBaseModel` and the queryset methods defined in `MyBaseQuerySet`, allowing them to share common logic and data without needing to rewrite them for each model.

For starters, this means the time-tracking fields `created_at` and `updated_at`, as well as these command-style QuerySet methods:

| Method                      | Usage                                                                                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `created_before(dt)`        | Model instances created (via `created_at`) before `dt` (a `datetime.datetime` or `datetime.date` object), inclusive (will return instances of `dt == created_at`). |
| `created_after(dt)`         | Instances created after `dt`.                                                                                                                                      |
| `created_on_date(dt)`       | Instances created on the date of `dt`. Uses Django's [date field lookup]. `dt` is coerced to a `datetime.date` object before being used in the query.           |
| `created_between(dt1, dt2)` | Instances created between `dt1` and `dt2`, inclusive. Uses Django's [range field lookup] (Note the warnings in their documentation for edge cases).             |
| `updated_before(dt)`        | Same as `created_before`, for `updated_at` field.                                                                                                                  |
| `updated_after(dt)`         | Same as `created_after`, for `updated_at` field.                                                                                                                   |
| `updated_on_date(dt)`       | Same as `created_on_date`, for `updated_at` field.                                                                                                                 |
| `updated_between(dt)`       | Same as `created_between`, for `updated_at` field.                                                                                                                 |

Each of these methods returns a QuerySet and can be chained like many other QuerySet methods:

```python
MyModel.objects.filter(...).created_before(...).exclude(...)
# and so on.
```

#### Extending `MyBaseModel` and `MyBaseQuerySet`

`MyBaseModel` serves as a hook for functionality that is shared by all models within a project. If all your models need some common logic - time tracking, soft-deletion, UUID primary keys, etc. - you can add those options to `MyBaseModel` rather than updating each model individually. This ensures that the same baseline functionality is available in any future model you use.

You can also define your own abstract models, either in `core.models` or anywhere else in your project, to follow the same pattern. Concrete models can inherit from multiple other model classes, giving the final model shared functionality of all its ancestors: so feel free to be as granular as you like with different kinds of base abstract models.

The same goes for `MyBaseQuerySet` when you add new fields to `MyBaseModel` and want to use custom filtering, similar to those used for `created_at` and `updated_at`. Simply add new methods to this QuerySet and they'll become available to every model that subclasses `MyBaseModel` and _uses its same QuerySet manager_.

Note that last part: that's where it can get tricky.

#### Subclassing `MyBaseQuerySet`

When you want to add custom fields to a model that subclasses `MyBaseModel`, you may also be inclined to make a new QuerySet and/or Manager class and assign this to the `objects` manager on that model. However, doing so will overwrite `MyBaseQuerySet` as a manager of that model, making its methods unavailable.

Django's documentation regarding [Custom managers and model inheritance][manager_model_inheritance] is quite helpful here. However, their solution revolves around creating multiple managers for a subclassed abstract model with its own base manager, so that you may need to reference a different manager besides `objects`.

Personally, I find it frustrating to use any other manager besides `objects` unless absolutely necessary; and I want to retain the ability to chain all the different custom methods together. My solution and recommendation is to subclass `MyBaseQuerySet`, then use the subclass as the new model's manager:

```python
from base_object.managers import MyBaseQuerySet

class MyQuerySet(MyBaseQuerySet):
    def my_new_method(self):
        ...

class MyModel(MyBaseModel):
    objects = MyQuerySet.as_manager()
```

This way, all methods from `MyBaseQuerySet` are still available in the `objects` manager; the new methods can also be found in the `objects` manager; and they can all be chained together:

```python
MyModel.objects.filter(...).my_new_method().created_before(...)
```

All of that, as I said, is a personal opinion: you can do differently as suits your needs.

### Starter templates

The front page you see when you first launch the project is a static template that includes a lot of handy features to get you started in frontend development:

- The page is served by a generic `TemplateView` defined in `<project_slug>/core/urls.py`, right below the standard `admin` path; no extra view code required! If you want to serve some static pages, this is a good example to follow.
- The main template, `homepage.html`, extends a base template from which all other site templates can be built to give a uniform look and feel. Find this at `templates/base.html` to see its code.
- The base template brings in Bootstrap CSS and JS via CDN; FontAwesome free edition icons via a local copy, served as a deferred script to load SVG icons; and site-specific CSS and JS files, which you'll find in `<project_name>/static/` and that you can edit freely.
- The base template also includes "widget"-style templates for `base_navbar.html` and `base_footer.html`, which inject a Bootstrap navbar in the top of each page and a custom footer, respectively. Separating templates in this way is helpful for compartmentalizing and re-using content: your templates don't need to be one-file monoliths!
  - Note also how `base_navbar.html` adds in a link to the Admin index. See more details on writing Admin URLs [here][reversing_admin_urls]
- You'll see `homepage.html` has very little code; in fact, all it does is include another "widget"-style template, `welcome_wagon.html`, which contains all the contents of the front page. You can quickly remove the "welcome wagon" display by removing the `{% include %}` tag for that template, giving you a blank slate to start from.
  - I would recommend keeping the `welcome_wagon.html` file in your project as a reference.
- One last template, `template_of_templates.html`, contains a basis for new site templates. It includes the `{% extends %}` tag for `base.html` and a copy of each `{% block %}` tag used in that base template. You can easily start up a new page by copying this file, adding the content you need, and removing the blocks you aren't changing.

### Other project contents

- A project-level `static/` directory is available to dump static files that don't fit within an app structure. You can still use app-level static files as needed (and remember to run `collectstatic` in production!), but it's good to have a central spot for site-level static content.
- The project is automatically built with the license of your choice, including your entry for Author Name and the current year.
- The models, querysets, and managers added to `core` have some sparse [type hinting] built in. Running the project in Python <3.5 (which is [not supported in Django, anyway][12]) will cause errors due to these type hints.
  - Since this is a template for a new project, you _should_ be (and I highly recommend) using the latest stable Python release that Django and your other dependencies support.

[abstract models]: https://docs.djangoproject.com/en/4.0/topics/db/models/#abstract-base-classes
[Bootstrap]: https://getbootstrap.com/docs/5.1/getting-started/introduction/
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[date field lookup]: https://docs.djangoproject.com/en/4.0/ref/models/querysets/#date
[Django]: https://www.djangoproject.com/
[FontAwesome]: https://fontawesome.com/
[manager_model_inheritance]: https://docs.djangoproject.com/en/4.0/topics/db/managers/#custom-managers-and-model-inheritance
[range field lookup]: https://docs.djangoproject.com/en/4.0/ref/models/querysets/#range
[reversing_admin_urls]: https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#reversing-admin-urls
[type hinting]: https://docs.python.org/3/library/typing.html
