from rest_framework import serializers

from facturation.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invoice
        fields = "__all__"
