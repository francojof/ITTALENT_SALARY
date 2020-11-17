# Generated by Django 3.1 on 2020-08-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioPersona', '0012_remove_persona_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.CharField(choices=[('Menor o igual de 20', 'Menor o igual de 20'), ('21-30', '21-30'), ('31-40', '31-40'), ('41-50', '41-50'), ('mas de 50', 'mas de 50')], default='31-40', max_length=25),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
        migrations.AlterField(
            model_name='persona',
            name='estudios',
            field=models.CharField(choices=[('Ninguno', 'Ninguno'), ('Bootcamp', 'Bootcamp'), ('Técnico', 'Técnico'), ('Licenciatura', 'Licenciatura'), ('Máster', 'Master'), ('Doctorado', 'Doctorado')], default='Técnico', max_length=15),
        ),
        migrations.AlterField(
            model_name='persona',
            name='genero',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], default='Hombre', max_length=10),
        ),
        migrations.AlterField(
            model_name='persona',
            name='ingles',
            field=models.CharField(choices=[('Indiferente', 'Indiferente'), ('Basico', 'Basico'), ('Intermedio', 'Intermedio'), ('Alto', 'Alto')], default='Intermedio', max_length=15),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tamano_empresa',
            field=models.CharField(choices=[('Micro Empresa / Independiente', 'Micro Empresa / Independiente'), ('Pequeña Empresa', 'Pequeña Empresa'), ('Mediana Empresa', 'Mediana Empresa'), ('Gran Empresa', 'Gran Empresa')], default='Micro Empresa / Independiente', max_length=30),
        ),
    ]
