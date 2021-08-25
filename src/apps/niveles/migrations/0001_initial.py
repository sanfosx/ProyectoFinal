# Generated by Django 3.2.6 on 2021-08-25 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('det_rta', models.CharField(max_length=255)),
                ('is_true', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'respuestas',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('det_preg', models.CharField(max_length=255)),
                ('rtas_preg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='niveles.respuesta')),
            ],
            options={
                'db_table': 'preguntas',
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descrip', models.CharField(max_length=255)),
                ('pregs_nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='niveles.pregunta')),
            ],
            options={
                'db_table': 'niveles',
            },
        ),
    ]