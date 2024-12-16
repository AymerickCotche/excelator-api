from django.shortcuts import render
from rest_framework import viewsets

from referenceabsolue.serializers import CountrySerializer

from referenceabsolue.models import Country

# Create your views here.
class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sales to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer