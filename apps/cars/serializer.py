from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body', 'created_at', 'updated_at')
        # fields = '__all__'

    # There is a certain field here
    # def validate_brand(self, brand):
    #     if brand == 'Sas':
    #         raise serializers.ValidationError({'detail': 'brand == Sas'})
    #     return brand
    #
    # # here are all the fields
    # def validate(self, attrs):
    #     price = attrs['price']
    #     year = attrs['year']
    #     if price == year:
    #         raise serializers.ValidationError({'detail': 'year==price'})
    #     return attrs
