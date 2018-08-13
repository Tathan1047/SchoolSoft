from statistics import mean

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView,ListView
from apps.student.form import registerpayments,registerstudent
from apps.student.models import Payments, Student

#Generador de Contadores para el Bar Dashboard
class ContextDataMixin(object):
    def get_context_data(self, **kwargs):
        kwargs.update(
            {'total_students': Student.objects.count(),
            'sum_income':Payments.objects.count()}

        )
        return super().get_context_data(**kwargs)


class InicioTemplateView(ContextDataMixin, TemplateView):
    template_name = 'student/index.html'


class RegisterpaymentsCreateView(SuccessMessageMixin, ContextDataMixin, CreateView):
    template_name = 'finance/registerpayments.html'
    model = Payments
    form_class = registerpayments
    success_url = reverse_lazy('student:registerpayments')
    success_message = 'Pago del Codigo %(code_student)s ha sido Registrado satisfactoriamente'


class RegisterstudentCreateView(SuccessMessageMixin, ContextDataMixin,CreateView):
    template_name = 'student/registerstudent.html'
    model = Student
    form_class = registerstudent
    success_url = reverse_lazy('student:registerstudent')
    success_message = 'Estudiante %(name_student)s ha sido Registrado satisfactoriamente'


class StudentListView(ContextDataMixin, ListView):
   template_name = 'student/list_students.html'
   context_object_name = 'students'
   model = Student

class ListpaymentsView(ContextDataMixin, ListView):
    template_name = 'finance/list_general_payments.html'
    context_object_name = 'payments'
    model = Payments

