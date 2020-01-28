from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import  get_user_model
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
	class Meta:
		model = Tip
		fields = '__all__'