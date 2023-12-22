from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.nazwa
    class Meta:
        verbose_name_plural = "Stanowiska"


def __str__(self):
        return self.nazwa

class Osoba(models.Model):
    class plec(models.IntegerChoices):
        KOBIETA = 1
        MEZCZYZNA = 2
        INNE = 3

    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    plec = models.IntegerField(choices=plec.choices, default=plec.INNE)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(auto_now_add=True)
    wlasciciel = models.ForeignKey(User, related_name='Osoba', on_delete=models.CASCADE)

    def __str__(self):
        return self.imie + " " + self.nazwisko

    class Meta:
        ordering = ["nazwisko"]
        verbose_name_plural = "osoby"

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text