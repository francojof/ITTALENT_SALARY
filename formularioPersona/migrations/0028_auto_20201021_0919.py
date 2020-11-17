# Generated by Django 3.1 on 2020-10-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioPersona', '0027_auto_20201007_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='ingles_escrito',
            field=models.CharField(choices=[('Indiferente', 'Indiferente'), ('Básico', 'Básico'), ('Intermedio', 'Intermedio'), ('Alto', 'Alto')], default='Intermedio', max_length=15),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cargo',
            field=models.CharField(choices=[('Management / CTO', 'Management / CTO'), ('Management / Head of Infraestructure', 'Management / Head of Infraestructure'), ('Management / CIO', 'Management / CIO'), ('Management / IT Manager', 'Management / IT Manager'), ('Management / PMO', 'Management / PMO'), ('Management / Subgerente TI', 'Management / Subgerente TI'), ('Management / Jefe Informática', 'Management / Jefe Informática'), ('Desarrollo / Gerente Desarrollo', 'Desarrollo / Gerente Desarrollo'), ('Desarrollo / Gerente Proyectos', 'Desarrollo / Gerente Proyectos'), ('Desarrollo / Lider Técnico', 'Desarrollo / Lider Técnico'), ('Desarrollo / Arquitecto Sotware', 'Desarrollo / Arquitecto Sotware'), ('Desarrollo / Arquitecto Empresarial', 'Desarrollo / Arquitecto Empresarial'), ('Desarrollo / Desarrollador Front End', 'Desarrollo / Desarrollador Front End'), ('Desarrollo / Desarrollador Back End', 'Desarrollo / Desarrollador Back End'), ('Desarrollo / Full Stack', 'Desarrollo / Full Stack'), ('Desarrollo / Desarrollador Mobile', 'Desarrollo / Desarrollador Mobile'), ('Desarrollo / Consultor QA', 'Desarrollo / Consultor QA'), ('Desarrollo / Diseñador UX/UI', 'Desarrollo / Diseñador UX/UI'), ('Desarrollo / Jefe de Proyectos', 'Desarrollo / Jefe de Proyectos'), ('Desarrollo / Scrum Master', 'Desarrollo / Scrum Master'), ('Desarrollo / Agile Coach', 'Desarrollo / Agile Coach'), ('Desarrollo / Product Owner', 'Desarrollo / Product Owner'), ('Desarrollo / Ingeniero Devops', 'Desarrollo / Ingeniero Devops'), ('Desarrollo / Consultor RPA', 'Desarrollo / Consultor RPA'), ('Data & Analytics / Arquitecto de Datos ', 'Data & Analytics / Arquitecto de Datos '), ('Data & Analytics / Ingniero de Datos ', 'Data & Analytics / Ingniero de Datos '), ('Data & Analytics / Manager BI ', 'Data & Analytics / Manager BI '), ('Data & Analytics / Consultor BI', 'Data & Analytics / Consultor BI'), ('Data & Analytics / Chief Data Officer ', 'Data & Analytics / Chief Data Officer '), ('Data & Analytics / Digital Analitics Manager ', 'Data & Analytics / Digital Analitics Manager '), ('Data & Analytics / Data Scientist ', 'Data & Analytics / Data Scientist '), ('SAP ERP / Project Manager SAP', 'SAP ERP / Project Manager SAP'), ('SAP ERP / Consultor ABAP ', 'SAP ERP / Consultor ABAP '), ('SAP ERP / Consultor FICO ', 'SAP ERP / Consultor FICO '), ('SAP ERP / Consultor MM', 'SAP ERP / Consultor MM'), ('SAP ERP / Consultor SD ', 'SAP ERP / Consultor SD '), ('SAP ERP / Consultor PIPO', 'SAP ERP / Consultor PIPO'), ('SAP ERP / Consultor HR ', 'SAP ERP / Consultor HR '), ('SAP ERP / Consultor SAP otro ', 'SAP ERP / Consultor SAP otro '), ('Ciberseguridad / CISO ', 'Ciberseguridad / CISO '), ('Ciberseguridad / Manager Ciberseguridad  ', 'Ciberseguridad / Manager Ciberseguridad  '), ('Ciberseguridad / Ethical Hacker  ', 'Ciberseguridad / Ethical Hacker  '), ('Ciberseguridad / Pentester ', 'Ciberseguridad / Pentester '), ('Ciberseguridad / Analista en Ciberseguridad  ', 'Ciberseguridad / Analista en Ciberseguridad  '), ('Ciberseguridad / Ingeniero en Ciberseguridad ', 'Ciberseguridad / Ingeniero en Ciberseguridad '), ('Ciberseguridad / Jefe Proyectos Ciberseguridad  ', 'Ciberseguridad / Jefe Proyectos Ciberseguridad  '), ('Ciberseguridad / Arquitecto Ciberseguridad ', 'Ciberseguridad / Arquitecto Ciberseguridad '), ('Infraestructura / Técnico en Monitoreo ', 'Infraestructura / Técnico en Monitoreo '), ('Infraestructura / Soporte Técnico ', 'Infraestructura / Soporte Técnico '), ('Infraestructura / Jefe de Infraestructura  ', 'Infraestructura / Jefe de Infraestructura  '), ('Infraestructura / Ingeniero de Redes ', 'Infraestructura / Ingeniero de Redes '), ('Infraestructura / Arquitecto de Redes', 'Infraestructura / Arquitecto de Redes'), ('Infraestructura / SysOps ', 'Infraestructura / SysOps '), ('Infraestructura / Administrador de sistemas ', 'Infraestructura / Administrador de sistemas ')], default='Desarrollo / Full Stack', max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='duracionTrabajo',
            field=models.CharField(choices=[('menos de 6 meses', 'menos de 6 meses'), ('6 meses a 12 meses', '6 meses a 12 meses'), ('1 año a 2 años', '1 año a 2 años'), ('más de 2 años', 'más de 2 años')], default='6 meses a 12 meses', max_length=50),
        ),
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.CharField(choices=[('Menor o igual de 20', 'menor o igual de 20'), ('21-30', '21-30'), ('31-40', '31-40'), ('41-50', '41-50'), ('más de 50', 'más de 50')], default='31-40', max_length=25),
        ),
        migrations.AlterField(
            model_name='persona',
            name='estudios',
            field=models.CharField(choices=[('Ninguno', 'Ninguno'), ('Bootcamp', 'Bootcamp'), ('Técnico', 'Técnico'), ('Licenciatura', 'Licenciatura'), ('Máster', 'Máster'), ('Doctorado', 'Doctorado')], default='Técnico', max_length=15),
        ),
        migrations.AlterField(
            model_name='persona',
            name='experiencia',
            field=models.IntegerField(choices=[(0, 'entre uno a once meses'), (2, 'un año'), (2, 'dos años'), (3, 'tres años'), (4, 'cuatro años'), (5, 'cinco años'), (6, 'seis años'), (7, 'siete años'), (8, 'ocho años'), (9, 'nueve años'), (10, 'más de diez años')], default=1),
        ),
        migrations.AlterField(
            model_name='persona',
            name='ingles',
            field=models.CharField(choices=[('Indiferente', 'Indiferente'), ('Básico', 'Básico'), ('Intermedio', 'Intermedio'), ('Alto', 'Alto')], default='Intermedio', max_length=15),
        ),
        migrations.AlterField(
            model_name='persona',
            name='pais',
            field=models.CharField(choices=[('Chile', 'Chile'), ('Argentina', 'Argentina'), ('Perú', 'Perú'), ('Colombia', 'Colombia'), ('México', 'Mexico'), ('Brasil', 'Brasil')], default='Chile', max_length=15),
        ),
    ]
