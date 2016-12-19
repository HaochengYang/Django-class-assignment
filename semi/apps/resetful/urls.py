from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^add_product$',views.add_product, name="add_product"),
    url(r'^create_product$',views.create_product, name="create_product"),
    url(r'^show_product/(?P<id>\d+)$',views.show_product, name="show_product"),
    url(r'^edit_product/(?P<id>\d+)$',views.edit_product, name="edit_product"),
    url(r'^edit_exit_product/(?P<id>\d+)$',views.edit_exit_product, name="edit_exit_product"),
    url(r'^remove_product/(?P<id>\d+)$',views.remove_product, name="remove_product"),
    url(r'^delete$',views.delete, name="delete")
]
