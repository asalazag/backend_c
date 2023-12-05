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
from settings.models.config import config
from zeep import Client, Settings, xsd
from bs4 import BeautifulSoup as bs
from hashlib import sha256
from pymongo import MongoClient

@csrf_exempt
def crearguiacoordinadora_completo(request):

    request_data = request._body
    database = request_data['database']

    if request.method == 'POST':

        transportadora = request_data["transportadora"] if "transportadora" in request_data else None
        datosguia = request_data["datosguia"] if "datosguia" in request_data else {
        }

        c = config(database, 'transportadoras')
        # Get coordinadora credentials
        usuario = c.get_config()['transportadoras'][transportadora]['usuario']
        clave = c.get_config()['transportadoras'][transportadora]['clave_guias']
        trasnportador_nit = c.get_config()['transportadoras'][transportadora]['nit']
        clave_despachos = c.get_config()['transportadoras'][transportadora]['clave_despachos']
        apikey_coordinadora =c.get_config()['transportadoras'][transportadora]['apikey']
        wsdl_1 = c.get_config()['transportadoras'][transportadora]['wsdl_1']
        wsdl_2 = c.get_config()['transportadoras'][transportadora]['wsdl_2']
        codigocuentacliente = c.get_config()['transportadoras'][transportadora]['id_cliente']
        clave_guias = sha256(clave.encode('utf-8')).hexdigest()
        
        print(codigocuentacliente,usuario, clave, trasnportador_nit, clave_despachos, apikey_coordinadora, clave_guias, wsdl_1, wsdl_2)

        # #Obtenemos las credenciales de la transportadora
        # sp = ''' SET NOCOUNT ON
        #      EXEC [web].[usp_obtenerDatosTranportadora] %s, %s'''

        # Query que se hace directamente a la base de datos
        try:
        #     data_transportadora = exec_query(
        #         sp, (transportadora, codigocuentacliente,), database=database)
        #     usuario = data_transportadora[0]['u']
        #     clave = data_transportadora[0]['c2']
        #     trasnportador_nit = data_transportadora[0]['n'].strip()
        #     clave_guias = sha256(clave.encode('utf-8')).hexdigest()
        #     apikey_coordinadora = 'b456932c-7dfc-11eb-9439-0242ac130002'
        #     clave_despachos = 'yC0nB1kJ4fP5bO5d'
            
        #     print(data_transportadora)
            
            # print(data_transportadora)
            # Extraemos los datos de datos guia para traer el detalle
            picking = datosguia['picking'] if 'picking' in datosguia else None
            bigpedido = datosguia['tipoDocto'] + '-' + \
                datosguia['doctoERP'] if 'tipoDocto' in datosguia and 'doctoERP' in datosguia else None

            sp = ''' SET NOCOUNT ON
                EXEC [web].[Agw_typeGenerarGuiaIn] %s , %s, %s '''

            
            try:
                # traemos el detalle de tte
                encabezado_tte = exec_query(
                    sp, (picking, bigpedido,0), database=database)
                # traemos el encabezado de tte
                detalle_tte = exec_query(
                    sp, (picking, bigpedido,1), database=database)

                print(detalle_tte)
                print('Detalle TTE-------------------------------')
                print(encabezado_tte)
                print('Encabezado TTE-------------------------------')
                if len(detalle_tte) > 0:

                    # Creamos el cliente
                    client = conexion_coordinadora_guia(wsdl_1)
                    
                    # Creamos el objeto de detalle
                    objeto_detalle = client.get_type('ns0:Agw_typeGuiaDetalle')

                    # Creamos el objeto de generar guia
                    objeto_generar_guia = client.get_type('ns0:Agw_typeGenerarGuiaIn')      
                    
                    
                    detalle = []
                    # Recorremos el detalle para crear el objeto de detalle
                    for item in detalle_tte:
                        d = objeto_detalle(ubl=item["ubl"], alto=str(item["alto"]), ancho=str(item["ancho"]), largo=str(item["largo"]), peso=str(item["peso"]), unidades=str(item["unidades"]),
                                           referencia=str(item["referencia"]), nombre_empaque=str(item["nombre_empaque"]))
                        detalle.append(d)

                    # Tomamos el primer item del detalle para traer los datos de la guia
                    encabezado = encabezado_tte[0]
                    obj = objeto_generar_guia(codigo_remision="", fecha=str(datetime.today().strftime('%Y-%m-%d')), id_cliente=str(codigocuentacliente),
                                              id_remitente=0, nit_remitente=trasnportador_nit, nombre_remitente=encabezado["nombre_remitente"],
                                              direccion_remitente=encabezado[
                                                  "direccion_remitente"], telefono_remitente=encabezado["telefono_remitente"],
                                              ciudad_remitente=encabezado["ciudad_remitente"], nit_destinatario=encabezado[
                                                  "nit_destinatario"],
                                              div_destinatario="1", nombre_destinatario=encabezado["nombre_destinatario"], direccion_destinatario=encabezado["direccion_destinatario"],
                                              ciudad_destinatario=encabezado[
                                                  "ciudad_destinatario"], telefono_destinatario=encabezado["telefono_remitente"],
                                              valor_declarado=str(
                                                  encabezado["valor_declarado"]),
                                              codigo_cuenta=str(1), codigo_producto=str(0), nivel_servicio=str(1),
                                              linea="", contenido=encabezado["contenido"], referencia=encabezado["referencia"],
                                              observaciones=encabezado["observaciones"], estado="IMPRESO",
                                              detalle=detalle,
                                              cuenta_contable="", centro_costos="", recaudos=xsd.SkipValue, margen_izquierdo="",
                                              margen_superior="", usuario_vmi="", formato_impresion="", atributo1_nombre="",
                                              atributo1_valor="", notificaciones=xsd.SkipValue, atributos_retorno=xsd.SkipValue, nro_doc_radicados="",
                                              nro_sobre="", codigo_vendedor="", usuario=usuario, clave=clave_guias)

                    # print(obj)
                    # Generamos la guia
                    xml = client.service.Guias_generarGuia(obj)
                    # print(xml.text)
                    data_dict = xmltodict.parse(xml.text)           
                    # response = json.dumps(data_dict)
                    # response_json = json.loads(response)
                    # Acceder a los valores dentro del diccionario
                    codigo_remision = data_dict.get('SOAP-ENV:Envelope', {}).get('SOAP-ENV:Body', {}).get('ns1:Guias_generarGuiaResponse', {}).get('return', {}).get('codigo_remision', {}).get('#text')
                    print(codigo_remision)
                    
                    if codigo_remision == None:
                        return JsonResponse('Error al generar la guia', safe=False, status=500)
                    
                    js = Rotulos_integracion(codigo_remision, apikey_coordinadora, clave_despachos,database,picking,bigpedido,wsdl_2)   
                    print (js)
                    if js == None:
                        return JsonResponse('Error al generar los rotulos', safe=False, status=500)
                    return JsonResponse(js, safe=False, status=200)

            except Exception as e:
                print(e)
                return JsonResponse('Server Error!', safe=False, status=500)
        except Exception as e:
            print(e)
            return JsonResponse('Server Error!', safe=False, status=500)

