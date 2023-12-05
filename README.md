# SGV-WMS-BACKEND
Backend wms

___
## API - Inventarios

#### Procedimientos para la visualizacion del inventario por bodega y por producto

```http
   inventory/comparativo$ | inventory/consolidadoxean$ | inventory/detalladoxean$ | 
```

| Parameter                        | Type     | Store procedure                                 					|
| :--------                        | :------- | :-------------------------                      					|
| `/api/inventory/comparativo`     | `GET`    | usp_ObtenerDsInventarioWMSConsolidado_RCT       					|
| `/api/inventory/consolidadoxean` | `GET`    | dwh_usp_ObtenerDsInventariosxEANWmsConsolidado  					|
| `/api/inventory/detalladoxean`   | `GET`    | dwh_usp_ObtenerDsInventariosxEANWmsDetallado    					|

___
## API - Dashboard

#### Procedimientos para la visualizacion de los dashboard de indicadores

```http
   kpi/reciboxrangorec$ | kpi/reciboxrango$ | kpi/pickingxrango$ | kpi/pendientexzona$ | 
   kpi/pendientexzona$  | kpi/aduanaxrango$ | kpi/layoutresume$  | kpi/generales$     |
```

| Parameter                        | Type     | Store procedure                                 				   	|
| :--------                        | :------- | :-------------------------                     					   	|
| `/api/kpi/reciboxrangorec`       | `GET`    | kpi_lineasRecibidasxdia                         					|
| `/api/kpi/reciboxrango` 	     | `GET`    | kpi_lineasAlmacenadasxdia                       					|
| `/api/kpi/pickingxrangon`        | `GET`    | kpi_lineasAlmacenadasxdia                       					|
| `/api/kpi/pendientexzona`        | `GET`    | kpi_pickingpendientesxzona                     	 					|
| `/api/kpi/aduanaxrango`          | `GET`    | kpi_lineasaduanaxrango                          					|
| `/api/kpi/layoutresume`          | `GET`    | kpi_layout                                      					|
| `/api/kpi/generales	`          | `GET`    | kpi_lineasnegadasxproceso                       					|
___
## API - Layout 

#### Procedimientos para la visualizacion del layout, slotting y la programacion de tareas de
     slotting

```http
   layout/showzona$| layout/showarticulosenubicacion$ | layout/slotting$ | 
```

| Parameter                        		| Type     | Store procedure                                 				|
| :--------                        		| :------- | :-------------------------                      				|
| `/api/layout/showzona`       		| `GET`    | usp_ObtenerCoordenadasCruzadaPorZonaFinal_RCT   				|
| `/api/layout/showarticulosenubicacion` 	| `GET`    | usp_ObtenerDsArticulosxUbicacion_RCT            				|
| `/api/layout/slotting`        		| `GET`    | usp_planningSlotTaskByBox                       				|
___

## API - Planeacion Despachos 

#### Procedimientos para la planeacion de picking y seguimiento de picking

```http
   picking_order$| picking$| picking/detail$ | 
   picking/seguimiento_detalleprepack$ | picking/seguimiento_sscc$ | picking/lista_vigencias$ |
   dwh_picking/pedidos_enc$ | dwh_picking/pedidos_det$ | dwh_picking/picking$ | dwh_picking/sscc$ | dwh_picking/aduana$ |
```

| Parameter                        				| Type     | Store procedure                                           |
| :--------                        				| :------- | :-------------------------                                |
| `/api/picking_order`       					| `POST`   | usp_spI_AddNewOrdenDeDespacho                             |
| ` ` 								| `GET`    | spI_T_materiales_por_orden_Customized_Despacho            |
| `/api/picking/detail`        				| `GET`    | usp_T_Narth_Serie_Pedido_ObtenerConUbicacionesFijas       |
| `/api/picking/detail`        				| `GET`    | usp_T_Narth_Serie_Pedido_ObtenerConUbicacionesFijas       |
| `/api/picking/seguimiento_detalleprepack` 		| `GET`    | usp_ObtenerProductosPicking                      	     |
| `/api/picking/seguimiento_sscc`        			| `GET`    | usp_detalleSSCCxCaja_rct                      		     |
| `/api/picking/lista_vigencias`        			| `GET`    | select * FROM t_detalle_referencia_CD                     |
| `/api/picking/seguimiento_sscc`        			| `GET`    | usp_detalleSSCCxCaja_rct                      		     |
| `/api/dwh_picking/pedidos_enc`        			| `GET`    | dwh_pedidos_enc                     			     |
| `/api/dwh_picking/pedidos_det`        			| `GET`    | dwh_pedidos_det                                           |
| `/api/dwh_picking/picking`        			| `GET`    | dwh_picking_det                                           |
| `/api/dwh_picking/sscc`        				| `GET`    | dwh_ssccxcaja                                             |
| `/api/dwh_picking/aduana`        				| `GET`    | dwh_aduana_wmspospedido                                   |

