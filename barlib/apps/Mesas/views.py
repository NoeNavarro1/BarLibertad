from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Mesa
from django.contrib import messages

@login_required
def mesas(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Acceso denegado.")
    mesas_registradas = Mesa.objects.all()

    mesas_libres = Mesa.objects.filter(estado='libre').count()
    mesas_reservadas = Mesa.objects.filter(estado='reservada').count()
    mesas_ocupadas = Mesa.objects.filter(estado='ocupada').count()

    context = {
        'mesas': mesas_registradas,
        'mesas_libres': mesas_libres,
        'mesas_reservadas': mesas_reservadas,
        'mesas_ocupadas': mesas_ocupadas,
    }

    return render(request, 'mesas/primero.html', context)

def crear_mesa(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero = request.POST.get('numero')
        piso = request.POST.get('piso')
        capacidad = request.POST.get('capacidad')
        estado = request.POST.get('estado')

        try:
            nueva_mesa = Mesa(
                nombre=nombre,
                numero=numero,
                piso=piso,
                capacidad=int(capacidad),
                estado=estado
            )
            nueva_mesa.save()
            messages.success(request, "Mesa creada exitosamente.")
            return redirect('/mesas/')
        except Exception as e:
            messages.error(request, f"Error al crear la mesa: {e}")

    return render(request, 'mesas/crear.html')

