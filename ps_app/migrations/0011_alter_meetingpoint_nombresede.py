# Generated by Django 5.1.3 on 2024-11-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps_app', '0010_meetingpoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingpoint',
            name='nombreSede',
            field=models.CharField(max_length=50),
        ),
    ]
