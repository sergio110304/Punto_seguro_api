# Generated by Django 5.1.3 on 2024-11-10 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps_app', '0002_observations_sensors_stations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations',
            name='codigoestacion',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stations',
            name='departamento',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stations',
            name='municipio',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stations',
            name='nombreestacion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stations',
            name='zonahidrografica',
            field=models.CharField(max_length=100),
        ),
    ]
