# Generated by Django 2.2 on 2021-04-13 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('puestos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('puesto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empleado', to='puestos.Puestos')),
            ],
        ),
    ]
