from petsapi import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pets', views.PetViewSet, basename='pet')


urlpatterns = [
    path('', include(router.urls))
]