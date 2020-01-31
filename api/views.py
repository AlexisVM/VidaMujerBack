from django.shortcuts import render
from rest_framework import status, viewsets
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

class ExperienciaViewSet(viewsets.ModelViewSet):
	serializer_class = ExperienciaSerializer
	queryset = Experiencia.objects.all()
