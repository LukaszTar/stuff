import sys

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

DIRECTIONS = {
    276: LEFT,
    275: RIGHT,
    273: UP,
    274: DOWN
}

def get_player_position(level, player_char='*'):
    """Zwraca krotkę (x,y) znaku gracza dla poziomu"""
    for y, row in enumerate(level):
        for x, char in enumerate(row):
            if char == player_char:
                return (x, y)


def move(level, direction):
    oldx, oldy = get_player_position(level)
    newx = oldx + direction[0]
    newy = oldy + direction[1]
    if level[newy][newx] == 'x':
        sys.exit(0)
    if level[newy][newx] == 'o':
        cratex = newx + direction[0]
        cratey = newy + direction[1]
        level[cratey][cratex] = 'o'
    if level[newy][newx] != '#':
        level[oldy][oldx] = ' '
        level[newy][newx] = '*'