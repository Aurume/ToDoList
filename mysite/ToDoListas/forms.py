from django import forms
from .models import Uzduotis, UzduotisApzvalga
from django.contrib.auth.models import User

class UzduotisApzvalgaForm(forms.ModelForm):
    class Meta:
        model = UzduotisApzvalga
        fields = ('uzduotis', 'vartotojas')  # ir cia istrynus, dingsta visa forma
        #widgets = {'uzsakymas': forms.HiddenInput(), 'vartotojas': forms.HiddenInput()}


class ManoDateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class UzduotisCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Uzduotis
        fields = ['pavadinimas', 'aprasymas', 'terminas', 'status']
        widgets = {'terminas': ManoDateTimeInput()}