from django.shortcuts import render
from rest_framework import viewsets

from eleves.serializers import EleveSerializer

from eleves.models import Eleve

# Create your views here.
class EleveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sales to be viewed or edited.
    """
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer