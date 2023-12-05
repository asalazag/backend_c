from BackendApp.utils import *

def create_sale_order():
    sp = ''' INSERT INTO [dbo].[TDA_WMS_EPK]
           ([tipoDocto]
           ,[doctoERP]
           ,[picking]
           ,[numPedido]
           ,[fechaplaneacion]
           ,[f_pedido]
           ,[item]
           ,[nombrecliente]
           ,[notas]
           ,[ciudad despacho]
           ,[pais Despacho]
           ,[departamento Despacho]
           ,[direccion Despacho]
           ,[ciudad]
           ,[pedidoRelacionado]
           ,[cargue]
           ,[nit]
           ,[estadoPicking]
           ,[fechaRegistro]
           ,[fPedido]
           ,[centroOperacion]
           ,[bodega])
     VALUES
           () '''

    # Query que se hace directamente a la base de datos
    # try:
    #     response = exec_query(sp, (group,))
    # except Exception as e:
    #     print("Server Error!: ", e)
    #     return JsonResponse('Server Error!', safe=False, status=500)












