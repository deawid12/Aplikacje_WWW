from django.db import models

class MyModel(models.Model):
    # Pole dla nazwy, maksymalna długość 100 znaków
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Osoba(models.Model):
    PLEC_CHOICES = [
        ('kobieta', 'Kobieta'),
        ('mezczyzna', 'Mężczyzna'),
        ('inne', 'Inne'),
    ]

    imie = models.CharField(max_length=255, verbose_name='Imię', blank=False, null=False)
    nazwisko = models.CharField(max_length=255, verbose_name='Nazwisko', blank=False, null=False)
    plec = models.CharField(max_length=10, choices=PLEC_CHOICES, verbose_name='Płeć')
    stanowisko = models.ForeignKey('Stanowisko', on_delete=models.CASCADE, verbose_name='Stanowisko')
    data_dodania = models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=255, verbose_name='Nazwa', blank=False, null=False)
    opis = models.TextField(blank=True, null=True, verbose_name='Opis')

    def __str__(self):
        return self.nazwa