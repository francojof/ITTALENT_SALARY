# Generated by Django 3.1 on 2020-08-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioPersona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='actividad',
            field=models.CharField(choices=[('Empresa Fabril / Industrial', 'Empresa Fabril / Industrial'), ('Empresa Comercial', 'Empresa Comercial'), ('Empresa de Servicios', 'Empresa de Servicios'), ('Empresa Financiera', 'Empresa Financiera'), ('Gobierno', 'Gobierno')], default='Empresa Comercial', max_length=30),
        ),
    ]
