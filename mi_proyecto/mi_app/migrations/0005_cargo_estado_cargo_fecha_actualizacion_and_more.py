# Generated by Django 4.2.15 on 2024-08-23 13:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0004_alter_horario_dia_alter_instructor_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cargo',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cargo',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='especialidad',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='especialidad',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='especialidad',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='horario',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='instructor',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='instructorespecialidad',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='instructorespecialidad',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='instructorespecialidad',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='local',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='local',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='local',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
