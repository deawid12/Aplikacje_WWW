# Wyświetla wszystkich obiektów modelu Osoba
Osoba.objects.all()

# Wyświetlanie obiektu modelu Osoba z id = 3
Osoba.objects.get(id=3)

# Wyświetla obiektu modelu Osoba, którego nazwa zsczyna się na wybraną literę
Osoba.objects.filter(nazwisko__istartswith='A')

# Wyświetlanie unikalnej listy stanowiska przypisanego dla modelu Osoba
Osoba.objects.values('stanowisko__nazwa').distinct()

# Wyświetla nazwy stanowisk posortowanych alfabetycznie malejąco
Stanowisko.objects.order_by('-nazwa')

# Nowa instancja obiektu klasy Osoba i zapisz w bazie
nowa_osoba = Osoba(imie='Nowe', nazwisko='Osoba', plec='inne', stanowisko=Stanowisko.objects.first())
nowa_osoba.save()
