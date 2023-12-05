from django.db import models
from wmsAdapter.models import *

class TdaWmsDuk(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    referencia = models.CharField(max_length=50, blank=True, null=True)
    refpadre = models.CharField(db_column='refPadre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=180, blank=True, null=True)
    qtypedido = models.DecimalField(db_column='qtyPedido', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qtyreservado = models.DecimalField(db_column='qtyReservado', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    # productoean = models.ForeignKey(TdaWmsArt, models.DO_NOTHING, db_column='productoEAN')  # Field name made lowercase.
    productoean = models.CharField(db_column='productoEAN',max_length=50 )  # Field name made lowercase.
    lineaidpicking = models.IntegerField(db_column='lineaIdPicking', blank=True, null=True)  # Field name made lowercase.
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


    def create_return_line(self, database, qtyenpicking, estadodetransferencia, date): 
        new_instance = TdaWmsDuk.objects.using(database).create(
            referencia=self.referencia,
            refpadre=self.refpadre,
            descripcion=self.descripcion,
            qtypedido=self.qtypedido,
            qtyreservado=self.qtyreservado,
            productoean=self.productoean,
            lineaidpicking=self.lineaidpicking,
            costo=self.costo,
            bodega=self.bodega,
            tipodocto=self.tipodocto,
            doctoerp=self.doctoerp,
            qtyenpicking=qtyenpicking,
            estadodetransferencia=estadodetransferencia,
            fecharegistro=date,
            ubicacion=self.ubicacion,
            numdocumento=self.numdocumento,
            item=self.item,
            ubicacion_sale=self.ubicacion_sale,
            origen=self.origen,
            caja_destino=self.caja_destino,
            fechaestadoalmdirigido=self.fechaestadoalmdirigido,
            unido=self.unido,
            etd=self.etd,
            eta=self.eta,
            pedproveedor=self.pedproveedor,
            ord_no=self.ord_no,
            loteproveedor=self.loteproveedor,
            codigoarticulo=self.codigoarticulo,
            cantidadempaque=self.cantidadempaque,
            f_ultima_actualizacion=date

        )
        return new_instance

