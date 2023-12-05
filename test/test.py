import os
import time
import pyodbc
import sqlite3
import unittest



############################################
direccion_servidor = '190.109.22.18,11443'
nombre_bd_BASE     = 'CO_PTH_BASE'        #
nombre_bd_ADAPTER  = 'CO_PTH_ADAPTER'       #
nombre_usuario     = 'sgvsoftware'         #
password           = 'O%O017ecy$2Q'            #
############################################

class Testing(unittest.TestCase):
    def test_database(self):
        try:
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                direccion_servidor+';DATABASE='+nombre_bd_BASE+';UID='+nombre_usuario+';PWD=' + password, timeout=5)
            print("SE CONECTO EXITOSAMENTE")
        except:
            print("NO SE PUDO CONECTAR")


if __name__ == '__main__':
    unittest.main()
