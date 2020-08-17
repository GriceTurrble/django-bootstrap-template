# 2020-08-17 - Changed from Dependabot.com to GitHub Dependabot proper.

Just a bit of housekeeping here. Now uses GitHub Dependabot (config defined in `.github/dependabot.yml`) instead of the older Dependabot.com config.

I got on this partly due to an issue with the dynamic `requirements.txt` file in the project template, which includes some Jinja2 template syntax to change some dependencies dynamically. Dependabot showed it can't read those lines, so dependency checking was disabled. This led to
writing a compiled version of the requirements file, `.github/dependabot_reqs/requirements.txt`.

This is all strictly project internals, and no changes have been made to the project template itself; but I figured I'd leave notes behind for myself and anyone else who might be curious. :)
