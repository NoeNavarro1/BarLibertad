from django.shortcuts import redirect
from django.conf import settings
import re

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = [
            re.compile(settings.LOGIN_URL.lstrip('/')),
            re.compile(r'^admin/'),
        ]

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not any(url.match(path) for url in self.exempt_urls):
                return redirect(settings.LOGIN_URL)

        response = self.get_response(request)

        # Evita el cacheado para páginas de usuarios autenticados
        if request.user.is_authenticated:
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'

        return response
