from django.shortcuts import render
from pets.serializers import PetSerializer
from rest_framework import viewsets
from petsapi.models import Pet
from petsapi.filters import PetFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from petsapi.models import Cart
from pets.serializers import CartSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PetFilter
    permission_classes = [permissions.IsAuthenticated]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


