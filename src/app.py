import os
import shlex
import subprocess  # noqa: S404 - needed to run commands; used safely below

# Read the password from an environment variable instead of hardcoding it
PASSWORD = os.environ.get("APP_PASSWORD", "")


def add(a, b):
    return a + b


def greet(name):
    message = (
        "Hello, " + name + "! "
        "Welcome to the DevSecOps assignment demo application for Assignment 9."
    )
    return message


def run(cmd):
    # shell=False with an argument list prevents shell injection
    args = shlex.split(cmd)
    return subprocess.call(args, shell=False)  # noqa: S603 - no shell is used


def login(username, password):
    # Never log the password; log only the username
    print("Login attempt:", username)
    return password == PASSWORD
