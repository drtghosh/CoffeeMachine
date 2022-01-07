# start a RockBand here
class RockBand:
    genre = "rock"
    key_instruments = ["electric guitar", "drums"]
    n_members = 4

    def __str__(self):
        return f'{self.genre}\n{self.n_members}\n{self.key_instruments}'


rock_me = RockBand()
print(rock_me)