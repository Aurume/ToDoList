# Generated by Django 4.1.6 on 2023-02-06 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Uzduotis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(blank=True, help_text='Įveskite užduoties pavadinimą: ', max_length=200, null=True, verbose_name='Pavadinimas')),
                ('sukurta', models.DateTimeField(auto_now_add=True, verbose_name='Sukūrimo data')),
                ('terminas', models.DateTimeField(blank=True, null=True, verbose_name='Įvykdyti iki:')),
                ('status', models.CharField(blank=True, choices=[('p', 'Reikia padaryti'), ('d', 'Daroma'), ('a', 'Atšaukta'), ('i', 'Įvykdyta')], default='p', help_text='Būsena', max_length=1)),
                ('vartotojas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Užduotis',
                'verbose_name_plural': 'Užduotys',
                'ordering': ['sukurta'],
            },
        ),
    ]
