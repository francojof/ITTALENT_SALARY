# Generated by Django 3.1 on 2020-08-13 19:53

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formularioPersona', '0008_persona_duraciontrabajo'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='BeneficiosEmpleador',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Alimentación', 'Alimentación'), ('Movilización', 'Movilización'), ('Plan de Salud', 'Plan de Salud'), ('Previsión / AFP', 'Previsión / AFP'), ('Celular / Computador', 'Celular / Computador'), ('Auto', 'Auto'), ('% Trading Profit Anual', '% Trading Profit Anual'), ('Gimnasio', 'Gimnasio'), ('Stock Options', 'Stock Options'), ('Equity', 'Equity'), ('Horario Flexible', 'Horario Flexible'), ('Trabajo Remoto', 'Trabajo Remoto'), ('Beneficios Flexibles', 'Beneficios Flexibles'), ('Capacitaciones', 'Capacitaciones')], default=0, max_length=202),
        ),
    ]
