# Testowanie Serializatorów Django Rest Framework

## Inicjalizacja środowiska

from polls.models import Osoba
from polls.serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Stworzenie nowej instancji klasy Person
person = Osoba(name='Adam', miesiac_dodania=1)
person.save()

# Inicjalizacja serializera i wyświetlenie danych
serializer = PersonSerializer(person)
serializer.data

# Serializacja danych do formatu JSON
content = JSONRenderer().render(serializer.data)
content

# Deserializacja danych
import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)

# Inicjalizacja dedykowanego serializera
deserializer = PersonSerializer(data=data)

# Sprawdzenie walidacji
deserializer.is_valid()
deserializer.errors

# Poprawienie walidacji
deserializer.allow_null = True
deserializer.is_valid()
deserializer.validated_data

# Utrwalenie danych
deserializer.save()
deserializer.data
