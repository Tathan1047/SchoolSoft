from django.conf.urls import url
from apps.student.views import (InicioTemplateView, RegisterpaymentsCreateView, StudentListView,DeletestudentView,
                                RegisterstudentCreateView, ListpaymentsView, UpdatestudentUpdateView,
                                SearchstudentView,SearchpaymentsView)

urlpatterns = [
    url(r'^$', InicioTemplateView.as_view(), name="inicio"),
    url(r'^registerpayments/$', RegisterpaymentsCreateView.as_view(), name="registerpayments"),
    url(r'^liststudents/$', StudentListView.as_view(), name="liststudents"),
    url(r'^registerstudent/$', RegisterstudentCreateView.as_view(), name="registerstudent"),
    url(r'^listpayments/$', ListpaymentsView.as_view(), name="listpayments"),
    url(r'^updatestudent/(?P<pk>\d+)/$', UpdatestudentUpdateView.as_view(), name="updatestudent"),
    url(r'^deletestudent/(?P<pk>\d+)/$', DeletestudentView.as_view(), name="deletestudent"),
    url(r'^searchestudent/$', SearchstudentView.as_view(), name="searchstudent"),
    url(r'^searchpayments/$', SearchpaymentsView.as_view(), name="searchpayments"),

]
