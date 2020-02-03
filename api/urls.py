from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from djoser.views import *
from .views import *
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'experiencias', ExperienciaViewSet)
router.register(r'fotos', FotoViewSet)
router.register(r'paquetes', PaqueteViewSet)
urlpatterns = [
	path('auth/login/', TokenCreateView.as_view()),
	path('auth/logout/', TokenDestroyView.as_view()),
	path('tips/', TipsViewSet.as_view({'get':'list'})),
	path('meds/',MedicamentosViewSet.as_view({'get':'list'})),
	path('conceptos/',ConceptosViewSet.as_view({'get':'list'})),
	path('comprobantes/', ComprobanteViewSet.as_view({'post':'create'})),
	path('compras/',CompraViewSet.as_view({'post':'create'})),
	] + router.urls
