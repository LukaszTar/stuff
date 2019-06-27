from pygame.locals import KEYDOWN
import pygame

def event_loop(handle_key, delay=10):
    """Przetwarzanie zdarzen i aktualzacja wywołań zwrotnych"""
    while True:
        pygame.event.pump()
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            handle_key(event.key)
        pygame.time.delay(delay)


if __name__ == "__main__":
    pygame.init()
    event_loop(print)