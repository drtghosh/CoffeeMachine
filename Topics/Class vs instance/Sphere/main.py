class Sphere:
    PI = 3.1415

    # finish class Sphere here
    def __init__(self, r):
        self.radius = r
        self.volume = 4 * self.PI * self.radius ** 3 / 3