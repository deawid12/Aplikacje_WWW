from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

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

    # Dodaj walidator dla pola nazwa
    validate_nazwa = RegexValidator(
        regex=r'^[a-zA-Z ]+$',
        message='Nazwa może zawierać tylko litery.',
        code='invalid_nazwa'
    )

    def clean(self):
        # Walidacja daty_dodania
        if self.data_dodania and self.data_dodania > timezone.now():
            raise ValidationError('Data dodania nie może być z przyszłości.')

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=255, verbose_name='Nazwa', blank=False, null=False)
    opis = models.TextField(blank=True, null=True, verbose_name='Opis')

    def __str__(self):
        return self.nazwa
