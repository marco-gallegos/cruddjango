from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm
# Create your views here.

## vistas basadas en funciones y clases


# vistas funciones

def inicio(request):
    print("hola desde mi vista")
    personas = Persona.objects.all() # select * from persona
    data = {
        'personas': personas
    }
    return render(request, 'list_persona.html', context=data)

def crearpersona(request):
    if request.method == "GET":
        form = PersonaForm()
    else:
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    data = {
        "form": form
    }
    return render(request, 'crear_persona.html', context=data)


def editarpersona(request, id):
    persona = Persona.objects.get(id = id)
    data = {}
    if request.method == "GET":
        form = PersonaForm(instance=persona)
        data={
            'form': form
        }
    else:
        form = PersonaForm(request.POST, instance=persona)
        data={
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_persona.html', context=data)


def eliminarpersona(request, id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')