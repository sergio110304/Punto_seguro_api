# Generated by Django 5.1.3 on 2024-11-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps_app', '0015_modelosprediccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelosPrediccionPrecipitacion',
            fields=[
                ('idmodelo', models.AutoField(primary_key=True, serialize=False)),
                ('modeloblob', models.BinaryField()),
                ('descripcion', models.TextField(max_length=100)),
                ('municipio', models.CharField(max_length=50)),
            ],
        ),
    ]
