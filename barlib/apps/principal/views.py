from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


@login_required
def principal(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Acceso denegado.")
    return render(request, 'principal/principal.html')
