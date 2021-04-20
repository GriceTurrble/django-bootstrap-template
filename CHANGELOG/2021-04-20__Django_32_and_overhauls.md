# 2021-04-20 - Update to Django 3.2, and some additional overhauls

The template now starts at Django 3.2, which was released on April 6, 2021.

**Details**: https://docs.djangoproject.com/en/3.2/releases/3.2/

Notable changes to this template:

- Django 3.2 adds [changing the type of auto-created primary keys][custom_auto_field] for new models, when no field is defined with `primary_key=True`.
  - New setting `DEFAULT_AUTO_FIELD` has been added to `settings.py`
- Project files have been moved one level down

## Other changes

- Bootstrap bumped to 4.6.0
- FontAwesome bumped to 5.15.3
- Generated README.rst changed to README.md (Markdown).
  - I figure most folks are more familiar with Markdown, anyway, so better to start there.
- Content of generated README.md updated with project installation instructions.
- The base project directory, containing your `settings.py` and root `urls.py` files, has been renamed to `core`.
  - By default, new Django projects using the `startproject` command create directories by the same name, such that you'd find `settings.py` at `my_project/my_project/settings.py`. This can be a stumbling block for some newcomers, and the purpose of this subdirectory named the same as the project is often unclear.
  - Some users opt for this `core` pattern, helping distinguish the "core" of the project from the other apps contained therein.
  - I've opted for this latter approach, so starting new projects from this template, you will see the `core/` directory instead of a directory named after your project slug.
- `ProjectBaseModel` renamed to `MyBaseModel`.
  - I figure this is an easier name to conceptualize.
  - Associated `ProjectBaseQuerySet` and `ProjectBaseManager` also renamed to `MyBaseQuerySet` and `MyBaseManager`, respectively.
  - You'll find these objects in the `core` directory (see next change).
- The `base_objects` app has been removed. The objects that were defined there now live in the `core` directory.

  - I found no reason to maintain that pseudo-app structure when it only contains abstract models and associated helper classes.
  - Using the new template, there is no need to list an extra "app" in settings: just import objects from `core` like any other Python package. For instance:

    ```python
    from core.models import MyBaseModel

    class MyModel(MyBaseModel):
        ...
    ```

- **Bug**: the `.env` file was not being read by django-environs properly due to a missing line in `settings.py`. This has been corrected, so new projects should be able to start up smoothly.

[custom_auto_field]: https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
[automatic_appconfig_discovery]: https://docs.djangoproject.com/en/3.2/releases/3.2/#automatic-appconfig-discovery
