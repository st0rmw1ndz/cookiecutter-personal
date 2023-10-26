import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="{{ cookiecutter.repository_name.replace('-', '_') }}",
        description="{{ cookiecutter.project_description }}",
        epilog="Source code: {{ cookiecutter.repository_url }}",
    )
    parser.add_argument("_", nargs="*")

    args = parser.parse_args()
    return args


def main() -> int:
    args = parse_args()
    print("Arguments:", args)

    return 0
