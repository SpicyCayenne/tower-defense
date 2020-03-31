"""Contains all the methods to calculate projectile travel and collision"""
import math
import os
import pygame

class Projectile:
    """Draw, move, and detect collision of projectiles"""

    fired = []

    def __init__(self, img, x, y, display_surface, target, direction=0):
        self.img_file = img
        self.img = pygame.image.load(os.path.join('assets', 'towers', self.img_file))
        self.ammo_rect = self.img.get_rect()
        self.x_coord = x
        self.y_coord = y
        self.ammo_rect.center = (x, y)
        self.display_surface = display_surface
        self.target = target
        self.direction = direction

    def draw(self):
        """Draws the projectile onto the screen"""
        self.display_surface.blit(self.img, (self.ammo_rect))

    def move(self):
        """Moves the projectile towards the target"""
        origin = (self.x_coord, self.y_coord)
        ammo_x = self.ammo_rect.center[0]
        ammo_y = self.ammo_rect.center[1]
        origin_vector = (origin[0] - ammo_x, origin[1] - ammo_y)
        distance_from_origin = math.sqrt(origin_vector[0]**2 + origin_vector[1]**2)
        movement_vector = (self.target.hostile_rect.center[0] - ammo_x,
                           self.target.hostile_rect.center[1] - ammo_y)
        distance_to_target = math.sqrt(movement_vector[0]**2 + movement_vector[1]**2)
        if distance_from_origin > 1:
            normalize = (origin_vector[0]/distance_from_origin * -1.25,
                         origin_vector[1]/distance_from_origin * -1.25)
            direction = normalize
        if distance_to_target > 5:
            normalize = (movement_vector[0]/distance_to_target,
                         movement_vector[1]/distance_to_target)
        direction = normalize
        speed_x = direction[0] * 2
        speed_y = direction[1] * 2
        ammo_x += speed_x
        ammo_y += speed_y
        self.ammo_rect.center = (ammo_x, ammo_y)

    def collision(self):
        """Calculates the distance between the projectile and the target
        If distance is small enough, triggers a hit on the target and despawns
        the projectile"""
        ammo_x = self.ammo_rect.center[0]
        ammo_y = self.ammo_rect.center[1]
        movement_vector = (self.target.hostile_rect.center[0] - ammo_x,
                           self.target.hostile_rect.center[1] - ammo_y)
        distance_to_target = math.sqrt(movement_vector[0]**2 + movement_vector[1]**2)
        if distance_to_target < 5:
            Projectile.fired.remove(self)
            self.target.damage(20)
