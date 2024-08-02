import django_filters
from petsapi.models import Pet, PET_TYPES

class PetFilter(django_filters.FilterSet):
    pettype = django_filters.ChoiceFilter(choices=PET_TYPES, lookup_expr='iexact')

    class Meta:
        model = Pet
        fields = ['pettype']