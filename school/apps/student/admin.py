from django.contrib import admin

from apps.student.models import Student, Documenttype, City, Paymentsconcepts, Payments


class AdminStudent(admin.ModelAdmin):
    list_display = ['code_student', 'name_student', 'lastname_student',
                    'document_type','number_document','gender', 'birthday','city',
                    'address','neighborhood','number_telephone','cellphone_number',
                    'register_date']


class AdminDocumenttype(admin.ModelAdmin):
    list_display = ['documet_type']


class AdminCity(admin.ModelAdmin):
    list_display = ['city']

class AdminPaymentsconcepts(admin.ModelAdmin):
    list_display = ['paymentsconcepts']

class AdminPayments(admin.ModelAdmin):
    list_display = ['code_student', 'paymentsconcepts', 'valuepayments', 'datepayment', 'observations']


admin.site.register(Student, AdminStudent)
admin.site.register(Documenttype, AdminDocumenttype)
admin.site.register(City, AdminCity)
admin.site.register(Payments, AdminPayments)
admin.site.register(Paymentsconcepts, AdminPaymentsconcepts)
