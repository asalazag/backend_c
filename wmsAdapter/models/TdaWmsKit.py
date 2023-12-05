# from django.db import models

# class TdaWmsKit(models.Model):
#     productoEAN_pack= models.CharField(max_length=50, blank=True, null=True)
#     Descripcion_pack= models.CharField(max_length=500, blank=True, null=True)
#     productoEAN_product= models.CharField(max_length=50, blank=True, null=True)
#     Descripcion_product= models.CharField(max_length=500, blank=True, null=True)
#     Cantidad= models.DecimalField(max_digits=14, decimal_places=3, blank=True, null=True)
#     bodega= models.CharField(max_length=20, blank=True, null=True)
#     proveedor= models.CharField(max_length=50, blank=True, null=True)
#     estado = models.IntegerField(blank=True, null=True)
#     fechaRegistro= models.DateTimeField(blank=True, null=True)
#    # id = models.AutoField()

#     class Meta:
#         managed = False
#         db_table = 'TDA_WMS_KIT'
#         unique_together = (('productoEAN_pack', 'productoEAN_product', 'bodega'),)

from django.db import models


class TdaWmsKit(models.Model):
    # id = models.AutoField()
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    productoean_pack = models.TextField(db_column='productoEAN_pack')  # Field name made lowercase.
    # productoean_pack = models.ForeignKey('TdaWmsArt', models.DO_NOTHING, db_column='productoEAN_pack')  # Field name made lowercase.
    descripcion_pack = models.TextField(db_column='Descripcion_pack', blank=True, null=True)  # Field name made lowercase.
    # productoean_product = models.ForeignKey('TdaWmsArt', models.DO_NOTHING, db_column='productoEAN_product')  # Field name made lowercase.
    productoean_product = models.TextField(db_column='productoEAN_product')  # Field name made lowercase.
    descripcion_product = models.TextField(db_column='Descripcion_product', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=14, decimal_places=3)  # Field name made lowercase.
    bodega = models.CharField(max_length=20, blank=True, null=True)
    proveedor = models.CharField(max_length=50, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tda_wms_kit'
