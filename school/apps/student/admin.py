from django.contrib import admin

from apps.student.models import Student, Documenttype, City, Paymentsconcepts, Payments, Socioeconomic,Health,Eps, Attendant


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

class AdminEps(admin.ModelAdmin):
    list_display = ['name_eps']

class AdminPayments(admin.ModelAdmin):
    list_display = ['code_student', 'paymentsconcepts', 'valuepayments', 'datepayment',
                    'paymentmethod','checknumber', 'observations']

class AdminSocioeconomic(admin.ModelAdmin):
    list_display = ['code_student','filesisben','scoresisben','stratum']

class AdminHealth(admin.ModelAdmin):
    list_display = ['code_student', 'eps_affiliate', 'ips_assigned', 'blood_type']

class AdminAttendant(admin.ModelAdmin):
    list_display = ['code_student','indetify_attendant', 'name_attendat', 'lastname_attendat','email', 'address_attendant',
                    'relationship', 'number_telephone','number_cellphone']


admin.site.register(Student, AdminStudent)
admin.site.register(Documenttype, AdminDocumenttype)
admin.site.register(City, AdminCity)
admin.site.register(Payments, AdminPayments)
admin.site.register(Paymentsconcepts, AdminPaymentsconcepts)
admin.site.register(Socioeconomic, AdminSocioeconomic)
admin.site.register(Health, AdminHealth)
admin.site.register(Eps, AdminEps)
admin.site.register(Attendant, AdminAttendant)

