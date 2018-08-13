import random
import string

from django.db import models

#Modelo tipo de documentos
class Documenttype(models.Model):
    documet_type=models.CharField(max_length=30)

    def __str__(self):
        return self.documet_type
#Modelo Ciudades
class City (models.Model):
    city=models.CharField(max_length=40)

    def __str__(self):
        return self.city

#Modelo Conceptos de Pago
class Paymentsconcepts (models.Model):
    paymentsconcepts=models.CharField(max_length=50)

    def __str__(self):
        return self.paymentsconcepts


#Modelo Estudiantes
class Student (models.Model):
    code_student= models.AutoField(max_length=9, primary_key= True, unique= True)
    name_student=models.CharField(max_length=50)
    lastname_student=models.CharField(max_length=50)
    document_type = models.ForeignKey(Documenttype, on_delete=models.CASCADE)
    number_document=models.CharField(max_length=30)
    gender=models.CharField(choices=(("Masculino","Masculino"),("Femenino","Femenino")),max_length=30)
    birthday=models.DateField()
    city= models.ForeignKey(City, on_delete=models.CASCADE)
    address=models.CharField(max_length=60)
    neighborhood=models.CharField(max_length=50)
    number_telephone=models.CharField(max_length=40)
    cellphone_number=models.CharField(max_length=40)
    register_date=models.DateField()

    def code_studen_format(self):
        return 'A'+ str(self.code_student).zfill(4)

    def __str__(self):
        return (str(self.code_studen_format())+ '-' + self.name_student + ' ' +  self.lastname_student)

#Modelo Pagos
class Payments (models.Model):
    code_student=models.ForeignKey(Student, on_delete=models.CASCADE)
    paymentsconcepts=models.ForeignKey(Paymentsconcepts, on_delete=models.CASCADE)
    valuepayments=models.IntegerField()
    datepayment=models.DateField()
    paymentmethod = models.CharField(choices=(("Efectivo", "Efectivo"),
                                              ("Cheque", "Cheque")), max_length=30)
    checknumber=models.CharField(max_length=30, blank=True)
    observations=models.CharField(max_length=50,blank=True)



