from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, CountriesSerializer, StatesSerializer, CitiesSerializer, CountriesInfoSerializer
from .models import Countries, States, Cities, CountriesInfo, Continents, CitiesInfo

# Create your views here.
class ProtectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "¡Tienes acceso porque estás autenticado con un token válido!"})
    
class UserViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo User.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CountriesViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo Country.
    """
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = [permissions.IsAuthenticated]

class CountriesInfoViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo CountryInfo.
    """
    queryset = CountriesInfo.objects.all()
    serializer_class = CountriesInfoSerializer
    permission_classes = [permissions.IsAuthenticated]   

class StatesViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo Region.
    """
    queryset = States.objects.all()
    serializer_class = StatesSerializer
    permission_classes = [permissions.IsAuthenticated]

class CitiesViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo City.
    """
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = [permissions.IsAuthenticated]