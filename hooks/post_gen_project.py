from pathlib import Path


def remove(path: Path) -> None:
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        path.rmdir()


if not "{{ cookiecutter.cli }}" == "True":
    remove(Path("{{ cookiecutter.__project_slug }}") / "__main__.py")
