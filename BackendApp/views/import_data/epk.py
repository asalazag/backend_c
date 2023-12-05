from settings.models.config import config
from wmsAdapter.models import *
from wmsAdapter.functions import *


def epk_to_wms(database, plantilla, body, tipoDocto):
    try:
        c = config(database, 'csv_import')
        epk_config = c.get_config()
        epk_config = epk_config['csv_import'][str(plantilla)]

        array_data = []

        for b in body:
            final_obj = {}
            final_obj["tipodocto"] = tipoDocto

            for c in epk_config:
                if c["field"] in b:
                    final_obj[c["WMSName"]] = b[c["field"]]

            array_data.append(final_obj)

        array_pedidos = []
        array_epk = []
        for a in array_data:
            if a["doctoerp"] not in array_pedidos:
                array_pedidos.append(a["doctoerp"])
                array_epk.append(a)

        for register in array_epk:
            try:
                e = {}
                if plantilla == 'SAK':
                    database_adapter = database + '_adapter'
                    # Para SAK, el cliente es siempre el mismo MABE
                    try:
                        cliente = TdaWmsClt.objects.using(
                            database_adapter).get(item='179-001')
                    except Exception as err:
                        print(err)
                        return str(err.__cause__).lower()

                    try:
                        e['numpedido'] = register['doctoerp']
                        e['tipodocto'] = register['tipodocto']
                        e['doctoerp'] = register['doctoerp']
                        e['item'] = cliente.item
                        e['nombrecliente'] = cliente.nombrecliente
                        e['contacto'] = cliente.contacto
                        e['email'] = cliente.email
                        e['ciudad_despacho'] = cliente.cuidaddespacho
                        e['pais_despacho'] = cliente.paisdespacho
                        e['departamento_despacho'] = cliente.departamentodespacho
                        e['sucursal_despacho'] = cliente.sucursaldespacho
                        e['direccion_despacho'] = cliente.direccion
                        e['idsucursal'] = cliente.idsucursal
                        e['ciudad'] = cliente.ciudaddestino
                        e['pedidorelacionado'] = str(
                            register['tipodocto']) + str(register['doctoerp'])
                        e['nit'] = cliente.nit
                        e['estadopicking'] = 0
                        e['centrooperacion'] = '121'
                        e['estadoerp'] = '1'
                        e['field_condicionpago'] = cliente.condicionescompra
                        e['field_documentoreferencia'] = '5200004328'

                        try:
                            t = TdaWmsEpk.objects.using(database_adapter).get(
                                tipodocto=e['tipodocto'], doctoerp=e['doctoerp'], item=e['item'], numpedido=e['numpedido'])
                            return 'El pedido ya existe'
                        except:
                            pass

                    except Exception as e:
                        print(e)
                        return str(e.__cause__).lower()

                    r = create_epk(None, database_adapter, e)

                    if r == 'created successfully':
                        try:
                            epk = TdaWmsEpk.objects.using(database_adapter).get(
                                tipodocto=e['tipodocto'], doctoerp=e['doctoerp'], item=e['item'], numpedido=e['numpedido'])

                            last = TdaWmsDpk.objects.using(
                                database_adapter).last()
                            last_id = last.lineaidpicking
                            for a in array_data:
                                if str(a['doctoerp']) == str(epk.doctoerp) and str(a['tipodocto']) == str(epk.tipodocto):
                                    # if a['doctoerp'] == epk.doctoerp and a['tipodocto'] == 'MBE':
                                    try:
                                        art = TdaWmsArt.objects.using(database_adapter).get(
                                            referencia=a['referencia'])
                                        a['referencia'] = art.referencia
                                        a['refpadre'] = art.referencia
                                        a['descripcion'] = art.descripcion
                                        a['qtyreservado'] = a['qtypedido']
                                        a['productoean'] = art.productoean
                                        a['picking'] = epk.picking
                                        a['lineaidpicking'] = last_id
                                        a['numpedido'] = epk.numpedido
                                        a['item'] = epk.item
                                        a['bodega'] = '12101'
                                        a['qtyenpicking'] = 0
                                        a['estadodetransferencia'] = 0
                                        a['serial'] = 0
                                        a['idco'] = '121'
                                        a['qtyremisionado'] = 0
                                        a['qtyfacturado'] = 0
                                        a['preciounitario'] = art.costo
                                        a['notasitem'] = a['notas'] if 'notas' in a else ''
                                        a['descripcionco'] = epk.centrooperacion
                                        a['factor'] = 1
                                        a['field_qtypedidabase'] = a['qtypedido']

                                        if 'notas' in a:
                                            a.pop('notas')

                                        last_id += 1

                                        r = create_dpk(
                                            None, database_adapter, a)

                                        # print(a['referencia'])
                                        print(r)

                                    except Exception as err:
                                        print(
                                            '#######################################')
                                        print(a)
                                        print(
                                            '#######################################')
                                        # print(a['referencia'])
                                        print(err)
                                        continue
                                        # return str(e.__cause__).lower()

                        except Exception as err:
                            print(err)
                            return str(err.__cause__).lower()
                        continue
                    else:
                        return str(r)

            except Exception as err:
                print(err)
                return str(err.__cause__).lower()

        return 'created successfully'
    except Exception as err:
        print(err)
        return str(err.__cause__).lower()
