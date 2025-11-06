from django.shortcuts import render
from .models import Usuarios

# Create your views here.

def index(request):
    return render(request, "apprender/index.html")


def insertar(request):
    if request.POST:
        correo = request.POST['correo']
        clave = request.POST['clave']
        usuario = Usuarios()
        usuario.correo = correo
        usuario.clave = clave
        usuario.save()
        usuarios = Usuarios.objects.all()
        contexto = {'usuarios': usuarios}
        return render(request, 'apprender/crud.html', contexto)