from django.db import models
from django.contrib.auth import authenticate, get_user_model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

User = get_user_model()

class Tip(models.Model):
	titulo = models.CharField(max_length=100,null=True, blank=True)
	desc = models.TextField()
	imagen = models.ImageField(upload_to='tips')
	photo_thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(250, 250)],
									  format='JPEG',
									  options={'quality': 60})
	class Meta:
		verbose_name_plural = "Tips"
		verbose_name = "Tip"

	def __str__(self):
		return '%s' % (self.titulo)

class Concepto(models.Model):
	titulo = models.CharField(max_length=100)
	desc = models.TextField()
	imagen = models.ImageField(upload_to='conceptos')
	photo_thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(250, 250)],
									  format='JPEG',
									  options={'quality': 60})

class Paquete(models.Model):
	titulo = models.CharField(max_length=100)
	desc = models.TextField()
	imagen = models.ImageField(upload_to='paquetes')
	photo_thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(250, 250)],
									  format='JPEG',
									  options={'quality': 60})
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

class Medicamento(models.Model):
	nombre = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='paquetes')
	desc = models.TextField()
	photo_thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(250, 250)],
									  format='JPEG',
									  options={'quality': 60})
	costo = models.PositiveSmallIntegerField()