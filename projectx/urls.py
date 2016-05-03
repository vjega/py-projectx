from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from projectx import views

urlpatterns = [
    url(r'^menus/$', views.menu_list),
    url(r'^employee/$', views.employee_list),
    url(r'^employee/(?P<pk>[0-9]+)/$', views.employee_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)