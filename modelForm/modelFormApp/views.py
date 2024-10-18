from django.shortcuts import render, redirect
from modelFormApp.forms import FormProyecto
from modelFormApp.models import Proyecto

# Create your views here.
def index(request):
    return render (request, 'modelFormApp/index.html')

def listadoProyectos(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos': proyectos}

    return render(request,'modelFormApp/proyectos.html',data)

def agregarProyecto(request):
    form = FormProyecto()
    if request.method == 'POST' :
        form = FormProyecto(request.POST)
        if form.is_valid() : 
            form.save()
        return index(request)
    data = {'form': form}
    return render (request,'modelFormApp/agregarProyecto.html',data)

def eliminarProyecto(request,id):
    proyecto = Proyecto.objects.get(id = id)
    proyecto.delete()
    return redirect ('/proyectos')

def actualizarProyecto(request,id):
    proyecto = Proyecto.objects.get(id = id)
    form = FormProyecto(instance=proyecto)
    if request.method == 'POST':
        form = FormProyecto(request.POST, instance=proyecto)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'modelFormApp/agregarProyecto.html',data)