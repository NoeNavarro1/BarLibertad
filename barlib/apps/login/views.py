from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Intentamos autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si la autenticación fue exitosa, iniciamos la sesión
            login(request, user)

<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> c68ff303cb6da680c24b2a64eca0ab6e18eb0677
            return redirect('home/')  # Redirige a la vista de bienvenida
            return redirect('principal/')  # Redirige a la vista de bienvenida
=======
         return redirect('home/')  # Redirige a la vista de bienvenida
         return redirect('principal/')  # Redirige a la vista de bienvenida
<<<<<<< HEAD
>>>>>>> develop
=======

>>>>>>> c68ff303cb6da680c24b2a64eca0ab6e18eb0677

        else:
            # Si falla, mostramos un mensaje de error
            messages.error(request, 'Usuario o contraseña inválidos.')

    return render(request, 'registration/login.html')

@login_required  # Proteger la vista
def principal(request):
    username = request.user.username

    return render(request, 'home.html', {'username': username})
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> develop
=======

=======


>>>>>>> c68ff303cb6da680c24b2a64eca0ab6e18eb0677
    return render(request, 'principal.html', {'username': username})

