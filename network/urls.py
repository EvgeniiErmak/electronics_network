# network/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkNodeViewSet, index

router = DefaultRouter()
router.register(r'nodes', NetworkNodeViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
