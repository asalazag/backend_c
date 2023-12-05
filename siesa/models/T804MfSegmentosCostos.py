# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class T804MfSegmentosCostos(models.Model):
    f804_ts = models.DateTimeField()
    f804_id_cia = models.OneToOneField('self', models.DO_NOTHING, db_column='f804_id_cia', primary_key=True)
    f804_id = models.SmallIntegerField()
    f804_descripcion = models.CharField(max_length=40)
    f804_desc_corta = models.CharField(max_length=10)
    f804_ind_tipo_costo = models.SmallIntegerField()
    f804_id_segmento_acumula = models.ForeignKey('self', models.DO_NOTHING, db_column='f804_id_segmento_acumula', blank=True, null=True)
    f804_notas = models.CharField(max_length=255)
    f804_ind_niif = models.SmallIntegerField()
    f804_ind_dscto_ppago = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 't804_mf_segmentos_costos'
        unique_together = (('f804_id_cia', 'f804_id_cia', 'f804_id'),)
