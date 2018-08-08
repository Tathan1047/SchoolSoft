from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView,ListView
from apps.student.form import registerpayments
from apps.student.models import Payments, Student

#Generador de Contadores para el Bar Dashboard
class ContextDataMixin(object):
    def get_context_data(self, **kwargs):
        kwargs.update(
            {'total_students': Student.objects.count()}

        )
        return super().get_context_data(**kwargs)


class InicioTemplateView(ContextDataMixin, TemplateView):
    template_name = 'student/index.html'


class RegisterpaymentsCreateView(ContextDataMixin, CreateView):
    template_name = 'student/registerpayments.html'
    model = Payments
    form_class = registerpayments
    success_url = reverse_lazy('student:inicio')


class StudentListView(ContextDataMixin, ListView):
   template_name = 'student/list_students.html'
   context_object_name = 'students'
   model = Student

