import random
from datetime import date
from random import choice
from faker import Faker

fake = Faker()

class Film:
    def __init__(self, tytuł, rok_wydania, gatunek, liczba_odtworzeń):
        self.tytuł = tytuł
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzeń = liczba_odtworzeń

    def __str__(self):
        return f'{self.tytuł} {self.rok_wydania} {self.gatunek} {self.liczba_odtworzeń}'
    
    def __repr__(self):
        return f"Film(tytuł={self.tytuł}, rok_wydania={self.rok_wydania}, gatunek={self.gatunek}, " \
               f"liczba_odtworzeń={self.liczba_odtworzeń})"

    def play(self):
        print(f"{self.tytuł}, ({self.rok_wydania}).")
        self.liczba_odtworzeń += 1
        return self.liczba_odtworzeń

class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __str__(self):
        return f'{self.tytuł} {self.rok_wydania} {self.gatunek} S0{self.numer_sezonu}E0{self.numer_odcinka} ' \
               f'{self.liczba_odtworzeń}'
    
    def __repr__(self):
        return f"Serial(tytuł={self.tytuł}, rok_wydania={self.rok_wydania}, gatunek={self.gatunek}, " \
               f"numer_odcinka={self.numer_odcinka}, numer_sezonu={self.numer_sezonu}, " \
               f"liczba_odtworzeń={self.liczba_odtworzeń})"

    def play(self):
        print(f"{self.tytuł}, S0{self.numer_sezonu}E0{self.numer_odcinka}.")
        self.liczba_odtworzeń += 1
        return self.liczba_odtworzeń

gatunek = ["Komedia", "Dramat", "Sensacja", "Horror", "Thriller", "Obyczajowy", "Biograficzny"]
biblioteka = []
today = date.today()

def get_movies():
    return [film for film in biblioteka if isinstance(film, Film) and not isinstance(film, Serial)]

def get_series():
    return [serial for serial in biblioteka if isinstance(serial, Serial)]

def search():
    wyszukanie = input("Podaj tytuł jakiego szukasz: ")
    results = [item for item in biblioteka if wyszukanie.lower() in item.tytuł.lower()]
    if results:
        for result in results:
            print(result)
    else:
        print("Nie znaleziono takiego tytułu w bibliotece.")

def generate_views():
    element = random.choice(biblioteka)
    increment = random.randint(1, 100)
    element.liczba_odtworzeń += increment
    print(f"{element.tytuł} teraz ma odtworzeń {element.liczba_odtworzeń} po dodaniu {increment} odtworzeń.")

def generate_views10():
    for _ in range(10):
        generate_views()

def top_titles(content_type):
    if content_type == "Film":
        items = get_movies()
    elif content_type == "Serial":
        items = get_series()
    else:
        items = biblioteka
    top = sorted(items, key=lambda x: x.liczba_odtworzeń, reverse=True)
    return [(type(item).__name__, item) for item in top[:3]]

def create_biblioteka(content_type, how_many):
    for i in range(how_many):
        if content_type == "Film":
            biblioteka.append(Film(
                tytuł=fake.word().title(),
                rok_wydania=fake.year(),
                gatunek=choice(gatunek),
                liczba_odtworzeń=0
            ))
        elif content_type == "Serial":
            biblioteka.append(Serial(
                tytuł=fake.word().title(),
                rok_wydania=fake.year(),
                gatunek=choice(gatunek),
                numer_odcinka=fake.random_int(min=1, max=8),
                numer_sezonu=fake.random_int(min=1, max=3),
                liczba_odtworzeń=0
            ))

if __name__ == "__main__":
    print("Biblioteka filmów")
    create_biblioteka("Film", 3)
    create_biblioteka("Serial", 3)
    print("Obecna biblioteka:", biblioteka)
    
    # Generate random views
    print("\nGenerating views:")
    generate_views10()
    
    # Display top 3 titles
    print(f"\nNajpopularniejsze filmy i seriale dnia {today.day}.{today.month}.{today.year}:")
    for content_type, title in top_titles("all"):
        print(f"{content_type}: {title}")