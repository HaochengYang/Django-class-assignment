from django.conf.urls import url
from . import views
from models import Coursenames, Descriptions

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^courses$',views.courses, name="Courses"),
    url(r'^review/(?P<id>\d+)$',views.review, name="review"),
    url(r'^destroy/(?P<id>\d+)$',views.destroy, name="destroy"),
]
