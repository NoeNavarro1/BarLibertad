from djongo import models

class Producto(models.Model):
    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    categoria = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    agotado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre
