from django.db import models


class T120McItems(models.Model):
    f120_ts = models.DateTimeField()
    f120_id_cia = models.SmallIntegerField()
    # f120_id_cia = models.ForeignKey('T804MfSegmentosCostos', models.DO_NOTHING, db_column='f120_id_cia')
    f120_id = models.IntegerField()
    f120_rowid = models.AutoField(primary_key=True)
    f120_referencia = models.CharField(max_length=50)
    f120_descripcion = models.CharField(max_length=40)
    f120_descripcion_corta = models.CharField(max_length=20)
    f120_id_grupo_impositivo = models.CharField(max_length=4)
    # f120_id_grupo_impositivo = models.ForeignKey('T113McGruposImpositivos', models.DO_NOTHING, db_column='f120_id_grupo_impositivo')
    f120_id_tipo_inv_serv = models.CharField(max_length=10)
    # f120_id_tipo_inv_serv = models.ForeignKey('T149McTipoInvServ', models.DO_NOTHING, db_column='f120_id_tipo_inv_serv')
    f120_id_grupo_dscto = models.CharField(max_length=4)
    # f120_id_grupo_dscto = models.ForeignKey('T109McGrupoDscto', models.DO_NOTHING, db_column='f120_id_grupo_dscto', blank=True, null=True)
    f120_ind_tipo_item = models.SmallIntegerField()
    f120_ind_compra = models.SmallIntegerField()
    f120_ind_venta = models.SmallIntegerField()
    f120_ind_manufactura = models.SmallIntegerField()
    f120_ind_lista_precios_ext = models.SmallIntegerField()
    f120_ind_lote = models.SmallIntegerField()
    f120_ind_lote_asignacion = models.SmallIntegerField()
    f120_ind_sobrecostos = models.SmallIntegerField()
    f120_vida_util = models.SmallIntegerField()
    f120_rowid_tercero_prov = models.IntegerField()
    # f120_rowid_tercero_prov = models.ForeignKey(
    #     'T202MmProveedores', models.DO_NOTHING, db_column='f120_rowid_tercero_prov', blank=True, null=True)
    f120_id_sucursal_prov = models.CharField(max_length=3)
    # f120_id_sucursal_prov = models.ForeignKey(
    #     'T202MmProveedores', models.DO_NOTHING, db_column='f120_id_sucursal_prov', blank=True, null=True)
    f120_rowid_tercero_cli = models.IntegerField()
    # f120_rowid_tercero_cli = models.ForeignKey(
    #     'T201MmClientes', models.DO_NOTHING, db_column='f120_rowid_tercero_cli', blank=True, null=True)
    f120_id_sucursal_cli = models.CharField(max_length=3)
    # f120_id_sucursal_cli = models.ForeignKey(
    #     'T201MmClientes', models.DO_NOTHING, db_column='f120_id_sucursal_cli', blank=True, null=True)
    f120_id_unidad_inventario = models.CharField(max_length=4)
    # f120_id_unidad_inventario = models.ForeignKey(
    #     'T101McUnidadesMedida', models.DO_NOTHING, db_column='f120_id_unidad_inventario')
    f120_id_unidad_adicional = models.CharField(max_length=4)
    # f120_id_unidad_adicional = models.ForeignKey(
    #     'T101McUnidadesMedida', models.DO_NOTHING, db_column='f120_id_unidad_adicional', blank=True, null=True)
    f120_id_unidad_orden = models.CharField(max_length=4)
    # f120_id_unidad_orden = models.ForeignKey(
    #     'T101McUnidadesMedida', models.DO_NOTHING, db_column='f120_id_unidad_orden')
    f120_id_unidad_empaque = models.CharField(max_length=4)
    # f120_id_unidad_empaque = models.ForeignKey(
    #     'T101McUnidadesMedida', models.DO_NOTHING, db_column='f120_id_unidad_empaque', blank=True, null=True)
    f120_id_descripcion_tecnica = models.CharField(max_length=4)
    # f120_id_descripcion_tecnica = models.ForeignKey(
    #     'T103McDescripcionesTecnicas', models.DO_NOTHING, db_column='f120_id_descripcion_tecnica', blank=True, null=True)
    f120_id_extension1 = models.CharField(max_length=2)
    # f120_id_extension1 = models.ForeignKey(
    #     'T116McExtensiones1', models.DO_NOTHING, db_column='f120_id_extension1', blank=True, null=True)
    f120_id_extension2 = models.CharField(max_length=2)
    # f120_id_extension2 = models.ForeignKey(
    #     'T118McExtensiones2', models.DO_NOTHING, db_column='f120_id_extension2', blank=True, null=True)
    f120_rowid_foto = models.IntegerField()
    # f120_rowid_foto = models.ForeignKey(
    #     'T580FfFotos', models.DO_NOTHING, db_column='f120_rowid_foto', blank=True, null=True)
    f120_notas = models.CharField(max_length=255)
    f120_id_segmento_costo = models.SmallIntegerField()
    # f120_id_segmento_costo = models.ForeignKey(
    #     'T804MfSegmentosCostos', models.DO_NOTHING, db_column='f120_id_segmento_costo', blank=True, null=True)
    f120_usuario_creacion = models.CharField(
        max_length=30, blank=True, null=True)
    f120_usuario_actualizacion = models.CharField(
        max_length=30, blank=True, null=True)
    f120_fecha_creacion = models.DateTimeField(blank=True, null=True)
    f120_fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    f120_ind_serial = models.SmallIntegerField()
    f120_id_cfg_serial = models.CharField(max_length=10)
    # f120_id_cfg_serial = models.ForeignKey(
    #     'T172McCfgSerial', models.DO_NOTHING, db_column='f120_id_cfg_serial', blank=True, null=True)
    f120_ind_paquete = models.SmallIntegerField()
    f120_rowid_movto_entidad = models.IntegerField(blank=True, null=True)
    f120_ind_exento = models.SmallIntegerField()
    f120_ind_venta_interno = models.SmallIntegerField()
    f120_ind_generico = models.SmallIntegerField()
    f120_ind_gum_unificado = models.SmallIntegerField()
    f120_id_unidad_precio = models.CharField(max_length=4)
    # f120_id_unidad_precio = models.ForeignKey(
    #     'T101McUnidadesMedida', models.DO_NOTHING, db_column='f120_id_unidad_precio', blank=True, null=True)
    f120_ind_controlado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 't120_mc_items'
        unique_together = (('f120_id', 'f120_id_cia'),
                           ('f120_referencia', 'f120_id_cia'),)
