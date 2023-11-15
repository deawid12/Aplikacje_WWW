from django.contrib import admin
from .models import Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    @admin.display(description='Stanowisko')
    def stanowisko_display(self, obj):
        return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'

    list_display = ('imie', 'nazwisko', 'plec', 'stanowisko_display', 'data_dodania')
    search_fields = ('imie', 'nazwisko')
    list_filter = ('stanowisko', 'data_dodania')  # Dodaj filtry dla stanowiska i daty utworzenia

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('nazwa',)
    search_fields = ('nazwa',)
    ordering = ('nazwa',)  # Dodaj sortowanie alfabetyczne dla nazw stanowisk

admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)



