from django.db import models


# Create your models here.
class Paquete(models.Model):
    TAMANO=[
        ("M", "Mensajereia"),
        ("B", "Basico"),
        ("S", "Sobre Dimensionado"),
    ]
    #ciudad_destino=  models.CharField('ciudad', max_length=100,null=False, blank=False)
    direccion_envio= models.CharField('Direccion envio', max_length=100,null=False, blank=False)
    nombre_remitente= models.CharField('remitente', max_length=100, null=False, blank=False)
    nombre_destinatario= models.CharField('destinatario', max_length=100, null=False, blank=False)
    fecha_creacion= models.DateField('fecha de creación', auto_now=False, auto_now_add=True)
    estado= models.BooleanField('en transito/ entregado',default=True)
    peso=models.IntegerField('peso en kg')
    tamano= models.CharField('mensajeria/basico/sobredimensionado', max_length=1, choices=TAMANO,default="M")
    fecha_entrega= models.DateField('fecha de creación', auto_now=False, auto_now_add=True)
    # todo devoluciones y detalles de devolucion numeros de telefono