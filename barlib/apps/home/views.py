<<<<<<< HEAD
import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Promocion
=======

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Producto
>>>>>>> 3683fc19d1ffde0f7a982c11d48deb30da92fc87
from bson import ObjectId
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Vista para editar un producto
def editar_producto_view(request, producto_id):
    producto = get_object_or_404(Producto, _id=ObjectId(producto_id))

    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.categoria = request.POST['categoria']
        producto.cantidad = request.POST['cantidad']
        producto.unidad = request.POST['unidad']
        
        imagen = request.FILES.get('imagen')
        if imagen:
            producto.imagen = imagen

        producto.agotado = 'agotado' in request.POST
        
        producto.save()
        return redirect('/home/')

    context = {
        'producto': producto
    }
    return render(request, 'home/editar.html', context)

# Vista home protegida
@login_required
def home(request):
    query = request.GET.get('search', '')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()

    menu_items = {}
    productos_agotados = 0
    for producto in productos:
        if producto.agotado:
            productos_agotados += 1
            continue
        if producto.categoria not in menu_items:
            menu_items[producto.categoria] = []
        menu_items[producto.categoria].append(producto)

    
    context = {
        'menu_items': menu_items,
        'search': query,
        'cantidad_agotados': productos_agotados,
        'MEDIA_URL': settings.MEDIA_URL

    }

    return render(request, 'home/home.html', context)


# Vista para cerrar sesión
def logout_view(request):
    logout(request)  # Cerrar sesión
    return redirect('/')  # Redirigir al login


def registro_producto_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        categoria = request.POST['categoria']
        cantidad = request.POST['cantidad']
        unidad = request.POST['unidad']
        imagen = request.FILES.get('imagen')
        agotado = 'agotado' in request.POST

        nuevo_producto = Producto(
            nombre=nombre,
            precio=precio,
            categoria=categoria,
            cantidad=cantidad,
            unidad=unidad,
            imagen=imagen,
            agotado=agotado)
        nuevo_producto.save()

        return redirect('/home/')

    return render(request, 'home/registro.html')

def ingredientes_view(request):
    return render(request, 'home/ingredientes.html')

def promos_view(request):
    # Obtener todos los productos
    productos = Producto.objects.all()
    # Obtener todas las promociones
    promociones = Promocion.objects.all()
    
    context = {
        'productos': productos,
        'promociones': promociones,
    }
    return render(request, 'home/promos.html', context)

def crear_promos_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        promo_type = request.POST.get('promoType')
        nombre_promocion = request.POST.get('amountOff')
        descuento = request.POST.get('porcentaje')  # Suponiendo que el descuento sea un porcentaje
        producto_id = request.POST.get('producto')
        producto = Producto.objects.get(pk=ObjectId(producto_id))

        # Crear la nueva promoción
        promocion = Promocion(
            nombre=nombre_promocion,
            tipo=promo_type,
            descuento=descuento,
            producto=producto
        )

        promocion.save()

        return redirect('home:promos')# Redirigir a la página de promociones
    
    productos = Producto.objects.all()
    return render(request, 'home/crearPromo.html', {'productos': productos})


@csrf_exempt
def toggle_promocion(request, promo_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        promo = Promocion.objects.get(id=promo_id)
        promo.activo = data.get('activo', False)
        promo.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def eliminar_producto_view(request, producto_id):
    producto = get_object_or_404(Producto, _id=ObjectId(producto_id))
    producto.delete()
    return redirect('/home/')

def toggle_stock(request, producto_id):
    producto = get_object_or_404(Producto,  _id=ObjectId(producto_id))
    producto.agotado = not producto.agotado
    producto.save()
    return redirect('home:home')

def productos_agotados_view(request):
    productos = Producto.objects.all()
    productos_agotados = [producto for producto in productos if producto.agotado]

    if request.is_ajax():
        data = {
            'productos_agotados': [
                {
                    '_id': str(producto._id),
                    'nombre': producto.nombre,
                    'precio': producto.precio,
                    'imagen_url': f"{settings.MEDIA_URL}{producto.imagen}",
                    'agotado': producto.agotado
                }
                for producto in productos_agotados
            ]
        }
        return JsonResponse(data)
    
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'home/home.html', context)


