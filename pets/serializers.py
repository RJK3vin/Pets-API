from django.contrib.auth.models import User
from rest_framework import serializers
from petsapi.models import Pet
from petsapi.models import Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'cart']

class PetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta: 
        model = Pet
        fields = [
            'url', 'id', 'name', 'pettype', 'description'
        ]

class CartSerializer(serializers.ModelSerializer):
    pets = PetSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'pets']

