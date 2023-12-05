from settings.models.config import config
from wmsAdapter.models import *
from wmsAdapter.functions import *


def euk_to_wms(database, plantilla, body):
    # try:
    mongo = config(database, 'csv_import')
    c_config = mongo.get_config()
    euk_config = c_config['csv_import']['EUK']
    array_data = []

    for b in body:
        euk_object = {}
        for c in euk_config:
            euk_object[c["campo_destino"]] = b[c["campo_origen"]]
        euk_object['bodega'] = '01'
        array_data.append(euk_object)
    if plantilla == 'PANINI':
        for e in array_data:
            create_euk(None, database + '_adapter', e)
    return True
    # except Exception as err:
    #     print(err.__cause__)
    #     return str(err.__cause__).lower()


def duk_to_wms(database, plantilla, body):
    mongo = config(database, 'csv_import')
    c_config = mongo.get_config()
    duk1_config = c_config['csv_import']['DUK1']
    array_data1 = []
    for b in body:
        duk1_object = {}
        for c in duk1_config:
            duk1_object[c["campo_destino"]] = b[c["campo_origen"]]
        duk1_object['bodega'] = '01'
        array_data1.append(duk1_object)
    duk2_config = c_config['csv_import']['DUK2']
    array_data2 = []
    for b in body:
        duk2_object = {}
        for c in duk2_config:
            duk2_object[c["campo_destino"]] = b[c["campo_origen"]]
        duk2_object['bodega'] = '01'
        array_data2.append(duk2_object)
    duk3_config = c_config['csv_import']['DUK3']
    array_data3 = []
    for b in body:
        duk3_object = {}
        for c in duk3_config:
            duk3_object[c["campo_destino"]] = b[c["campo_origen"]]
        duk3_object['bodega'] = '01'
        array_data3.append(duk3_object)

    if plantilla == 'PANINI':
        for e in array_data1:
            create_duk(None, database + '_adapter', e)
        for e in array_data2:
            create_duk(None, database + '_adapter', e)
        for e in array_data3:
            create_duk(None, database + '_adapter', e)
    return True
