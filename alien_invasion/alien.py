import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load alien image
        self.image = pygame.image.load('./images/alien.bmp')
        self.rect = self.image.get_rect()

        # Set location
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store location
        self.x = float(self.rect.x)
