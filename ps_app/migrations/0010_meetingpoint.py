# Generated by Django 5.1.3 on 2024-11-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps_app', '0009_rename_addrest_users_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSede', models.CharField(default='', max_length=50)),
                ('departamentoSedeDesc', models.CharField(max_length=100)),
                ('municipioSedeDesc', models.CharField(max_length=100)),
                ('emailSede', models.EmailField(max_length=50)),
                ('telefonoSede', models.CharField(max_length=10)),
                ('direccionSede', models.TextField(max_length=50)),
            ],
        ),
    ]
