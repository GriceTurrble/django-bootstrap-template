"""Custom querysets and managers for base abstract models."""

import datetime

from django.db import models

from core.typing import DTType


class MyBaseQuerySet(models.QuerySet):
    """Base queryset with custom filtering methods for base abstract models."""

    ## `created_at` command-style filtering ##
    def created_before(self, dt_: DTType) -> models.QuerySet:
        """Returns instances created before the given date/datetime."""
        return self.filter(created_at__lte=dt_)

    def created_after(self, dt_: DTType) -> models.QuerySet:
        """Returns instances created after the given date/datetime."""
        return self.filter(created_at__gte=dt_)

    def created_on_date(self, dt_: DTType) -> models.QuerySet:
        """Returns instances created on the date of the given date/datetime."""
        date = dt_
        if isinstance(dt_, datetime.datetime):
            date = dt_.date()
        return self.filter(created_at__date=date)

    def created_between(self, dt_one: DTType, dt_two: DTType) -> models.QuerySet:
        """Returns instances created within the range (dt_one, dt_two)."""
        return self.filter(created_at__range=(dt_one, dt_two))

    ## `updated_at` command-style filtering ##
    def updated_before(self, dt_: DTType) -> models.QuerySet:
        """Returns instances updated before the given date/datetime."""
        return self.filter(updated_at__lte=dt_)

    def updated_after(self, dt_: DTType) -> models.QuerySet:
        """Returns instances updated after the given date/datetime."""
        return self.filter(updated_at__gte=dt_)

    def updated_on_date(self, dt_: DTType) -> models.QuerySet:
        """Returns instances updated on the date of the given date/datetime."""
        date = dt_
        if isinstance(dt_, datetime.datetime):
            date = dt_.date()
        return self.filter(updated_at__date=date)

    def updated_between(self, dt_one: DTType, dt_two: DTType) -> models.QuerySet:
        """Returns instances updated within the range (dt_one, dt_two)."""
        return self.filter(updated_at__range=(dt_one, dt_two))
