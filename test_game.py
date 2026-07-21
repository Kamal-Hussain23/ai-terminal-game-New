import io
import sys
from contextlib import redirect_stdout
from unittest.mock import patch

import game


def reset():
    game.player_x = 0
    game.player_y = 0
    game.score = 0
    game.collectible_x = 2
    game.collectible_y = 2


def capture_grid():
    f = io.StringIO()
    with redirect_stdout(f):
        game.draw_grid()
    return f.getvalue().strip().splitlines()


def setup_function():
    reset()


def test_start_position():
    assert game.player_x == 0
    assert game.player_y == 0


def test_draw_grid_shows_player():
    lines = capture_grid()
    assert lines[0].strip() == "P . . . ."


def test_draw_grid_shows_collectible():
    game.collectible_x = 0
    game.collectible_y = 1
    lines = capture_grid()
    assert lines[1].strip() == "C . . . ."


def test_move_right():
    game.move(1, 0)
    assert game.player_x == 1
    assert game.player_y == 0
    lines = capture_grid()
    assert lines[0].strip() == ". P . . ."


def test_move_down():
    game.player_x, game.player_y = 1, 0
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


def test_collect_increases_score():
    game.player_x, game.player_y = 2, 2
    game.move(0, 0)
    assert game.score == 1


def test_collect_respawns_collectible():
    game.player_x, game.player_y = 2, 2
    old_cx, old_cy = game.collectible_x, game.collectible_y
    game.move(0, 0)
    assert (game.collectible_x, game.collectible_y) != (old_cx, old_cy)


def test_collect_respawns_not_on_player():
    game.player_x, game.player_y = 2, 2
    game.move(0, 0)
    assert (game.collectible_x, game.collectible_y) != (game.player_x, game.player_y)


def test_score_starts_at_zero():
    assert game.score == 0


def test_main_loop_quit():
    with patch("builtins.input", return_value="quit"):
        with redirect_stdout(io.StringIO()):
            game.main_loop()


def test_main_loop_unknown_command():
    inputs = iter(["xyz", "quit"])
    with patch("builtins.input", side_effect=inputs):
        f = io.StringIO()
        with redirect_stdout(f):
            game.main_loop()
    output = f.getvalue()
    assert "Unknown command." in output


def test_main_loop_wasd():
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


def test_main_loop_shows_score():
    inputs = iter(["d", "quit"])
    with patch("builtins.input", side_effect=inputs):
        f = io.StringIO()
        with redirect_stdout(f):
            game.main_loop()
    assert "Score:" in f.getvalue()


def test_spawn_collectible_not_on_player():
    game.spawn_collectible()
    assert (game.collectible_x, game.collectible_y) != (game.player_x, game.player_y)
