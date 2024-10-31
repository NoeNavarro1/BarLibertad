from django.shortcuts import render, redirect,  get_object_or_404
from .models import Producto
from bson import ObjectId
from django.conf import settings

# Vista para editar un producto
def editar_producto_view(request, producto_id):
    producto = get_object_or_404(Producto, _id=ObjectId(producto_id))

    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.categoria = request.POST['categoria']
        
        imagen = request.FILES.get('imagen')
        if imagen:
            producto.imagen = imagen

        producto.save()
        return redirect('/home/')

    context = {
        'producto': producto
    }
    return render(request, 'home/editar.html', context)

# Vista home
def home(request):
    query = request.GET.get('search', '')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()

    # Agrupar productos por categoría
    menu_items = {}
    for producto in productos:
        if producto.categoria not in menu_items:
            menu_items[producto.categoria] = []
        menu_items[producto.categoria].append(producto)
    
    context = {
        'menu_items': menu_items,
        'search': query,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'home/home.html', context)

def registro_producto_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        categoria = request.POST['categoria']
        imagen = request.FILES.get('imagen')

        # Crear y guardar el producto en MongoDB
        nuevo_producto = Producto(nombre=nombre, precio=precio, categoria=categoria, imagen=imagen)
        nuevo_producto.save()

        return redirect('/home/')  # Redirige después de guardar

    return render(request, 'home/registro.html')

def eliminar_producto_view(request, producto_id):
    producto = get_object_or_404(Producto, _id=ObjectId(producto_id))
    producto.delete()  # Elimina el producto de la base de datos
    return redirect('/home/')


