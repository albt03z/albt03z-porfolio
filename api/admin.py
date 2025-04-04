from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Continents, Countries, CountriesInfo, States, Cities, CitiesInfo

# Register your models here.
admin.site.register(Continents)
admin.site.register(Countries)
admin.site.register(CountriesInfo)
admin.site.register(States)
admin.site.register(Cities)
admin.site.register(CitiesInfo)