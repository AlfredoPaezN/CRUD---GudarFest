# Generated by Django 3.2.5 on 2021-07-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=120)),
                ('correo', models.EmailField(max_length=200)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
