# Changelog

## 2020-08-04 - Update to Django 3.1

The template now starts at Django 3.1, released same day as this PR.

- `settings.py` has been regenerated from 3.1. This now uses `pathlib` to build `BASE_DIR`, instead of the older method that used `os.path`.
- All docs references to 3.0 have been updated to link to the 3.1 docs.
- Dependabot badge added to README cuz why not?
- Files have been formatted with Black.
