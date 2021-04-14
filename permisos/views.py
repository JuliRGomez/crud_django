from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from permisos.models import Permisos
from permisos.serializers import PermisosSerializer, DetailSerializer


class PermisosViewSet(ModelViewSet):
    queryset = Permisos.objects.all()
    serializer_class = PermisosSerializer

    def get_serializer_class(self, *argsl, **kwargs):
        if self.action == 'retrieve':
            return DetailSerializer

        return PermisosSerializer