___
## API - Inventario

#### Procedimientos para la visualizacion del inventario por bodega y por producto

```http
  inventory/comparativo$| inventory/consolidadoxean$ |  inventory/detalladoxean$ |

```

| Parameter                        				| Type     | Store procedure                                           |
| :--------                        				| :------- | :-------------------------                                |
| `/api/inventory/comparativo`       			| `GET`    | usp_ObtenerDsInventarioWMSConsolidado_RCT                 |
| `/api/inventory/consolidadoxean` 				| `GET`    | dwh_usp_ObtenerDsInventariosxEANWmsConsolidado            |
| `/api/inventory/detalladoxean`        			| `GET`    | dwh_usp_ObtenerDsInventariosxEANWmsDetallado              |

___
## API - Lotes

#### Procedimientos para la generacion de status calidad, actualizacion de lotes, registro sanitario y 

```http
  statuscalidad/lotes$ | statuscalidad/modificarlote$ |  statuscalidad/trazabilidadlote$ |
  maestros/regsanitario$ | maestros/descriptoreslogisticos$ |

```

| Parameter                        				| Type     	| Store procedure                                		|
| :--------                        				| :------- 	| :-------------------------           	       		|
| `/api/statuscalidad/lotes`       				| `GET`    	| usp_getLotesEnLista_rct                		 		|
| `/api/statuscalidad/lotes` 					| `PUT`    	| usp_ActualizarStatusCalidadLote_rct            		|
| `/api/statuscalidad/modificarlote`        		| `PUT`    	| spU_T_Maestro_lote_PT_customized_rct           		|
| `/api/statuscalidad/trazabilidadlote`        		| `PUT`    	| spU_T_Maestro_lote_PT_customized_rct		 		|
| `/api/maestros/regsanitario`        			| `GET`    	| usp_obtenerRegistroSanitarioxEan               		|
| `/api/maestros/regsanitario`        			| `POST`    | usp_spWMS_Insertar_Registo_Sanitario           		|
| `/api/maestros/regsanitario`        			| `PUT`    	| spWMS_Actualizar_Registo_Sanitario             		|
| `/api/maestros/regsanitario`        			| `DELETE`  | spWMS_Eliminar_Registo_Sanitario            	 		|
| `/api/maestros/descriptoreslogisticos`        	| `GET`    	| spS_LogisticasXCaja              			 		|
| `/api/maestros/descriptoreslogisticos`        	| `POST`    | spI_LogisticasXCaja              			 		|
| `/api/maestros/descriptoreslogisticos`        	| `PUT`    	| spU_LogisticasXCaja              			 		|
| `/api/maestros/descriptoreslogisticos`        	| `DELETE`  | spD_LogisticasXCaja              			 		|

___
## API - Maestros Descripciones 

#### Procedimientos para el CRUD de archivos maestros

```http
   descriptions$ | descriptions/groups$ | descriptions/bygroup$ | 
```

| Parameter                        | Type     | Store procedure                                				 		|
| :--------                        | :------- | :-------------------------                     				 		|
| `/api/descriptions`    	     | `GET`    | spS_T_ins_descripciones       						 		|
| `/api/descriptions`              | `POST`   | spI_T_ins_Descripciones       						 		|
| `/api/descriptions`              | `DELETE` | spD_T_ins_Descripciones       						 		|
| `/api/descriptions/groups`       | `GET`    | spS_t_ins_grupos       								 		|
| `/api/descriptions/bygroup`      | `GET`    | spS_T_ins_descripciones 							 		|

___
## API - Dinamicas 

