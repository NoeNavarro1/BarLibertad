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

class Promocion(models.Model):
    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=100)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.CharField(max_length=50)
    inicio = models.DateField(null=True, blank=True)
    finaliza = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.nombre_producto = self.producto.nombre
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre