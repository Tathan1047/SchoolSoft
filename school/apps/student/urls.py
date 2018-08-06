from django.conf.urls import url
from apps.student.views import InicioTemplateView


urlpatterns = [
    url(r'^$', InicioTemplateView.as_view(), name="inicio"),
]
