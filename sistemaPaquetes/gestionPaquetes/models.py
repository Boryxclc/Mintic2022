from django.db import models

# Create your models here.
class Paquetes(models.Model):
    direccion_envio= models.CharField('Direccion envio', max_length=100,null=False, blank=False)
    nombre_remitente= models.CharField('remitente', max_length=100, null=False, blank=False)
    nombre_destinatario= models.CharField('remitente', max_length=100, null=False, blank=False)
    fecha_creacion= models.DateField('fecha de creación', auto_now=False, auto_now_add=True)
    estado= models.BooleanField('en transito/ entregado',default=True)
    peso=models.IntegerField('peso en kg',max_length=10)
    tamano= models.CharField('mensajeria/basico/sobredimensionado', max_length=50)
    fecha_entrega= models.DateField('fecha de creación', auto_now=False, auto_now_add=True)
