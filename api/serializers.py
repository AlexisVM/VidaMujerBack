from djoser.serializers import UserCreateSerializer
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

class CompraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Compra
		fields = 'all'

class FotoSerializer(serializers.ModelSerializer):
	photo_thumbnail = serializers.ImageField(read_only=True)
	foto = Base64ImageField()
	class Meta:
		model = Foto
		fields = ('experiencia','foto','photo_thumbnail')

class ExperienciaSerializer(serializers.ModelSerializer):
	fotos = FotoSerializer(many=True)
	username = serializers.CharField(source='usuario.username', read_only=True)
	class Meta:
		model = Experiencia
		fields = ('id','usuario','username','titulo','desc','fotos')