"""Contains the class used to generate towers"""
import os
import pygame
from scaling import get_scaling_info

get_scaling_info()

class Defender:
    """Defender information"""
    selection_dict = {49:"elf_tower.png", 50:"dwarf_tower.png"}
    towers = []
    tower_coords = []
    def __init__(self, img, x, y, display_surface):
        self.tower_scale = 25
        self.img_file = img
        self.img = pygame.image.load(os.path.join('assets', 'towers', self.img_file))
        self.img = pygame.transform.scale(self.img, (self.tower_scale, self.tower_scale))
        self.x_coord = x
        self.y_coord = y
        self.display_surface = display_surface
        self.attack_radius = 50
        self.tower_rect = self.img.get_rect()
        self.tower_rect.center = x, y


    def create_tower(self):
        """Creates a tower of the selected type and scales to the correct size"""
        Defender.towers.append(Defender(self.img_file, self.x_coord,
                                        self.y_coord, self.display_surface))
        Defender.tower_coords.append((self.x_coord, self.y_coord))
        print(Defender.tower_coords)

    def draw(self):
        """Draws the tower on the screen using the specified image at coordinates x and y"""
        self.display_surface.blit(self.img, (self.tower_rect))

    def attack(self, target):
        """Causes the tower to attack enemies in range"""
