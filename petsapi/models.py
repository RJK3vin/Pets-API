from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

PET_TYPES = [
    ('dog', 'dog'),('cat', 'cat'),('bird', 'bird'),('fish', 'fish'),('reptile', 'reptile'),
    ('hamster', 'hamster'), ('bunny', 'bunny')
]

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Cart"

class Pet(models.Model):
    name = models.CharField(max_length=100, blank = False, default='')
    description = models.CharField(max_length=300, blank = False, default='')
    pettype = models.CharField(choices=PET_TYPES, blank = False, default='', max_length = 100)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True, related_name='pets')

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Cart.objects.create(user=instance)

