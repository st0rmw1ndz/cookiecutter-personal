import os
import shutil


def remove(path: str) -> None:
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


use_cli: bool = "{{ cookiecutter.cli }}" == "True"


if not use_cli:
    remove(os.path.join("{{ cookiecutter.__project_slug }}", "__main__.py"))
    remove(os.path.join("{{ cookiecutter.__project_slug }}", "cli.py"))
