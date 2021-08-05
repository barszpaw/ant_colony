from random import randint
from point import point


class Ant:
    path = []

    def __init__(self, world, name):
        ant_colony_pos = vars(world.ant_colony_pos)
        self.position = point(ant_colony_pos['x'], ant_colony_pos['y'])
        self.world = world
        self.__update_path(ant_colony_pos['x'], ant_colony_pos['y'])
        self.world.world_matrix[ant_colony_pos['y']][ant_colony_pos['x']].visit()
        self.return_to_colony = False
        self.name = name

    def move(self):
        if self.return_to_colony:
            pass
        vector = [randint(-1, 1), randint(-1, 1)]
        (x_pos, y_pos) = [self.position.x + vector[0], self.position.y + vector[1]]

        if x_pos == self.position.x and y_pos == self.position.y:
            pass
        if (x_pos < self.world.world_width and y_pos < self.world.world_height) and (x_pos >= 0 and y_pos >= 0):
            self.position = point(x_pos, y_pos)
            if self.position.x == self.world.food_pos.x and self.position.y == self.world.food_pos.y:
                self.return_to_colony = True
            self.world.world_matrix[y_pos][x_pos].visit()
            self.__update_path(x_pos, y_pos)

    def __update_path(self, x_pos=0, y_pos=0):
        for p in self.path:
            if p.x == x_pos and p.y == y_pos:
                p.visit()
                return self
        p = point(x_pos, y_pos)
        p.visit()
        self.path.append(p)
        return self
