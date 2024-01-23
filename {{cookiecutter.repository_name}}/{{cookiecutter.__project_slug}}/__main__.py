import click

from {{cookiecutter.__project_slug}} import __version__


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__)
def cli() -> None:
    """{{cookiecutter.project_description}}

    Copyright (c) 2024 {{cookiecutter.__author}}.
    """
    pass
