# from django.db import models
# from siesa.models import *

# class T200MmTerceros(models.Model):
#     f200_id_cia = models.ForeignKey('T203MmTipoIdent', models.DO_NOTHING, db_column='f200_id_cia')
#     f200_rowid = models.AutoField(primary_key=True)
#     f200_id = models.CharField(max_length=15)
#     f200_nit = models.CharField(max_length=25, blank=True, null=True)
#     f200_dv_nit = models.CharField(max_length=3, blank=True, null=True)
#     f200_id_tipo_ident = models.ForeignKey('T203MmTipoIdent', models.DO_NOTHING, db_column='f200_id_tipo_ident', blank=True, null=True)
#     f200_ind_tipo_tercero = models.SmallIntegerField()
#     f200_razon_social = models.CharField(max_length=100)
#     f200_apellido1 = models.CharField(max_length=30)
#     f200_apellido2 = models.CharField(max_length=30)
#     f200_nombres = models.CharField(max_length=40)
#     f200_rowid_contacto = models.ForeignKey(T015MmContactos, models.DO_NOTHING, db_column='f200_rowid_contacto', blank=True, null=True)
#     f200_ind_cliente = models.SmallIntegerField()
#     f200_ind_proveedor = models.SmallIntegerField()
#     f200_ind_empleado = models.SmallIntegerField()
#     f200_ind_accionista = models.SmallIntegerField()
#     f200_ind_otros = models.SmallIntegerField()
#     f200_ind_interno = models.SmallIntegerField()
#     f200_nombre_est = models.CharField(max_length=100)
#     f200_fecha_nacimiento = models.DateTimeField()
#     f200_id_ciiu = models.ForeignKey('T224MmCiiu', models.DO_NOTHING, db_column='f200_id_ciiu', blank=True, null=True)
#     f200_rowid_movto_entidad = models.IntegerField(blank=True, null=True)
#     f200_ind_estado = models.SmallIntegerField()
#     f200_rowid_foto = models.ForeignKey('T580FfFotos', models.DO_NOTHING, db_column='f200_rowid_foto', blank=True, null=True)
#     f200_ind_no_domiciliado = models.SmallIntegerField()
#     f200_ts = models.DateTimeField()
#     f200_ind_gum_unificado = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 't200_mm_terceros'
#         unique_together = (('f200_id_cia', 'f200_id'),)