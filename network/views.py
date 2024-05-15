# network/views.py

from rest_framework import viewsets
from .models import NetworkNode
from .serializers import NetworkNodeSerializer
from .permissions import IsActiveEmployee
from rest_framework.filters import SearchFilter


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [SearchFilter]
    search_fields = ['country']
