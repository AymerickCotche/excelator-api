from rest_framework import serializers

from lesbases.models import Product, Purchase, Sale


class ProductSerializer(serializers.ModelSerializer):

    total_sales = serializers.IntegerField(read_only=True)
    total_purchases = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Product
        fields = "__all__"

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"
