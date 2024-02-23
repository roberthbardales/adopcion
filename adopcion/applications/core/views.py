
from django.shortcuts import render

# Create your views here.
# vista basada en funcion
from .models import Mascota,Propietario
from .forms import MascotaForm
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.urls import reverse

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
            des=form.cleaned_data.get("descripcion")
            fot=form.cleaned_data.get("foto")
            obj=Mascota.objects.create(
                nombre=nom,
                edad=ed,
                descripcion=des,
                foto=fot,
            )
            obj.save()
    else:
        form=MascotaForm()
    context['form']=form

    return render(request,template_name,context)

def mascota(request,mascota_id):
    template_name='mascota.html'
    try:
        mascota=Mascota.objects.get(pk=mascota_id)  #uno se usa get, varios se usa filter
    except Mascota.DoesNotExist:
        raise Http404("Mascota no Existe.....")
    contexto={
        "mascota":mascota,
        "no_clientes":Propietario.objects.exclude(mascota=mascota).all()
    }
    return render(request,template_name,contexto)


def adoptar(request,mascota_id):
    try:
        template_name='index.html'
        cliente_id=request.POST['cliente']
        cliente=Propietario.objects.get(pk=cliente_id)
        mascota=Mascota.objects.get(pk=mascota_id)

    except KeyError:
        print("no selecciono el cliente")
    except Mascota.DoesNotExist:
        print("no existe la mascota")
    except Propietario().DoesNotExist:
        print("no existe la propietario")

    cliente.mascota.add(mascota)
    mascota.adoptada=cliente.nombre
    mascota.save()
    return HttpResponseRedirect(reverse('core_app:mascota',args=(mascota_id,)))