from django.contrib import admin
from .models import Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    @admin.display(description='Stanowisko')
    def stanowisko_display(self, obj):
        return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'

    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_display', 'data_dodania']
    list_filter = ['stanowisko', 'data_dodania']
    readonly_fields = ["data_dodania"]
    @admin.display(description='Stanowisko (id)')
    def Stanowisko_ID(self, object):
        return f"{object.stanowisko.nazwa} {object.stanowisko.id}"

class StanowiskoAdmin(admin.ModelAdmin):
    list_filter =['nazwa']

admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)