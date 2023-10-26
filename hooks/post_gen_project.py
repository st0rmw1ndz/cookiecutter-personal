import os
import shutil


def remove(path: str) -> None:
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


use_cli: bool = "{{cookiecutter.cli}}" == "True"
mypy_strict: bool = "{{cookiecutter.mypy_strict}}" == "True"


if not use_cli:
    remove(os.path.join("src", "__main__.py"))
    remove(os.path.join("src", "cli.py"))

if not mypy_strict:
    remove("mypy.ini")
