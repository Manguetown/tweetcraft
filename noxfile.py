import nox

import os


@nox.session
def tests_and_coverage(session):
    """ Install all requirements, run pytest.
    """
    session.install("-r", "requirements.txt")
    session.install("coverage")
    session.install("pytest")
    session.run("coverage", "run",  "-m",  "--omit=.nox/*", "pytest")
    session.run("coverage", "report", "--fail-under=70", "--show-missing")
    session.run("coverage", "erase")

@nox.session
def black_check(session):
    """ Install all requirements, run pytest.
    """
    session.install("black")
    session.run("black", "--check", "--diff",  "src")