def conexion_coordinadora_guia(wsdl_1):
    # Datos para hacer la conexión al WSDL de generación de guias
    wsdl = wsdl_1
    settings = Settings(strict=False, xml_huge_tree=True, raw_response = True)
    client = Client(wsdl=wsdl, settings=settings)
    return client


def conexion_coordinadora_rotulos(wsdl_2):
   # Datos para hacer la conexión al WSDL de seguimiento de despachos
    wsdl2 = wsdl_2
    settings2 = Settings(strict=False, xml_huge_tree=True, raw_response = True)
    client2 = Client(wsdl=wsdl2, settings=settings2)
    return client2

def Rotulos_integracion(codigo_remision, APIKEY, clave_despachos,database,picking,bigpedido,wsdl_2):
    # Generamos los rotulos
    client2 = conexion_coordinadora_rotulos(wsdl_2)
    ro_inte = client2.get_type('ns0:Rotulos_integracionIn')
    rotulos_dict = {
        "codigo" : codigo_remision, # Entero
        "apikey" : APIKEY, # Float
        "clave" : clave_despachos # Float
    }
    rotulos = ro_inte(codigo = rotulos_dict['codigo'], apikey = rotulos_dict['apikey'],
                                  clave = rotulos_dict['clave'])
    xml_rotulos = client2.service.Rotulos_integracion(rotulos)
    print (xml_rotulos.text)
    # bs_content_rotulos = bs(xml_rotulos.text, "lxml")
    bs_content_rotulos = bs(xml_rotulos.text, "lxml")
    print (bs_content_rotulos)
    items = bs_content_rotulos.find_all('item')
    print (items)
    js = []
    for item in items:
        etiqueta1d = item.find("etiqueta1d").text
        etiqueta2d = item.find("etiqueta2d").text
        nombre_nivel_servicio = item.find("nombre_nivel_servicio").text
        abreviado_cuenta = item.find("abreviado_cuenta").text
        abreviado_producto = item.find("abreviado_producto").text
        codigo_terminal_origen = item.find("codigo_terminal_origen").text
        abreviado_terminal_origen = item.find("abreviado_terminal_origen").text
        codigo_terminal_destino = item.find("codigo_terminal_destino").text
        abreviado_terminal_destino = item.find("abreviado_terminal_destino").text
        zona_reparto = item.find("zona_reparto").text
        subzona_reparto = item.find("subzona_reparto").text
        referencia_detalle = item.find("referencia_detalle").text
        dict = {
            "etiqueta1d" : etiqueta1d,
            "etiqueta2d" : etiqueta2d,
            "nombre_nivel_servicio" : nombre_nivel_servicio,
            "abreviado_cuenta" : abreviado_cuenta,
            "abreviado_producto" : abreviado_producto,
            "codigo_terminal_origen" : codigo_terminal_origen,
            "abreviado_terminal_origen" : abreviado_terminal_origen,
            "codigo_terminal_destino" : codigo_terminal_destino,
            "abreviado_terminal_destino" : abreviado_terminal_destino,
            "zona_reparto" : zona_reparto,
            "subzona_reparto" : subzona_reparto,
            "referencia_detalle" : referencia_detalle
        }
        # Guardamos los datos en la base de datos
        sp = ''' SET NOCOUNT ON
                EXEC [dbo].[spi_TDA_GTTE_COO]
                @abreviado_cuenta = %s
                ,@abreviado_producto = %s
                ,@abreviado_terminal_destino = %s
                ,@abreviado_terminal_origen = %s
                ,@codigo_terminal_destino = %s
                ,@codigo_terminal_origen =  %s
                ,@etiqueta1d = %s
                ,@etiqueta2d =  %s
                ,@nombre_nivel_servicio = %s
                ,@referencia_detalle = %s
                ,@subzona_reparto = %s
                ,@zona_reparto = %s
                ,@picking = %s
                ,@numpedido = %s
        '''
        exec_query(
                    sp, (abreviado_cuenta,abreviado_producto,codigo_terminal_destino,
                         abreviado_terminal_origen,codigo_terminal_destino,codigo_terminal_origen,
                         etiqueta1d,etiqueta2d,nombre_nivel_servicio,referencia_detalle,subzona_reparto,
                         zona_reparto,picking,bigpedido), database=database)
        js.append(dict)

    return js