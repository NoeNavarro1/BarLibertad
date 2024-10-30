from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Producto

# Vista home protegida
@login_required
def home(request):
    # Obtener el término de búsqueda
    query = request.GET.get('search', '')

    # Obtener todos los productos y aplicar el filtro si hay un término de búsqueda
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
        'search': query
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
        imagen = request.FILES.get('imagen')

        # Crear y guardar el producto en MongoDB
        nuevo_producto = Producto(nombre=nombre, precio=precio, categoria=categoria)
        nuevo_producto.save()

        return redirect('/home/')

    return render(request, 'home/registro.html')
