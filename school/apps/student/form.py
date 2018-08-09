from django import forms
from apps.student.models import Payments


class registerpayments(forms.ModelForm):
    class Meta:
        model = Payments

        fields =[
            'code_student',
            'paymentsconcepts',
            'valuepayments',
            'datepayment',
            'paymentmethod',
            'checknumber',
            'observations'
        ]

        labels = {
            'code_student': 'Codigo Estudiante',
            'paymentsconcepts': 'Concepto de Pago',
            'valuepayments':'Valor a Pagar',
            'datepayment':'Fecha de Pago',
            'paymentmethod':'Forma de Pago',
            'checknumber':'N° Cheque',
            'observations':'Observaciones'
        }

        widgets = {
            'code_student': forms.Select(attrs={'class':'form-control' }),
            'paymentsconcepts': forms.Select(attrs={'class':'form-control', 'placeholder': 'Concepto de Pago'}),
            'valuepayments':forms.TextInput(attrs={'class':'form-control','placeholder':'Valor a Pagar'}),
            'datepayment':forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha de Pago', 'type':'date'}),
            'paymentmethod': forms.Select(attrs={'class': 'form-control'}),
            'checknumber': forms.TextInput(attrs={'class': 'form-control','placeholder':'N° Cheuqe'}),
            'observations': forms.TextInput(attrs={'class': 'form-control'}),
        }