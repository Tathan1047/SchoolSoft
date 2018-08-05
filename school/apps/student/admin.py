from django.contrib import admin

from apps.student.models import Student, Documenttype, City


class AdminStudent(admin.ModelAdmin):
    list_display = ['code_student', 'name_student', 'lastname_student',
                    'document_type','number_document','gender', 'birthday','city',
                    'address','neighborhood','number_telephone','cellphone_number',
                    'register_date']


class AdminDocumenttype(admin.ModelAdmin):
    list_display = ['documet_type']


class AdminCity(admin.ModelAdmin):
    list_display = ['city']


admin.site.register(Student, AdminStudent)
admin.site.register(Documenttype, AdminDocumenttype)
admin.site.register(City, AdminCity)