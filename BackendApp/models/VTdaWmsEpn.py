from django.db import models


class VWmsEpn(models.Model):
    tipodocto = models.CharField(max_length=50)
    # Field name made lowercase.
    doctoerp = models.CharField(db_column='doctoERP', max_length=20)
    picking = models.CharField(max_length=20)
    numpedido = models.CharField(max_length=50)
    fechaplaneacion = models.DateTimeField(blank=True, null=True)
    fechapedido = models.DateTimeField(blank=True, null=True)
    item = models.CharField(max_length=50)
    fecharegistro = models.DateTimeField(blank=True, null=True)
    bodega = models.CharField(max_length=50, blank=True, null=True)
    estadodetransferencia = models.IntegerField(blank=True, null=True)
    fechatransferencia = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    cantidad = models.IntegerField()
    unidadempaque = models.CharField(max_length=20, blank=True, null=True)
    cantidadempaque = models.IntegerField()
    # Field name made lowercase.
    productoean = models.CharField(db_column='productoEAN', max_length=50)
    referencia = models.CharField(max_length=50, blank=True, null=True)
    item_art = models.CharField(max_length=50, blank=True, null=True)
    # Field name made lowercase.
    numet = models.IntegerField(db_column='NumEt', blank=True, null=True)
    # Field name made lowercase.
    resto = models.IntegerField(db_column='Resto', blank=True, null=True)
    # Field name made lowercase.
    opextendida = models.CharField(
        db_column='opExtendida', max_length=61, blank=True, null=True)
    # Field name made lowercase.
    planificador = models.CharField(
        db_column='PLANIFICADOR', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    nit = models.CharField(db_column='Nit', max_length=50)
    estadoerp = models.CharField(max_length=20, blank=True, null=True)
    unido = models.CharField(max_length=61, blank=True, null=True)
    pedproveedor = models.CharField(max_length=50, blank=True, null=True)
    loteproveedor = models.CharField(max_length=50, blank=True, null=True)
    ord_no = models.CharField(max_length=50, blank=True, null=True)
    fechavence = models.DateTimeField(blank=True, null=True)
    # id     = models.IntegerField(primary_key=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'V_WMS_EPN'
