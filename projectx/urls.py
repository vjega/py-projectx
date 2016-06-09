from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from projectx import views

urlpatterns = [
    url(r'^menus/$', views.menu_list),
    url(r'^employee/$', views.employee_list),
    url(r'^emp_docs/$', views.emp_documents_list),
    url(r'^emp_docs/(?P<emp_id>[\w\-]+)/$', views.emp_documents_detail),
    url(r'^employee/(?P<emp_id>[\w\-]+)/$', views.employee_detail),
    url(r'^candidate/$', views.candidate_list),
    url(r'^candidate/(?P<id>[\w\-]+)/$', views.candidate_detail),
    url(r'^selectedcandidate/$', views.candidate_selected),   
    url(r'^rejectedcandidate/$', views.candidate_rejected),   
    url(r'^assetsmaster/$', views.assets_list),
    url(r'^assetsmaster/(?P<code>[\w\-]+)/$', views.assets_detail),
    url(r'^assets/$', views.assets_selected), 
    url(r'^documents/$', views.documents_list),
    url(r'^projects/$', views.projects_list),
    url(r'^courses/$',views.courses_list),
    url(r'^circulars/$', views.circulars_list),
    url(r'^circulars/(?P<slno>[\w\-]+)/$', views.circulars_detail),
    url(r'^reporting/$', views.reporting_list),
    url(r'^reporting/(?P<project>[\w\-]+)/$', views.reporting_detail),
    url(r'^location/$', views.location_list),
    url(r'^location/(?P<code>[\w\-]+)/$', views.location_detail),
    url(r'^companysettings/$', views.companysettings_list),
    url(r'^companysettings/(?P<id>[\w\-]+)/$', views.companysettings_detail),
    url(r'^user/$', views.user_list),
    url(r'^user/(?P<user_id>[\w\-]+)/$', views.user_detail),
    url(r'^group/$', views.group_list),
    url(r'^group/(?P<group_id>[\w\-]+)/$', views.group_detail),
]
# url(r'^polls/(?P<string>[\w\-]+)/$','polls.views.detail')
urlpatterns = format_suffix_patterns(urlpatterns)	