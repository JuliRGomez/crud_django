from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from empleados.models import Empleados
from empleados.serializers import EmpleadosSerializer, DetailSerializer


class EmpleadosViewSet(ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer

    def get_serializer_class(self, *argsl, **kwargs):
        if self.action == 'retrieve':
            return DetailSerializer

        return EmpleadosSerializer

