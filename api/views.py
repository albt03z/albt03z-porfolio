from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, CountrySerializer, RegionSerializer, CitySerializer, CountryInfoSerializer
from .models import Countries, Region, City, CountryInfo

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

class CountryViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo Country.
    """
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

class CountryInfoViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo CountryInfo.
    """
    queryset = CountryInfo.objects.all()
    serializer_class = CountryInfoSerializer
    permission_classes = [permissions.IsAuthenticated]   

class RegionViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo Region.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]

class CityViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo City.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]