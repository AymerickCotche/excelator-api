from rest_framework import viewsets
from django.db.models import Sum, Subquery, OuterRef, Value
from django.db.models.functions import Coalesce
from rest_framework.response import Response


from lesbases.serializers import ProductSerializer, PurchaseSerializer, SaleSerializer

from lesbases.models import Product, Purchase, Sale


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.annotate(
        total_sales=Coalesce(
            Subquery(
                Sale.objects.filter(product=OuterRef('pk'))
                .values('product')
                .annotate(total=Sum('quantity'))
                .values('total')[:1]
            ),
            Value(0)
        ),
        total_purchases=Coalesce(
            Subquery(
                Purchase.objects.filter(product=OuterRef('pk'))
                .values('product')
                .annotate(total=Sum('quantity'))
                .values('total')[:1]
            ),
            Value(0)
        )
    )
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        # Appel à la méthode par défaut pour créer l'instance
        response = super().create(request, *args, **kwargs)
        
        # Récupérer l'instance créée avec les annotations
        product_id = response.data['id']
        product = Product.objects.annotate(
            total_sales=Coalesce(Sum('sales__quantity'), Value(0)),
            total_purchases=Coalesce(Sum('purchases__quantity'), Value(0))
        ).get(pk=product_id)
        
        # Sérialiser l'objet annoté
        serializer = self.get_serializer(product)
        return Response(serializer.data)

class PurchaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows purchases to be viewed or edited.
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class SaleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sales to be viewed or edited.
    """
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer