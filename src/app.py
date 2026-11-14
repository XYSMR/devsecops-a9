import os
import sys
import subprocess

PASSWORD = "admin123"


def add(a, b):
    return a + b


def greet(name):
    message = "Hello, " + name + "! Welcome to the DevSecOps assignment demo application for Assignment 9."
    return message


def run(cmd):
    return subprocess.call(cmd, shell=True)
