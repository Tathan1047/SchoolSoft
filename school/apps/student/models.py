from django.db import models

# Create Models Students
class Documenttype(models.Model):
    documet_type=models.CharField(max_length=30)

    def __str__(self):
        return self.documet_type

class City (models.Model):
    city=models.CharField(max_length=40)

    def __str__(self):
        return self.city


class Student (models.Model):
    code_student= models.CharField(max_length=10, primary_key= True)
    name_student=models.CharField(max_length=50)
    lastname_student=models.CharField(max_length=50)
    document_type = models.ForeignKey(Documenttype, on_delete=models.CASCADE)
    number_document=models.CharField(max_length=30)
    gender=models.CharField(choices=(("Masculino","Masculino"),("Femenino","Femenino")),max_length=30)
    birthday=models.DateField
    city= models.ForeignKey(City, on_delete=models.CASCADE)
    address=models.CharField(max_length=60)
    neighborhood=models.CharField(max_length=50)
    number_telephone=models.CharField(max_length=40)
    cellphone_number=models.CharField(max_length=40)
    register_date=models.DateField()