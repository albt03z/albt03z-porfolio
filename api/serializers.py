from django.contrib.auth.models import User
from .models import Countries, States, Cities, CountriesInfo, Continents, CitiesInfo
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class CountriesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountriesInfo
        fields = '__all__'

class CitiesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitiesInfo
        fields = '__all__'

class CitiesSerializer(serializers.ModelSerializer):
    info = CitiesInfoSerializer(read_only=True)

    class Meta:
        model = Cities
        fields = '__all__'

class StatesSerializer(serializers.ModelSerializer):
    cities = CitiesSerializer(many=True, read_only=True)

    class Meta:
        model = States
        fields = '__all__'

class CountriesSerializer(serializers.ModelSerializer):
    info = CountriesInfoSerializer(read_only=True)
    regions = StatesSerializer(many=True, read_only=True)
    
    class Meta:
        model = Countries
        fields = '__all__'

class ContinentsSerializer(serializers.ModelSerializer):
    countries = CountriesSerializer(many=True, read_only=True)

    class Meta:
        model = Continents
        fields = '__all__'