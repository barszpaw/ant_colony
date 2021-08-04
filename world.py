from random import randint, sample
from math import sqrt
from point import point


class World:
    points = None

    def __init__(self):
        self.points = [point(randint(0, 40), randint(0, 40)) for k in range(50)]

