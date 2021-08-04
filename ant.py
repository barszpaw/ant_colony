from random import randint, sample
from math import sqrt


class Ant:
    def __init__(self,world):
        self.position = [randint(0, 40), randint(0, 40)]
        self.world = world


    def  move(self):
        vector = [randint(-1, 1),randint(-1, 1),]
        position = [self.position[0] + vector[0], self.position[1] + vector[1]]
        self.position = position
        for point in self.world.points:
            if position[0] == point.x and position[1] == point.y:
                point.score()
                break





