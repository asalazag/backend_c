from BackendApp.functions.mongo.plantillas.get_plantillas import get_plantillas
from wmsAdapter.functions import *
from wmsAdapter.models import *
from datetime import datetime
import time
from django.db.models import Q
# This function is used to create registers in ADAPTER from a template configured in mongo


def get_last_lineaidpicking(db_name):
    db_adapter = db_name + '_adapter'
    try:
        linea_id = TdaWmsDpk.objects.using(db_adapter).last().lineaidpicking
    except:
        linea_id = 1

    return linea_id

def create_from_plantilla(db_name, table, plantilla, data):

    plantilla_to_use = plantilla

    # Get the fields from the plantilla in mongo
    mongo_fields = get_plantillas(db_name, table, plantilla)

    # print(mongo_fields)

    line_id = get_last_lineaidpicking(db_name)

    try:

        # final array to return
        final_fields = []

        # Loop through the data
        for plantilla in data:
            # Create a new line for each row
            line = {}


            # Loop through the fields from the plantilla in mongo
            for p in mongo_fields:
                # print(p)
                # print(line)

                # If the field is not empty and the field exists in the data
                if p['campo_origen'] != '' and p['campo_origen'] in plantilla:
                    # Add the field to the line with name Campo_destino and value Campo_origen in the data+
                    line[str(p['campo_destino'])
                         ] = plantilla[p['campo_origen']]
                else:
                    # If the field is empty or the field does not exist in the data, add the default value
                    if p['campo_destino'] == 'lineaidpicking' and p['default'] == None:

                        line_id += 1
                        line[str(p['campo_destino'])] = int(line_id)

                    elif p['default']:

                        if p['default'][0] == '$' and p['default'][-1] == '$':
                            try:

                                db_adapter = db_name + '_adapter'

                                query = p['default'][1:-1]
                                line[str(p['campo_destino'])] = eval(query)
                            except Exception as e:
                                print("Error processing default value:", p['default'])
                                line[str(p['campo_destino'])] = None
                        else:
                            line[str(p['campo_destino'])] = p['default']

                    else:
                        line[str(p['campo_destino'])] = p['default']

            # Add the line to the final array
            final_fields.append(line)
    except Exception as e:
        print()
        print("-------------------------------------")
        print(e)
    # Array to store the concatenated fields required to be created

    unique_records = []  # Contains the final records to be created
    unique_fields = []  # doctoerp, tipodocto y numdocumento si es euk

    # Filter repeted records for EPK, EPN and EUK
    if str(table) == 'EUK':
        for f in final_fields:
            if (str(f['tipodocto']) + str(f['doctoerp']) + str(f['numdocumento'])) not in unique_fields:
                unique_fields.append(
                    str(f['tipodocto']) + str(f['doctoerp']) + str(f['numdocumento']))
                unique_records.append(f)

    elif str(table) == 'EPK':
        for f in final_fields:
            if (str(f['tipodocto']) + str(f['doctoerp']) + str(f['numpedido'])) not in unique_fields:
                unique_fields.append(
                    str(f['tipodocto']) + str(f['doctoerp']) + str(f['numpedido']))
                unique_records.append(f)

    elif str(table) == 'EPN':
        for f in final_fields:
            if (str(f['tipodocto']) + str(f['doctoerp']) + str(f['numdocumento'])) not in unique_fields:
                unique_fields.append(
                    str(f['tipodocto']) + str(f['doctoerp']) + str(f['numdocumento']))
                unique_records.append(f)

    else:
        unique_records = final_fields


    try:
        db_adapter = db_name + '_adapter'

        response = {}
        lines = []
        error = []
        log = []

        print('Creating records in ' + str(table))
        # print(unique_records)   
        if str(table) == 'ART':
            for f in unique_records:
                art = TdaWmsArt.objects.using(db_adapter).filter(
                    productoean=f['productoean'])
                if art:
                    print('ART already exists')
                    f['error'] = 'ART already exists'
                    error.append(f)
                    log.append('ART already exists')
                    continue
                lines.append(f)
                r = create_articles(None, db_adapter, f)
                if r != 'created successfully':
                    # print(r)
                    f['error'] = str(r)
                    error.append(f)
                    log.append(r)

        if str(table) == 'CLT':
            for f in unique_records:
                art = TdaWmsClt.objects.using(db_adapter).filter(
                    item=f['item'])
                if art:
                    print('CLT already exists')
                    f['error'] = 'CLT already exists'
                    error.append(f)
                    log.append('CLT already exists')
                    continue
                lines.append(f)
                r = create_clt(None, db_adapter, f)
                if r != 'created successfully':
                    # print(r)
                    f['error'] = str(r)
                    error.append(f)
                    log.append(r)

        if str(table) == 'PRV':
            for f in unique_records:
                art = TdaWmsPrv.objects.using(db_adapter).filter(
                    item=f['item'])
                if art:
                    print('PRV already exists')
                    f['error'] = 'PRV already exists'
                    error.append(f)
                    log.append('PRV already exists')
                    continue
                lines.append(f)
                r = create_prv(None, db_adapter, f)
                if r != 'created successfully':
                    # print(r)
                    f['error'] = str(r)
                    error.append(f)
                    log.append(r)

        if str(table) == 'EPK':
            for f in unique_records:
                epk = TdaWmsEpk.objects.using(db_adapter).filter(
                    doctoerp=f['doctoerp'], tipodocto=f['tipodocto'], numpedido=f['numpedido'])
                if epk:
                    print('EPK already exists')
                    error.append(f)
                    f['error'] = 'EPK already exists'
                    log.append('EPK already exists')
                    continue
                lines.append(f)
                r = create_epk(None, db_adapter, f)
                if r != 'created successfully':
                    # print(r)
                    f['error'] = str(r)
                    error.append(f)
                    log.append(r)

        if str(table) == 'EUK':
            for f in unique_records:
                euk = TdaWmsEuk.objects.using(db_adapter).filter(
                    doctoerp=f['doctoerp'], tipodocto=f['tipodocto'], numdocumento=f['numdocumento'])
                if len(euk) > 0:
                    print('EUK already exists')

                    if plantilla_to_use == 'WEB':
                        continue

                    error.append(f)
                    f['error'] = 'EUK already exists'
                    log.append('EUK already exists')
                    continue
                lines.append(f)
                r = create_euk(None, db_adapter, f)
                if r != 'created successfully':
                    # print(r)
                    f['error'] = str(r)
                    error.append(f)
                    log.append(r)

        if str(table) == 'DPK':
            for f in unique_records:
                lines.append(f)
                r = create_dpk(None, db_adapter, f)
                if r != 'created successfully':
                    # print(r)
                    f['error'] = str(r)
                    error.append(f)
                    log.append(r)

        if str(table) == 'DUK':

            if plantilla_to_use == 'WEB':
                for f in unique_records:
                    print (f)
                    lines.append(f)
                    if f['lineaidpicking']:
                        duk = TdaWmsDuk.objects.using(db_adapter).filter(
                            lineaidpicking = f['lineaidpicking'])

                    # duk = TdaWmsDuk.objects.using(db_adapter).filter(
                    #     doctoerp=f['doctoerp'], tipodocto=f['tipodocto'], numdocumento=f['numdocumento'], productoean=f['productoean'], bodega= f['bodega']) 
                                    
                    if len(duk) > 0:
                        duk = duk[0]
                        duk.qtypedido = f['qtypedido']
                        duk.qtyreservado = f['qtyreservado']
                        duk.costo = f['costo']
                        duk.save(using = db_adapter)

                        try:
                            art = TdaWmsArt.objects.using(db_adapter).get(productoean=f['productoean'])
                            print(art)
                            if float(f['qtypedido']) > 0:
                                art.preciounitario = float(float(f['costo']) / float(f['qtypedido']))
                                art.save(using = db_adapter)

                        except Exception as e:
                            f['error'] = str(e)
                            error.append(f)
                            log.append(e)

                        continue
                    else:
                        r = create_duk(None, db_adapter, f)
                        if r != 'created successfully':
                            # print(r)
                            f['error'] = str(r)
                            error.append(f)
                            log.append(r)

            else:
                for f in unique_records:
                    lines.append(f)

                    duk = TdaWmsDuk.objects.using(db_adapter).filter(
                        doctoerp=f['doctoerp'], tipodocto=f['tipodocto'], numdocumento=f['numdocumento'], productoean=f['productoean'], bodega= f['bodega'], qtypedido = f['qtypedido'])
                    
                    if duk:
                        error.append(f)
                        f['error'] = 'DUK already exists'
                        log.append('DUK already exists')
                        continue
                    else:
                        r = create_duk(None, db_adapter, f)
                        if r != 'created successfully':
                            # print(r)
                            f['error'] = str(r)
                            error.append(f)
                            log.append(r)

        if str(table) == 'SERIALES':
            for f in unique_records:
                lines.append(f)
                r = create_seriales(None, db_adapter, f)
                if r != 'created successfully':
                    # print(r)
                    f['error'] = str(r)
                    error.append(f)
                    log.append(r)

        response['lines'] = lines
        response['error'] = error
        response['log'] = log

    except Exception as e:
        print(e)

    return response