#### Procedimientos para el CRUD de consultas dinamicas

```http
   dynamics$ | random$ | 
```

| Parameter                        | Type     | Store procedure                                 					|
| :--------                        | :------- | :-------------------------                      					|
| `/api/dynamics`    	     	     | `GET`    | spS_ObtenerCamposDeTabla       								|
| `/api/dynamics`    	     	     | `POST`   | spS_ObtenerCamposDeTabla       								|
| `/api/random`                    | `GET`    | spS_T_ins_Consultas_Aleatorias      							|


___
## API - Plan Conteo

#### Procedimientos para la programacion de conteos de inventario

```http
  conteo/programarconteo$| conteo/programarreconteo$ |  conteo/ajustarconteo$ | conteo/asignar$ |

```

| Parameter                        				| Type     | Store procedure                                           |
| :--------                        				| :------- | :-------------------------                                |
| `/api/conteo/programarconteo`       			| `GET`    | usp_ObtenerResultadoxIDConteo                 		     |
| `/api/conteo/programarconteo`       			| `POST`   | sp_ObtienedatosparaConteo_ext                 		     |
| `/api/conteo/programarconteo`       			| `PUT`    | usp_ActualizaReconteoEnConteoBase                 	     |
| `/api/conteo/programarconteo`       			| `DELETE` | spD_T_Temporar_Encabezado_ConteoWMS_Customized            |
| `/api/conteo/programarreconteo` 				| `POST`   | usp_recarga_T_Temporar_Encabezado_Conteo         	     |
| `/api/conteo/programarreconteo` 				| `GET`    | usp_obtenerlistaxobjetofninvxbodega            	     |
| `/api/conteo/ajustarconteo`        			| `PUT`    | usp_ajusteDeCajasxvaloresDeIDConteo              	     |
| `/api/conteo/asignar`        				| `PUT`    | usp_asigna_lineasConteoxIdEmpleado              	     |


___
## API - Plan Despachos (Seguimiento picking)

#### Procedimientos para la programacion de picking por los modelos de batch y discreto

```http
  dwh_picking/pedidos_enc$| dwh_picking/pedidos_det$ |  dwh_picking/picking$ | dwh_picking/sscc$ | dwh_picking/aduana$ |

```

| Parameter                        				| Type     | Store procedure                                           |
| :--------                        				| :------- | :-------------------------                                |
| `/api/dwh_picking/pedidos_enc`       			| `GET`    | dwh_pedidos_enc			                 		     |
| `/api/dwh_picking/pedidos_det`       			| `GET`    | dwh_pedidos_det               	 	  		     |
| `/api/dwh_picking/picking`   	    			| `GET`    | dwh_picking_det				                 	     |
| `/api/dwh_picking/sscc`     	  			| `GET`    | dwh_ssccxcaja	          					     |
| `/api/dwh_picking/aduana` 					| `GET`    | dwh_aduana_wmspospedido     				    	     |

___
## API - Inventario

#### Procedimientos para la visualizacion del inventario por bodega comparativo ERP vs WMS y el inventario por producto

```http
  inventory/comparativo$ | inventory/consolidadoxean$ |  inventory/detalladoxean$ | 

```

| Parameter                        				| Type     | Store procedure                                           |
| :--------                        				| :------- | :-------------------------                                |
| `/api/inventory/comparativo`       			| `GET`    | usp_ObtenerDsInventarioWMSConsolidado_RCT		     |
| `/api/inventory/consolidadoxean`       			| `GET`    | dwh_usp_ObtenerDsInventariosxEANWmsConsolidado      	     |
| `/api/inventory/detalladoxean`   	    			| `GET`    | dwh_usp_ObtenerDsInventariosxEANWmsDetallado        	     |

___
## API - Layout

#### Procedimientos para la visualizacion del layout y el slotting de la zona 

```http
  layout/showzona$ | layout/showarticulosenubicacion$ |  layout/slotting$ | 

```

| Parameter                        				| Type     | Store procedure                                           |
| :--------                        				| :------- | :-------------------------                                |
| `/api/layout/showzona`       				| `GET`    | usp_ObtenerCoordenadasCruzadaPorZonaFinal_RCT		     |
| `/api/layout/showarticulosenubicacion`       		| `GET`    | usp_ObtenerDsArticulosxUbicacion_RCT      		     |
| `/api/layout/slotting`   	    				| `GET`    | usp_planningSlotTaskByBox        	 			     |

