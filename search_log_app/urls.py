
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^view_log/$', views.view_log, name='view_log'),  
]

