from django.db import models
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()

class Tip(models.Model):
	desc = models.TextField()

class Conceptos(models.Model):
	titulo = models.CharField(max_length=100)
	desc = models.TextField()
	imagen = models.FileField()

class Paquete(models.Model):
	titulo = models.CharField(max_length=100)
	desc = models.TextField()
	imagen = models.FileField()
	consulta = models.BooleanField()
	costo = models.PositiveSmallIntegerField()
	usuarios = models.ManyToManyField(User,through='Compra')

class Compra(models.Model):
	TIPO_PAGO = [('D','Depósito'),
	('T','Transferencia'),
	('E','Efectivo'),]
	paquete = models.ForeignKey(Paquete, on_delete=models.SET_NULL, null=True)
	usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	fecha_de_pago = models.DateTimeField()
