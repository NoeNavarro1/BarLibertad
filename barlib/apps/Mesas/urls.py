from django.urls import path
from . import views

app_name = 'mesas'
urlpatterns = [
    path('', views.mesas, name='mesas'),
    path('crear/', views.crear_mesa, name='crear_mesa'),
]