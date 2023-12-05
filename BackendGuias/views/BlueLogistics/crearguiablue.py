#from asyncio.windows_events import NULL
from urllib.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ...utils import *
import requests
import json
import xmltodict

url = "http://testsolex.blulogistics.net/solexPRE/services/webservicesolex.asmx"


@csrf_exempt
def crearguiablue(request):

    request_data = request._body
    print(request_data)
    database = request_data['database']

#  CONSULTAR LAS CREDENCIALES DE LA TRANSPORTADORA
    if request.method == 'POST':

        transportadora = request_data["transportadora"] if "transportadora" in request_data else None
        codigocuentacliente = request_data["codigocuentacliente"] if "codigocuentacliente" in request_data else None
        datosguia = request_data["datosguia"] if "datosguia" in request_data else {
        }

        response = []
        sp = ''' SET NOCOUNT ON
             EXEC [web].[usp_obtenerDatosTranportadora] %s, %s'''
         
        # Query que se hace directamente a la base de datos
        try:
            response = exec_query(
                sp, (transportadora, codigocuentacliente,), database=database)

            print(response)
            usuario = response[0]['u']
            clave = response[0]['c2']

            payload = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CrearGuiaBlulogisticsV2 xmlns="http://tempuri.org/">
                    <user>{usuario}</user>
                    <password>{clave}</password>
                    <guia>
                        <DestinatarioIdentificacion>{str(datosguia["identificacionDestinatario"])}</DestinatarioIdentificacion>
                        <DestinatarioNombre>{str(datosguia["nombreDestinataro"])}</DestinatarioNombre>
                        <DestinatarioDireccion>{str(datosguia["dirDestinatario"])}</DestinatarioDireccion>
                        <DestinatarioTelefono>{str(datosguia["telefono_remitente"])}</DestinatarioTelefono>
                        <CiudadOrigen>{str(datosguia["cod_ciudadRemitente"])}</CiudadOrigen>
                        <CiudadDestino>{str(datosguia["codCiudadDestinatario"])}</CiudadDestino>
                        <Observacion>{str(datosguia["notas"])}</Observacion>
                        <Kilos>{int(float(datosguia["peso"]))}</Kilos>
                        <ValorDeclarado>{int(float(datosguia["valorDeclarado"]))}</ValorDeclarado>
                        <Cantidad>{int(float(datosguia["unidades"]))}</Cantidad>
                        <IdCuentaCliente>{int(datosguia["codigoCuentaAcuerdo"])}</IdCuentaCliente>
                        <DocumentoExterno>{str(datosguia["docRelacionado"])}</DocumentoExterno>
                        <Correo>{str(datosguia["email"])}</Correo>
                        <ValorRecaudo>0</ValorRecaudo>
                    </guia>
                    </CrearGuiaBlulogisticsV2>
                </soap:Body>
                </soap:Envelope>"""
            headers = {
                'Content-Type': 'text/xml; charset=utf-8',
                'Content-Length': 'length',
                'SOAPAction': 'http://tempuri.org/CrearGuiaBlulogisticsV2'
            }
            # POST request
            response_bl = requests.request(
                "POST", url, headers=headers, data=payload)

            data_dict = xmltodict.parse(response_bl.text)
            response_bl = json.dumps(data_dict)
            response_bl = json.loads(response_bl)
            response_bl = response_bl['soap:Envelope']['soap:Body'][
                'CrearGuiaBlulogisticsV2Response']['CrearGuiaBlulogisticsV2Result']['EResponseGuia']
            return JsonResponse(response_bl, safe=False, status=200)

        except Exception as e:
            print("Server Error!: ", e)
            return JsonResponse('Server Error!', safe=False, status=500)
