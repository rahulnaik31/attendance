"""attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include #for include,path
from django.conf.urls import url        #for url
from ams import views
from django.contrib.auth import views   #REQUIRED FOR LOGIN
from django.conf import settings        #REQUIRED FOR LOGIN

urlpatterns = [
    url(r'',include('ams.urls')),
    path('admin/', admin.site.urls),
    # url(r'^accounts/', include('allauth.urls')),      #FOR fb authentication
    url(r'accounts/login/$',views.LoginView.as_view(),name='login'),
    url(r'accounts/logout/$',views.LogoutView.as_view(),name='logout',kwargs={'next_page':'/'})

]
