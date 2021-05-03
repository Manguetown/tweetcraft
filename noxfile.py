import nox

import os

@nox.session
def tests_coverage(session):
    """ Install all requirements, run pytest.
    """
    session.install("-r", "requirements.txt")
    session.run("coverage", "run",  "-m",  "--omit=.nox/*", "pytest")
    session.run("coverage", "report", "--fail-under=70", "--show-missing")
    session.run("coverage", "erase")
    

@nox.session
def lint(session):
    """ Lint using flake8.
    """
    session.install("flake8")
    
    folders = ["text", "tests"]
    
    for folder_name in folders:
        for files in os.listdir(folder_name):
            if files[0] not in ['_', '.']:
                session.run("flake8", f"{folder_name}/{files}")
