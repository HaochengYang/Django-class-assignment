from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.survey, name='survey'),
    url(r'^result$', views.result, name='result'),
]
