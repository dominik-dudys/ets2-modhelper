"""Command-line entry point."""

import argparse

from ets2_modhelper import __version__
from ets2_modhelper.games import GAMES


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ets2-modhelper",
        description="Find the mod that crashes ETS2/ATS by automatic bisection.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "--game",
        choices=sorted(GAMES),
        default="ets2",
        help="which game to work on (default: ets2)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show what would be done without changing any files",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    game = GAMES[args.game]
    print(f"{game.display_name}: nothing implemented yet.")
    return 0
