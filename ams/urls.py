from django.conf.urls import url
from ams import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    # url(r'^home/(?P<pk>\d+)', views.home, name='home'),
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^MarkAttendance/(?P<pk>\d+)', views.MarkAttendance.as_view(), name='markattendance'),
    # url(r'^StudentProfile/$', views.MarkAttendance.as_view(), name='studentprofile'),
    # url(r'')
]
