import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        #Load teh alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near teh top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store teh alien's exact horizontal position.
        self.x = float(self.rect.x)