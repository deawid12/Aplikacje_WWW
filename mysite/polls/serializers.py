from rest_framework import serializers
from .models import Osoba, Question, Choice,Team, Stanowisko
from datetime import datetime

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=60)
    country = serializers.CharField(required=True)

    def create(self, validated_data):
        validated_data['data_dodania'] = validated_data.get('data_dodania', datetime.now().date())
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.data_dodanie = validated_data.get('data_dodania', instance.miesiac_dodania)
        instance.stanowisko = validated_data.get('stanowisko', instance.team)
        instance.save()
        return instance

class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = ['id', 'nazwa']
        read_only_fields = ['id']

    def validate_imie(self, value):
        if not all(char.isalpha() or char==' ' for char in value):
            raise serializers.ValidationError("Imię powinno zaczynać się od wielkiej litery.")
        return value

    def validate_nazwisko(self, value):
        if not all(char.isalpha() or char==' ' for char in value):
            raise serializers.ValidationError("Nazwisko powinno zaczynać się od wielkiej litery.")
        return value
    def validate_data_dodania(self, value):
        if value > datetime.now().date():
            raise serializers.ValidationError("Data dodania nie może być z przyszłości.")
        return value

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        self.validate_imie(instance.imie)

        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        self.validate_nazwisko(instance.nazwisko)

        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        self.validate_data_dodania(instance.data_dodania)

        instance.save()
        return instance

class StanowiskoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['id','nazwa']
        read_only_fields = ['id']

class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question_text','pub_date']
        read_only_fields = ['id']

class ChoiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'votes']
        read_only_fields = ['id']
