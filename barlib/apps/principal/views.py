from django.shortcuts import render

# Create your views here.
# Vista principal
def principal(request):
    return render(request, 'principal/principal.html')