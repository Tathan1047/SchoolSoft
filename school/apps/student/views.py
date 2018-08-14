from statistics import mean

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView,ListView,UpdateView
from apps.student.form import registerpayments,registerstudent,registersocioeconomic,registerhealth, registerattendant
from apps.student.models import Payments, Student, Socioeconomic

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

#Inserciones Multiples en los Modelos Relacionados con Estudiantes ----------------------------------------------------
class RegisterstudentCreateView(SuccessMessageMixin, ContextDataMixin,CreateView):
    model = Student
    template_name = 'student/registerstudent.html'
    form_class = registerstudent
    second_form_class = registersocioeconomic
    three_form_class = registerhealth
    four_form_class = registerattendant
    success_url = reverse_lazy('student:registerstudent')
    success_message = 'Estudiante %(name_student)s ha sido Registrado satisfactoriamente'

    def get_context_data(self, **kwargs):
        context = super(RegisterstudentCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.three_form_class(self.request.GET)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(self.request.GET)

        return context

    def post (self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.three_form_class(request.POST)
        form4 = self.four_form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            form2.instance.code_student = instance
            form3.instance.code_student = instance
            form4.instance.code_student = instance
            if form2.is_valid():
                form2.save()
                if form3.is_valid():
                    form3.save()
                    if form4.is_valid():
                        form4.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


#Fin Inserciones Multiples a Modelos Estudiantes ----------------------------------------------------------------------

class StudentListView(ContextDataMixin, ListView):
   template_name = 'student/list_students.html'
   context_object_name = 'students'
   model = Student

class SocioeconomicCreateView(CreateView):
    template_name = 'student/registerstudent.html'
    model = Socioeconomic
    form_class = registersocioeconomic

class UpdatestudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/registerstudent.html'
    form_class = registerstudent
    success_url = reverse_lazy('student:liststudents')


class RegisterpaymentsCreateView(SuccessMessageMixin, ContextDataMixin, CreateView):
    template_name = 'finance/registerpayments.html'
    model = Payments
    form_class = registerpayments
    success_url = reverse_lazy('student:registerpayments')
    success_message = 'Pago del Codigo %(code_student)s ha sido Registrado satisfactoriamente'


class ListpaymentsView(ContextDataMixin, ListView):
    template_name = 'finance/list_general_payments.html'
    context_object_name = 'payments'
    model = Payments


