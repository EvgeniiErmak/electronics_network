# network/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkNodeViewSet, SupplierViewSet, index, add_node

router = DefaultRouter()
router.register(r'nodes', NetworkNodeViewSet, basename='networknode')
router.register(r'suppliers', SupplierViewSet, basename='supplier')

urlpatterns = [
    path('', index, name='index'),
    path('add_node/', add_node, name='add_node'),
    path('api/', include(router.urls)),
]
