import random
from datetime import date
from random import choice
from faker import Faker

fake = Faker()

# Define the Film class
class Film:
    def __init__(self, title, release_year, genre, views_count):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views_count = views_count

    def __str__(self):
        return f'{self.title} {self.release_year} {self.genre} {self.views_count}'
    
    def __repr__(self):
        return f"Film(title={self.title}, release_year={self.release_year}, genre={self.genre}, " \
               f"views_count={self.views_count})"

    def play(self):
        print(f"{self.title}, ({self.release_year}).")
        self.views_count += 1
        return self.views_count

# Define the Serial (TV Series) class, inheriting from Film
class Serial(Film):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title} {self.release_year} {self.genre} S0{self.season_number}E0{self.episode_number} ' \
               f'{self.views_count}'
    
    def __repr__(self):
        return f"Serial(title={self.title}, release_year={self.release_year}, genre={self.genre}, " \
               f"episode_number={self.episode_number}, season_number={self.season_number}, " \
               f"views_count={self.views_count})"

    def play(self):
        print(f"{self.title}, S0{self.season_number}E0{self.episode_number}.")
        self.views_count += 1
        return self.views_count

# Define genres and create an empty library
genres = ["Comedy", "Drama", "Action", "Horror", "Thriller", "Documentary", "Biographical"]
library = []
today = date.today()

# Function to get only movies from the library
def get_movies():
    return [film for film in library if isinstance(film, Film) and not isinstance(film, Serial)]

# Function to get only series from the library
def get_series():
    return [serial for serial in library if isinstance(serial, Serial)]

# Function to search for a title in the library
def search():
    search_query = input("Enter the title you are looking for: ")
    results = [item for item in library if search_query.lower() in item.title.lower()]
    if results:
        for result in results:
            print(result)
    else:
        print("No such title found in the library.")

# Function to generate a random number of views for a random item in the library
def generate_views(count=1):
    for _ in range(count):
        element = random.choice(library)
        increment = random.randint(1, 100)
        element.views_count += increment
        print(f"{element.title} now has {element.views_count} views after adding {increment} views.")

# Function to get the top 3 titles by view count
def top_titles(content_type):
    if content_type == "Film":
        items = get_movies()
    elif content_type == "Serial":
        items = get_series()
    else:
        items = library
    top = sorted(items, key=lambda x: x.views_count, reverse=True)
    return [(type(item).__name__, item) for item in top[:3]]

# Function to create the library with a specified number of films or series
def create_library(content_type, how_many):
    for i in range(how_many):
        if content_type == "Film":
            library.append(Film(
                title=fake.word().title(),
                release_year=fake.year(),
                genre=choice(genres),
                views_count=0
            ))
        elif content_type == "Serial":
            library.append(Serial(
                title=fake.word().title(),
                release_year=fake.year(),
                genre=choice(genres),
                episode_number=fake.random_int(min=1, max=8),
                season_number=fake.random_int(min=1, max=3),
                views_count=0
            ))

if __name__ == "__main__":
    print("Movie Library")
    create_library("Film", 3)
    create_library("Serial", 3)
    print("Current library:", library)
    
    # Generate random views
    print("\nGenerating views:")
    generate_views(10)
    
    # Display top 3 titles
    print(f"\nTop movies and series on {today.day}.{today.month}.{today.year}:")
    for content_type, title in top_titles("all"):
        print(f"{content_type}: {title}")
