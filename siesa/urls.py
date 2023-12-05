from django.urls import re_path
from BackendApp.views.conteosinventario import reconteo
from BackendApp.views.conteosinventario.ajustarconteo import ajustarconteo
from BackendApp.views.conteosinventario.asignarlineaconteo import asignarlineaconteo
from BackendApp.views.conteosinventario.conteo import conteo
from BackendApp.views.layout import layoutarticulosxubicacion, layoutzona
from BackendApp.views.registrosanitario import regsanitario
from BackendApp.views.descriptoreslogisticos import descriptoreslogisticos
# from BackendApp.views import logistiusecsvar
from BackendApp.views.users import *
from BackendApp.views.dwh_picking import *
from BackendApp.views.users.users import users
from .views import *
# from BackendApp.views.pickinglist import pickinglist

urlpatternsSiesa = [
    # Nota:
    # Aqui se le indica a la aplicacion que cuando se le diga el ENPOINT en color naranja
    # Ejecute el archivo que esta en color amarillo al lado derecho
    re_path(r'^T120$', T120Mc),
    re_path(r'^T121$', T121Mc),
    re_path(r'^sync/articles$', sync_articles),
    # re_path(r'^warehouses/([A-Za-z0-9]+)$', warehouses)


]
