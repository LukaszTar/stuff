from load_tiles import load_tiles
from generate_maze import create_maze
from event_loop import event_loop
from draw_maze import draw_grid, parse_grid
from moves import move, LEFT, RIGHT, UP, DOWN, DIRECTIONS
from pygame import Rect
import pygame

pygame.init()
pygame.display.set_mode((800, 600))
display = pygame.display.get_surface()

maze = parse_grid((create_maze(12, 7)))
maze[1][1] = '*'
maze[5][10] = 'x'
tile_img, tiles = load_tiles()
img = draw_grid(maze, tile_img, tiles)
display.blit(img, Rect(0, 0, 384, 224), Rect(0, 0, 384, 224))
pygame.display.update()
def handle_key(key):
    """Obsluguje zdarzenia nacisniecia klawiszy w grze"""
    direction = DIRECTIONS.get(key)
    if direction:
        move(maze, DIRECTIONS.get(key))
    img = draw_grid(maze, tile_img, tiles)
    display.blit(img, Rect(0, 0, 384, 224), Rect(0, 0, 384, 224))
    pygame.display.update()

event_loop(handle_key)
