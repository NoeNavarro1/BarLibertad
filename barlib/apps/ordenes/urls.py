from django.urls import path
from . import views

app_name = 'ordenes'
urlpatterns = [
    path('', views.ordenes, name='ordenes')
]