from django.conf.urls import url
from apps.student.views import InicioTemplateView, RegisterpaymentsCreateView, StudentListView


urlpatterns = [
    url(r'^$', InicioTemplateView.as_view(), name="inicio"),
    url(r'^registerpayments/$', RegisterpaymentsCreateView.as_view(), name="registerpayments"),
    url(r'^liststudents/$', StudentListView.as_view(), name="liststudents")
]
