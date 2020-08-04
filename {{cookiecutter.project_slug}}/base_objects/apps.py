from django.apps import AppConfig

# AppConfig documentation:
# https://docs.djangoproject.com/en/3.1/ref/applications/


class BaseObjectsConfig(AppConfig):
    name = "base_objects"
    verbose_name = "Project base objects"

    def ready(self):
        """Got some code you want to run once on site startup, when the app is fully loaded?
        Here's a good spot to put it!
        See: https://docs.djangoproject.com/en/3.1/ref/applications/#django.apps.AppConfig.ready
        """
        pass
