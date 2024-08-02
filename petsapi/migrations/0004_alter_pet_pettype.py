# Generated by Django 4.2.14 on 2024-08-02 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsapi', '0003_pet_pettype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pettype',
            field=models.CharField(choices=[('dog', 'dog'), ('cat', 'cat'), ('bird', 'bird'), ('fish', 'fish'), ('reptile', 'reptile'), ('hamster', 'hamster'), ('bunny', 'bunny')], default='', max_length=100),
        ),
    ]
