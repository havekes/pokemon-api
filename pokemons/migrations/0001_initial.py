# Generated by Django 3.2.3 on 2021-05-23 18:51
import csv
from django.db import migrations, models
from django.conf import settings
from pokemons.models import PokemonManager


def import_pokemon_csv(apps, schema_editor):
    Pokemon = apps.get_model('pokemons', 'Pokemon')
    with open(settings.POKEMON_CSV) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            Pokemon.objects.create_pokemon_from_csv_row(row)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('type_1', models.TextField()),
                ('type_2', models.TextField()),
                ('total', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defence', models.IntegerField()),
                ('special_attack', models.IntegerField()),
                ('special_defence', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('generation', models.IntegerField()),
                ('legendary', models.BooleanField()),
            ],
            managers=[
                ('objects', PokemonManager()),
            ],
        ),
        migrations.RunPython(import_pokemon_csv)
    ]
