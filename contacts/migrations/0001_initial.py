# Generated by Django 5.0.1 on 2024-01-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=50, verbose_name='Página')),
                ('greeting', models.TextField(verbose_name='Saludo')),
                ('message', models.TextField(verbose_name='Mensaje')),
                ('ubication', models.TextField(verbose_name='Ubicación')),
                ('phone', models.TextField(verbose_name='Teléfono')),
                ('email', models.TextField(verbose_name='Correo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'contactos',
                'ordering': ['-created'],
            },
        ),
    ]