___
## API - Descriptores logisticos

#### Procedimientos para el CRUD del los descriptories logisticos asociados a un lote

```http
  | maestros/descriptoreslogisticos$ |

```

| Parameter                        					| Type     | Store procedure                                     |
| :--------                        					| :------- | :-------------------------                          |
| `/api/maestros/descriptoreslogisticos`       			| `GET`    | spS_LogisticasXCaja		  			     |
| `/api/maestros/descriptoreslogisticos`       			| `GET`    | spI_LogisticasXCaja		     			     |
| `/api/maestros/descriptoreslogisticos`       			| `GET`    | spU_LogisticasXCaja		                       |
| `/api/maestros/descriptoreslogisticos`       			| `GET`    | spD_LogisticasXCaja		                       |

___
## API - Registro sanitario

#### Procedimientos para el CRUD del los registros sanitarios asociados a un lote

```http
 | maestros/regsanitario$ | 

```

| Parameter                        					| Type     | Store procedure                                     |
| :--------                        					| :------- | :-------------------------                          |
| `/api/maestros/regsanitario`       				| `GET`    | usp_obtenerRegistroSanitarioxEan		  	     |
| `/api/maestros/regsanitario`       				| `POST`   | spWMS_Insertar_Registo_Sanitario		     	     |
| `/api/maestros/regsanitario`       				| `PUT`    | spWMS_Actualizar_Registo_Sanitario		           |
| `/api/maestros/regsanitario`       				| `DELETE` | spWMS_Eliminar_Registo_Sanitario		           |

___
## API - Lotes - Estados de calidad

#### Procedimientos para el CRUD de los estados de calidad del lote

```http
 | statuscalidad/lotes$ | statuscalidad/modificarlote$ | statuscalidad/trazabilidadlote$ |

```

| Parameter                        					| Type     | Store procedure                                     |
| :--------                        					| :------- | :-------------------------                          |
| `/api/statuscalidad/lotes`       					| `GET`    | usp_getLotesEnLista_rct		  	     	     |
| `/api/statuscalidad/lotes`       					| `PUT`    | usp_ActualizarStatusCalidadLote_rct		     |
| `/api/statuscalidad/modificarlote`       			| `PUT`    | spU_T_Maestro_lote_PT_customized_rct		     |
| `/api/prcGetHistoricoLote`       					| `GET`    | prcGetHistoricoLote		           		     |


## API - Dashboard - Recibo

#### Procedimientos para la visualizacion de KPI de recibo

```http
 | kpi/reciboxrangorec$ | kpi/reciboxrango$ | 

```

| Parameter                        					| Type     | Store procedure                                     |
| :--------                        					| :------- | :-------------------------                          |
| `/api/kpi/reciboxrangorec`       					| `GET`    | usp_getLotesEnLista_rct		  	     	     |
| `/api/kpi/reciboxrango`       					| `PUT`    | usp_ActualizarStatusCalidadLote_rct		     |
| `/api/statuscalidad/modificarlote`       			| `PUT`    | spU_T_Maestro_lote_PT_customized_rct		     |
| `/api/prcGetHistoricoLote`       					| `GET`    | prcGetHistoricoLote		           		     |

## API - Planeacion de despachos (Planeacion de picking)

#### Procedimientos para realizar la planeacion de picking por diferentes modelos

```http
 | picking_order$ | picking$ | picking/detail$ |

```

| Parameter                        					| Type     | Store procedure                                    				              |
| :--------                        					| :------- | :-------------------------                         						  |
| `/api/picking_order	`       					| `GET`    | usp_ObtenerTblPlanDespachos_RCT / ufn_obtenertblplandespachos_epk_ext_allcompany_RCT |
| `/api/picking/detail`       					| `PUT`    | usp_ActualizarStatusCalidadLote_rct		     |
| `/api/statuscalidad/modificarlote`       			| `PUT`    | spU_T_Maestro_lote_PT_customized_rct		     |
| `/api/prcGetHistoricoLote`       					| `GET`    | prcGetHistoricoLote		           		     |

