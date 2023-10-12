from django.contrib import admin
from .models import Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ('data_dodania',)

admin.site.register(Osoba)
admin.site.register(Stanowisko)



