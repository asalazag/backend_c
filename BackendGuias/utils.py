from django.db import connections

from BackendApp.producer import PublishAMQP


def convert_array_records_to_array_json(array=[], descriptions = () ) -> list:
    if len(array)==0:
        return []
    if len(descriptions)==0:
        return []

    columnNames = [column[0] for column in descriptions]
    response = []
    for record in array:
        response.append(dict(zip(columnNames, record)))
    return response


def exec_query(query='', params=(), database="default"):
    cursor = connections[database].cursor()
    # cadena_conexion = varibale_global                                                                        PublishAMQP()
    # connection_handler = ConnectionHandler(cadena_conexion)
    # cursor = connection_handler.cursor()
    # query = ''' 
    #         SET NOCOUNT ON
    #         EXEC [web].[usp_T_Narth_Serie_Pedido_ObtenerConUbicacionesFijas]  %s, %s, %s
    #         '''
    print(query)
    print(params)
    cursor.execute(query, params)
    try: 
        response = cursor.fetchall() 
        descriptions = cursor.description
        response = convert_array_records_to_array_json(response, descriptions)
    except:
        response = []
    cursor.close()
    return response






