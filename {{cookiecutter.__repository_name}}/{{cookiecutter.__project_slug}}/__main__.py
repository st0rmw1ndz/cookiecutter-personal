import sys

from loguru import logger

from .cli import main


def _setup_loggers() -> None:
    """Sets up the logging handlers using Loguru."""

    logger.remove()
    logger.add(
        "{{ cookiecutter.__project_slug }}_{time}.log",
        format="[{time:HH:mm:ss}] {level} - {message}",
        level="INFO",
    )
    logger.add(
        sys.stdout,
        format="{message}",
        level="DEBUG",
    )


if __name__ == "__main__":
    _setup_loggers()
    sys.exit(main())
