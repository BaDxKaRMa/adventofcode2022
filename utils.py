#!/usr/bin/env python3


def _parse_into_list(file) -> list:
    try:
        with open(file, "r") as f:
            input_file = f.read()
            input_file = input_file.splitlines()
            return input_file
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


if __name__ == "__main__":
    pass
