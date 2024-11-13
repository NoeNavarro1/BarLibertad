from django.db import models

# Create your models here.
class Mesa(models.Model):
    nombre = models.CharField(max_length=10)
    hora = models.CharField(max_length=10)
    numero = models.IntegerField(unique=True)  # Número único para la mesa
    piso = models.CharField(
        max_length=10,
        choices=[('primer', 'Primer Piso'), ('segundo', 'Segundo Piso'), ('tercer', 'Tercer Piso')],
        default='primer'
    )
    capacidad = models.IntegerField()  # Capacidad de la mesa (cuántas personas puede acomodar)
    estado = models.CharField(
        max_length=20,
        choices=[('libre', 'Libre'), ('reservada', 'Reservada'), ('ocupada', 'Ocupada')],
        default='libre',
    )

    def __str__(self):
        return f"{self.nombre} - {self.numero}"
