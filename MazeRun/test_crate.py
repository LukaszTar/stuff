from draw_maze import parse_grid
from moves import move
from moves import LEFT, RIGHT, UP, DOWN

LEVEL = """
#######
#.....#
#..o..#
#.o*o.#
#..o..#
#.....#
#######"""

def move_crate(direction, plr_pos, crate_pos):
    maze = parse_grid(LEVEL)
    move(maze, direction)
    assert maze[plr_pos[0]][plr_pos[1]] == '*'
    assert maze[crate_pos[0]][crate_pos[1]] == 'o'

def test_move_crate_left():
    move_crate(LEFT, (3, 2), (3, 1))

def test_move_crate_right():
    move_crate(RIGHT, (3, 4), (3, 5))

def test_move_crate_up():
    move_crate(UP, (2, 3), (1, 3))

def test_move_crate_down():
    move_crate(DOWN, (4, 3), (5, 3))
