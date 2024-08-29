# Generated by Django 5.1 on 2024-08-21 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('años_experiencia', models.IntegerField()),
                ('horario_disponible', models.CharField(max_length=100)),
                ('inicio_contrato', models.DateField()),
                ('fin_contrato', models.DateField()),
                ('imagen', models.ImageField(upload_to='instructores/')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.cargo')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.local')),
            ],
        ),
    ]
