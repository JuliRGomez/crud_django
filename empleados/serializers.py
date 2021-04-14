from rest_framework.serializers import ModelSerializer

from empleados.models import Empleados
from puestos.serializers import PuestosSerializer


class EmpleadosSerializer(ModelSerializer):

    class Meta:
        model = Empleados
        fields = "__all__"  # when you write every field use a tuple


class DetailSerializer(ModelSerializer):
    puesto = PuestosSerializer()
    class Meta:
        model = Empleados
        fields = "__all__"  # when you write every field use a tuple