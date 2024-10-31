from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro_producto_view, name='registro_producto'),
    path('editar/<str:producto_id>/', views.editar_producto_view, name='editar_producto'),
    path('eliminar/<str:producto_id>/', views.eliminar_producto_view, name='eliminar_producto'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)