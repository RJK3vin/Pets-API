from django.db import models

PET_TYPES = [
    ('dog', 'dog'),('cat', 'cat'),('bird', 'bird'),('fish', 'fish'),('reptile', 'reptile'),
    ('hamster', 'hamster'),
]

class Pet(models.Model):
    name = models.CharField(max_length=100, blank = False, default='')
    description = models.CharField(max_length=300, blank = False, default='')
    pettype = models.CharField(choices=PET_TYPES, blank = False, default='', max_length = 100)