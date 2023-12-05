from BackendApp.utils import *

def create_customer():
    sp = ''' INSERT INTO [dbo].[TDA_WMS_CLT]
           ([nit]
           ,[nombreCliente]
           ,[Direccion]
           ,[isActivoProveedor]
           ,[CondicionesCompra]
           ,[CodigoPais]
           ,[MonedaDeFacturacion]
           ,[item]
           ,[ActivoCliente]
           ,[CiudadDestino]
           ,[DptoDestino]
           ,[PaisDestino]
           ,[CodCiudadDestino]
           ,[CodDptoDestino]
           ,[CodPaisDestino]
           ,[fechaRegistro]
           ,[Telefono]
           ,[Cuidad]
           ,[CuidadDespacho]
           ,[Notas]
           ,[contacto]
           ,[email]
           ,[paisDespacho]
           ,[departamentoDespacho]
           ,[sucursalDespacho]
           ,[idSucursal]
           ,[isactivocliente]
           ,[isactivoproveed]
           ,[estadotransferencia]
           ,[vendedor]
           ,[zip_code]
           ,[licencia])
     VALUES
           ('nit_prueba', 
           ,'nombreCliente'
           ,'Direccion prueba'
           ,0
           ,0
           ,169
           ,'COP'
           ,'1-prueba'
           ,1
           ,'Medellin'
           ,'Antioquia
           ,'Colombia
           ,'001'
           ,'05'
           ,'169'
           ,getdate()
           ,'telefono prueba'
           ,'Medellin'
           ,'Medellin'
           ,'Notas prueba
           ,'contacto prueba'
           ,'eamil prueba'
           ,'Colombia'
           ,'Antioquia'
           ,'sucursal 1'
           ,'1'
           ,1
           ,0
           ,0
           ,'vendedor prueba'
           ,'zip code'
           ,'licencia') '''

    # Query que se hace directamente a la base de datos
    try:
        exec_query(sp)
    except Exception as e:
        raise ValueError(e)

def validate_customer():
    sp = ''' select * 
            from [dbo].[TDA_WMS_CLT]
            where item = '1-prueba' '''

    try:
        response = exec_query(sp)
        if response !=[]:
            print("Customer created")
        else:
            raise ValueError("CUSTOMER NOT FOUND")
    except Exception as e:
        raise ValueError(e)


def delete_customer():
    sp = ''' delete
            from [dbo].[TDA_WMS_CLT]
            where item = '1-prueba' '''

    try:
        exec_query(sp)
    except Exception as e:
        raise ValueError(e)

    
        