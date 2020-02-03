import random
import os
import re
import fileinput

def generate_key(length=50):
    choice_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    return "".join([random.SystemRandom().choice(choice_set) for i in range(length)])


target = "!!!SET_DJANGO_SECRET_KEY!!!"
new_key = generate_key()
filepath = os.path.join(
    "{{cookiecutter.directory_name}}", "{{cookiecutter.directory_name}}", "settings.py"
)

with fileinput.FileInput(filepath, inplace=True) as thefile:
    for line in thefile:
        print(line.replace(target, new_key), end='')
