from django.shortcuts import render
from pets.serializers import PetSerializer
from rest_framework import viewsets
from petsapi.models import Pet
from petsapi.filters import PetFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PetFilter
    permission_classes = [permissions.IsAuthenticated]


