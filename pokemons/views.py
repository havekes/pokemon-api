from rest_framework import viewsets
from pokemons.models import Pokemon
from pokemons.serializers import PokemonSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
