import requests
from settings.models import config_api

def get_apikey(database):
    '''
    This function returns the apikey of the database

    Parameters:
    database (str): Database name
    '''

    try:
        c = config_api(database, 'apikey')
        apikey  = c.get_config()['apikey']

        return apikey
    
    except Exception as e:
        print(e)
        raise ValueError("Error getting apikey")



    # return requests.get(
    #     f'https://api.copernicowms.com/wms/get-apikey?database={database}').json()['apikey']