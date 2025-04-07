from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, CountriesSerializer, StatesSerializer, CountriesInfoSerializer, ContinentsSerializer, TypesDocumentSerializer
from .models import Countries, States, Countries_Info, Continents, Types_Document

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
    queryset = Countries.objects.prefetch_related(
        'states',
        'additional_info' 
    ).all()
    serializer_class = CountriesSerializer
    permission_classes = [permissions.IsAuthenticated]

class CountriesInfoViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo CountryInfo.
    """
    queryset = Countries_Info.objects.all()
    serializer_class = CountriesInfoSerializer
    permission_classes = [permissions.IsAuthenticated]   

class StatesViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo Region.
    """
    queryset = States.objects.select_related('country').all()
    serializer_class = StatesSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContinentsViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo Continents.
    """
    queryset = Continents.objects.prefetch_related('countries__states').all()
    serializer_class = ContinentsSerializer
    permission_classes = [permissions.IsAuthenticated]


class TypesDocumentViewSet(viewsets.ModelViewSet):
    """
    Este viewset provee métodos GET, POST, PUT, DELETE para el modelo TypesDocument.
    """
    queryset = Types_Document.objects.all()
    serializer_class = TypesDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]