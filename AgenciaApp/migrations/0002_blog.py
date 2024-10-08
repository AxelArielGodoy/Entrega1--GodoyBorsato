# Generated by Django 4.0.6 on 2024-09-05 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgenciaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('subtitulo', models.CharField(max_length=30)),
                ('contenido', models.TextField(max_length=100)),
                ('fecha_creacion', models.DateField(null=True)),
                ('imagen', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
