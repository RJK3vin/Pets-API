# Generated by Django 4.2.14 on 2024-08-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=300)),
                ('pettype', models.CharField(choices=[('dog', 'dog'), ('cat', 'cat'), ('bird', 'bird'), ('fish', 'fish'), ('reptile', 'reptile'), ('hamster', 'hamster'), ('bunny', 'bunny')], default='', max_length=100)),
            ],
        ),
    ]
