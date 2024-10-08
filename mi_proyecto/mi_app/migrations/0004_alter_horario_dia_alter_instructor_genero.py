# Generated by Django 4.2.15 on 2024-08-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0003_remove_instructor_horario_disponible_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], max_length=10),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1),
        ),
    ]
