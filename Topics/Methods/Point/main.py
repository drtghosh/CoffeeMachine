class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        sq_dist = (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        return sq_dist ** 0.5
