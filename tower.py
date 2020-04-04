"""Contains the class used to generate towers"""
import math
import os
import pygame
from enemy import Hostile
from projectiles import Projectile

class Defender:
    """Defender information"""
    selection_dict = {49:"elf", 50:"dwarf"}
    towers = []

    def __init__(self, tower_type, x, y, display_surface):
        self.tower_type = tower_type
        self.img = pygame.image.load(os.path.join('assets', 'towers',
                                                  self.tower_type + "_tower.png")).convert()
        self.img = pygame.transform.scale(self.img, (20, 20))
        self.display_surface = display_surface
        self.attack_radius = 100
        self.tower_rect = self.img.get_rect()
        self.tower_rect.center = (x, y)

    def create_tower(self):
        """Creates a tower of the selected type and scales to the correct size"""
        Defender.towers.append(Defender(self.tower_type, self.tower_rect.center[0],
                                        self.tower_rect.center[1], self.display_surface))

    def draw(self):
        """Draws the tower on the screen using the specified image at coordinates x and y"""
        self.display_surface.blit(self.img, (self.tower_rect.center))

    def attack(self):
        """Causes the tower to attack enemies in range"""
        for target in Hostile.enemies:
            distance = math.sqrt((self.tower_rect.center[0] - target.hostile_rect.center[0])**2 +
                                 (self.tower_rect.center[1] - target.hostile_rect.center[1])**2)
            if distance <= self.attack_radius:
                Projectile.fired.append(Projectile('ammo.png', self.tower_rect.center[0],
                                                   self.tower_rect.center[1], self.display_surface,
                                                   target))
                break
