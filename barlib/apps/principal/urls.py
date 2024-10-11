from django.urls import path
from . import views

app_name = 'principal'
urlpatterns = [
    path('', views.principal, name='principal')
]

