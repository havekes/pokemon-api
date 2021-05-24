# pylint: disable=missing-function-docstring

import os
import csv
from io import StringIO
from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase
from pokemons.models import Pokemon


class PokemonsTest(APITestCase):
    """CRUD pokemons API endpoint"""

    ENDPOINT = "/pokemons"
    test_pokemon = None

    def setUp(self):
        data = {
            'name': 'Test',
            'type_1': 'Type 1',
            'type_2': 'Type 2',
            'total': 1,
            'hp': 2,
            'attack': 3,
            'defence': 4,
            'special_attack': 5,
            'special_defence': 6,
            'speed': 7,
            'generation': 8,
            'legendary': True
        }
        self.test_pokemon = Pokemon(**data)
        self.test_pokemon.save()

    def test_list(self):
        response = self.client.get(f'{self.ENDPOINT}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 800)

    def test_list_limit(self):
        response = self.client.get(
            f'{self.ENDPOINT}/', {'limit': 10})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)

    def test_list_offset(self):
        response1 = self.client.get(
            f'{self.ENDPOINT}/', {'limit': 10, 'offset': 0})
        response2 = self.client.get(
            f'{self.ENDPOINT}/', {'limit': 10, 'offset': 1})

        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response1.data['results']), 10)
        self.assertEqual(len(response2.data['results']), 10)
        self.assertNotEqual(
            response1.data['results'], response2.data['results'])

    def test_get(self):
        response = self.client.get(f'{self.ENDPOINT}/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Bulbasaur')

    def test_get_when_does_not_exist(self):
        response = self.client.get(f'{self.ENDPOINT}/9999/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create(self):
        data = {
            'name': 'Test create',
            'type_1': 'Type 1',
            'type_2': 'Type 2',
            'total': 1,
            'hp': 2,
            'attack': 3,
            'defence': 4,
            'special_attack': 5,
            'special_defence': 6,
            'speed': 7,
            'generation': 8,
            'legendary': True
        }
        response = self.client.post(f'{self.ENDPOINT}/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])

    def test_create_when_bad_data(self):
        response = self.client.post(f'{self.ENDPOINT}/', {'bad_field': 0})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update(self):
        data = {
            'name': 'Test update',
            'type_1': 'Type 1',
            'type_2': 'Type 2',
            'total': 1,
            'hp': 2,
            'attack': 3,
            'defence': 4,
            'special_attack': 5,
            'special_defence': 6,
            'speed': 7,
            'generation': 8,
            'legendary': True
        }
        response = self.client.put(
            f'{self.ENDPOINT}/{self.test_pokemon.id}/', data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])

    def test_update_when_bad_data(self):
        response = self.client.put(
            f'{self.ENDPOINT}/{self.test_pokemon.id}/', {'bad_field': 0})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        response = self.client.delete(
            f'{self.ENDPOINT}/{self.test_pokemon.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_when_does_not_exist(self):
        response = self.client.delete(f'{self.ENDPOINT}/9999/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_command_export(self):
        file_name = 'test.csv'
        length = Pokemon.objects.count()
        out = StringIO()
        call_command('export_pokemons', file_name, stdout=out)

        with open(file_name) as csvfile:
            reader = csv.reader(csvfile)
            self.assertIn(str(length), out.getvalue())
            self.assertEqual(sum(1 for row in reader), length)

        os.remove(file_name)
