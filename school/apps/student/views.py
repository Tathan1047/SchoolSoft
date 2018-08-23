from statistics import mean

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView, FormView
from apps.student.form import registerpayments,registerstudentForm,registersocioeconomicForm,registerhealthForm, registerattendantForm
from apps.student.models import Payments, Student, Socioeconomic, Health, Attendant

#Generador de Contadores para el Bar Dashboard
class ContextDataMixin(object):
    def get_context_data(self, **kwargs):
        kwargs.update(
            {'total_students': Student.objects.count(),
            'sum_income':Payments.objects.all().aggregate(total = Sum('valuepayments'))['total']}
        )
        return super().get_context_data(**kwargs)


class InicioTemplateView(ContextDataMixin, TemplateView):
    template_name = 'student/index.html'


#Inserciones Multiples en los Modelos Relacionados con Estudiantes ----------------------------------------------------
class RegisterstudentCreateView(SuccessMessageMixin, ContextDataMixin,CreateView):
    model = Student
    template_name = 'student/registerstudent.html'
    form_class = registerstudentForm
    second_form_class = registersocioeconomicForm
    three_form_class = registerhealthForm
    four_form_class = registerattendantForm
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
    form_class = registersocioeconomicForm

#Inicio Actualizaciones Multiples a Modelos Estudiantes ----------------------------------------------------------------------
class UpdatestudentUpdateView(ContextDataMixin, UpdateView):
    model = Student
    second_model = Socioeconomic
    three_model = Health
    four_model = Attendant
    template_name = 'student/registerstudent.html'
    form_class = registerstudentForm
    second_form_class = registersocioeconomicForm
    three_form_class = registerhealthForm
    four_form_class = registerattendantForm
    success_url = reverse_lazy('student:liststudents')

    def get_context_data(self, **kwargs):
        context = super(UpdatestudentUpdateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        student = self.model.objects.get(code_student=pk)
        socioeconomic = self.second_model.objects.get(code_student=student.code_student)
        health = self.three_model.objects.get(code_student=student.code_student)
        attendant = self.four_model.objects.get(code_student=student.code_student)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=socioeconomic)
        if 'form3' not in context:
            context['form3'] = self.three_form_class(instance=health)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(instance=attendant)
        context['code_student'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        code_student = kwargs['pk']
        student = self.model.objects.get(code_student=code_student)
        socioeconomic = self.second_model.objects.get(code_student=student.code_student)
        health = self.three_model.objects.get(code_student=student.code_student)
        attendant = self.four_model.objects.get(code_student=student.code_student)
        form = self.form_class(request.POST, instance=student)
        form2 = self.second_form_class(request.POST, instance=socioeconomic)
        form3 = self.three_form_class(request.POST, instance=health)
        form4 = self.four_form_class(request.POST, instance=attendant)
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            form.save()
            form2.save()
            form3.save()
            form4.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class DeletestudentView(DeleteView):
    model = Student
    template_name = 'student/deletestudent.html'
    success_url = reverse_lazy('student:liststudents')



#Fin Actulizaciones Multiples a Modelos Estudiantes ----------------------------------------------------------------------
class SearchstudentView(ListView):
      
    def post(self, request):
        code_student= request.POST['code_student']
        student= Student.objects.get(code_student=code_student)
        socioeconomic = Socioeconomic.objects.get(code_student=code_student)
        health = Health.objects.get(code_student=code_student)
        attendant = Attendant.objects.get(code_student=code_student)
        return render(request, 'student/infostudent.html', {'student':student,
                                                             'socioeconomic':socioeconomic,
                                                             'health': health,
                                                             'attendant':attendant})
        
class RegisterpaymentsCreateView(SuccessMessageMixin, ContextDataMixin, CreateView):
    template_name = 'finance/registerpayments.html'
    model = Payments
    form_class = registerpayments
    success_url = reverse_lazy('student:registerpayments')
    success_message = 'Pago del Codigo %(code_student)s ha sido Registrado satisfactoriamente'

    def get(self, request, *args, **kwargs):
        # Esto intenta obtener el valor de usuario, sino devuelve None
        code_student = request.GET.get('code_student')
        if code_student:
            # Intentamos recuperar ese usario desde la DB
            infostudent = Student.objects.get(code_student=code_student)
            # Ese get puede fallar, deberías capturar la excepción
            # Inicializamos el form con ese usuario ya cargado
            kwargs.update({'students': infostudent})
            form = self.form_class(initial=vars(infostudent))
        else:
            # Si no especificaron usuario en el request
            # mostramos el form vacio
            form = self.form_class()
        kwargs.update({'form': form})
        self.object = None
        return self.render_to_response(self.get_context_data(**kwargs))




class ListpaymentsView(ContextDataMixin, ListView):
    template_name = 'finance/list_general_payments.html'
    context_object_name = 'payments'
    model = Payments


class SearchpaymentsView(ListView):

    def post(self, request):
        code_student = request.POST['code_student']
        student = Student.objects.get(code_student=code_student)
        return render(request, 'finance/registerpayments.html', {'student': student})

    




