# network/views.py

from rest_framework import viewsets
from .serializers import NetworkNodeSerializer, SupplierSerializer
from .permissions import IsActiveEmployee
from rest_framework.filters import SearchFilter
from .models import NetworkNode
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def add_node(request):
    if request.user.is_staff:
        return redirect('/admin/network/networknode/add/')
    else:
        messages.error(request, "У вас нет прав доступа")
        return redirect('/login/')


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


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [SearchFilter]
    search_fields = ['country']
