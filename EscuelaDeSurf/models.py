from django.db import models

# Create your models here.
from django.db import models

class MembershipPlan(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)  
    

    def __str__(self):
        return self.nombre

class Products(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    

    def __str__(self):
        return self.nombre

class SurfClass(models.Model):
    titulo = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.titulo} - {self.instructor}"
