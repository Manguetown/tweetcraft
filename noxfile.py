import nox

import os


@nox.session
def tests(session):
    session.install("-r", "requirements.txt")
    session.run("pytest")


@nox.session
def lint(session):
    session.install("flake8")

    folders = ["text", "tests", "scrape"]

    for folder_name in folders:
        for files in os.listdir(folder_name):
            if files[0] != '_':
                session.run("flake8", f"{folder_name}/{files}")

    out_files = ["app.py", "noxfile.py"]

    for files in out_files:
        session.run("flake8", f"{files}")
