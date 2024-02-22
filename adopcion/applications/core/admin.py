from django.contrib import admin

# Register your models here.
from .models import Propietario, Mascota

admin.site.register(Mascota)
admin.site.register(Propietario)