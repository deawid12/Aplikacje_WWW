# twoja_aplikacja/serializers.py

from rest_framework import serializers
from .models import MyModel
from .models import Osoba, Stanowisko

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = '__all__'
class MyModelSerializer(serializers.Serializer):
    # Pole do odczytu, np. dla identyfikatora
    id = serializers.IntegerField(read_only=True)

    # Pole wymagane dla np. dla nazwy
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        return MyModel.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance

class PersonSerializer(serializers.Serializer):
    # Definicja pola, które chce uwzględnić w serializatorze
    id = serializers.IntegerField(read_only=True)
    pole1 = serializers.CharField(max_length=100)
    pole2 = serializers.IntegerField()

    def create(self, validated_data):
        # Metoda wywoływana podczas tworzenia nowego obiektu
        return MyModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Metoda wywoływana podczas aktualizacji obiektu
        instance.pole1 = validated_data.get('pole1', instance.pole1)
        instance.pole2 = validated_data.get('pole2', instance.pole2)
        instance.save()
        return instance
