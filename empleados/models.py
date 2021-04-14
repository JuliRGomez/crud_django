from django.db import models

from puestos.models import Puestos


class Empleados (models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    puesto = models.ForeignKey(Puestos, related_name='empleado', on_delete=models.SET_NULL, null=True)
