from django.contrib import admin
from django.urls import path,include


from .import views

from .views import index,listado_mascotas,GrabarMascota,mascota,adoptar

app_name = "core_app"
urlpatterns = [
    path(
        '',
        index,
        name="inicio"
        ),
    path(
        'listar',
        listado_mascotas,
        name="listar-mascotas"
        ),
    path(
        'grabar_mascota',
        GrabarMascota,
        name="grabar_mascota"
        ),
    path(
        '<int:mascota_id>',
        mascota,
        name="mascota"
        ),
    path(
        '<int:mascota_id>/adoptar',
        adoptar,
        name="adoptar"
        ),

]
