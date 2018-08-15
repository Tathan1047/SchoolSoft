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

#Modelo Conceptos de Pago0
class Paymentsconcepts (models.Model):
    paymentsconcepts=models.CharField(max_length=50)

    def __str__(self):
        return self.paymentsconcepts
#Model EPS
class Eps (models.Model):
    name_eps=models.CharField(max_length=50)

    def __str__(self):
        return self.name_eps

def random_id(lenght=6):
    return ''.join(random.choice(string.digits) for x in range(lenght))

#Modelo Estudiantes
class Student (models.Model):
    code_student= models.AutoField(max_length=10, primary_key= True, unique= True, default= random_id)
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
    register_date=models.DateField(auto_now_add=True, editable=False)


    def __str__(self):
        return str(self.code_student)



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

#model Socioeconomic Student
class Socioeconomic (models.Model):
    code_student=models.ForeignKey(Student, blank=True, on_delete=models.CASCADE)
    filesisben=models.CharField(max_length=10, blank=True)
    scoresisben=models.FloatField(null=True, blank= True)
    stratum=models.CharField(choices=(("0", "0"),
                                         ("1", "Estrato 1"),
                                         ("2", "2"),
                                         ("3", "3"),
                                         ("4", "4"),
                                         ("5", "5"),
                                         ("6", "6"),
                                         ("7", "7"),),max_length=2)
#Model Health Student
class Health (models.Model):
    code_student=models.ForeignKey(Student, blank=True, on_delete=models.CASCADE)
    eps_affiliate=models.ForeignKey(Eps, blank=True, on_delete=models.CASCADE)
    ips_assigned=models.CharField(max_length=50, blank=True)
    blood_type=models.CharField(choices=(("O+", "O+"),
                                         ("O-", "O-"),
                                         ("A+", "A+"),
                                         ("A-", "A-"),
                                         ("B+", "B+"),
                                         ("B-", "B-"),
                                         ("AB-", "AB-"),
                                         ("AB+", "AB+"),),max_length=5)

#Model Attendant Student
class Attendant (models.Model):
    code_student=models.ForeignKey(Student, blank=False, on_delete=models.CASCADE)
    indetify_attendant=models.CharField(max_length=20, blank=False)
    name_attendat=models.CharField(max_length=30, blank=False)
    lastname_attendat=models.CharField(max_length=30, blank=False)
    email=models.CharField(max_length=50, blank=False)
    address_attendant=models.CharField(max_length=60)
    relationship = models.CharField(choices=(("Madre", "Madre"),
                                           ("Padre", "Padre"),
                                           ("Abuelo(a)", "Abuelo(a)"),
                                           ("Tio(a)", "Tio(a)"),
                                           ("Hermano(a)", "Hermano(a)")), max_length=20)
    number_telephone=models.CharField(max_length=40, blank=True)
    number_cellphone=models.CharField(max_length=15, blank= False)


