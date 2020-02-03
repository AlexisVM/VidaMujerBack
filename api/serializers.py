from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers
from django.contrib.auth import  get_user_model
from drf_extra_fields.fields import Base64ImageField
#from djoser.conf import settings
from django.conf import settings
User = get_user_model()
from .models import *

class UserCreateSerializerCustom(UserCreateSerializer):
	class Meta:
			model = User
			fields = tuple(User.REQUIRED_FIELDS) + (
				"email",
				"username",
				"password",
				"first_name",
				"last_name"
			)

class TipsSerializer(serializers.ModelSerializer):
	photo_thumbnail = serializers.ImageField(read_only=True)
	class Meta:
		model = Tip
		fields = ('titulo','desc','photo_thumbnail')

class MedicamentosSerializer(serializers.ModelSerializer):
	photo_thumbnail = serializers.ImageField(read_only=True)
	class Meta:
		model = Medicamento
		fields = ('nombre','desc','costo','photo_thumbnail')

class ConceptosSerializer(serializers.ModelSerializer):
	photo_thumbnail = serializers.ImageField(read_only=True)
	class Meta:
		model = Concepto
		fields = ('titulo','desc','photo_thumbnail')

class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = '__all__'

class PaqueteSerializer(serializers.ModelSerializer):
	videos = VideoSerializer(many=True)
	photo_thumbnail = serializers.ImageField(read_only=True)
	class Meta:
		model = Paquete
		fields = ('id','titulo','desc','imagen','photo_thumbnail','consulta','costo','videos')

class ComprobanteSerializer(serializers.ModelSerializer):
	uri = Base64ImageField()
	class Meta:
		model = Comprobante
		fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
	#paquete = PaqueteSerializer(many=False)

	class Meta:
		model = Compra
		fields = ('id','usuario','paquete')

class MeSerializer(UserSerializer):
	compras = CompraSerializer(many=True)
	class Meta:
			model = User
			fields = tuple(User.REQUIRED_FIELDS) + (
				"id",	
				"email",
				"username",
				"first_name",
				"last_name",
				"compras"
			)

class FotoSerializer(serializers.ModelSerializer):
	photo_thumbnail = serializers.ImageField(read_only=True)
	uri = Base64ImageField()
	class Meta:
		model = Foto
		fields = ('experiencia','uri','photo_thumbnail')
	def to_representation(self, obj):
		request = self.context.get('request')
		return str(request.build_absolute_uri(obj.uri.url))

class ExperienciaSerializer(serializers.ModelSerializer):
	fotos = FotoSerializer(many=True,read_only=True)
	username = serializers.CharField(source='usuario.username', read_only=True)
	fecha = serializers.DateTimeField(read_only=True)
	class Meta:
		model = Experiencia
		fields = ('id','fecha','usuario','username','titulo','desc','fotos')