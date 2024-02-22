from django.shortcuts import render

# Create your views here.
# vista basada en funcion
from .models import Mascota
from .forms import MascotaForm

def index(request):
    template_name="index.html"
    obj_mascota=Mascota.objects.all()
    context={'mascotas':obj_mascota
    }
    return render(request,template_name,context)

def listado_mascotas(request):
    template_name="listar.html"
    return render(request,template_name)


def GrabarMascota(request):
    context={}
    template_name='grabar_mascota.html'
    if request.method=='POST':
        form=MascotaForm(request.POST,request.FILES)
        if form.is_valid():
            nom=form.cleaned_data.get("nombre")
            ed=form.cleaned_data.get("edad")
            pro=form.cleaned_data.get("propietario")
            des=form.cleaned_data.get("descripcion")
            fot=form.cleaned_data.get("foto")
            obj=Mascota.objects.create(
                nombre=nom,
                edad=ed,
                # propietario=pro,
                descripcion=des,
                foto=fot,
            )
            obj.propietario.set(pro)
            obj.save()
    else:
        form=MascotaForm()
    context['form']=form

    return render(request,template_name,context)

