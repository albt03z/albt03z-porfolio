from django.contrib.auth.models import User
from .models import Countries, Region, City, CountryInfo
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class CountryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryInfo
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)
    class Meta:
        model = Region
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    info = CountryInfoSerializer(read_only=True)
    regions = RegionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Countries
        fields = '__all__'