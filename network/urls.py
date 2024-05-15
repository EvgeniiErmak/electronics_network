# network/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkNodeViewSet
from . import views

router = DefaultRouter()
router.register(r'nodes', NetworkNodeViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include('rest_framework.urls')),
]
