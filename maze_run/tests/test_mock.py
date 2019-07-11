from pygame import image, Rect
import pygame
from unittest import mock


pygame.init()
pygame.display.set_mode((80, 60))

def draw(surface):
    img = image.load('tiles.xpm')
    surface.blit(img, Rect((0, 0, 32, 32)), Rect((0, 0, 32, 32)))
    pygame.display.update()

@mock.patch('pygame.display.update')
def test_mocking(mock_update):
    display = pygame.display.get_surface()
    draw(display)
    assert mock_update.called is True
    assert mock_update.call_count == 1

def test_blit():
    mock_disp = mock.MagicMock(name='display')
    draw(mock_disp)
    assert mock_disp.blit.called is True