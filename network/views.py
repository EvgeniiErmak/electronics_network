# network/views.py

from rest_framework import viewsets
from .serializers import NetworkNodeSerializer
from .permissions import IsActiveEmployee
from rest_framework.filters import SearchFilter
from django.shortcuts import render
from .models import NetworkNode


def index(request):
    city = request.GET.get('city', '')
    if city:
        nodes = NetworkNode.objects.filter(city__icontains=city)
    else:
        nodes = NetworkNode.objects.all()
    return render(request, 'network/index.html', {'nodes': nodes})


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [SearchFilter]
    search_fields = ['country']
