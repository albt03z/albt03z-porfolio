from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """ Vista de la página de inicio """
    template_name = 'index.html'