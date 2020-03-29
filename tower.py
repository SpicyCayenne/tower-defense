"""Contains the class used to generate towers"""
import pygame

class Tower:
    """Tower information"""
    def __init__(self, display_surface, image, x, y):
        self.display_surface = display_surface
        self.image = pygame.image.load(image).convert()
        self.x_coord = x
        self.y_coord = y

    def draw(self):
        """Draws the tower on teh screen using the specified image at coordinates x and y"""
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.display_surface.blit(self.image, (self.x_coord, self.y_coord))

    def attack(self):
        """Causes the tower to attack enemies in range"""
