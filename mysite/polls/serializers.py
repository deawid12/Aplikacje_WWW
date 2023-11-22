from rest_framework import serializers
from .models import TwojModel
from datetime import datetime

class TwojModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    pole1 = serializers.CharField(max_length=100)
    pole2 = serializers.IntegerField()
    data_dodania = serializers.DateField()

    def create(self, validated_data):
        # Dodaj domyślną wartość dla data_dodania, jeśli nie została podana
        validated_data['data_dodania'] = validated_data.get('data_dodania', datetime.now().date())
        return TwojModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pole1 = validated_data.get('pole1', instance.pole1)
        instance.pole2 = validated_data.get('pole2', instance.pole2)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.save()
        return instance
