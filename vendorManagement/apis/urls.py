from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseDetailVIewSet

router = DefaultRouter()
router.register(r'vendors',VendorViewSet )
router.register(r'purchase-details', PurchaseDetailVIewSet)

urlpatterns = [
    path('', include(router.urls)),
]
