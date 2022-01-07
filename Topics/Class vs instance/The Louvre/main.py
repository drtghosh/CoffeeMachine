class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.creation_year = year

    def __str__(self):
        return f'"{self.title}" by {self.artist} ({self.creation_year}) hangs in the {Painting.museum}.'


title_input = input()
artist_input = input()
year_input = input()

painting = Painting(title_input, artist_input, year_input)

print(painting)