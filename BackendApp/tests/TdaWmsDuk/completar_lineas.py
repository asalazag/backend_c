from wmsAdapter.models import TdaWmsDuk
from random import randint
from django.utils import timezone


def completar_lineas_TdaWmsDuk(tipodocto, doctoerp, numdocumento, database):
    '''
    Este procedimiento completa lineas al azar o en su totalidad de una orden de despacho
    '''

    # Se obtiene el numero de orden de despacho

    print("Se obtiene el numero de orden de despacho")
    print(tipodocto, doctoerp, numdocumento, database)

    database = database.lower() + '_adapter'

    duk = TdaWmsDuk.objects.using(database).filter(tipodocto=tipodocto, doctoerp=doctoerp, numdocumento=numdocumento)

    lineas_base = []
    lineas_entregadas = []
    cantidades_entregadas = {}

    for d in duk:
        if d.estadodetransferencia == 0:
            lineas_base.append(d)
        else:
            lineas_entregadas.append(d)

    print("Lineas base: " + str(len(lineas_base)))

    if len(lineas_base) == 0:
        print("No se encontró el pedido")
        return {"Lineas": 0}

    # Se obtienen las lineas entregadas
    for le in lineas_entregadas:
        if le.lineaidpicking not in cantidades_entregadas:
            cantidades_entregadas[le.lineaidpicking] = 0
        cantidades_entregadas[le.lineaidpicking] += float(le.qtyenpicking)
    
    print("Lineas entregadas: " + str(len(lineas_entregadas)))


    lineas_por_entregar = []
    for lb in lineas_base:
        if lb.lineaidpicking not in cantidades_entregadas:
            cantidades_entregadas[lb.lineaidpicking] = 0
        if float(lb.qtypedido) - float(cantidades_entregadas[lb.lineaidpicking]) > 0:
            lineas_por_entregar.append(lb)

    # Entregar
    lineas_exitosas = []
    lineas_error = []


    for lb in lineas_por_entregar:
        try:
            linea_duk = lb.create_return_line(database, 
                                              qtyenpicking= (float(lb.qtypedido) - float(cantidades_entregadas[lb.lineaidpicking])),
                                              estadodetransferencia=3, 
                                              date=timezone.now())
            lineas_exitosas.append(linea_duk.lineaidpicking)
        except Exception as e:
            print(e)
            lineas_error.append(lb.lineaidpicking)
            continue


    return {"LineasExitosas": lineas_exitosas, "LineasError": lineas_error}

  