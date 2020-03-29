"""Contains the class information to generate enemies"""
import itertools
import math
import os
import pygame

class Hostile:
    """Hostile information"""
    enemies = []
    path = [(3, 564), (7, 557), (12, 547), (19, 538), (26, 531), (32, 521), (39, 515),
            (46, 510), (54, 507), (63, 504), (73, 502), (83, 501), (92, 499), (102, 499),
            (115, 500), (126, 500), (134, 502), (146, 503), (154, 505), (170, 505),
            (182, 507), (194, 507), (210, 507), (226, 502), (237, 498), (252, 494),
            (270, 488), (283, 479), (296, 469), (312, 456), (325, 441), (341, 428),
            (354, 409), (367, 389), (382, 370), (393, 353), (401, 342), (410, 326),
            (421, 308), (432, 291), (445, 276), (456, 261), (474, 248), (489, 238),
            (514, 228), (535, 221), (559, 214), (584, 211), (613, 210), (627, 213),
            (651, 220), (673, 229), (690, 236), (706, 243), (725, 250), (744, 260),
            (766, 259), (788, 252), (797, 248)]

    def __init__(self, img, x, y, display_surface):
        self.img_file = img
        self.img = pygame.image.load(os.path.join('assets', 'enemies', self.img_file))
        self.hostile_rect = self.img.get_rect()
        self.hostile_rect.center = (x, y)
        self.x_spawn, self.x_coord = x, x
        self.y_spawn, self.y_coord = y, y
        self.display_surface = display_surface
        self.waypoints = itertools.cycle(Hostile.path)
        self.target = next(self.waypoints)
        self.speed = 0.5

    def spawn(self):
        """Spawns new enemy"""
        Hostile.enemies.append(Hostile(self.img_file,
                                       self.x_spawn, self.y_spawn, self.display_surface))

    def move(self):
        """Moves the enemy down the path"""
        distance_to_target = math.sqrt((self.x_coord - self.target[0])**2 +
                                       (self.y_coord - self.target[1])**2)
        if distance_to_target <= 0.5 and next(self.waypoints) != Hostile.path[0]:
            self.target = next(self.waypoints)
        new_x, new_y = self.x_coord, self.y_coord
        if self.x_coord < self.target[0]:
            new_x = self.x_coord + self.speed
        elif self.x_coord > self.target[0]:
            new_x = self.x_coord - self.speed
        if self.y_coord < self.target[1]:
            new_y = self.y_coord + self.speed
        elif self.y_coord > self.target[1]:
            new_y = self.y_coord - self.speed
        self.x_coord, self.y_coord = new_x, new_y
        self.hostile_rect.center = self.x_coord, self.y_coord
        if (self.x_coord, self.y_coord) == Hostile.path[-1]:
            Hostile.enemies.remove(self)

    def draw(self):
        """Draws image on the screen"""
        self.display_surface.blit(self.img, (self.hostile_rect))
