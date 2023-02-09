from datetime import datetime

import pytz as pytz
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.templatetags.tz import utc
from django.urls import reverse
utc = pytz.UTC

# Create your models here.

class Uzduotis(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=200, null=True, blank=True, help_text='Įveskite užduoties pavadinimą')
    vartotojas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    sukurta = models.DateTimeField('Sukūrimo data:', auto_now_add=True)
    terminas = models.DateTimeField('Įvykdyti iki:', null=True, blank=True, help_text='Užduoties terminas')
    aprasymas = models.TextField('Aprašymas', null=True, blank=True, help_text='Aprašykite užduotį plačiau')

    def baigesi_laikas(self):
        if self.terminas:
            return self.terminas.replace(tzinfo=utc) < datetime.today().replace(tzinfo=utc)
        else:
            return False


    LOAN_STATUS = (
        ('p', 'Reikia padaryti'),
        ('d', 'Daroma'),
        ('a', 'Atšaukta'),
        ('i', 'Įvykdyta'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='p',
        help_text='Būsena',
    )
    class Meta:
        verbose_name = 'Užduotis'
        verbose_name_plural = 'Užduotys'
        ordering = ['-sukurta']

    def __str__(self):
        return f"{self.pavadinimas} ({self.sukurta})"  # uzduoties atvaizdavimas admin puslapyje

class UzduotisApzvalga(models.Model):
    uzduotis = models.ForeignKey(Uzduotis, on_delete=models.SET_NULL, null=True, blank=True)
    vartotojas = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='vartotojas')
    sukurta = models.DateTimeField('Sukūrimo data', auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.vartotojas} on {self.uzduotis} at {self.sukurta}"
