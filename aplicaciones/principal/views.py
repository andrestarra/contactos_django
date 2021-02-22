from django.shortcuts import redirect, render
from .models import Persona
from .forms import PersonaForm

# Función para la página de inicio
def inicio(request):
    personas = Persona.objects.all()
    contexto = {
        'personas': personas
    }
    return render(request, 'index.html', contexto)

def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
    else:
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    contexto = {
        'form': form
    }
    return render(request, 'crear_persona.html', contexto)

def editarPersona(request, id):
    persona = Persona.objects.get(id = id)
    if request.method == 'GET':
        form = PersonaForm(instance= persona)
    else:
        form = PersonaForm(request.POST, instance= persona)
        if form.is_valid():
            form.save()
            return redirect('index')
    contexto = {
        'form': form
    }
    return render(request, 'crear_persona.html', contexto)

def eliminarPersona(request, id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')
