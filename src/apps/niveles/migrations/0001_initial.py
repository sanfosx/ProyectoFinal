# Generated by Django 3.2.6 on 2021-08-23 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.CharField(max_length=250)),
                ('cantidad_de_preguntas', models.IntegerField(help_text='cantidad de preguntas por nivel')),
                ('puntaje_minimo_para_aprobar', models.IntegerField(help_text='puntaje minimo para aprobar el nivel')),
                ('dificultad', models.CharField(choices=[('fácil', 'facil'), ('medio', 'medio'), ('dicífil', 'difícil'), ('chaqueñaso', 'chaqueñaso')], max_length=10)),
            ],
        ),
    ]
