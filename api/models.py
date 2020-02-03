from django.db import models
from django.contrib.auth import authenticate, get_user_model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils import timezone


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
	def __str__(self):
		return '%s' % (self.titulo)

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
	
	def __str__(self):
		return '%s' % (self.titulo)

class Video(models.Model):
	titulo = models.CharField(max_length=100)
	video = models.FileField()
	paquete = models.ManyToManyField(Paquete,related_name='videos')

	def __str__(self):
		return '%s' % (self.titulo)

class Compra(models.Model):
	TIPO_PAGO = [('D','Depósito'),
	('T','Transferencia'),
	('E','Efectivo'),]
	paquete = models.ForeignKey(Paquete, on_delete=models.SET_NULL, null=True)
	usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='compras')
	fecha_de_pago = models.DateTimeField(default=timezone.now)
	aprobada = models.BooleanField(default=False)
	def __str__(self):
		return 'Usuario: %s Paquete: %s' % (self.usuario, self.paquete)

class Comprobante(models.Model):
	compra = models.ForeignKey(Compra, on_delete=models.SET_NULL, null=True)
	uri = models.ImageField()
	photo_thumbnail = ImageSpecField(source='uri',
									  processors=[ResizeToFill(250, 250)],
									  format='JPEG',
									  options={'quality': 60})
class Medicamento(models.Model):
	nombre = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='paquetes')
	desc = models.TextField()
	photo_thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(250, 250)],
									  format='JPEG',
									  options={'quality': 60})
	costo = models.PositiveSmallIntegerField()
	def __str__(self):
		return '%s' % (self.nombre)

class Experiencia(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	titulo = models.CharField(max_length=100)
	desc = models.TextField()
	fecha = models.DateTimeField(	default=timezone.now)
	def __str__(self):
		return '%s por %s' % (self.titulo, self.usuario)

class Foto(models.Model):
	uri = models.ImageField(upload_to='experiencias')
	photo_thumbnail = ImageSpecField(source='uri',
									  processors=[ResizeToFill(250, 250)],
									  format='JPEG',
									  options={'quality': 60})
	experiencia = models.ForeignKey(Experiencia, on_delete=models.SET_NULL, null=True,related_name='fotos')
	
	class Meta:
		verbose_name_plural = "Fotos"

	def __str__(self):
		return '%s' % (self.experiencia)