
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Producto
from bson import ObjectId
from django.conf import settings
from django.http import JsonResponse

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

        # Manejar el estado de agotado
        producto.agotado = 'agotado' in request.POST  # Esto asume que el checkbox tiene el nombre 'agotado'
        
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
    logout(request)  # Cierra la sesión

    # Redirige al login y añade encabezados para evitar caché
    request.session.flush() 
    response = redirect('/')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


def registro_producto_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        categoria = request.POST['categoria']
        cantidad = request.POST['cantidad']
        unidad = request.POST['unidad']
        imagen = request.FILES.get('imagen')
        agotado = 'agotado' in request.POST  # Esto asume que el checkbox tiene el nombre 'agotado'

        # Crear y guardar el producto en MongoDB
        nuevo_producto = Producto(
            nombre=nombre,
            precio=precio,
            categoria=categoria,
            cantidad=cantidad,
            unidad=unidad,
            imagen=imagen,
            agotado=agotado)  # Guardar el estado de agotado
        nuevo_producto.save()

        return redirect('/home/')


    return render(request, 'home/registro.html')
=======
    return render(request, 'home/registro.html')

def ingredientes_view(request):
    return render(request, 'home/ingredientes.html')

def eliminar_producto_view(request, producto_id):
    producto = get_object_or_404(Producto, _id=ObjectId(producto_id))
    producto.delete()  # Elimina el producto de la base de datos
    return redirect('/home/')

def toggle_stock(request, producto_id):
    producto = get_object_or_404(Producto,  _id=ObjectId(producto_id))
    producto.agotado = not producto.agotado  # Alterna el estado de agotado
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

