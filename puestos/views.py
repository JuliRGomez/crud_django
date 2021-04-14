from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from empleados.models import Empleados
from puestos.models import Puestos
from puestos.serializers import PuestosSerializer


class PuestosViewSet(ModelViewSet):
    queryset = Puestos.objects.all()
    serializer_class = PuestosSerializer
