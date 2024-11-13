# apps/login/middleware/auth_middleware.py

from django.shortcuts import redirect
from django.conf import settings
import re

class LoginRequiredMiddleware:
    """
    Middleware que redirige al inicio de sesión si el usuario no está autenticado,
    excepto para las rutas permitidas (como /login/).
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # Rutas permitidas sin autenticación
        self.exempt_urls = [
            re.compile(settings.LOGIN_URL.lstrip('/')),  # /login/
            re.compile(r'^admin/'),  # /admin/ (opcional)
        ]

    def __call__(self, request):
        # Verifica si la ruta solicitada está exenta de autenticación
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not any(url.match(path) for url in self.exempt_urls):
                return redirect(settings.LOGIN_URL)

        # Si está autenticado o la ruta está exenta, continúa
        response = self.get_response(request)
        return response
