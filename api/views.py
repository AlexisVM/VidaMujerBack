from django.shortcuts import render
from rest_framework import status, viewsets
from .serializers import *

# Create your views here.
class TipsViewSet(viewsets.ModelViewSet):
	serializer_class = TipsSerializer
	queryset = Tip.objects.all()
