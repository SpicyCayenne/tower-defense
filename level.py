"""Contains all level information"""
import pygame

class Level:
    """Class used to build each level"""
    tower_coords = []
    used_towers = []
    spawn_coords = []
    enemy_path = []
    end_point_coords = []
    def __init__(self, tower_locations, bg_image, enemy_spawns,
                 end_points, enemy_count, spawn_rate):
        self.tower_locations = tower_locations
        self.bg_image = bg_image
        self.enemy_spawns = enemy_spawns
        self.end_points = end_points
        self.enemy_count = enemy_count
        self.spawn_rate = spawn_rate

    def load(self):
        """returns coordinate information and image"""
        for loc in self.tower_locations:
            self.tower_coords.append(loc)

        for loc in self.enemy_spawns:
            self.spawn_coords.append(loc)

        for loc in self.end_points:
            self.end_point_coords.append(loc)
        return self.bg_image, self.tower_coords, self. spawn_coords, self.end_point_coords

    def draw_towers(self, surface):
        """draws tower spawn locations"""
        for loc in Level.tower_coords:
            pygame.draw.rect(surface, (255, 255, 255), (loc[0], loc[1], 20, 20))


LEVEL_0 = Level([(38, 463), (179, 465), (292, 407), (370, 306), (517, 173), (752, 213),
                 (593, 250), (257, 536), (30, 593)], 'assets/levels/level_0_bg.png',
                [(3, 564)], (797, 248), 10, 10)
LEVEL_0_ENEMY_PATH = [(3, 564), (7, 557), (12, 547), (19, 538), (26, 531), (32, 521), (39, 515),
                      (46, 510), (54, 507), (63, 504), (73, 502), (83, 501), (92, 499), (102, 499),
                      (115, 500), (126, 500), (134, 502), (146, 503), (154, 505), (170, 505),
                      (182, 507), (194, 507), (210, 507), (226, 502), (237, 498), (252, 494),
                      (270, 488), (283, 479), (296, 469), (312, 456), (325, 441), (341, 428),
                      (354, 409), (367, 389), (382, 370), (393, 353), (401, 342), (410, 326),
                      (421, 308), (432, 291), (445, 276), (456, 261), (474, 248), (489, 238),
                      (514, 228), (535, 221), (559, 214), (584, 211), (613, 210), (627, 213),
                      (651, 220), (673, 229), (690, 236), (706, 243), (725, 250), (744, 260),
                      (766, 259), (788, 252), (797, 248)]
#level_1 = Level([list of coords], path_to_image, [list of coords], [list of coords])
#level_2 = Level([list of coords], path_to_image, [list of coords], [list of coords])
#level_3 = Level([list of coords], path_to_image, [list of coords], [list of coords])
#...etc
