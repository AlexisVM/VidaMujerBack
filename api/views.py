from django.shortcuts import render
from rest_framework import status, viewsets, filters
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


class ExperienciaViewSet(viewsets.ModelViewSet):
	serializer_class = ExperienciaSerializer
	queryset = Experiencia.objects.all()
	filter_backends = (filters.OrderingFilter,)
	filter_mappings = {
        'fecha': 'fecha',
    }

class PaqueteViewSet(viewsets.ModelViewSet):
	serializer_class = ExperienciaSerializer
	queryset = Paquete.objects.all()