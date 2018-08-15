from django.conf.urls import url
from apps.student.views import InicioTemplateView, RegisterpaymentsCreateView, StudentListView, RegisterstudentCreateView,\
    ListpaymentsView,UpdatestudentUpdateView, SearchstudentView

urlpatterns = [
    url(r'^$', InicioTemplateView.as_view(), name="inicio"),
    url(r'^registerpayments/$', RegisterpaymentsCreateView.as_view(), name="registerpayments"),
    url(r'^liststudents/$', StudentListView.as_view(), name="liststudents"),
    url(r'^registerstudent/$', RegisterstudentCreateView.as_view(), name="registerstudent"),
    url(r'^listpayments/$', ListpaymentsView.as_view(), name="listpayments"),
    url(r'^updatestudent/(?P<pk>\d+)/$', UpdatestudentUpdateView.as_view(), name="updatestudent"),
    url(r'^searchestudent/$', SearchstudentView.as_view(), name="searchstudent")
]
