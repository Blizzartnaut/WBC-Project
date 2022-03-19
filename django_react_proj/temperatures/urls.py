from django.urls import path, re_path#, register_converter
#from datetime import datetime
from temperatures.views import ListTemperature

'''class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')'''

urlpatterns = [
    #path('', views.index, name='index'),
    # path('api/temperatures/', views.TemperatureList.as_view()),#, name='search_results'),
    # re_path(r'^api/temperatures/$', temperatures_list.as_view())
    path('', ListTemperature)
    ]
