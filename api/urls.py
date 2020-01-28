from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from djoser.views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
	path('auth/login/', TokenCreateView.as_view()),
	path('auth/logout/', TokenDestroyView.as_view()),

	] + router.urls
