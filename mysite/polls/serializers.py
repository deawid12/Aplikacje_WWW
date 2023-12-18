from rest_framework import serializers
from .models import Osoba, Stanowisko, MONTHS, SHIRT_SIZES
from datetime import datetime

class PersonSerializer(serializers.Serializer):
    class Meta:
        model = Osoba
        fields = '__all__'

    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(max_length=100)
    pole1 = serializers.CharField(max_length=100)
    pole2 = serializers.IntegerField()
    shirt_size = serializers.ChoiceField(choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    miesiac_dodania = serializers.ChoiceField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())
    def validate_nazwa(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Nazwa może zawierać tylko litery.")
        return value

    def validate_data_dodania(self, value):
        if value > datetime.now().date():
            raise serializers.ValidationError("Data dodania nie może być z przyszłości.")
        return value

    def create(self, validated_data):
        validated_data['data_dodania'] = validated_data.get('data_dodania', datetime.now().date())
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.team = validated_data.get('team', instance.team)
        instance.save()
        return instance

    def validate_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Imię powinno zaczynać się od wielkiej litery.")
        return value

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.data_dodanie = validated_data.get('data_dodania', instance.miesiac_dodania)
        instance.stanowisko = validated_data.get('stanowisko', instance.team)
        instance.save()
        return instance
class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = '__all__'