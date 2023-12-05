from django.db import models


class TdaWmsLogWeb(models.Model):
    url_endpoint = models.TextField(blank=True, null=True)
    valor = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tda_wms_log_web'
