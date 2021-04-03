"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from products import views
from pages.views import home_view, contact_view, about_view
#from products.views import Temperature_view, Temperature_detail_view, Temperature_request_view
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.staticfiles import views
from django.conf.urls import url
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name="Watsontown Brick"),
    path('about/', about_view),
    path('contact/', contact_view),
    #path('createburner/', Temperature_view),
    #path('burnerdetail/<str:date>/', Temperature_detail_view, name='Temperature'),'''
    #path('requestdate/', Temperature_request_view),
    re_path(r'^api/products/$', views.Temperature_list),
    re_path(r'^api/products/([0-9])$', views.Temperature_detail)
]