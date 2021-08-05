
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = 0

    def visit(self):
        self.visited += 1
