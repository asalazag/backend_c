# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class T149McTipoInvServ(models.Model):
    f149_ts = models.DateTimeField()
    f149_id_cia = models.OneToOneField('T118McExtensiones2', models.DO_NOTHING, db_column='f149_id_cia', primary_key=True)
    f149_id = models.CharField(max_length=10)
    f149_descripcion = models.CharField(max_length=40)
    f149_ind_contabilizacion_costo = models.SmallIntegerField()
    f149_ind_clase = models.SmallIntegerField()
    f149_ind_ajustable = models.SmallIntegerField()
    f149_ind_depreciable = models.SmallIntegerField()
    f149_ind_contabiliza = models.SmallIntegerField()
    f149_ind_lote = models.SmallIntegerField()
    f149_ind_lote_asignacion = models.SmallIntegerField()
    f149_ind_extension = models.SmallIntegerField()
    f149_id_extension1 = models.ForeignKey('T116McExtensiones1', models.DO_NOTHING, db_column='f149_id_extension1', blank=True, null=True)
    f149_id_extension2 = models.ForeignKey('T118McExtensiones2', models.DO_NOTHING, db_column='f149_id_extension2', blank=True, null=True)
    f149_vida_util = models.SmallIntegerField()
    f149_notas = models.CharField(max_length=255)
    f149_tipo_equiv = models.CharField(max_length=10, blank=True, null=True)
    f149_rowid_movto_entidad = models.IntegerField(blank=True, null=True)
    f149_ind_ajuste_vnr = models.SmallIntegerField()
    f149_ind_desc_variable = models.SmallIntegerField()
    f149_ind_recalcular_um_adic = models.SmallIntegerField()
    f149_ind_gum_unificado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 't149_mc_tipo_inv_serv'
        unique_together = (('f149_id_cia', 'f149_id_cia', 'f149_id_cia', 'f149_id'),)
