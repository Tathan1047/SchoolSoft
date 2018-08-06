from django.shortcuts import render
from django.views.generic import TemplateView



class InicioTemplateView(TemplateView):
    template_name = 'student/index.html'