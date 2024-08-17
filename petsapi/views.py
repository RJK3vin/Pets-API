from django.shortcuts import render
from pets.serializers import PetSerializer
from rest_framework import viewsets
from petsapi.models import Pet
from petsapi.filters import PetFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from petsapi.models import Cart
from pets.serializers import CartSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PetFilter
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart = self.request.user.cart
        serializer.save(cart=cart)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_pet(self, request, pk=None):
        cart = self.get_object()
        pet_id = request.data.get('pet_id')
        try:
            pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response({"detail": "Pet not found."}, status=status.HTTP_404_NOT_FOUND)
        
        pet.cart = cart
        pet.save()
        return Response({"detail": "Pet added to cart."}, status=status.HTTP_200_OK)

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


