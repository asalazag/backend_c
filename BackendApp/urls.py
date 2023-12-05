from django.urls import re_path
from BackendApp.views.api.shipstation.create_label import create_label_shipstation
from BackendApp.views.conteosinventario import reconteo
from BackendApp.views.conteosinventario.ajustarconteo import ajustarconteo
from BackendApp.views.conteosinventario.asignarlineaconteo import asignarlineaconteo
from BackendApp.views.conteosinventario.conteo import conteo
from BackendApp.views.layout import layoutarticulosxubicacion, layoutzona
# from BackendApp.views.picking.orden_picking import 
from BackendApp.views.picking.picking_finished import get_picking_finished
from BackendApp.views.registrosanitario import regsanitario
from BackendApp.views.descriptoreslogisticos import descriptoreslogisticos
# from BackendApp.views import logistiusecsvar
from BackendApp.views.users import *
from BackendApp.views.dwh_picking import *
from BackendApp.views.users.users import users
from BackendApp.views.recibo import *
from BackendApp.views.autofill import *
from BackendApp.views.cajas import *
from BackendApp.views.dashboard_general import *
from .views import *
# from BackendApp.views.pickinglist import pickinglist

urlpatternsBack = [
    # Nota:
    # Aqui se le indica a la aplicacion que cuando se le diga el ENPOINT en color naranja
    # Ejecute el archivo que esta en color amarillo al lado derecho
    re_path(r'^warehouses$', warehouses),
    re_path(r'^warehouses/([A-Za-z0-9]+)$', warehouses),

    # spS_T_ins_descripciones (GET), #spI_T_ins_Descripciones (POST) , # spD_T_ins_Descripciones (DELETE)
    re_path(r'^descriptions$', descriptions),
    re_path(r'^descriptions/groups$', groups),  # spS_t_ins_grupos (GET)
    # spS_T_ins_descripciones (GET)
    re_path(r'^descriptions/bygroup$', descriptionsbygroup),

    # Planeacion despachos (Planeacion de)
    # spI_AddNewOrdenDeDespacho (POST) ,#spI_T_materiales_por_orden_Customized_Despacho
    re_path(r'^picking_order$', picking_order),
    re_path(r'^picking_remision$', picking_remision),
    re_path(r'^picking$', picking),  # usp_obtenerTblPlanDespachos (GET)
    # usp_T_Narth_Serie_Pedido_ObtenerConUbicacionesFijas (GET)
    re_path(r'^picking/detail$', picking_detail),
    re_path(r'^picking/employee$', actualizar_employee_picking), #[web].[usp_actualizaEmpleadoDePicking](PUT),
    re_path(r'^picking/send_erp$', picking_to_erp), #[web].[usp_LlevarLotesWMSToERP_QP](POST),
    re_path(r'^picking/detail/report$', picking_detail_report),
    re_path(r'^picking/seguimiento_detalleprepack$',
            seguimiento_detallepicking),  # usp_ObtenerProductosPicking  (GET)
    # usp_detalleSSCCxCaja_rct (GET)
    re_path(r'^picking/seguimiento_sscc$', seguimiento_pickingsscc),
    # select * FROM t_detalle_referencia_CD (GET)
    re_path(r'^picking/lista_vigencias$', lista_vigencias),
    re_path(r'^picking/getdetailordentda$', get_Picking_Summary_tda), # [web].[usp_ConsultaTransferenciasTDA]

    # spS_ObtenerCamposDeTabla (GET) , # spS_ObtenerCamposDeTabla (POST)
    re_path(r'^dynamics$', dynamics),
    # spS_T_ins_Consultas_Aleatorias (GET)
    re_path(r'^random$', random_queries),

    # sp_empleadosxID (GET), #usp_actualizarPermisosAppxIdEmpleado (PUT)
    re_path(r'^employee$', employee),
    re_path(r'^users$', users),


    re_path(r'^employee/zone$', zone),  # spS_T_ins_Zona_Empleado_rct (GET)

    # sps_t_Detalle_referencia_CV_rct (GET), #spi_t_detalle_refencia_CV_rct (POST), # spu_t_detalle_refencia_CV_rct (PUT), # spD_t_detalle_refencia_CV_rct (DELETE)
    re_path(r'^logisticsvars$', logisticsvars),
    re_path(r'^logisticsvars/imageurl$', images_url),
    re_path(r'^articles$', articles),  # sps_v_wms_articulos_rct (GET)
    # usp_searchbydescription (GET)
    re_path(r'^articles/search$', articles_search),

    # sps_t_detalle_referencia_CD_rct  (GET), spi_t_detalle_referencia_CD_rct (POST), spu_t_detalle_referencia_CD_rct (PUT), # spD_t_detalle_referencia_CD_rct (DELETE)
    re_path(r'^listasvigenciadespacho$', listasvigenciadespacho),
    # spS_TiposDeCaja (GET), spI_TiposDeCaja (POST), spU_TiposDeCaja (PUT), # spD_TiposDeCaja (DELETE)
    re_path(r'^tiposdecaja$', tiposdecaja),

    # usp_ObtenerDsInventarioWMSConsolidado_RCT (GET),
    re_path(r'^inventory$', inventory),

    # usp_ObtenerResultadoxIDConteo  (GET), # sp_ObtienedatosparaConteo_ext (POST), # usp_ActualizaReconteoEnConteoBase (PUT), # spD_T_Temporar_Encabezado_ConteoWMS_Customized (DELETE)
    re_path(r'^conteo/programarconteo$', conteo),
    # usp_recarga_T_Temporar_Encabezado_Conteo (POST), # usp_obtenerlistaxobjetofninvxbodega (GET)
    re_path(r'^conteo/programarreconteo$', reconteo),
    # usp_ajusteDeCajasxvaloresDeIDConteo (PUT)
    re_path(r'^conteo/ajustarconteo$', ajustarconteo),
    # usp_asigna_lineasConteoxIdEmpleado (PUT)
    re_path(r'^conteo/asignar$', asignarlineaconteo),

    re_path(r'^conteo/conteosactivos$', verconteosactivos),  # get_ConteosActivos (GET)

    re_path(r'^conteo/conteosterminados$', verconteosterminados),  # get_ConteosFinalizados (GET)

    # Endpoint DWH PICKING
    # dwh_pedidos_enc (GET)
    # dwh_pedidos_enc (GET)
    re_path(r'^dwh_picking/pedidos_enc$', dwh_pedidos_enc),
    # dwh_pedidos_det (GET)
    # dwh_pedidos_det (GET)
    re_path(r'^dwh_picking/pedidos_det$', dwh_pedidos_det),
    re_path(r'^dwh_picking/picking$', dwh_picking),  # dwh_picking_det (GET)
    re_path(r'^dwh_picking/sscc$', dwh_sscc),  # dwh_ssccxcaja (GET)
    # dwh_aduana_wmspospedido (GET)
    re_path(r'^dwh_picking/aduana$', dwh_aduana_pos),

    # Endpoint DWH INVENTARIO search
    # usp_ObtenerDsInventarioWMSConsolidado_RCT (GET)
    # usp_ObtenerDsInventarioWMSConsolidado_RCT (GET)
    re_path(r'^inventory/comparativo$', inventory),
    # dwh_usp_ObtenerDsInventariosxEANWmsConsolidado (GET)
    # dwh_usp_ObtenerDsInventariosxEANWmsConsolidado (GET)
    re_path(r'^inventory/consolidadoxean$', inventorybyeanconsolidado),
    # dwh_usp_ObtenerDsInventariosxEANWmsDetallado (GET)
    # dwh_usp_ObtenerDsInventariosxEANWmsDetallado
    re_path(r'^inventory/detalladoxean$', inventorybyeandetallado),

    # Endpoint LAYOUT-MAPA (Muestra la ocupacion de la zona y lo que hay en la ubicacion)
    # usp_ObtenerCoordenadasCruzadaPorZonaFinal_RCT (GET)
    re_path(r'^layout/showzona$', layoutzona),
    # usp_ObtenerDsArticulosxUbicacion_RCT (GET)
    re_path(r'^layout/showarticulosenubicacion$', layoutarticulosxubicacion),
    # usp_planningSlotTaskByBox (POST)
    re_path(r'^layout/slotting$', slotting),

    # Maestros registros sanitarios y descriptores logisticos
    # usp_obtenerRegistroSanitarioxEan (GET), spWMS_Insertar_Registo_Sanitario (POST), spWMS_Actualizar_Registo_Sanitario (PUT), spWMS_Eliminar_Registo_Sanitario (DELETE)
    re_path(r'^maestros/regsanitario$', regsanitario),
    # spS_LogisticasXCaja (GET), # spI_LogisticasXCaja (POST),# spU_LogisticasXCaja (PUT), # spD_LogisticasXCaja (DELETE)
    re_path(r'^maestros/descriptoreslogisticos$', descriptoreslogisticos),

    # Endpoint STATUS CALIDAD
    # usp_getLotesEnLista_rct (GET) , #usp_ActualizarStatusCalidadLote_rct (PUT)
    re_path(r'^statuscalidad/lotes$', lotes),
    # spU_T_Maestro_lote_PT_customized_rct (PUT)
    re_path(r'^statuscalidad/modificarlote$', modificalote),
    # spU_T_Maestro_lote_PT_customized_rct (PUT)
    re_path(r'^statuscalidad/trazabilidadlote$', trazabilidadlote),#[web].[usp_ActualizarStatusCalidadLote_rct],[web].[usp_getLotesEnLista_rct]
    
    re_path(r'^statuscalidad/variablesxlote$', variables_lote),
    re_path(r'^statuscalidad/regsanitarioxlote$', registrosanitario_lote),
    re_path(r'^statuscalidad/cuarentenaxlote$', establecer_cuerentena),# [web].[EstableceEstadoCuarentena]


    # kpi RECIBO
    # kpi_lineasRecibidasxdia (GET)
    re_path(r'^kpi/reciboxrangorec$', kpi_lineasrecibidasxrango),
    # kpi_lineasAlmacenadasxdia (GET)
    re_path(r'^kpi/reciboxrango$', kpi_lineasalmacenadasxrango),

    # kpi PICKING
    # kpi_lineasAlmacenadasxdia (GET)
    re_path(r'^kpi/pickingxrango$', kpi_lineaspickingxrango),
    # kpi_pickingpendientesxzona (GET)
    re_path(r'^kpi/pendientexzona$', kpi_pendientesxzona),

    # #kpi ADUANA
    re_path(r'^kpi/aduanaxrango$', aduana),  # kpi_lineasaduanaxrango (GET)


    # kpi LAYOUT RESUMEN
    re_path(r'^kpi/layoutresume$', kpi_layoutresumen),  # kpi_layout (GET)

    # kpi GENERAL
    # kpi_lineasnegadasxproceso (GET)
    re_path(r'^kpi/generales$', kpi_negados),


    # generacion GUIAS TRANSPORTE
    # sps_ciudadesDANE (GET) , #spi_tda_wms_tte (POST),#spu_tda_wms_tte (PUT)
    # usp_obtenerTransportadoraconvenio (GET),# spi_tda_wms_tte (POST)
    re_path(r'^guias/copiarguia$', copiarguia),

    # spu_tda_wms_tte_guia (PUT) #awg_obtenerDataparaGuiaTte (GET),#spu_tda_wms_tte (PUT)
    re_path(r'^guias/obtenerguia$', obtenerdatosguia),
    re_path(r'^guias/obtenerciudades$', obtenerciudades),  # sps_ciudadesDANE


    # CRUD EPK -- POBLADO DE TABLAS EPK Y DPK
    re_path(r'^epk/epk$', crud_epk),  # Insert_TDA_WMS_EPK_Json_RCT (POST)
    re_path(r'^epk/dpk$', crud_dpk),  # Insert_TDA_WMS_DPK_Json_RCT (POST)

    # CRUD EPN -- POBLADO DE TABLAS EPN Y DPN
    re_path(r'^epn/epn$', crud_epn),  # Insert_TDA_WMS_EPK_Json_RCT (POST)
    # re_path(r'^epk/dpk$', crud_dpk),  # Insert_TDA_WMS_DPK_Json_RCT (POST)

    re_path(r'^config$', config_wms),  # Insert_TDA_WMS_DPK_Json_RCT (POST)

    # Insert_TDA_WMS_DPK_Json_RCT (POST)
    re_path(r'^tablesFields$', tables_fields),

    re_path(r'^api$', api),  # Insert_TDA_WMS_DPK_Json_RCT (POST)
    re_path(r'^api/dynamic_queries$', dynamic_queries_view),  # Insert_TDA_WMS_DPK_Json_RCT (POST)
    re_path(r'^api/execute/dynamic_queries$', dynamic_queries_execute_view),  # Insert_TDA_WMS_DPK_Json_RCT (POST)

    # This endpoint is for create users from database to users table
    re_path(r'^create/users$', users),


    # ZPL PRINT
    re_path(r'^zpl/pdf$', zpl),

    re_path(r'^pruebas$', pruebas),

    re_path(r'^databasesList$', databases_list),

    re_path(r'^importdata$', import_csv),

    re_path(r'^mongo/plantillas$', plantillas),

    re_path(r'^activities$', activities),

    re_path(r'^tipodocto$', tipodocumento),

    re_path(r'^autoaduana$', crud_autoaduana),

    re_path(r'^autoaduana/documentos$', crud_documentos_autoaduana),


    # API integration 
    re_path(r'^api/integrations$', active_integrations),

    # API integration 
    re_path(r'^api/integrations/shipstation$', create_label_shipstation),

    #Flash ADUANA
    re_path(r'^aduana/flash/getordersinflashbypicking$', GetOrdersInFlashByPicking), #[web].[usp_obtenerPedidosDestelladosxEanEnPicking]
    re_path(r'^aduana/flash/getflashinorder$', GetFlashInOrder), #[web].[usp_estableceOrdenDestelle] 
    re_path(r'^aduana/flash/getinfobybarcodepicking$', GetInfoByBarcodePicking), #[web].[usp_obtenerDSPickingDestelle]
    re_path(r'^aduana/flash/getinfotransactionbyeanpicking$', GetInfoTransactionByEanPicking), #[web].[usp_obtenerPedidosDestelladosxEanEnPicking_filtered] 
    re_path(r'^aduana/flash/setflasheanpicking$', SetFlashEanPicking), #[web].[usp_confirmaEANdestelladoxpickingxdestelle]
    re_path(r'^aduana/flash/confirmeanflashpicking$', ConfirmEanFlashPicking), #[web].[usp_confirmaEANdestelladoxpicking]
    re_path(r'^aduana/flash/getconfirmedreferencesinflash$', GetConfirmedReferencesInFlash), #[web].[usp_obtenerReferciasValidadasEnDestelle_App]
    re_path(r'^aduana/flash/finishcustomsbypicking$', FinishCustomsByPicking), #[web].[usp_EstableceAutoAduanagMDC_Nw]
    re_path(r'^aduana/flash/createlabelbypicking$', CreateLabelByPicking), #[web].[usp_ssccxcaja_ZPL_destelle]
    re_path(r'^aduana/flash/sendzpltoprinter$', SendZPLToPrinter), #[cmn].[generarTxtImpresionCajas]
    re_path(r'^aduana/flash/getnotesbyorderpicking$', GetNotesByOrderPicking), #[web].[usp_obtenerListaNotasxpedido]


   # Orders ADUANA
    re_path(r'^aduana/orders/getlistordersorterbypicking$', GetListOrderSorterByPicking), #[web].[usp_obtenerListaSorterByPicking]
    re_path(r'^aduana/orders/getProductsbyPicking$', GetProductsByPicking), #[web].[usp_obtenerDsArticulosxPicking]
    re_path(r'^aduana/orders/getBoxSecuence$', GetBoxSecuence), #[web].[usp_obtenerListaSorterByPicking]
    re_path(r'^aduana/orders/getordersbypicking$', GetOrdersByPicking), #[web].[usp_obtenerPedidosEnPicking]
    re_path(r'^aduana/orders/getregisteropencustoms$', GetRegisterOpenCustoms), #[web].[usp_regaperturaaduana]
    re_path(r'^aduana/orders/getcomparecustomsorder$', GetCompareCustomsOrder), #[web].[usp_verdiferenciasaduanavspedido] 
    re_path(r'^aduana/orders/getinfocustomsconteiners$', GetInfoCustomsConteiners), #[web].[usp_obtenerDsContenedoresAduanados_app_Pedido]
    re_path(r'^aduana/orders/getpickingbyorder$', GetPickingByOrder), #[web].[usp_ObtenerResumenContenidoxContenedor]
    re_path(r'^aduana/orders/getinfoordercustomsconteiners$', GetInfoOrderCustomsConteiners), #[web].[usp_obtenerDsContenedoresAduanados_app_Pedido_Peso]
    re_path(r'^aduana/orders/finishcustomsbyorder$', FinishCustomsByOrder), #[web].[usp_TerminarAduanaDePicking_AduanaNew_app_pedido]
    re_path(r'^aduana/orders/finishcustomsbypicking$', FinishCustomsByPicking), #[web].[usp_TerminarAduanaDePicking_AduanaNew_app]
    re_path(r'^aduana/orders/updateweightbycontainer$', UpdateWeightByContainer), #[web].[usp_registraPesoxIdContenedorPicking]
    re_path(r'^aduana/orders/createzplboxbypicking$', CreateZplBoxByPicking), #[web].[usp_ssccxcajaCR_ZPL_YMH]
    re_path(r'^aduana/orders/setcustomstosmc$', SetCustomsToSMC), #[web].[usp_sendAduanaToSMC] 

    #Orders Detail ADUANA

    re_path(r'^aduana/orders/updateboxinconteiner$', UpdateBoxInConteiner), #[web].[usp_actualizaTipoCajaEnContenedor]
    re_path(r'^aduana/orders/validatestocksbyean$', ValidateStocksByEan), #[web].[usp_validaexistenciaean]
    re_path(r'^aduana/orders/customsposfromorder$', CustomsPosFromOrder), #[web].[spI_T_Aduana_WMS_POS_FromPedido]
    re_path(r'^aduana/orders/getcustomsbyorder$', GetCustomsByOrder), #[web].[T_Aduana_WMS_POS_PEDIDOxPedido]
    re_path(r'^aduana/orders/removeitemcustomsbyid$', RemoveItemCustomsById), #[web].[usp_eliminarItemAduanaxID]
    re_path(r'^aduana/orders/getinfoconteneinerbyeanorder$', GetInfoConteneinerByEanOrder), #[web].[usp_ObtenerInformacionDeContenidoxEanDeCaja_newPedido]
    re_path(r'^aduana/orders/getinfoselecteditemcustoms$', GetInfoSelectedItemCustoms), #[web].[usp_obtenerInformacionIdseleccionadoAduanaPosPedido]
    re_path(r'^aduana/orders/getpendingbycustoms$', GetPendingByCustoms), #[web].[usp_obtenerDsArticulosPendientesxAduana]
    re_path(r'^aduana/orders/getContenedoresAduanados$', GetContenedoresAduanados), #[web].[usp_obtenerContenedoresAduanados]

    #Orders Pickings
    re_path(r'^picking/progress/getPickinginProgress$', get_picking_in_progress), #[web].[usp_ShowCardPicking]
    re_path(r'^picking/progress/getPickingFinished$', get_picking_finished), #[web].[usp_ShowCardPicking_finalizados]
    re_path(r'^picking/progress/actualizarOrdenPicking$', actualizar_orden_picking),# [web].[usp_actualizaOrdenInicioDePicking]
    re_path(r'^picking/progress/getPickingNumpedido$', get_Picking_con_numpedido),# [web].[usp_getPicking_con_numpedido] '270'
    re_path(r'^picking/progress/getPickingNumdocumento$', get_Picking_con_numdocumento),# [web].[usp_getPicking_con_numdocumento]
    re_path(r'^picking/progress/getPickingSummary$', get_Picking_Summary),#[web].[usp_summaryPicking]
    re_path(r'^picking/actualizarcantidadlinea$', actualizar_cantidad_picking),#[web].[spi_prcActualizarCantidadesLineaPicking]
    re_path(r'^picking/actionhook$', actionhookPicking), # [web].[usp_actionhookPicking]
    re_path(r'^picking/processparameters$', parametros_picking),
    re_path(r'^picking/crearlotes$', lotes_picking), # [web].[usp_crearLotesDesdeOPExterna_1]
    re_path(r'^picking/crearsubcomponentes$', subcomponentes_picking), # [web].[USP_RPT_SERIAL_OP_PARTES_NW2_TDA]
    re_path(r'^picking/epngenerictransfer$', reenvio_epn_generic_transfer), # API

    
    
    #Sp_Tables
    re_path(r'^sp/migrate$', create_alter_stored_procedures),
    re_path(r'^sp/alterUpdate$', alter_update_procedures),
    re_path(r'^sp/migrate_table$', create_alter_tables),
    re_path(r'^sp/equalize_update$', equalize_update_procedures),
    re_path(r'^table/equalize_validate$', equalize_validate_tables),
    re_path(r'^table/datatable$', insertdatatable),
    re_path(r'^sp/execute_sp$', execute_sp), #ejecuta una query completa

    #Varios
    re_path(r'^sp/mantenimiento$', execute_mantemimiento),
    re_path(r'^autofill/detallerefenciaCV$', autofill_detalle_refencia),# [dbo].[usp_autofill_detalle_refencia_CV]
    re_path(r'^sp/massive_custommized$', massive_custommized),# [dbo].[dev_sp_customized_massive]]
    
    
    #Autoaduana
    
    re_path(r'^aduana/autoaduana/obtenerLista$', autoAduanaList),#[web].[usp_ObtenerListaAutoAduana]
    re_path(r'^aduana/autoaduana/autoAduanaxUnitarizador$', autoAduanaxPicking),#[web].[spi_prcAutoAduanaxPicking]
    
    #Resurtido
    re_path(r'^resurtido/obtenerdatos$', get_Data_Resurtido),#[web].[usp_Datos_Resurtido]
    re_path(r'^resurtido/obtenerdetalle$', get_Detalle_Resurtido),#[web].[usp_Detalle_Resurtido]
    re_path(r'^resurtido/obtenercantidadEmpaque$', cantidad_unidades_empaque),#dbo.fnT_CantidadEnUnidadesEmpaqueEAN
    re_path(r'^resurtido/asignartareareasurtido$', resurtido_asignar_tarea),#[web].[usp_Add_Tarea_Resurtido]
    
    #Inventario
    re_path(r'^inventario/obtenerdetalle', get_Detalle_Inventario),#[web].[usp_Obtener_Datos_Inventario]
    re_path(r'^inventario/obtenerdatosprioridad', get_datos_prioridad),#[web].[usp_DatosPrioridad_Inventario]
    re_path(r'^inventario/obtenerresumenproducto', get_Resumen_Producto),#[web].[usp_DatosPrioridad_Inventario]
    re_path(r'^picking/actualizarpicking', actualizar_picking),#[web].[usp_ActualizarPicking]
    
    #Recibo
    re_path(r'^recibo/addbarcode', AddBarcode), #[web].[spI_T_RelacionCodBarras_app]
    re_path(r'^recibo/oddblindlotext', AddBlindLotExt), #[web].[usp_ingloteciego_extendido]
    re_path(r'^recibo/boxbyorder', BoxByOrder), #[web].[usp_obtenerDSCajasGeneradasxOrd_no]
    re_path(r'^recibo/createZPLCo', CreateZPLCo),#[web].[usp_recibociegoxdocto_zpl]
    re_path(r'^recibo/endReceive', EndReceive), #[web].[usp_descuentaLineasConIgualCodigo_DUK]
    re_path(r'^recibo/articleslistblinddocument', GetArticlesListInBlindDocument), # [web].[usp_ObtenerDsListaArticulosEnCiego]
    re_path(r'^recibo/articlesListblinddocumentExt', GetArticlesListInBlindDocumentExt), #[web].[usp_ObtenerDsListaArticulosEnCiego_ext]
    re_path(r'^recibo/documenttype', GetDocumentType), #[web].[usp_obtenerTipoDocRecepcion]
    re_path(r'^recibo/entrydocuments', GetEntryDocuments), #[web].[usp_documentosEntrada]
    re_path(r'^recibo/infobyarticle', GetInfoByArticle), #[web].[usp_obtenerDsInfoxWMS_Articulo]
    re_path(r'^recibo/infobyEANoc', GetInfoByEANinOC), #[web].[usp_obtenerInfoxEANenOC]
    re_path(r'^recibo/lotebyarticle', GetLotByArticle), #[web].[usp_obtenerDSlistaDelotesxArticulo]
    re_path(r'^recibo/receivedocument', GetReceiveDocument), #[web].[usp_ObtenerDsDocumentoRecepcion_DUK]
    re_path(r'^recibo/loadboxbliend', LoadBoxBliend), #[web].[usp_MDC_CargaInicial_From_ciego]
    re_path(r'^recibo/undoreferenceblind', UndoReferenceInBlind), #[web].[usp_deshacerReferenciaEnCiego]

    re_path(r'^recibo/agendamuelle', agendaMuelle), #dbo.T_plan_agendamuelle
    re_path(r'^recibo/ubicacionmuelle', muelleUbicacionBodega), #dbo.T_Ins_Coordenadas
    re_path(r'^planrecibo', getplanrecibo), #[web].[usp_ObtenerTblPlanRecibo_RCT]


    
    #Cajas
    re_path(r'^caja/getubicaciones', getubicacionesxCaja), #[web].[usp_ObtenerUbicacionesDeCaja]
    re_path(r'^caja/getmovimientos', getmovimientosxCaja), #[web].[usp_deshacerReferenciaEnCiego]
    re_path(r'^caja/getinventario', getinventarioCajas), #[web].[usp_ObtenerInventarioCajas]
    
    #Dashboard
    re_path(r'^dashboard/adapterdata', dashboard_adapter), #[web].[sp_ObtenerDashboardAdapter] 
    re_path(r'^dashboard/actividadesrecientes', dashboard_actividad_reciente), #[web].[sp_DashboardActividadReciente] 
    re_path(r'^dashboard/estadosactividades', dashboard_estados_actividades), #[web].[sp_Dashboard_Estados_Actividades] 
    
    # Plan Recibo
    re_path(r'^recibo/planrecibo/detalle', GetDetallePlanReciboxDto), #[web].[usp_DetallePlanReciboxDto]

    # Completar orden de despacho retornando las lineas en estado 3
    re_path(r'^despacho/completar', completar_orden_despacho), #[web].[usp_ObtenerOrdenDespacho]

    #  Completar orden de compra retornando las lineas en estado 3
    re_path(r'^duk/completar', completar_orden_compra), #[web].[usp_ObtenerOrdenDespacho]

    re_path(r'^duk/obtenerdatos', crud_euk), #[web].[usp_Obtener_Datos_Recibo]
    
    re_path(r'^euk/changestatuseuk', change_estatus_euk), #[web].[usp_changeStatusEuk]

    re_path(r'^recibo/imprimirCaja', imprimircajas), #[web].[usp_GenerarZPLCajaMP_RangoCajas]

    re_path(r'coordenadas/imprimir', imprimir_coordenadas)  # [web].[usp_tmpCargaInvInicial_ZPL_SMT_FULL_app]


]

    
  