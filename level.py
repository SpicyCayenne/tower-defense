"""Contains all level information"""
class Level:
    """Class used to build each level"""
    tower_coords = []
    spawn_coords = []
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
        """Loads the tower and enemy coordinates"""
        for loc in self.tower_locations:
            self.tower_coords.append(loc)
            #draw.a.square.on.screen.at.each.point() #there's a way to do this

        for loc in self.enemy_spawns:
            self.spawn_coords.append(loc)

        for loc in self.end_points:
            self.end_point_coords.append(loc)

        return self.bg_image, self.tower_coords, self. spawn_coords, self.end_point_coords

LEVEL_0 = Level([(38, 463), (179, 465), (292, 407), (370, 306), (517, 173), (752, 213),
                 (593, 250), (257, 536), (30, 593)], 'assets/levels/level_0_bg.png',
                [(3, 564)], (797, 248), 10, 10)
#level_1 = Level([list of coords], path_to_image, [list of coords], [list of coords])
#level_2 = Level([list of coords], path_to_image, [list of coords], [list of coords])
#level_3 = Level([list of coords], path_to_image, [list of coords], [list of coords])
#...etc
