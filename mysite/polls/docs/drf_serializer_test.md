from mysite.serializers import PersonSerializer, TeamSerializer
from mysite.models import Person, Team
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Przykładowe dane dla Person
person_data = {'name': 'John Doe', 'shirt_size': 'L', 'miesiac_dodania': 2, 'team': 1}

# Tworzenie instancji serializera dla Person
person_serializer = PersonSerializer(data=person_data)
if person_serializer.is_valid():
    person_instance = person_serializer.save()
    print(f'Utworzono obiekt Person: {person_instance}')

# Przykładowe dane dla Team
team_data = {'name': 'Engineering', 'description': 'Development Team'}

# Tworzenie instancji serializera dla Team
team_serializer = TeamSerializer(data=team_data)
if team_serializer.is_valid():
    team_instance = team_serializer.save()
    print(f'Utworzono obiekt Team: {team_instance}')

# Serializacja danych do formatu JSON
person_json = JSONRenderer().render(person_serializer.data)
team_json = JSONRenderer().render(team_serializer.data)

print('Dane Person w formacie JSON:')
print(person_json)

print('Dane Team w formacie JSON:')
print(team_json)

# Deserializacja danych z formatu JSON
person_stream = BytesIO(person_json)
team_stream = BytesIO(team_json)

person_data_deserialized = JSONParser().parse(person_stream)
team_data_deserialized = JSONParser().parse(team_stream)

# Tworzenie nowych instancji obiektów na podstawie zdeserializowanych danych
person_deserializer = PersonSerializer(data=person_data_deserialized)
if person_deserializer.is_valid():
    person_instance_deserialized = person_deserializer.save()
    print(f'Utworzono obiekt Person na podstawie zdeserializowanych danych: {person_instance_deserialized}')

team_deserializer = TeamSerializer(data=team_data_deserialized)
if team_deserializer.is_valid():
    team_instance_deserialized = team_deserializer.save()
    print(f'Utworzono obiekt Team na podstawie zdeserializowanych danych: {team_instance_deserialized}')
