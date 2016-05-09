from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^index', views.employee, name='employee'),
    url(r'^(?P<page_name>\w+)/$', views.template_render, name='template_render'),
]