from django.db import models


class T121McItemsExtensiones(models.Model):
    f121_ts = models.DateTimeField()
    f121_id_cia = models.SmallIntegerField()
    # f121_id_cia = models.ForeignKey(
    #     'T131McItemsBarras', models.DO_NOTHING, db_column='f121_id_cia')
    f121_rowid = models.AutoField(primary_key=True)
    f121_rowid_item = models.IntegerField()
    # f121_rowid_item = models.ForeignKey(
    #     T120McItems, models.DO_NOTHING, db_column='f121_rowid_item')
    f121_id_ext1_detalle = models.CharField(max_length=20)
    # f121_id_ext1_detalle = models.ForeignKey(
    #     T117McExtensiones1Detalle, models.DO_NOTHING, db_column='f121_id_ext1_detalle', blank=True, null=True)
    f121_id_ext2_detalle = models.CharField(max_length=20)
    # f121_id_ext2_detalle = models.ForeignKey(
    #     T119McExtensiones2Detalle, models.DO_NOTHING, db_column='f121_id_ext2_detalle', blank=True, null=True)
    f121_ind_estado = models.SmallIntegerField()
    f121_fecha_inactivacion = models.DateTimeField(blank=True, null=True)
    f121_fecha_creacion = models.DateTimeField()
    f121_rowid_foto = models.IntegerField()
    # f121_rowid_foto = models.ForeignKey(
    #     'T580FfFotos', models.DO_NOTHING, db_column='f121_rowid_foto', blank=True, null=True)
    f121_notas = models.CharField(max_length=255)
    f121_usuario_inactivacion = models.CharField(
        max_length=30, blank=True, null=True)
    f121_usuario_creacion = models.CharField(
        max_length=30, blank=True, null=True)
    f121_usuario_actualizacion = models.CharField(
        max_length=30, blank=True, null=True)
    f121_fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    f121_id_extension1 = models.CharField(max_length=2)
    # f121_id_extension1 = models.ForeignKey(
    #     T117McExtensiones1Detalle, models.DO_NOTHING, db_column='f121_id_extension1', blank=True, null=True)
    f121_id_extension2 = models.CharField(max_length=2)
    # f121_id_extension2 = models.ForeignKey(
    #     T119McExtensiones2Detalle, models.DO_NOTHING, db_column='f121_id_extension2', blank=True, null=True)
    f121_rowid_movto_entidad = models.IntegerField(blank=True, null=True)
    f121_porc_max_exceso_kit = models.DecimalField(
        max_digits=7, decimal_places=4)
    f121_porc_min_exceso_kit = models.DecimalField(
        max_digits=7, decimal_places=4)
    f121_id_unidad_validacion_kit = models.CharField(max_length=4)
    # f121_id_unidad_validacion_kit = models.ForeignKey(
    #     T101McUnidadesMedida, models.DO_NOTHING, db_column='f121_id_unidad_validacion_kit', blank=True, null=True)
    f121_id_barras_principal = models.CharField(max_length=20)
    # f121_id_barras_principal = models.ForeignKey(
    #     'T131McItemsBarras', models.DO_NOTHING, db_column='f121_id_barras_principal', blank=True, null=True)
    f121_id_plan_kit = models.CharField(max_length=3)
    # f121_id_plan_kit = models.ForeignKey(
    #     T105McCriteriosItemPlanes, models.DO_NOTHING, db_column='f121_id_plan_kit', blank=True, null=True)
    f121_rowid_item_ext_gen = models.IntegerField()
    # f121_rowid_item_ext_gen = models.ForeignKey(
    #     'self', models.DO_NOTHING, db_column='f121_rowid_item_ext_gen', blank=True, null=True)
    f121_ind_gum_unificado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 't121_mc_items_extensiones'
        unique_together = (('f121_rowid_item', 'f121_id_ext1_detalle',
                           'f121_id_ext2_detalle', 'f121_id_cia'),)
