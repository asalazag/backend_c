# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class T113McGruposImpositivos(models.Model):
    f113_ts = models.DateTimeField()
    f113_id_cia = models.OneToOneField('T189McServicios', models.DO_NOTHING, db_column='f113_id_cia', primary_key=True)
    f113_id = models.CharField(max_length=4)
    f113_descripcion = models.CharField(max_length=40)
    f113_notas = models.CharField(max_length=255)
    f113_id_servicio_int = models.ForeignKey('T189McServicios', models.DO_NOTHING, db_column='f113_id_servicio_int', blank=True, null=True)
    f113_id_concepto_int = models.ForeignKey('T146McMotivos', models.DO_NOTHING, db_column='f113_id_concepto_int', blank=True, null=True)
    f113_id_motivo_int = models.ForeignKey('T146McMotivos', models.DO_NOTHING, db_column='f113_id_motivo_int', blank=True, null=True)
    f113_ind_gum_unificado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 't113_mc_grupos_impositivos'
        unique_together = (('f113_id_cia', 'f113_id_cia', 'f113_id_cia', 'f113_id'),)
