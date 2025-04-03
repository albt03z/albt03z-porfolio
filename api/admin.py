from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Countries, CountryInfo, Region, City

# Register your models here.
admin.site.register(Countries)
admin.site.register(CountryInfo)
admin.site.register(Region)
admin.site.register(City)