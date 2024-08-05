from rest_framework import serializers
from petsapi.models import Pet

class PetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta: 
        model = Pet
        fields = [
            'url', 'id', 'name', 'pettype', 'description'
        ]

