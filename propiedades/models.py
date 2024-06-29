from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class TipoPropiedad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Propiedad(models.Model):
    ESTADO_CHOICES = [
        ('venta', 'Venta'),
        ('arriendo', 'Arriendo'),
    ]

    direccion_calle = models.CharField(max_length=255)
    direccion_numero = models.CharField(max_length=10)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoPropiedad, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    habitaciones = models.PositiveIntegerField()
    banos = models.PositiveIntegerField()
    estacionamiento_si_no = models.BooleanField(default=False)
    estacionamiento_cantidad = models.PositiveIntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    valor_uf = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Aquí puedes usar una API para calcular el valor UF basado en el precio
        if not self.valor_uf:
            self.valor_uf = self.calcular_valor_uf(self.precio)
        super().save(*args, **kwargs)

    def calcular_valor_uf(self, precio_clp):
        # Implementar lógica para calcular el valor UF basado en una API
        # Ejemplo:
        # valor_uf = obtener_valor_uf_desde_api(precio_clp)
        # return valor_uf
        pass

    def __str__(self):
        return f'{self.direccion_calle} {self.direccion_numero}, {self.comuna.nombre}'

# Implementación de la función para obtener valor UF desde una API
def obtener_valor_uf_desde_api(precio_clp):
    # Aquí puedes hacer una llamada a una API externa para obtener el valor UF
    # Ejemplo:
    # response = requests.get('url_de_la_api')
    # data = response.json()
    # valor_uf = data['valor_uf']
    # return valor_uf
    pass
