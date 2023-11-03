from pathlib import Path


def _get_version() -> str:
    """Reads the version from file

    :return: Version from file
    """
    version_path = Path(__file__).parent.resolve() / "version.txt"

    return version_path.read_text(encoding="utf-8").strip()


__version__ = _get_version()
