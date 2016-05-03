from django.conf.urls import url
from projectx import views

urlpatterns = [
    url(r'^menus/$', views.menu_list),
    url(r'^employee/$', views.employee_list),
    url(r'^employee/(?P<pk>[0-9]+)/$', views.employee_list),
]