from django import forms
from apps.student.models import Payments, Student, Socioeconomic


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


class registerstudent(forms.ModelForm):
    class Meta:
        model = Student

        fields=['code_student', 'name_student', 'lastname_student','document_type',
                'number_document','gender', 'birthday','city','address','neighborhood',
                'number_telephone','cellphone_number']

        labels={'code_student':'Codigo Estudiante',
                'name_student':' Nombre Estudiante',
                'lastname_student':' Apellidos Estudiante',
                'document_type':' Tipo de Documento',
                'number_document':' N° Documento Identidad',
                'gender':' Sexo',
                'birthday':' Fecha de Nacimiento',
                'city':' Ciudad',
                'address':' Direccion',
                'neighborhood':' Barrio',
                'number_telephone':' Telefono Fijo',
                'cellphone_number':' Telefono Celular'

                }

        widgets={'code_student': forms.TextInput(attrs={'class':'form-control' }),
                 'name_student': forms.TextInput(attrs={'class':'form-control' }),
                 'lastname_student': forms.TextInput(attrs={'class':'form-control' }),
                 'document_type': forms.Select(attrs={'class':'form-control' }),
                 'number_document': forms.TextInput(attrs={'class':'form-control' }),
                 'gender': forms.Select(attrs={'class':'form-control' }),
                 'birthday': forms.TextInput(attrs={'class':'form-control','type':'date' }),
                 'city': forms.Select(attrs={'class':'form-control' }),
                 'address': forms.TextInput(attrs={'class':'form-control' }),
                 'neighborhood': forms.TextInput(attrs={'class':'form-control' }),
                 'number_telephone': forms.TextInput(attrs={'class':'form-control' }),
                 'cellphone_number': forms.TextInput(attrs={'class':'form-control' })

                 }

class registersocioeconomic(forms.ModelForm):
    class Meta:
        model = Socioeconomic

        fields=['code_student','filesisben','scoresisben','stratum']
        labels={'code_student':'Codigo Estudiante','filesisben':'Ficha Sisben','scoresisben':'Puntaje Sisben','stratum':'Estrato'}
        widgets={'code_student': forms.TextInput(attrs={'class':'form-control'}),
                 'filesisben': forms.TextInput(attrs={'class':'form-control'}),
                 'scoresisben': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
                 'stratum':forms.TextInput(attrs={'class':'form-control', 'type':'number'})}
