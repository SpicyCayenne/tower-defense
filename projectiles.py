"""Contains all the methods to calculate projectile travel and collision"""
import os
import pygame
#from pygame import Vector2

class Projectile:
    """Draw, move, and detect collision of projectiles"""

    fired = []

    def __init__(self, img, x, y, display_surface, target_x, target_y):
        self.img_file = img
        self.img = pygame.image.load(os.path.join('assets', 'towers', self.img_file))
        self.ammo_rect = self.img.get_rect()
        self.ammo_rect.center = (x, y)
        self.display_surface = display_surface
        self.target_x = target_x
        self.target_y = target_y

    def draw(self):
        """Draws the projectile onto the screen"""
        self.display_surface.blit(self.img, (self.ammo_rect))

    def move(self):
        """Moves the projectile towards the target"""
        print(self.target_x, self.target_y)
        print(self.ammo_rect[0], self.ammo_rect[1])
        print(self.ammo_rect.center[0], self.ammo_rect.center[1])

    def collision(self, target):
        """Calculates the distance between the projectile and the target
        If distance is small enough, triggers a hit on the target and despawns
        the projectile"""
