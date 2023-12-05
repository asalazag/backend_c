from django.db import models


class DimEmpleados(models.Model):
    id_empleados = models.IntegerField(db_column='Id_Empleados', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombrecompleto = models.CharField(db_column='NombreCompleto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    des_grupo = models.CharField(db_column='Des_Grupo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    des_cargo = models.CharField(db_column='Des_Cargo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombreempleado = models.CharField(db_column='NombreEmpleado', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DIM_EMPLEADOS'


class TdaDwhRotxubic(models.Model):
    ean = models.CharField(db_column='EAN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    frecuencia = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    porceitem = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    acumula = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    clasificacion = models.CharField(db_column='Clasificacion', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    saldo = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    zonapiso = models.CharField(db_column='ZonaPiso', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fila_piso = models.CharField(max_length=5, blank=True, null=True)
    columna_piso = models.CharField(db_column='Columna_piso', max_length=5, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id_slt = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    fecha_corta = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'TDA_DWH_ROTXUBIC'


class TdaErpBod(models.Model):
    f150_id = models.CharField(max_length=50, blank=True, null=True)
    f150_descripcion = models.CharField(max_length=40)
    f150_descripcion_corta = models.CharField(max_length=20)
    f150_id_co = models.CharField(max_length=50, blank=True, null=True)
    f150_id_instalacion = models.CharField(max_length=3)
    f150_rowid = models.CharField(max_length=20)
    f150_id_cia = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_ERP_BOD'


class TdaErpPrvExt(models.Model):
    item = models.ForeignKey('TdaWmsPrv', models.DO_NOTHING, db_column='item')
    f200_razon_social = models.CharField(max_length=100)
    f015_contacto = models.CharField(max_length=50)
    f015_direccion1 = models.CharField(max_length=40)
    f015_telefono = models.CharField(max_length=20)
    f015_email = models.CharField(max_length=255)
    f202_id_cond_pago = models.CharField(max_length=3, blank=True, null=True)
    f015_id_depto = models.CharField(max_length=2, blank=True, null=True)
    f015_id_ciudad = models.CharField(max_length=3, blank=True, null=True)
    f015_id_pais = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_ERP_PRV_EXT'


class TdaGtteCoo(models.Model):
    id = models.AutoField()
    abreviado_cuenta = models.CharField(max_length=20, blank=True, null=True)
    abreviado_producto = models.CharField(max_length=50, blank=True, null=True)
    abreviado_terminal_destino = models.CharField(max_length=10, blank=True, null=True)
    abreviado_terminal_origen = models.CharField(max_length=10, blank=True, null=True)
    codigo_terminal_destino = models.CharField(max_length=5, blank=True, null=True)
    codigo_terminal_origen = models.CharField(max_length=5, blank=True, null=True)
    etiqueta1d = models.CharField(max_length=20, blank=True, null=True)
    etiqueta2d = models.CharField(max_length=50, blank=True, null=True)
    nombre_nivel_servicio = models.CharField(max_length=10, blank=True, null=True)
    referencia_detalle = models.CharField(max_length=20, blank=True, null=True)
    subzona_reparto = models.CharField(max_length=10, blank=True, null=True)
    zona_reparto = models.CharField(max_length=10, blank=True, null=True)
    picking = models.CharField(db_column='Picking', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estacaja = models.IntegerField(blank=True, null=True)
    numpedido = models.CharField(max_length=20, blank=True, null=True)
    fecharegistro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'TDA_GTTE_COO'


class TdaWmsArt(models.Model):
    productoean = models.CharField(db_column='productoEAN', primary_key=True, max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    referencia = models.CharField(max_length=50)
    inventariable = models.IntegerField(blank=True, null=True)
    um1 = models.CharField(max_length=10, blank=True, null=True)
    presentacion = models.CharField(max_length=100, blank=True, null=True)
    costo = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    referenciamdc = models.CharField(db_column='referenciaMDC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcioningles = models.CharField(db_column='descripcionIngles', max_length=250, blank=True, null=True)  # Field name made lowercase.
    item = models.CharField(max_length=50, blank=True, null=True)
    u_inv = models.CharField(db_column='u_Inv', max_length=25, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(max_length=100, blank=True, null=True)
    subgrupo = models.CharField(max_length=100, blank=True, null=True)
    extension1 = models.CharField(max_length=50, blank=True, null=True)
    extension2 = models.CharField(max_length=50, blank=True, null=True)
    nuevoean = models.CharField(db_column='nuevoEAN', max_length=100)  # Field name made lowercase.
    qtyequivalente = models.DecimalField(db_column='qtyEquivalente', max_digits=14, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    origencompra = models.CharField(db_column='origenCompra', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=30, blank=True, null=True)
    factor = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    f120_tipo_item = models.CharField(max_length=10, blank=True, null=True)
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.
    peso = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    bodega = models.CharField(max_length=20, blank=True, null=True)
    procedencia = models.CharField(max_length=20, blank=True, null=True)
    estadotransferencia = models.IntegerField(blank=True, null=True)
    volumen = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    proveedor = models.CharField(max_length=50, blank=True, null=True)
    preciounitario = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    ingredientes = models.CharField(db_column='Ingredientes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    instrucciones_de_uso = models.CharField(db_column='Instrucciones de uso', max_length=300, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    u_inv_p = models.CharField(db_column='u_Inv_p', max_length=10, blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(max_length=250, blank=True, null=True)
    controla_status_calidad = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    alergenos = models.CharField(max_length=1200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_ART'
        unique_together = (('productoean', 'referencia', 'nuevoean'),)


class TdaWmsArtCon(models.Model):
    productoean = models.CharField(primary_key=True, max_length=100)
    id_product_shopify = models.CharField(max_length=100, blank=True, null=True)
    id_product_variant_shopify = models.CharField(max_length=100, blank=True, null=True)
    id_product_bigcommerce = models.CharField(max_length=100, blank=True, null=True)
    id_product_variant_bigcommerce = models.CharField(max_length=50, blank=True, null=True)
    id_product_quickbooks = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_ART_CON'


class TdaWmsAxu(models.Model):
    productoean = models.CharField(db_column='Productoean', primary_key=True, max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.CharField(db_column='Ubicacion', max_length=50)  # Field name made lowercase.
    bodega = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_AXU'
        unique_together = (('productoean', 'ubicacion', 'bodega'),)


class TdaWmsBin(models.Model):
    ubicacionwms = models.CharField(db_column='Ubicacionwms', max_length=30)  # Field name made lowercase.
    ubicacionerp = models.CharField(db_column='Ubicacionerp', primary_key=True, max_length=30)  # Field name made lowercase.
    bodega = models.CharField(max_length=20)
    bodegaerp = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_BIN'
        unique_together = (('ubicacionerp', 'ubicacionwms', 'bodega'),)


class TdaWmsBpk(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bigpicking = models.ForeignKey('TdaWmsEpk', models.DO_NOTHING, db_column='bigpicking', blank=True, null=True)
    unitarizador = models.CharField(max_length=20)
    tipocaja = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=14, decimal_places=2)
    fechatransmision = models.DateTimeField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    refxcaja = models.IntegerField(blank=True, null=True)
    unidades = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_BPK'
        unique_together = (('bigpicking', 'unitarizador', 'tipocaja'),)


class TdaWmsClt(models.Model):
    nit = models.CharField(max_length=50, blank=True, null=True)
    nombrecliente = models.CharField(db_column='nombreCliente', max_length=250, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    isactivoproveedor = models.IntegerField(db_column='isActivoProveedor', blank=True, null=True)  # Field name made lowercase.
    condicionescompra = models.CharField(db_column='CondicionesCompra', max_length=6, blank=True, null=True)  # Field name made lowercase.
    codigopais = models.CharField(db_column='CodigoPais', max_length=6, blank=True, null=True)  # Field name made lowercase.
    monedadefacturacion = models.CharField(db_column='MonedaDeFacturacion', max_length=3, blank=True, null=True)  # Field name made lowercase.
    item = models.CharField(primary_key=True, max_length=50)
    activocliente = models.IntegerField(db_column='ActivoCliente', blank=True, null=True)  # Field name made lowercase.
    ciudaddestino = models.CharField(db_column='CiudadDestino', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dptodestino = models.CharField(db_column='DptoDestino', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paisdestino = models.CharField(db_column='PaisDestino', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codciudaddestino = models.CharField(db_column='CodCiudadDestino', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coddptodestino = models.CharField(db_column='CodDptoDestino', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codpaisdestino = models.CharField(db_column='CodPaisDestino', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.CharField(db_column='fechaRegistro', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cuidad = models.CharField(db_column='Cuidad', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cuidaddespacho = models.CharField(db_column='CuidadDespacho', max_length=100, blank=True, null=True)  # Field name made lowercase.
    notas = models.CharField(db_column='Notas', max_length=500, blank=True, null=True)  # Field name made lowercase.
    contacto = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    paisdespacho = models.CharField(db_column='paisDespacho', max_length=250, blank=True, null=True)  # Field name made lowercase.
    departamentodespacho = models.CharField(db_column='departamentoDespacho', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sucursaldespacho = models.CharField(db_column='sucursalDespacho', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idsucursal = models.CharField(db_column='idSucursal', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isactivocliente = models.IntegerField(blank=True, null=True)
    isactivoproveed = models.IntegerField(blank=True, null=True)
    estadotransferencia = models.IntegerField(blank=True, null=True)
    vendedor = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    licencia = models.CharField(max_length=20, blank=True, null=True)
    compania = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_CLT'
        unique_together = (('item', 'nit'),)


class TdaWmsCltCon(models.Model):
    item = models.CharField(primary_key=True, max_length=50)
    id_customer_shopify = models.CharField(max_length=50, blank=True, null=True)
    id_customer_bigcommerce = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_CLT_CON'


class TdaWmsCltExt(models.Model):
    codigo = models.ForeignKey(TdaWmsClt, models.DO_NOTHING, db_column='codigo')
    nombre = models.CharField(max_length=150)
    direccioncliente = models.CharField(db_column='DireccionCliente', max_length=200)  # Field name made lowercase.
    poblacion = models.CharField(max_length=100)
    direccionprimeraentrega2 = models.CharField(db_column='direccionPrimeraEntrega2', max_length=150)  # Field name made lowercase.
    nombreentrega2 = models.CharField(max_length=150)
    poblacionentrega2 = models.CharField(db_column='poblacionEntrega2', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDA_WMS_CLT_EXT'


class TdaWmsDaj(models.Model):
    tipodocto = models.CharField(db_column='tipoDocto', max_length=20)  # Field name made lowercase.
    numdocumento = models.CharField(max_length=30)
    fecha = models.DateTimeField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    fechatransferencia = models.DateTimeField(db_column='fechaTransferencia', blank=True, null=True)  # Field name made lowercase.
    motivoajuste = models.CharField(db_column='MotivoAjuste', max_length=100)  # Field name made lowercase.
    idempleado = models.IntegerField()
    caja = models.IntegerField()
    productoean = models.CharField(max_length=50)
    saldoinicial = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtyentrada = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    qtysalida = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pedproveedor = models.CharField(max_length=50)
    id_ajuste = models.CharField(max_length=50, blank=True, null=True)
    loteproveedor = models.CharField(max_length=20)
    bodega = models.CharField(max_length=20, blank=True, null=True)
    ubicacion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_DAJ'


class TdaWmsDpk(models.Model):
    referencia = models.CharField(db_column='Referencia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refpadre = models.CharField(db_column='RefPadre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=180, blank=True, null=True)  # Field name made lowercase.
    qtypedido = models.DecimalField(db_column='qtyPedido', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtyreservado = models.DecimalField(db_column='qtyReservado', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    productoean = models.ForeignKey(TdaWmsArt, models.DO_NOTHING, db_column='productoEAN')  # Field name made lowercase.
    picking = models.ForeignKey('TdaWmsEpk', models.DO_NOTHING, db_column='picking')
    lineaidpicking = models.IntegerField(db_column='LineaIdPicking')  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bodega = models.CharField(db_column='Bodega', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipodocto = models.CharField(db_column='tipoDocto', max_length=20, blank=True, null=True)  # Field name made lowercase.
    doctoerp = models.CharField(db_column='doctoERP', max_length=50)  # Field name made lowercase.
    qtyenpicking = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    estadodetransferencia = models.IntegerField(blank=True, null=True)
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ubicacion_plan = models.CharField(max_length=20, blank=True, null=True)
    fechatransferencia = models.DateTimeField(blank=True, null=True)
    clasifart = models.CharField(max_length=20, blank=True, null=True)
    serial = models.CharField(max_length=50, blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    idco = models.CharField(db_column='idCo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qtyremisionado = models.DecimalField(db_column='qtyRemisionado', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qtyfacturado = models.DecimalField(db_column='qtyFacturado', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    preciounitario = models.DecimalField(db_column='precioUnitario', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    notasitem = models.CharField(max_length=500, blank=True, null=True)
    descripcionco = models.CharField(db_column='descripcionCo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    factor = models.IntegerField(blank=True, null=True)
    numpedido = models.CharField(max_length=30, blank=True, null=True)
    pedproveedor = models.CharField(max_length=50, blank=True, null=True)
    loteproveedor = models.CharField(max_length=20, blank=True, null=True)
    field_qtypedidabase = models.DecimalField(db_column='_qtypedidabase', max_digits=14, decimal_places=2, blank=True, null=True)  # Field renamed because it started with '_'.
    lineaidpickingint = models.IntegerField(db_column='lineaIdPickingInt', blank=True, null=True)  # Field name made lowercase.
    f_ultima_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_DPK'
        unique_together = (('lineaidpicking', 'picking', 'picking', 'productoean', 'loteproveedor', 'estadodetransferencia'),)


class TdaWmsDpn(models.Model):
    numpedido = models.CharField(max_length=50)
    productoean = models.ForeignKey(TdaWmsArt, models.DO_NOTHING, db_column='productoEAN')  # Field name made lowercase.
    picking = models.ForeignKey('TdaWmsEpn', models.DO_NOTHING, db_column='picking')
    lineaidop = models.IntegerField()
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    ref = models.CharField(max_length=50, blank=True, null=True)
    qtypedido = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    qtyreservado = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    bodega = models.CharField(max_length=20)
    ubicacion_plan = models.CharField(max_length=20, blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)
    estadotransferencia = models.IntegerField(blank=True, null=True)
    fechatransferencia = models.DateTimeField(blank=True, null=True)
    qtypicking = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    tipodocto = models.CharField(max_length=50, blank=True, null=True)
    doctoerp = models.CharField(db_column='doctoERP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loteproveedor = models.IntegerField(blank=True, null=True)
    pedproveedor = models.CharField(max_length=50, blank=True, null=True)
    f_ultima_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_DPN'
        unique_together = (('numpedido', 'productoean', 'picking', 'lineaidop', 'loteproveedor'),)


class TdaWmsDuk(models.Model):
    referencia = models.CharField(max_length=50, blank=True, null=True)
    refpadre = models.CharField(db_column='refPadre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=180, blank=True, null=True)
    qtypedido = models.DecimalField(db_column='qtyPedido', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qtyreservado = models.DecimalField(db_column='qtyReservado', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    productoean = models.ForeignKey(TdaWmsArt, models.DO_NOTHING, db_column='productoEAN')  # Field name made lowercase.
    lineaidpicking = models.IntegerField(db_column='lineaIdPicking')  # Field name made lowercase.
    costo = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    bodega = models.CharField(max_length=20)
    tipodocto = models.CharField(db_column='tipoDocto', max_length=20)  # Field name made lowercase.
    doctoerp = models.CharField(db_column='doctoERP', max_length=30)  # Field name made lowercase.
    qtyenpicking = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    estadodetransferencia = models.IntegerField(blank=True, null=True)
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.CharField(max_length=20, blank=True, null=True)
    numdocumento = models.CharField(max_length=50)
    item = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_sale = models.CharField(db_column='ubicacion_Sale', max_length=20, blank=True, null=True)  # Field name made lowercase.
    origen = models.CharField(max_length=20, blank=True, null=True)
    caja_destino = models.FloatField(blank=True, null=True)
    fechaestadoalmdirigido = models.DateTimeField(blank=True, null=True)
    unido = models.CharField(db_column='UNIDO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etd = models.DateTimeField(blank=True, null=True)
    eta = models.DateTimeField(blank=True, null=True)
    pedproveedor = models.CharField(max_length=50, blank=True, null=True)
    ord_no = models.CharField(max_length=50, blank=True, null=True)
    loteproveedor = models.CharField(max_length=20, blank=True, null=True)
    codigoarticulo = models.CharField(db_column='codigoArticulo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cantidadempaque = models.IntegerField(blank=True, null=True)
    f_ultima_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_DUK'


class TdaWmsEaj(models.Model):
    tipodocto = models.CharField(db_column='tipoDocto', max_length=20)  # Field name made lowercase.
    numdocumento = models.CharField(max_length=30)
    fecha = models.DateTimeField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    fechatransferencia = models.DateTimeField(db_column='fechaTransferencia', blank=True, null=True)  # Field name made lowercase.
    motivoajuste = models.CharField(db_column='MotivoAjuste', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDA_WMS_EAJ'
        unique_together = (('tipodocto', 'numdocumento', 'motivoajuste'),)


class TdaWmsEpk(models.Model):
    tipodocto = models.CharField(db_column='tipoDocto', max_length=20)  # Field name made lowercase.
    doctoerp = models.CharField(db_column='doctoERP', max_length=50)  # Field name made lowercase.
    picking = models.CharField(primary_key=True, max_length=20)
    numpedido = models.CharField(db_column='numPedido', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fechaplaneacion = models.DateTimeField(blank=True, null=True)
    f_pedido = models.DateTimeField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    nombrecliente = models.CharField(max_length=200, blank=True, null=True)
    contacto = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    notas = models.CharField(max_length=500, blank=True, null=True)
    ciudad_despacho = models.CharField(db_column='ciudad despacho', max_length=150, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pais_despacho = models.CharField(db_column='pais Despacho', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    departamento_despacho = models.CharField(db_column='departamento Despacho', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sucursal_despacho = models.CharField(db_column='sucursal Despacho', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    direccion_despacho = models.CharField(db_column='direccion Despacho', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    idsucursal = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=150, blank=True, null=True)
    pedidorelacionado = models.CharField(db_column='pedidoRelacionado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cargue = models.CharField(max_length=50, blank=True, null=True)
    nit = models.CharField(max_length=50, blank=True, null=True)
    estadopicking = models.IntegerField(db_column='estadoPicking', blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.
    fpedido = models.DateTimeField(db_column='fPedido', blank=True, null=True)  # Field name made lowercase.
    fechtrans = models.DateTimeField(db_column='fechTrans', blank=True, null=True)  # Field name made lowercase.
    transportadora = models.CharField(max_length=100, blank=True, null=True)
    centrooperacion = models.CharField(db_column='centroOperacion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    estadoerp = models.CharField(db_column='estadoERP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    picking_batch = models.CharField(max_length=20, blank=True, null=True)
    field_condicionpago = models.CharField(db_column='_condicionpago', max_length=20, blank=True, null=True)  # Field renamed because it started with '_'.
    field_documentoreferencia = models.CharField(db_column='_documentoReferencia', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    bodega = models.CharField(max_length=20, blank=True, null=True)
    vendedor2 = models.CharField(max_length=50, blank=True, null=True)
    numguia = models.CharField(max_length=50, blank=True, null=True)
    id = models.AutoField()
    f_ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    bodegaerp = models.CharField(db_column='BodegaERP', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDA_WMS_EPK'
        unique_together = (('tipodocto', 'doctoerp', 'numpedido', 'picking'),)


class TdaWmsEpn(models.Model):
    tipodocto = models.CharField(max_length=50)
    doctoerp = models.CharField(db_column='doctoERP', max_length=20)  # Field name made lowercase.
    picking = models.CharField(primary_key=True, max_length=20)
    numpedido = models.CharField(max_length=50)
    fechaplaneacion = models.DateTimeField(blank=True, null=True)
    fechapedido = models.DateTimeField(blank=True, null=True)
    item = models.ForeignKey('TdaWmsPrv', models.DO_NOTHING, db_column='item')
    fecharegistro = models.DateTimeField(blank=True, null=True)
    bodega = models.CharField(max_length=20)
    estadodetransferencia = models.IntegerField(blank=True, null=True)
    fechatransferencia = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    cantidad = models.IntegerField()
    unidadempaque = models.CharField(max_length=20, blank=True, null=True)
    cantidadempaque = models.IntegerField()
    productoean = models.CharField(db_column='productoEAN', max_length=50)  # Field name made lowercase.
    referencia = models.CharField(max_length=50, blank=True, null=True)
    item_art = models.CharField(max_length=50, blank=True, null=True)
    planificador = models.CharField(max_length=50, blank=True, null=True)
    estadoerp = models.CharField(db_column='estadoERP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qtyenpicking = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    pedproveedor = models.CharField(max_length=50, blank=True, null=True)
    loteproveedor = models.CharField(max_length=50, blank=True, null=True)
    ord_no = models.CharField(max_length=50, blank=True, null=True)
    fechavence = models.DateTimeField(blank=True, null=True)
    f_ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    bodegaerp = models.CharField(db_column='BodegaERP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'TDA_WMS_EPN'
        unique_together = (('tipodocto', 'doctoerp', 'picking', 'numpedido'),)


class TdaWmsEst(models.Model):
    productoean = models.CharField(db_column='productoEAN', primary_key=True, max_length=50)  # Field name made lowercase.
    cantidad = models.IntegerField(blank=True, null=True)
    bodega = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_EST'
        unique_together = (('productoean', 'bodega'),)


class TdaWmsEuk(models.Model):
    tipodocto = models.CharField(db_column='tipoDocto', max_length=20)  # Field name made lowercase.
    doctoerp = models.CharField(db_column='doctoERP', max_length=30)  # Field name made lowercase.
    numdocumento = models.CharField(max_length=50)
    fecha = models.DateTimeField(blank=True, null=True)
    item = models.ForeignKey('TdaWmsPrv', models.DO_NOTHING, db_column='item', blank=True, null=True)
    nombreproveedor = models.CharField(db_column='nombreProveedor', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contacto = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    nit = models.CharField(max_length=30, blank=True, null=True)
    estadodocumentoubicacion = models.IntegerField(blank=True, null=True)
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.
    bl = models.CharField(max_length=50, blank=True, null=True)
    contenedor = models.CharField(max_length=50, blank=True, null=True)
    embarque = models.CharField(max_length=50, blank=True, null=True)
    id = models.AutoField(db_column='Id')  # Field name made lowercase.
    unido = models.CharField(db_column='UNIDO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etd = models.DateTimeField(blank=True, null=True)
    eta = models.DateTimeField(blank=True, null=True)
    codigoarticulo = models.CharField(db_column='codigoArticulo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f_ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    bodega = models.CharField(max_length=30, blank=True, null=True)
    bodegaerp = models.CharField(db_column='BodegaERP', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDA_WMS_EUK'
        unique_together = (('tipodocto', 'doctoerp', 'numdocumento', 'item'),)


class TdaWmsFac(models.Model):
    tipodoctofac = models.CharField(db_column='tipoDoctoFac', max_length=20)  # Field name made lowercase.
    doctoerpfac = models.CharField(db_column='doctoERPFac', max_length=20)  # Field name made lowercase.
    tipodocto = models.CharField(db_column='tipoDocto', max_length=20)  # Field name made lowercase.
    doctoerp = models.CharField(db_column='doctoERP', max_length=20)  # Field name made lowercase.
    numpedido = models.CharField(max_length=20)
    fechafactura = models.DateTimeField(blank=True, null=True)
    itemcliente = models.CharField(db_column='itemCliente', max_length=20)  # Field name made lowercase.
    productoean = models.CharField(db_column='productoEAN', max_length=50)  # Field name made lowercase.
    referencia = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    u_medida = models.CharField(max_length=10, blank=True, null=True)
    estadofactura = models.IntegerField(blank=True, null=True)
    fechatransmite = models.DateTimeField(db_column='fechaTransmite', blank=True, null=True)  # Field name made lowercase.
    id_externo = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_FAC'


class TdaWmsGen(models.Model):
    referencia = models.CharField(max_length=50)
    productoean = models.CharField(db_column='productoEAN', max_length=50)  # Field name made lowercase.
    descripcionpt = models.CharField(db_column='descripcionPT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    referencia_insumo = models.CharField(max_length=50)
    productoean_insumo = models.CharField(db_column='productoEAN_insumo', primary_key=True, max_length=50)  # Field name made lowercase.
    descripcion_insumo = models.CharField(max_length=200, blank=True, null=True)
    cant_requerida = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)
    cant_base = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)
    consumo = models.DecimalField(max_digits=14, decimal_places=5, blank=True, null=True)
    idlista = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'TDA_WMS_GEN'
        unique_together = (('productoean_insumo', 'idlista'),)


class TdaWmsInv(models.Model):
    bod = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=60)
    productoean = models.CharField(db_column='productoEAN', max_length=50)  # Field name made lowercase.
    saldopt = models.DecimalField(db_column='saldoPT', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=400)
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.
    codigoalmacen = models.CharField(db_column='codigoAlmacen', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cantbloqueadoerp = models.DecimalField(db_column='cantBloqueadoERP', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estadodetransferencia = models.IntegerField(blank=True, null=True)
    referencia = models.CharField(max_length=50)
    valor = models.IntegerField(blank=True, null=True)
    tipo_inventario = models.CharField(max_length=50, blank=True, null=True)
    saldowms = models.DecimalField(db_column='saldoWMS', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    etl = models.CharField(max_length=10, blank=True, null=True)
    fecha_ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_prox_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_INV'
        unique_together = (('bod', 'ubicacion', 'productoean'),)


class TdaWmsInvConteo(models.Model):
    id = models.AutoField(db_column='Id')  # Field name made lowercase.
    idconteerp = models.IntegerField(db_column='IDConteERP', blank=True, null=True)  # Field name made lowercase.
    idconteowms = models.IntegerField(db_column='IdConteoWMS', blank=True, null=True)  # Field name made lowercase.
    productoean = models.CharField(db_column='productoEAN', max_length=50)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=180, blank=True, null=True)  # Field name made lowercase.
    qtyteorico = models.DecimalField(db_column='qtyTeorico', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtycontabilizado = models.DecimalField(db_column='qtyContabilizado', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unidades = models.CharField(db_column='Unidades', max_length=20, blank=True, null=True)  # Field name made lowercase.
    estadodetransferencia = models.IntegerField(blank=True, null=True)
    bodega = models.CharField(db_column='Bodega', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.
    fechatransferencia = models.DateTimeField(blank=True, null=True)
    centrooperacion = models.CharField(db_column='CentroOperacion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDA_WMS_INV_CONTEO'


class TdaWmsLot(models.Model):
    idlote = models.IntegerField(db_column='idLote', unique=True)  # Field name made lowercase.
    loteproveedor = models.CharField(primary_key=True, max_length=20)
    nitprov = models.CharField(max_length=50)
    codean = models.CharField(db_column='codEan', max_length=50)  # Field name made lowercase.
    fechaingresa = models.DateTimeField()
    fechavence = models.DateTimeField()
    confirmacertif = models.IntegerField(db_column='Confirmacertif')  # Field name made lowercase.
    pedproveedor = models.CharField(db_column='PedProveedor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='Ord_no', max_length=20)  # Field name made lowercase.
    numcontrolliberacion = models.CharField(db_column='NumControlLiberacion', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDA_WMS_LOT'
        unique_together = (('loteproveedor', 'codean'),)


class TdaWmsLotStatus(models.Model):
    id = models.IntegerField()
    loteproveedor = models.CharField(max_length=50)
    productoean = models.CharField(db_column='productoEAN', max_length=50)  # Field name made lowercase.
    pedproveedor = models.CharField(max_length=50)
    fechainglote = models.DateTimeField(blank=True, null=True)
    fechavencelote = models.DateTimeField(blank=True, null=True)
    fechastatus = models.DateTimeField(blank=True, null=True)
    statuscalidad = models.CharField(max_length=20)
    ord_no = models.CharField(max_length=50, blank=True, null=True)
    numcontrolliberacion = models.CharField(max_length=50, blank=True, null=True)
    estadotransferencia = models.IntegerField(blank=True, null=True)
    fechaestadotransferencia = models.DateTimeField(blank=True, null=True)
    idempleadostatus = models.IntegerField(blank=True, null=True)
    origen_rotulo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_LOT_STATUS'
        unique_together = (('loteproveedor', 'productoean', 'statuscalidad', 'origen_rotulo'),)


class TdaWmsMov(models.Model):
    id = models.IntegerField()
    caja = models.IntegerField()
    ubicacion_inicial = models.CharField(max_length=30)
    ubicacion_final = models.CharField(max_length=30)
    idempleado = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    estadodetransferencia = models.IntegerField(blank=True, null=True)
    fechatransferencia = models.DateTimeField(blank=True, null=True)
    saldo = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    productoean = models.CharField(max_length=50, blank=True, null=True)
    loteproveedor = models.CharField(max_length=30, blank=True, null=True)
    bodega_inicial = models.CharField(max_length=30, blank=True, null=True)
    bodega_final = models.CharField(max_length=30, blank=True, null=True)
    transaccion = models.CharField(max_length=50, blank=True, null=True)
    pallet = models.IntegerField(blank=True, null=True)
    documentooc = models.CharField(max_length=50, blank=True, null=True)
    tipodocto = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_MOV'


class TdaWmsPes(models.Model):
    id = models.AutoField()
    cod_bascula = models.CharField(primary_key=True, max_length=20)
    peso = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    pesotara = models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    pesoneto = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_PES'


class TdaWmsPrv(models.Model):
    nit = models.CharField(max_length=50, blank=True, null=True)
    nombrecliente = models.CharField(db_column='nombreCliente', max_length=250, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=250, blank=True, null=True)
    isactivoproveedor = models.IntegerField(db_column='isActivoProveedor', blank=True, null=True)  # Field name made lowercase.
    condicionescompra = models.CharField(db_column='condicionesCompra', max_length=6, blank=True, null=True)  # Field name made lowercase.
    codigopais = models.CharField(db_column='codigoPais', max_length=6, blank=True, null=True)  # Field name made lowercase.
    monedadefacturacion = models.CharField(db_column='monedaDeFacturacion', max_length=3, blank=True, null=True)  # Field name made lowercase.
    item = models.CharField(primary_key=True, max_length=50)
    activocliente = models.IntegerField(db_column='activoCliente', blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(blank=True, null=True)
    estadotransferencia = models.IntegerField(blank=True, null=True)
    sucursal = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    beneficiario = models.CharField(max_length=50, blank=True, null=True)
    item_sucursal = models.CharField(db_column='Item_sucursal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codigoter = models.CharField(db_column='codigoTer', max_length=10, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'TDA_WMS_PRV'


class TdaWmsPrvExt(models.Model):
    item = models.ForeignKey(TdaWmsPrv, models.DO_NOTHING, db_column='item')
    field_sapstore = models.CharField(db_column='_SAPStore', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_store = models.CharField(db_column='_store', max_length=20, blank=True, null=True)  # Field renamed because it started with '_'.
    field_ciudad = models.CharField(db_column='_ciudad', max_length=120, blank=True, null=True)  # Field renamed because it started with '_'.
    field_st = models.CharField(db_column='_st', max_length=120, blank=True, null=True)  # Field renamed because it started with '_'.
    field_zip = models.CharField(db_column='_zip', max_length=120, blank=True, null=True)  # Field renamed because it started with '_'.
    field_tt = models.CharField(db_column='_TT', max_length=120, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_region = models.CharField(db_column='_region', max_length=120, blank=True, null=True)  # Field renamed because it started with '_'.
    field_distict = models.CharField(db_column='_distict', max_length=20, blank=True, null=True)  # Field renamed because it started with '_'.
    field_ra = models.CharField(db_column='_RA', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_labeltracking = models.CharField(db_column='_labeltracking', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'TDA_WMS_PRV_EXT'


class TdaWmsRelacionSeriales(models.Model):
    documento = models.CharField(primary_key=True, max_length=50)
    cajamp = models.CharField(db_column='CajaMP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    productoean = models.CharField(db_column='ProductoEAN', max_length=50)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numserial = models.CharField(db_column='NumSerial', max_length=50)  # Field name made lowercase.
    empleadopalletiza = models.CharField(db_column='EmpleadoPalletiza', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.
    estadotransferencia = models.IntegerField(db_column='EstadoTransferencia', blank=True, null=True)  # Field name made lowercase.
    fechatransferencia = models.DateTimeField(db_column='FechaTransferencia', blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.CharField(db_column='UBICACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numchasis = models.CharField(max_length=50, blank=True, null=True)
    id = models.AutoField()
    caja = models.IntegerField(blank=True, null=True)
    pedproveedor = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_RELACION_SERIALES'
        unique_together = (('documento', 'productoean', 'numserial'),)


class TdaWmsScm(models.Model):
    id = models.AutoField()
    bigpicking = models.CharField(primary_key=True, max_length=20)
    numpedido = models.CharField(max_length=50, blank=True, null=True)
    unitarizador = models.CharField(max_length=50)
    codsedeorigen = models.CharField(max_length=20)
    codesededestino = models.CharField(max_length=20)
    barcode = models.CharField(max_length=20)
    productoean = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    cantidad = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    tipocaja = models.CharField(db_column='tipoCaja', max_length=20, blank=True, null=True)  # Field name made lowercase.
    peso = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    loteproveedor = models.CharField(max_length=50, blank=True, null=True)
    pedproveedor = models.CharField(max_length=50, blank=True, null=True)
    fechavencelote = models.DateTimeField(blank=True, null=True)
    fecharegistro_origen = models.DateTimeField(blank=True, null=True)
    estadoenvio = models.IntegerField(blank=True, null=True)
    fecharegistro_destino = models.DateTimeField(blank=True, null=True)
    tipodocto = models.CharField(max_length=20)
    doctoerp = models.CharField(db_column='doctoERP', max_length=20)  # Field name made lowercase.
    id_aduana = models.IntegerField(db_column='ID_aduana')  # Field name made lowercase.
    referencia = models.CharField(max_length=50, blank=True, null=True)
    cajamp_estanto = models.IntegerField(db_column='cajaMP_estanto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDA_WMS_SCM'
        unique_together = (('bigpicking', 'unitarizador', 'id_aduana'),)


class TdaWmsTtd(models.Model):
    id = models.AutoField()
    tipodocto = models.ForeignKey('TdaWmsTte', models.DO_NOTHING, db_column='tipoDocto')  # Field name made lowercase.
    doctoerp = models.ForeignKey('TdaWmsTte', models.DO_NOTHING, db_column='doctoERP')  # Field name made lowercase.
    numpedido = models.ForeignKey('TdaWmsTte', models.DO_NOTHING, db_column='numpedido')
    picking = models.ForeignKey('TdaWmsTte', models.DO_NOTHING, db_column='picking')
    alto = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ancho = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    largo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    peso = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    unidades = models.IntegerField(blank=True, null=True)
    referencia_empaque = models.CharField(max_length=10, blank=True, null=True)
    tipocaja = models.CharField(db_column='tipoCaja', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombreempaque = models.CharField(db_column='nombreEmpaque', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDA_WMS_TTD'


class TdaWmsTte(models.Model):
    id = models.AutoField()
    tipodocto = models.CharField(db_column='tipoDocto', primary_key=True, max_length=10)  # Field name made lowercase.
    doctoerp = models.CharField(db_column='doctoERP', max_length=20)  # Field name made lowercase.
    numpedido = models.CharField(max_length=20)
    picking = models.IntegerField()
    nombredestinataro = models.CharField(db_column='nombreDestinataro', max_length=150, blank=True, null=True)  # Field name made lowercase.
    codciudaddestinatario = models.CharField(db_column='codCiudadDestinatario', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dptodestinatario = models.CharField(db_column='dptoDestinatario', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dirdestinatario = models.CharField(db_column='dirDestinatario', max_length=200, blank=True, null=True)  # Field name made lowercase.
    docrelacionado = models.CharField(db_column='docRelacionado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contacto = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    valordeclarado = models.DecimalField(db_column='valorDeclarado', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    codigo_cuenta = models.CharField(max_length=10, blank=True, null=True)
    codigo_producto = models.CharField(max_length=10, blank=True, null=True)
    nivel_servicio = models.CharField(max_length=10, blank=True, null=True)
    nombre_remitente = models.CharField(max_length=100, blank=True, null=True)
    direccion_remitente = models.CharField(max_length=200, blank=True, null=True)
    telefono_remitente = models.CharField(max_length=50, blank=True, null=True)
    cod_ciudadremitente = models.CharField(db_column='cod_ciudadRemitente', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codigocuentaacuerdo = models.CharField(db_column='codigoCuentaAcuerdo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transportadora = models.CharField(max_length=100, blank=True, null=True)
    guiagenerada = models.CharField(db_column='guiaGenerada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    notas = models.CharField(max_length=600, blank=True, null=True)
    fechacreacion = models.DateTimeField(db_column='fechaCreacion', blank=True, null=True)  # Field name made lowercase.
    identificaciondestinatario = models.CharField(db_column='identificacionDestinatario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estadoguia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TDA_WMS_TTE'
        unique_together = (('tipodocto', 'doctoerp', 'numpedido', 'picking'),)


class TggTdaWmsDpk(models.Model):
    referencia = models.CharField(db_column='Referencia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    productoean = models.ForeignKey(TdaWmsArt, models.DO_NOTHING, db_column='productoEAN')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=180, blank=True, null=True)  # Field name made lowercase.
    picking = models.ForeignKey(TdaWmsEpk, models.DO_NOTHING, db_column='picking')
    qtypedido = models.DecimalField(db_column='qtyPedido', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qtyreservado = models.DecimalField(db_column='qtyReservado', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lineaidpicking = models.IntegerField(db_column='LineaIdPicking')  # Field name made lowercase.
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    fecha_movimiento = models.DateTimeField(db_column='Fecha_movimiento', blank=True, null=True)  # Field name made lowercase.
    idconsecutivo = models.AutoField()

    class Meta:
        managed = False
        db_table = 'TGG_TDA_WMS_DPK'


class TObjetosPersonalizados(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=1000, blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_objetos_personalizados'
