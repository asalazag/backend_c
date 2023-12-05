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

]

    
  
