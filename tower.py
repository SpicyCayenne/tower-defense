"""Contains the class used to generate towers"""
import pygame

class Tower:
    """Tower information"""
    def __init__(self, display_surface, image, x, y):
        self.display_surface = display_surface
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y

    def draw(self):
        """Draws the tower on teh screen using the specified image at coordinates x and y"""
        self.display_surface.blit(self.image, (self.x, self.y))

    def attack(self):
        pass
