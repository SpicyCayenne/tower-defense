"""Contains all the methods to calculate projectile travel and collision"""
import os
import pygame

class Projectile:
    """Draw, move, and detect collision of projectiles"""
    def __init__(self, img, x, y, display_surface):
        self.img_file = img
        self.img = pygame.image.load(os.path.join('assets', 'towers', self.img_file))
        self.ammo_rect = self.img.get_rect()
        self.ammo_rect.center(x, y)
        self.display_surface = display_surface

    def draw(self):
        """Draws the projectile onto the screen"""
        self.display_surface.blit(self.img, (self.ammo_rect))

    def move(self):
        """Moves the projectile towards the target"""

    def collision(self, target):
        """Calculates the distance between the projectile and the target
        If distance is small enough, triggers a hit on the target and despawns
        the projectile"""
