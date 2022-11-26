import pygame


class Ship:
    def __init__(self, ai_game):
        '''Settings about ship'''
        # Initial ship and set location
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get circumscribed rectangle shape
        self.image = pygame.image.load(
            '/home/setsuna/workspace/python_exercises/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Put ship at the bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Generate ship on screen'''
        self.screen.blit(self.image, self.rect)
