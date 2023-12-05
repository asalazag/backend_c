#from asyncio.windows_events import NULL
from itertools import product
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ...utils import *
from datetime import datetime
import requests
import json
import xmltodict
from zeep import Client, Settings, xsd
from bs4 import BeautifulSoup as bs
from hashlib import sha256


@csrf_exempt
def crearguiacoordinadora(request):

    request_data = request._body
    database = request_data['database']

    if request.method == 'POST':

        transportadora = request_data["transportadora"] if "transportadora" in request_data else None
        codigocuentacliente = request_data["codigocuentacliente"] if "codigocuentacliente" in request_data else None
        datosguia = request_data["datosguia"] if "datosguia" in request_data else {
        }

        # Obtenemos las credenciales de la transportadora
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_obtenerDatosTranportadora] %s, %s'''

        # Query que se hace directamente a la base de datos
        try:
            data_transportadora = exec_query(
                sp, (transportadora, codigocuentacliente,), database=database)
            usuario = data_transportadora[0]['u']
            clave = data_transportadora[0]['c2']
            trasnportador_nit = data_transportadora[0]['n']
            clave_guias = sha256(clave.encode('utf-8')).hexdigest()

            print(data_transportadora)
            # Extraemos los datos de datos guia para traer el detalle
            picking = datosguia['picking'] if 'picking' in datosguia else None
            bigpedido = datosguia['tipoDocto'] + '-' + \
                datosguia['doctoERP'] if 'tipoDocto' in datosguia and 'doctoERP' in datosguia else None

            sp = ''' SET NOCOUNT ON
                EXEC [web].[awg_obtenerDataparaGuiaTte] %s , %s  '''

            # traemos el detalle de tte
            try:
                detalle_tte = exec_query(
                    sp, (picking, bigpedido), database=database)

                print(detalle_tte)
                print('Detalle TTE-------------------------------')
                if len(detalle_tte) > 0:

                    # url del wsdl
                    wsdl = 'https://sandbox.coordinadora.com/agw/ws/guias/1.6/server.php?wsdl'

                    # Creamos el cliente
                    settings = Settings(
                        strict=False, xml_huge_tree=True, raw_response=True)
                    client = Client(wsdl=wsdl, settings=settings)

                    # Creamos el objeto de detalle
                    objeto_detalle = client.get_type(
                        'ns0:Agw_typeGuiaDetalle')

                    # Creamos el objeto de generar guia
                    objeto_generar_guia = client.get_type(
                        'ns0:Agw_typeGenerarGuiaIn')

                    detalle = []
                    # Recorremos el detalle para crear el objeto de detalle
                    for item in detalle_tte:
                        d = objeto_detalle(ubl=0, alto=float(item["alto"]), ancho=float(item["ancho"]), largo=float(item["largo"]), peso=float(item["peso"]), unidades=int(item["unidades"]),
                                           referencia=str(item["referencia_empaque"]), nombre_empaque=str(item["nombreEmpaque"]))
                        detalle.append(d)

                    # Tomamos el primer item del detalle para traer los datos de la guia
                    encabezado = detalle_tte[0]
                    obj = objeto_generar_guia(codigo_remision="", fecha=str(datetime.today().strftime('%Y-%m-%d')), id_cliente=codigocuentacliente,
                                              id_remitente=0, nit_remitente=trasnportador_nit, nombre_remitente=encabezado["nombre_remitente"],
                                              direccion_remitente=encabezado[
                                                  "direccion_remitente"], telefono_remitente=encabezado["telefono_remitente"],
                                              ciudad_remitente=encabezado["cod_ciudadRemitente"], nit_destinatario=encabezado[
                                                  "identificacionDestinatario"],
                                              div_destinatario="1", nombre_destinatario=encabezado["nombreDestinataro"], direccion_destinatario=encabezado["dirDestinatario"],
                                              ciudad_destinatario=encabezado[
                                                  "codCiudadDestinatario"], telefono_destinatario=encabezado["telefono_remitente"],
                                              valor_declarado=float(
                                                  encabezado["valorDeclarado"]),
                                              codigo_cuenta=int(1), codigo_producto=int(0), nivel_servicio=int(1),
                                              linea="", contenido=encabezado["nombreEmpaque"], referencia=encabezado["referencia_empaque"],
                                              observaciones=encabezado["notas"], estado="PENDIENTE",
                                              detalle=detalle,
                                              cuenta_contable="", centro_costos="", recaudos=xsd.SkipValue, margen_izquierdo=float(0),
                                              margen_superior=float(0), usuario_vmi="", formato_impresion="", atributo1_nombre="",
                                              atributo1_valor="", notificaciones=xsd.SkipValue, atributos_retorno=xsd.SkipValue, nro_doc_radicados="",
                                              nro_sobre="", codigo_vendedor="", usuario=usuario, clave=clave_guias)

                    print(obj)
                    # Generamos la guia
                    print(obj)
                    xml = client.service.Guias_generarGuia(obj)
                    print(xml.text)
                    data_dict = xmltodict.parse(xml.text)
                    response = json.dumps(data_dict)
                    response_json = json.loads(response)
                    # response_json = response_json["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]["ns1:Guias_generarGuiaResponse"]["return"]
                    return JsonResponse(response_json, safe=False, status=200)

            except Exception as e:
                print(e)
                return JsonResponse('Server Error!', safe=False, status=500)
        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)
