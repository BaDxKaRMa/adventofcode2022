#!/usr/bin/env python3
import argparse
import sys


try:
    from loguru import logger
except ImportError:
    print("Please pip install loguru")
    sys.exit(1)


def parse_args():
    """
    Parses debug and folder arguments.

    Variables:
    debug (bool): If True, debug logging will be enabled. Default = False

    Returns: (argparse.Namespace): Parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        required=False,
        help="Enable debug logging",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        default=False,
        required=False,
        help="Run tests",
    )
    return parser.parse_args()


def setup_logging(debug: bool):
    """
    Setup loguru logging.

    Variables:
    debug (bool): If True, debug logging will be enabled. Default = False

    Returns:
    logger (loguru.logger): Loguru logger object.
    """
    # Remove all built in handlers
    logger.remove()
    # Set custom loguru format
    fmt = (
        "<level>{time:YYYY-MM-DD hh:mm:ss A}</level> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{"
        "function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level> "
    )
    # Set Debug level if --debug is passed
    if debug:
        logger.add(sys.stderr, format=fmt, level="DEBUG")
    else:
        logger.add(sys.stderr, format=fmt, level="INFO")
    return logger


if __name__ == "__main__":
    pass
