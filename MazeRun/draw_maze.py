from pygame import image, Rect, Surface
from load_tiles import load_tiles, get_tile_rect, SIZE
from generate_maze import create_maze
from moves import move
import random

def parse_grid(data):
    """Parsuje reprezentacje tekstową do postaci zagnieżdżonej listy"""
    return [list(row) for row in data.strip().split("\n")]

def draw_grid(data, tile_img, tiles):
    """Zwraca obraz siatki złożonej z płytek"""
    xs = len(data[0]) * SIZE
    ys = len(data) * SIZE
    img = Surface((xs, ys))
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            img.blit(tile_img, get_tile_rect(x, y), tiles[char])
    return img

if __name__ == "__main__":
    tile_img, tiles = load_tiles()
    maze = create_maze(12, 7)
    maze = parse_grid(maze)
    maze[1][1] = '*'
    for i in range(100):
        direction = random.choice([LEFT, RIGHT, UP, DOWN])
        move(maze, direction)
    img = draw_grid(maze, tile_img, tiles)
    image.save(img, 'maze.png')