# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, destination):
        return "The {} has sailed for {}!".format(self.name, destination)


pearl_capacity = 800
black_pearl = Ship("Black Pearl", pearl_capacity)
destination_input = input()
print(black_pearl.sail(destination_input))