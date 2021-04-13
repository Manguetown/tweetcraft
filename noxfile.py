import nox

@nox.session
def tests(session):
    session.install("-r", "requirements.txt")
    session.run("pytest")

@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8", "text/text.py")
