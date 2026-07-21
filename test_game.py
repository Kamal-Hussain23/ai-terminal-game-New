import io
import sys
from contextlib import redirect_stdout
from unittest.mock import patch

import game


def capture_grid():
    f = io.StringIO()
    with redirect_stdout(f):
        game.draw_grid()
    return f.getvalue().strip().splitlines()


def test_start_position():
    assert game.player_x == 0
    assert game.player_y == 0


def test_draw_grid_shows_player():
    lines = capture_grid()
    assert lines[0].strip() == "P . . . ."


def test_move_right():
    game.move(1, 0)
    assert game.player_x == 1
    assert game.player_y == 0
    lines = capture_grid()
    assert lines[0].strip() == ". P . . ."


def test_move_down():
    game.move(0, 1)
    assert game.player_x == 1
    assert game.player_y == 1
    lines = capture_grid()
    assert lines[1].strip() == ". P . . ."


def test_move_left():
    game.player_x, game.player_y = 2, 0
    game.move(-1, 0)
    assert game.player_x == 1


def test_move_up():
    game.player_x, game.player_y = 0, 2
    game.move(0, -1)
    assert game.player_y == 1


def test_boundary_top():
    game.player_x, game.player_y = 0, 0
    game.move(0, -1)
    assert game.player_x == 0 and game.player_y == 0


def test_boundary_left():
    game.player_x, game.player_y = 0, 0
    game.move(-1, 0)
    assert game.player_x == 0 and game.player_y == 0


def test_boundary_bottom():
    game.player_x, game.player_y = 0, 4
    game.move(0, 1)
    assert game.player_x == 0 and game.player_y == 4


def test_boundary_right():
    game.player_x, game.player_y = 4, 0
    game.move(1, 0)
    assert game.player_x == 4 and game.player_y == 0


def test_main_loop_quit():
    game.player_x, game.player_y = 0, 0
    with patch("builtins.input", return_value="quit"):
        with redirect_stdout(io.StringIO()):
            game.main_loop()


def test_main_loop_unknown_command():
    game.player_x, game.player_y = 0, 0
    inputs = iter(["xyz", "quit"])
    with patch("builtins.input", side_effect=inputs):
        f = io.StringIO()
        with redirect_stdout(f):
            game.main_loop()
    output = f.getvalue()
    assert "Unknown command." in output


def test_main_loop_wasd():
    game.player_x, game.player_y = 0, 0
    inputs = iter(["d", "quit"])
    with patch("builtins.input", side_effect=inputs):
        with redirect_stdout(io.StringIO()):
            game.main_loop()
    assert game.player_x == 1 and game.player_y == 0


def test_main_loop_wasd_all_directions():
    game.player_x, game.player_y = 2, 2
    inputs = iter(["w", "a", "s", "d", "quit"])
    with patch("builtins.input", side_effect=inputs):
        with redirect_stdout(io.StringIO()):
            game.main_loop()
    assert game.player_x == 2 and game.player_y == 2
