from rest_framework import serializers

from apps.auto_parks.models import AutoParkModel
from apps.cars.serializer import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(read_only=True, many=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'created_at', 'updated_at', 'cars')
        # read_only_fields = ('cars',)


class AutoParkWithOutCarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'created_at', 'updated_at')
