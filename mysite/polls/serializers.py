from rest_framework import serializers
from .models import TwojModel
from datetime import datetime

class TwojModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(max_length=100)
    pole1 = serializers.CharField(max_length=100)
    pole2 = serializers.IntegerField()
    data_dodania = serializers.DateField()

    def validate_nazwa(self, value):
        # Walidacja dla pola nazwa - może zawierać tylko litery
        if not value.isalpha():
            raise serializers.ValidationError("Nazwa może zawierać tylko litery.")
        return value

    def validate_data_dodania(self, value):
        # Walidacja dla pola data_dodania
        if value > datetime.now().date():
            raise serializers.ValidationError("Data dodania nie może być z przyszłości.")
        return value

    def create(self, validated_data):
        validated_data['data_dodania'] = validated_data.get('data_dodania', datetime.now().date())
        return TwojModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.pole1 = validated_data.get('pole1', instance.pole1)
        instance.pole2 = validated_data.get('pole2', instance.pole2)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.save()
        return instance
