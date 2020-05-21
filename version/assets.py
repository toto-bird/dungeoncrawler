import pygame
from os import *

class Assets:
    def __init__(self, options):
        self.background = pygame.image.load(path.join(options['assets'], 'background.png'))

        self.buttons = pygame.image.load(path.join(options['assets'], 'buttons.png'))
        self.buttons_hover = pygame.image.load(path.join(options['assets'], 'buttons_hover.png'))
        self.buttons_click = pygame.image.load(path.join(options['assets'], 'buttons_click.png'))