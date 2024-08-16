from petsapi import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from petsapi.views import CartViewSet

router = DefaultRouter()
router.register(r'pets', views.PetViewSet, basename='pet')
router.register(r'carts', CartViewSet)


urlpatterns = [
    path('', include(router.urls))
]