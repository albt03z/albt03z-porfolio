from django.contrib.auth.models import User
from .models import Countries, States, Countries_Info, Continents, Types_Document
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class CountriesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries_Info
        fields = '__all__'

class StatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = States
        fields = '__all__'

class CountriesSerializer(serializers.ModelSerializer):
    states = StatesSerializer(many=True, read_only=True)
    info = CountriesInfoSerializer(read_only=True)
    
    class Meta:
        model = Countries
        fields = '__all__'

class ContinentsSerializer(serializers.ModelSerializer):
    countries = CountriesSerializer(many=True, read_only=True)

    class Meta:
        model = Continents
        fields = '__all__'

class TypesDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types_Document
        fields = '__all__'