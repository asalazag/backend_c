# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Templeados(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='APELLIDOS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fecha_nacimiento = models.CharField(db_column='FECHA_NACIMIENTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='CEDULA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cuentabancaria = models.CharField(db_column='CUENTABANCARIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    corporacion = models.CharField(db_column='CORPORACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eps = models.CharField(db_column='EPS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numero_eps = models.CharField(db_column='NUMERO_EPS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ips = models.CharField(db_column='IPS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numero_ips = models.CharField(db_column='NUMERO_IPS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    foto = models.BinaryField(db_column='FOTO', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateTimeField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    fechatermina = models.DateTimeField(blank=True, null=True)
    salabasico = models.FloatField(db_column='Salabasico', blank=True, null=True)  # Field name made lowercase.
    horastraba = models.FloatField(blank=True, null=True)
    prestamos = models.FloatField(blank=True, null=True)
    subtte = models.FloatField(blank=True, null=True)
    dediss = models.FloatField(blank=True, null=True)
    otrasdeducciones = models.FloatField(blank=True, null=True)
    ingresoscontrato = models.IntegerField(blank=True, null=True)
    valorhora = models.FloatField(blank=True, null=True)
    nivelempleado = models.CharField(db_column='NivelEmpleado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='AREA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado')  # Field name made lowercase.
    turno = models.CharField(db_column='Turno', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Templeados'
