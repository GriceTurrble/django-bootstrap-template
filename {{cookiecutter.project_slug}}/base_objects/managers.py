"""Custom querysets and managers for base abstract models."""

import datetime

from django.db import models

from base_objects.typing import DTType


class ProjectBaseQuerySet(models.QuerySet):
    """Base queryset with custom filtering methods for base abstract models."""

    ## `time_created` command-style filtering ##
    def created_before(self, dt_: DTType) -> models.QuerySet:
        """Returns instances created before the given date/datetime."""
        return self.filter(time_created__lte=dt_)

    def created_after(self, dt_: DTType) -> models.QuerySet:
        """Returns instances created after the given date/datetime."""
        return self.filter(time_created__gte=dt_)

    def created_on_date(self, dt_: DTType) -> models.QuerySet:
        """Returns instances created on the date of the given date/datetime."""
        date = dt_
        if isinstance(dt_, datetime.datetime):
            date = dt_.date()
        return self.filter(time_created__date=date)

    def created_between(self, dt_one: DTType, dt_two: DTType) -> models.QuerySet:
        """Returns instances created within the range (dt_one, dt_two)."""
        return self.filter(time_created__range=(dt_one, dt_two))

    ## `time_modified` command-style filtering ##
    def modified_before(self, dt_: DTType) -> models.QuerySet:
        """Returns instances modified before the given date/datetime."""
        return self.filter(time_modified__lte=dt_)

    def modified_after(self, dt_: DTType) -> models.QuerySet:
        """Returns instances modified after the given date/datetime."""
        return self.filter(time_modified__gte=dt_)

    def modified_on_date(self, dt_: DTType) -> models.QuerySet:
        """Returns instances modified on the date of the given date/datetime."""
        date = dt_
        if isinstance(dt_, datetime.datetime):
            date = dt_.date()
        return self.filter(time_modified__date=date)

    def modified_between(self, dt_one: DTType, dt_two: DTType) -> models.QuerySet:
        """Returns instances modified within the range (dt_one, dt_two)."""
        return self.filter(time_modified__range=(dt_one, dt_two))
