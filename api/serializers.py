from djoser.serializers import UserCreateSerializer
from django.contrib.auth import  get_user_model
#from djoser.conf import settings
from django.conf import settings
User = get_user_model()


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