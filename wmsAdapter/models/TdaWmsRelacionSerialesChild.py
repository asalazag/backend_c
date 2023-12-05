# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TdaWmsRelacionSerialesChild(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    com = models.CharField(db_column='Com', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ein = models.CharField(db_column='EIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hq_do = models.CharField(db_column='HQ_Do', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hq_do_item = models.CharField(db_column='HQ_Do_Item', max_length=255, blank=True, null=True)  # Field name made lowercase.
    plant = models.CharField(db_column='Plant', max_length=255, blank=True, null=True)  # Field name made lowercase.
    basic = models.CharField(db_column='Basic', max_length=255, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subsidiary_po = models.CharField(db_column='Subsidiary_PO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subsidiary_po_item = models.CharField(db_column='Subsidiary_PO_Item', max_length=255, blank=True, null=True)  # Field name made lowercase.
    export_date = models.CharField(db_column='Export_Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
    goods_status = models.CharField(db_column='Goods_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    carton = models.CharField(db_column='Carton', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pallet = models.CharField(db_column='Pallet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    production_date = models.CharField(db_column='Production_Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lot_number = models.CharField(db_column='Lot_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    software_version = models.CharField(db_column='Software_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sim_sku = models.CharField(db_column='SIM_SKU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sim_esn = models.CharField(db_column='SIM_ESN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sim_serial = models.CharField(db_column='SIM_Serial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone_lock_code = models.CharField(db_column='Phone_Lock_Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eid = models.CharField(db_column='EID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    akey = models.CharField(db_column='AKey', max_length=255, blank=True, null=True)  # Field name made lowercase.
    decimal_esn = models.CharField(db_column='Decimal_ESN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imsi_for_cdma = models.CharField(db_column='IMSI_for_CDMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    one_time_keypad_subsidy_lock = models.CharField(db_column='One_Time_Keypad_Subsidy_Lock', max_length=255, blank=True, null=True)  # Field name made lowercase.
    master_subsidy_lock = models.CharField(db_column='Master_Subsidy_Lock', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sha_random_code = models.CharField(db_column='SHA_Random_Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imei_for_world_phone_model = models.CharField(db_column='IMEI_for_World_Phone_Model', max_length=255, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dual_imei_no = models.CharField(db_column='Dual_IMEI_No', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prl_version = models.CharField(db_column='PRL_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.
    serial_no = models.CharField(db_column='Serial_No', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone_no = models.CharField(db_column='Phone_No', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nck = models.CharField(db_column='NCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mck = models.CharField(db_column='MCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sck_1 = models.CharField(db_column='SCK_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    spck = models.CharField(db_column='SPCK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='Created_by', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_on = models.CharField(db_column='Created_on', max_length=255, blank=True, null=True)  # Field name made lowercase.
    changed_by = models.CharField(db_column='Changed_by', max_length=255, blank=True, null=True)  # Field name made lowercase.
    changed_on = models.CharField(db_column='Changed_on', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sha_code = models.CharField(db_column='SHA_Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDA_WMS_RELACION_SERIALES_CHILD'
