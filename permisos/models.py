from django.db import models

from empleados.models import Empleados


class Permisos(models.Model):

    type = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    checkout = models.DateTimeField()
    empleado = models.ForeignKey(Empleados, related_name='permiso', on_delete=models.SET_NULL, null=True)