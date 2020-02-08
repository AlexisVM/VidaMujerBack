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

	def update(self, request, *args, **kwargs):
			partial = kwargs.pop('partial', False)
			instance = self.get_object()
			instance.aprobada = False
			serializer = self.get_serializer(instance, data=request.data, partial=partial)
			serializer.is_valid(raise_exception=True)
			self.perform_update(serializer)

			if getattr(instance, '_prefetched_objects_cache', None):
				# If 'prefetch_related' has been applied to a queryset, we need to
				# forcibly invalidate the prefetch cache on the instance.
				instance._prefetched_objects_cache = {}

			return Response(serializer.data)




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