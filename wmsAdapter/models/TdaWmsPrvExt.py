from django.db import models
from wmsAdapter.models import *

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