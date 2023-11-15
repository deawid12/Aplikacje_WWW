# twoja_aplikacja/serializers.py

from rest_framework import serializers
from .models import TwojModel

class TwojModelSerializer(serializers.Serializer):
    # Definiujesz pola, które chcesz uwzględnić w serializatorze
    id = serializers.IntegerField(read_only=True)
    pole1 = serializers.CharField(max_length=100)
    pole2 = serializers.IntegerField()

    def create(self, validated_data):
        # Metoda wywoływana podczas tworzenia nowego obiektu
        return TwojModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Metoda wywoływana podczas aktualizacji obiektu
        instance.pole1 = validated_data.get('pole1', instance.pole1)
        instance.pole2 = validated_data.get('pole2', instance.pole2)
        instance.save()
        return instance
