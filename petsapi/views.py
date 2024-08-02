from django.shortcuts import render
from pets.serializers import PetSerializer
from rest_framework import viewsets
from petsapi.models import Pet

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
