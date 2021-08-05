from random import randint
from typing import Any

from point import point


class World:
    food_pos = Any
    ant_colony_pos = Any
    world_matrix = []
    world_width = 0
    world_height = 0


    def __init__(self):
        self.world_matrix = []
        self.world_width = 40
        self.world_height = 20
        for y in range(self.world_height + 1):
            row = []
            for x in range(self.world_width + 1):
                row.append(point(x, y))
            self.world_matrix.append(row)

        self.food_pos = point(randint(0, self.world_height), randint(0, self.world_height))
        self.ant_colony_pos = point(randint(0, self.world_height), randint(0, self.world_height))
