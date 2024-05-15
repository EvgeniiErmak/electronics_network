# network/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkNodeViewSet, SupplierViewSet, index

router = DefaultRouter()
router.register(r'nodes', NetworkNodeViewSet, basename='networknode')
router.register(r'suppliers', SupplierViewSet, basename='supplier')

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
