# Generated by Django 5.1.3 on 2024-11-10 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps_app', '0005_alter_observations_fechaobservacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='users',
            name='longitud',
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccioncasa', models.TextField(max_length=50)),
                ('latitudcasa', models.FloatField()),
                ('longitudcasa', models.FloatField()),
                ('ubicacionactual', models.CharField(max_length=100)),
                ('latitudactual', models.FloatField()),
                ('longitudactual', models.FloatField()),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ps_app.users')),
            ],
        ),
    ]
