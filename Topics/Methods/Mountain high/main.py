class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # create convert_height here
    def convert_height(self):
        conversion_factor = 0.3048
        return self.height / conversion_factor