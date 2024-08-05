from rest_framework import serializers
from petsapi.models import Pet

class PetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta: 
        model = Pet
        fields = [
            'url', 'id', 'name', 'pettype', 'description', 'owner'
        ]

