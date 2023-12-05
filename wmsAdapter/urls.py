from .views import *
from django.urls import re_path
from settings import *

wms_endpoints = [
    re_path(r'^art$', article),
    re_path(r'^epk$', epk),
    re_path(r'^epkLabels$', epkLabels),
    re_path(r'^dpk$', dpk),
    re_path(r'^euk$', euk),
    re_path(r'^duk$', duk),
    re_path(r'^epn$', epn),
    re_path(r'^dpn$', dpn),
    re_path(r'^clt$', clt),
    re_path(r'^prv$', prv),
    re_path(r'^prv_ext$', prv),
    re_path(r'^execute$', executeSp),
    re_path(r'^get-apikey$', get_apikey),
    # re_path(r'^create-apikey$', create_apikey),
    re_path(r'^history$', vtggtpicmp),
    re_path(r'^location$', vtpicmp),
    re_path(r'^insert/inv$', insertinv),
    re_path(r'^update/inv$', updatetinv),
    re_path(r'^update/euk$', updateEuk),
    re_path(r'^read/filterclt', filterclt),
    re_path(r'^read/filterart', filterart),
    re_path(r'^read/filterprv', filterprv),
    re_path(r'^kit', kit),

]

# for i in global_settings():
#     wms_endpoints.append(re_path(r'^'+i+'/art$', article))
