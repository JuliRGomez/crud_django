from rest_framework.serializers import ModelSerializer

from puestos.models import Puestos


class PuestosSerializer(ModelSerializer):

    class Meta:
        model = Puestos
        fields = "__all__"  # when you write every field use a tuple