import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Set screen resolution
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Set title
        pygame.display.set_caption("Alien Invasion")

        # Init ship
        self.ship = Ship(self)

    def run_game(self):
        '''Start game'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        '''Response to mouse and keyboard'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    '''Ship moves to right'''
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    '''Ship moves to left'''
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        '''Update contents on screen'''
        self.screen.fill(self.settings.bg_color)  # Set background color
        self.ship.blitme()  # Generate ship
        pygame.display.flip()  # Regenerate screen


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
