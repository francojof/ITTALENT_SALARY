# Generated by Django 3.1 on 2020-10-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioPersona', '0018_auto_20201005_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='experiencia',
            field=models.IntegerField(choices=[(0, 'menos de 1'), (2, 'un año'), (2, 'dos años'), (3, 'tres años'), (4, 'cuatro años'), (5, 'cinco años'), (6, 'seis años'), (7, 'siete años'), (8, 'ocho años'), (9, 'nueve años'), (10, 'mas de diez años')], default=1),
        ),
    ]
