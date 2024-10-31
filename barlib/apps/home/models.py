from djongo import models

class Producto(models.Model):
    _id = models.ObjectIdField()  # Agregar este campo si no está presente
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
