from django.conf.urls import url
from projectx import views

urlpatterns = [
    url(r'^menus/$', views.menu_list),
]