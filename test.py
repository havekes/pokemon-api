import csv
from pokemons.models import Pokemon

def test():
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    with open('pokemon.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            p = Pokemon(
                id=row.get('#')
            )


test()
