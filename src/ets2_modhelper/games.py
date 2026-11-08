"""Supported games. ETS2 and ATS share the same engine and file formats."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Game:
    key: str
    display_name: str
    steam_app_id: int
    install_dir_name: str  # folder name under steamapps/common
    user_dir_name: str  # folder name of the user data directory


GAMES: dict[str, Game] = {
    "ets2": Game(
        "ets2", "Euro Truck Simulator 2", 227300, "Euro Truck Simulator 2", "Euro Truck Simulator 2"
    ),
    "ats": Game(
        "ats",
        "American Truck Simulator",
        270880,
        "American Truck Simulator",
        "American Truck Simulator",
    ),
}
