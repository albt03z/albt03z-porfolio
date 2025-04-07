from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Continents, Countries, Countries_Info, States

# Register your models here.
admin.site.register(Continents)
admin.site.register(Countries)
admin.site.register(Countries_Info)
admin.site.register(States)