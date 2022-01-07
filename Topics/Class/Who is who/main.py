class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"

    def __str__(self):
        return f'{self.color}\n{self.feature}\n{self.home}'


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"

    def __str__(self):
        return f'{self.color}\n{self.feature}\n{self.home}'


angel = Angel()
demon = Demon()
print(angel)
print(demon)