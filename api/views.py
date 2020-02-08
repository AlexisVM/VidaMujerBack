from django.shortcuts import render
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.
class TipsViewSet(viewsets.ModelViewSet):
	serializer_class = TipsSerializer
	queryset = Tip.objects.all()

class MedicamentosViewSet(viewsets.ModelViewSet):
	serializer_class = MedicamentosSerializer
	queryset = Medicamento.objects.all()

class ConceptosViewSet(viewsets.ModelViewSet):
	serializer_class = ConceptosSerializer
	queryset = Concepto.objects.all()

class FotoViewSet(viewsets.ModelViewSet):
	serializer_class = FotoSerializer
	queryset = Foto.objects.all()
	
class CompraViewSet(viewsets.ModelViewSet):
	serializer_class = CompraSerializer
	queryset = Compra.objects.all()

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




class ExperienciaViewSet(viewsets.ModelViewSet):
	serializer_class = ExperienciaSerializer
	queryset = Experiencia.objects.all()
	filter_backends = (filters.OrderingFilter,)
	filter_mappings = {
		'fecha': 'fecha',
	}

class PaqueteViewSet(viewsets.ModelViewSet):
	serializer_class = PaqueteSerializer
	queryset = Paquete.objects.all()
	def get_queryset(self):
		user = self.request.user
		auth = self.request.auth
		if auth:
			return Paquete.objects.all().difference(Paquete.objects.filter(usuarios=user))
		else:
			return Paquete.objects.all()