from django.db import models


class T122McItemsUnidades(models.Model):
    f122_ts = models.DateTimeField()
    f122_id_cia = models.SmallIntegerField()
    # f122_id_cia = models.ForeignKey(
    #     T101McUnidadesMedida, models.DO_NOTHING, db_column='f122_id_cia')
    f122_rowid_item = models.ImageField(primary_key=True)
    # f122_rowid_item = models.OneToOneField(
    #     T120McItems, models.DO_NOTHING, db_column='f122_rowid_item', primary_key=True)
    f122_id_unidad = models.CharField(max_length=4)
    # f122_id_unidad = models.ForeignKey(
    #     T101McUnidadesMedida, models.DO_NOTHING, db_column='f122_id_unidad')
    f122_factor = models.DecimalField(max_digits=28, decimal_places=4)
    f122_peso = models.DecimalField(max_digits=28, decimal_places=4)
    f122_volumen = models.DecimalField(max_digits=28, decimal_places=4)

    class Meta:
        managed = False
        db_table = 't122_mc_items_unidades'
        unique_together = (
            ('f122_rowid_item', 'f122_id_unidad', 'f122_id_cia', 'f122_id_cia'),)
