import pytest

from {{ cookiecutter.project_name }}.{{ cookiecutter.project_name }} import main

def test_main():
    assert main() == "Hello, world."
