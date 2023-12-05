from django.urls import re_path
from .views import *
# from BackendApp.views.pickinglist import pickinglist

urlpatternsGuias = [
    # Nota:
    # Aqui se le indica a la aplicacion que cuando se le diga el ENPOINT en color naranja
    # Ejecute el archivo que esta en color amarillo al lado derecho
    # usp_obtenerDatosTranportadora
    re_path(r'^crearguia/bluelogistics$', crearguiablue),
    re_path(r'^crearguia/coordinadora$', crearguiacoordinadora),
    re_path(r'^crearguiacompleta/coordinadora$', crearguiacoordinadora_completo),
    re_path(r'^genera_rotulo_zpl/coordinadora$', genera_rotulo_zpl)
]
