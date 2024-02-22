from django.db import models

# Create your models here.

class Propietario(models.Model):

    codigo = models.CharField(max_length=8,primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Propietario'
        verbose_name_plural = 'Propietarios'

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.CharField(default=0,max_length=50)
    raza = models.CharField(null=True,blank=True,max_length=50)
    foto = models.ImageField(upload_to='mascotas', null=True,blank=True)
    descripcion = models.TextField()
    propietario=models.ManyToManyField(Propietario)
    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

    def __str__(self):
        return self.nombre
