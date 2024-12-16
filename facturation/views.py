from rest_framework import viewsets

from facturation.serializers import InvoiceSerializer

from facturation.models import Invoice

# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sales to be viewed or edited.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def perform_create(self, serializer):
        invoice = serializer.save()
        invoice.calculer_facture()