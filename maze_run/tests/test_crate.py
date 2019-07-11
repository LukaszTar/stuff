from moves import move
from moves import LEFT, RIGHT, UP, DOWN
from draw_maze import parse_grid
import pytest

LEVEL = """
#######
#.....#
#..o..#
#.o*o.#
#..o..#
#.....#
#######"""

LEVEL_NO_DOTS = LEVEL.replace('.', ' ')

PATH_PLAYERPOS = [
    ((UP, LEFT), 2, 2),
    ((LEFT, UP), 2, 2),
    ((RIGHT, UP, LEFT, LEFT), 2, 2),
    ((UP,), 2, 3),
    ((LEFT, RIGHT), 3, 3),
    ((RIGHT, RIGHT), 4, 3)
]

CRATE_MOVES = [
    (LEFT, (3, 2), (3, 1)),
    (RIGHT, (3, 4), (3, 5)),
    (UP, (2, 3), (1, 3)),
    (DOWN, (4, 3), (5, 3))
]

@pytest.fixture(params=[LEVEL, LEVEL_NO_DOTS])
def level(request):
    return parse_grid(request.param)

@pytest.mark.parametrize('path, expected_x, expected_y', PATH_PLAYERPOS)
def test_paths(path,expected_x, expected_y, level):
    """różne ścieżki prowadzą do tego samego miejsca"""
    for direction in path:
        move(level, direction)
    assert level[expected_x][expected_y] == '*'

class TestCrateMoves:
    @pytest.mark.parametrize('direction, plr_pos, crate_pos',CRATE_MOVES)
    def test_move_crate(self, level, direction, plr_pos, crate_pos):
        """Po wykonaniu funkcji move gracz i skrzynia przesunieci o jedna kratke"""
        print(direction, plr_pos, crate_pos)
        move(level, direction)
        assert level[plr_pos[0]][plr_pos[1]] == '*'
        assert level[crate_pos[0]][crate_pos[1]] == 'o'

class TestPlayerMoves:
    def test_move_to_none(self):
        """direction=None generuje wyjatek"""
        with pytest.xfail(TypeError):
            move(level, None)

    @pytest.mark.parametrize('path, expected_x, expected_y', PATH_PLAYERPOS)
    def test_move_player(self, level, path, expected_x, expected_y):
        """pozycja gracza prawidlowo zmienila polozenie"""
        for direction in path:
            move(level, direction)
        assert level[expected_y][expected_x]

def test_push_crate_to_wall():
    maze = parse_grid('*o#')
    move(maze, RIGHT)
    assert maze[0] == ['*', 'o', '#']

def test_push_crate_to_crate():
    maze = parse_grid('*oo')
    move(maze, RIGHT)
    assert maze[0] == ['*', 'o', 'o']