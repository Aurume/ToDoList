from django.contrib import admin
from .models import Uzduotis, UzduotisApzvalga


# Register your models here.
class UzduotisAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'vartotojas', 'sukurta', 'terminas', 'status')
    list_filter = ('status', 'terminas')

class UzduotisApzvalgaAdmin(admin.ModelAdmin):
    list_display = ('uzduotis', 'vartotojas', 'sukurta')


admin.site.register(Uzduotis, UzduotisAdmin)
admin.site.register(UzduotisApzvalga, UzduotisApzvalgaAdmin)
# admin.site.register(Genre)
# admin.site.register(BookInstance)