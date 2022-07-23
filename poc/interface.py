import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from pygame.locals import *

# FPS
FPS = 8
FP = 1000 // FPS

# window resolution
WIDTH = 640
HEIGHT = 480

# window mode

FULLSCREEN = False
WINDOW_MODE = pygame.FULLSCREEN if FULLSCREEN else 0

# window position
LEFT_TOP = (0, 0)

# some colors
BLACK = (0, 0, 0)

# initilize pyagme
pygame.init()

print(pygame.display.Info())

class GameInterface:
    def __init__(self):
        # create Window
        self.window = pygame.display.set_mode((WIDTH, HEIGHT), WINDOW_MODE)
        pygame.display.set_caption('Land War')

        # create background
        self.background = pygame.Surface((WIDTH, HEIGHT))
        self.background.fill(BLACK)

        # looping status
        self.looping = True

    def run(self):
        self.looping = True
        while self.looping:
            self.check_event()
            self.render()
            pygame.display.flip()
            pygame.time.delay(FP)

    def render(self):
        self.window.blit(self.background, LEFT_TOP)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.looping = False

class PlayerInterface(GameInterface):
    pass

class SpectatorInteface(GameInterface):
    pass


def start_interface():

    # initialize pygame
    pygame.init()

    # create window


