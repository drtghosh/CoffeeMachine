class Movie:
    # create class here
    def __init__(self, name, director, release_year):
        self.title = name
        self.director = director
        self.year = release_year


# objects of the class Movie
titanic = Movie('Titanic', 'James Cameron', 1997)
star_wars = Movie('Star Wars', 'George Lucas', 1977)
fight_club = Movie('Fight Club', 'David Fincher', 1999)