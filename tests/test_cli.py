from ets2_modhelper.cli import main
from ets2_modhelper.games import GAMES


def test_main_runs_for_every_game(capsys):
    for key in GAMES:
        assert main(["--game", key]) == 0
        assert GAMES[key].display_name in capsys.readouterr().out
