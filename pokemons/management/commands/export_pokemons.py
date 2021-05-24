import csv
import argparse
from django.core.management.base import BaseCommand
from pokemons.models import Pokemon
from pokemons.serializers import PokemonSerializer


class Command(BaseCommand):
    help = 'Exports all pokemons to a csv file'

    def add_arguments(self, parser):
        parser.add_argument('dest_file', type=argparse.FileType('w+'))

    def handle(self, *args, **options):
        dest_file = options.get('dest_file')
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        writer = csv.DictWriter(dest_file, fieldnames=[
            field.name for field in Pokemon._meta.fields])
        writer.writerows(serializer.data)

        self.stdout.write(self.style.SUCCESS(
            f'Successfully exported {len(serializer.data)} pokemons'))
