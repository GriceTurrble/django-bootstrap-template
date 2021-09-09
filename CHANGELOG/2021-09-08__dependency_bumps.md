# 2021-09-08 - Update to Django 3.2 latest

Dependencies have been updated to use [compatible release format](https://www.python.org/dev/peps/pep-0440/#compatible-release), setting the minimum versions for packages and allowing later patch versions to be installed more easily.

Have also changed the `psycopg2` dependency (for those who might use it) to `psycopg2-binary`. I find the latter easier to work with in most scenarios.

Finally, set the min version for `pytz`. Can never be too careful with that one!
