from django.db import models

# Create your models here.

class Propietario(models.Model):

    codigo = models.CharField(max_length=8,primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    mascota = models.ManyToManyField("Mascota",blank=True,related_name="clientes")

    class Meta:
        verbose_name = 'Propietario'
        verbose_name_plural = 'Propietarios'

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=3, default=0,)
    foto = models.ImageField(upload_to='mascotas',null=True,blank=True)
    descripcion = models.TextField()
    adoptada = models.CharField(max_length=50,null=True,blank=True)
    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

    def __str__(self):
        return self.nombre
