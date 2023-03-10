# Generated by Django 4.1.6 on 2023-02-09 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ToDoListas', '0004_alter_uzduotis_pavadinimas_alter_uzduotis_terminas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uzduotis',
            options={'ordering': ['-sukurta'], 'verbose_name': 'Užduotis', 'verbose_name_plural': 'Užduotys'},
        ),
        migrations.CreateModel(
            name='UzduotisApzvalga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sukurta', models.DateTimeField(auto_now_add=True, verbose_name='Sukūrimo data')),
                ('uzduotis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ToDoListas.uzduotis')),
                ('vartotojas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vartotojas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
