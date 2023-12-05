from settings.models.config import config
from wmsAdapter.models import *
from wmsAdapter.functions import *


def prv_to_wms(database, plantilla, body, tipoDocto):
    try:
        c = config(database, 'csv_import')
        prv_config = c.get_config()
        prv_config = prv_config['csv_import'][str(plantilla)]

        array_data = []

        for b in body:
            final_obj = {}
            final_obj["tipodocto"] = tipoDocto

            for c in prv_config:
                if c["campo_origen"] in b:
                    final_obj[c["campo_destino"]] = b[c["campo_origen"]]
                else:
                    final_obj[c["campo_destino"]] = c[c["default"]]

            array_data.append(final_obj)

        array_pedidos = []
        array_prv = []
        for a in array_data:
            if a["doctoerp"] not in array_pedidos:
                array_pedidos.append(a["doctoerp"])
                array_prv.append(a)

        for register in array_prv:
            try:
                e = {}
                if plantilla == 'WC22_1':
                    database_adapter = database + '_adapter'
                    try:
                        cliente = TdaWmsClt.objects.using(
                            database_adapter).get(item='179-001')
                    except Exception as err:
                        print(err)
                        return str(err.__cause__).lower()

                    try:
                        e['nit'] = cliente.nit
                        e['nombrecliente'] = cliente.nombrecliente
                        e['direccion'] = cliente.direccion
                        e['is_activo_proveedor'] = 1
                        e['condiciones_compra'] = register['condiciones_compra']
                        e['codigo_pais'] = '0001'
                        e['moneda_de_facturacion'] = 'USD'
                        e['item'] = str(register['region']) + str(register['district'])
                        e['activo_cliente'] = 1
                        e['fecha_registro'] = "2020-01-11"
                        e["estado_tranferencia"] = 0
                        e["sucursal"] = cliente.sucursal
                        e["email"] = cliente.email
                        e["beneficiario"] = cliente.beneficiario
                        e["item_sucursal"] = cliente.item
                        e["codidigo_ter"] = cliente.codigo_ter
                        e["id"] = cliente.id

                        try:
                            t = TdaWmsPrv.objects.using(database_adapter).get(
                                tipodocto=e['tipodocto'], doctoerp=e['doctoerp'], item=e['item'], numpedido=e['numpedido'])
                            return 'El pedido ya existe'
                        except:
                            pass

                    except Exception as e:
                        print(e)
                        return str(e.__cause__).lower()
                    
                    print(e)


                    #r = create_prv(None, database_adapter, e)

                    # if r == 'created successfully':
                    #     try:
                    #         print(r)

                    #     except Exception as err:
                    #         print(err)
                    #         return str(err.__cause__).lower()
                    #     continue
                    # else:
                    #     return str(r)

            except Exception as err:
                print(err)
                return str(err.__cause__).lower()

        return 'created successfully'
    except Exception as err:
        print(err)
        return str(err.__cause__).lower()
