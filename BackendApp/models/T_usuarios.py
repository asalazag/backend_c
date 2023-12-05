# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TUsuarios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50)  # Field name made lowercase.
    clave = models.CharField(db_column='Clave', max_length=50)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=50)  # Field name made lowercase.
    codcia = models.CharField(db_column='CodCia', max_length=50)  # Field name made lowercase.
    # codcia = models.ForeignKey('TCompanias', models.DO_NOTHING, db_column='CodCia')  # Field name made lowercase.
    direlectronica = models.CharField(db_column='DirElectronica', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccionip = models.CharField(db_column='DireccionIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nombrecompleto = models.CharField(db_column='NombreCompleto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imgfirma = models.BinaryField(db_column='ImgFirma', blank=True, null=True)  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='FechaCreacion', blank=True, null=True)  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='FechaModificacion', blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechavencimiento = models.DateTimeField(db_column='FechaVencimiento', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    fechaultimaconexion = models.DateTimeField(db_column='FechaUltimaConexion', blank=True, null=True)  # Field name made lowercase.
    adminmodificacion = models.IntegerField(db_column='AdminModificacion', blank=True, null=True)  # Field name made lowercase.
    idmac = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_usuarios'