# Generated by Django 3.1 on 2020-11-11 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioPersona', '0035_auto_20201111_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='genero',
            field=models.CharField(choices=[('Seleccionar', 'Seleccionar'), ('Hombre', 'Hombre'), ('Mujer', 'Mujer')], default='Seleccionar', max_length=11),
        ),
    ]
