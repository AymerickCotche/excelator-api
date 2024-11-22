from django.urls import include, path
from rest_framework import routers

from lesbases import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'sales', views.SaleViewSet)
router.register(r'purchases', views.PurchaseViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]