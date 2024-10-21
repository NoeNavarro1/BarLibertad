from django.shortcuts import render, redirect
from .models import Producto

# Vista home
def home(request):
    # Obtener el término de búsqueda
    query = request.GET.get('search', '')

    # Obtener todos los productos y aplicar el filtro si hay un término de búsqueda
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)  # Filtra productos que contengan el término de búsqueda
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
        'search': query  # Opcional: puedes pasar la consulta de búsqueda al contexto
    }

    return render(request, 'home/home.html', context)

def registro_producto_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        categoria = request.POST['categoria']
        imagen = request.FILES.get('imagen')

        # Crear y guardar el producto en MongoDB
        nuevo_producto = Producto(nombre=nombre, precio=precio, categoria=categoria)
        nuevo_producto.save()

        return redirect('/home/')  # Redirige después de guardar

    return render(request, 'home/registro.html')

