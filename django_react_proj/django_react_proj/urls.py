"""django_react_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from urllib import request
from django.contrib import admin
from django.urls import path, re_path, include
from temperatures import views
from django.conf.urls import url
from temperatures import views
#from temperatures.views import temperatures_list ,TemperatureList
#from temperatures.views import DynamicSearchFilter
#from temperatures.views import TemperatureDayArchiveView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('temperatures.urls')),
    # re_path(r'^api/temperatures/$', views.temperatures_list())
    #re_path(r'^api/temperatures/$', views.temperatures_list),
    #re_path(r'^api/temperatures/', views.temperatures_search, name='temperatures_search'), #([0-9-]*)
    #path('api/temperatures/?temperatures=<str:date>', views.temperature_get),
    # re_path(r'^api/temperatures/([0-9])$', views.temperatures_detail),
]
