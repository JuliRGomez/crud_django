from rest_framework.serializers import ModelSerializer

from empleados.serializers import EmpleadosSerializer
from permisos.models import Permisos


class PermisosSerializer(ModelSerializer):

    class Meta:
        model = Permisos
        fields = "__all__"  # when you write every field use a tuple


class DetailSerializer(ModelSerializer):
    empleado = EmpleadosSerializer()

    class Meta:
        model = Permisos
        fields = "__all__"  # when you write every field use a tuple

