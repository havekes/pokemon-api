from django.db import models


class PokemonManager(models.Manager):
    use_in_migrations = True

    def create_pokemon_from_csv_row(self, row: dict):
        """ Create a pokemon object from a row of the csv file"""
        pokemon = self.create(
            name=row.get('Name'),
            type_1=row.get('Type 1'),
            type_2=row.get('Type 2'),
            total=row.get('Total'),
            hp=row.get('HP'),
            attack=row.get('Attack'),
            defence=row.get('Defense'),
            special_attack=row.get('Sp. Atk'),
            special_defence=row.get('Sp. Def'),
            speed=row.get('Speed'),
            generation=row.get('Generation'),
            legendary=row.get('Legendary')
        )
        return pokemon


class Pokemon(models.Model):
    name = models.TextField()
    type_1 = models.TextField()
    type_2 = models.TextField()
    total = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defence = models.IntegerField()
    special_attack = models.IntegerField()
    special_defence = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    legendary = models.BooleanField()

    objects = PokemonManager()
