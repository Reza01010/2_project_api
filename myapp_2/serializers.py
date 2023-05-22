from rest_framework import serializers

from myapp_1.models import Cryptocurrency1, Cryptocurrency2, Cryptocurrency23  # import model


class Cryptocurrency2Serializer(serializers.ModelSerializer):
    class Meta:
        model =Cryptocurrency2
        fields = '__all__'


class Cryptocurrency1Serializer(serializers.ModelSerializer):
    class Meta:
        model =Cryptocurrency1
        fields = '__all__'


class Cryptocurrency23Serializer(serializers.ModelSerializer):
    class Meta:
        model =Cryptocurrency23
        fields = '__all__'

