from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.login.urls')),
    path('admin/', admin.site.urls),
    path('principal/', include('apps.principal.urls')),
    path('home/', include('apps.home.urls')),
    path('ordenes/', include('apps.ordenes.urls')),
    path('mesas/', include('apps.Mesas.urls')),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
