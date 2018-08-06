from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from apps.student.form import registerpayments
from apps.student.models import Payments


class InicioTemplateView(TemplateView):
    template_name = 'student/index.html'


class RegisterpaymentsCreateView(CreateView):
    template_name = 'student/registerpayments.html'
    model = Payments
    form_class = registerpayments
    success_url = reverse_lazy('student:inicio')