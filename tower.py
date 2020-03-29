"""Contains the class used to generate towers"""
import os
import pygame
from scaling import get_scaling_info

get_scaling_info()

class Tower:
    """Tower information"""
    selection_dict = {49:"elf_tower.png", 50:"dwarf_tower.png"}
    towers = []
    def __init__(self, img, x, y, display_surface):
        self.img_file = img
        self.img = pygame.image.load(os.path.join('assets', self.img_file))
        self.x_coord = x
        self.y_coord = y
        self.display_surface = display_surface

    def create_tower(self):
        """Creates a tower of the selected type and scales to the correct size"""
        get_scaling_info()
        x_scale, y_scale = get_scaling_info()[1:]
        Tower.towers.append(Tower(self.img_file, self.x_coord * x_scale,
                                  self.y_coord * y_scale, self.display_surface))
        print(x_scale, y_scale)

    def draw(self):
        """Draws the tower on the screen using the specified image at coordinates x and y"""
        pygame.transform.scale(self.img, (32, 32))
        self.display_surface.blit(self.img, (self.x_coord, self.y_coord))

 #   def attack(self):
 #       """Causes the tower to attack enemies in range
 #       Not yet written"""
