
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.home.views import logout_view


urlpatterns = [
    path('', include('apps.login.urls')),
    path('admin/', admin.site.urls),
    path('principal/', include('apps.principal.urls')),
<<<<<<< HEAD
=======

    path('home/', include('apps.home.urls')),
    path('logout/', logout_view, name='logout'),
]
=======

>>>>>>> c68ff303cb6da680c24b2a64eca0ab6e18eb0677
    path('home/', include('apps.home.urls')),
    path('logout/', logout_view, name='logout'),
    path('ordenes/', include('apps.ordenes.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


<<<<<<< HEAD
=======
    path('home/', include('apps.home.urls')),
    path('logout/', logout_view, name='logout'),



>>>>>>> c68ff303cb6da680c24b2a64eca0ab6e18eb0677
