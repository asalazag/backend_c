"""" Dependencies """
import requests

""" Functions """
from BackendApp.functions.api.apikey import get_apikey


def create_dynamic_queries(db_name:str,body:dict) :
    '''
    Create dynamic queries

    Parameters:
    db_name (str): Database name
    body (dict): Body request

    '''

    try: 

        # Get apikey
        apikey = get_apikey(db_name)

        # Url
        url = "https://api.copernicowms.com/wms/dynamic_queries"
        
        # Headers
        headers = {
            "Authorization": apikey
        }

        # Body
        body = dict(body)

        # Remove keys
        body.pop('database')
        body.pop('id_employee')
        body.pop('warehouse')
        body.pop('id_customer')
        body.pop('role')

        # Request
        response = requests.post(url, headers=headers, json=body)

        # Return response
        return response
    
    # Error
    except Exception as e:
        print (str(e))
        raise ValueError(str(e))

def read_dynamic_queries(db_name:str,params=None) :
    '''
    Get dynamic queries

    Parameters:
    db_name (str): Database name
    params (dict): Params request
    '''

    try: 

        # Get apikey
        apikey = get_apikey(db_name)

        # Url
        url = "https://api.copernicowms.com/wms/dynamic_queries"
        
        # Headers
        headers = {
            "Authorization": apikey
        }

        # Body
        if params is None:
            params = {}
        else:
            params = dict(params)

        # Request
        response = requests.get(url, headers=headers, params=params)
        print(response.json())
        # Return response
        return response
    
    # Error
    except Exception as e:
        print (str(e))
        raise ValueError(str(e))
    

def update_dynamic_queries(db_name:str,params={}, body={}) :
    '''
    update dynamic queries

    Parameters:
    db_name (str): Database name
    params (dict): Params request
    body (dict): Body request
    '''

    try: 

        # Get apikey
        apikey = get_apikey(db_name)

        # Url
        url = "https://api.copernicowms.com/wms/dynamic_queries"
        
        # Headers
        headers = {
            "Authorization": apikey
        }

        # Body
        if params is None:
            params = {}
        else:
            params = dict(params)

        if body is None:
            body = {}
        else:
            body = dict(body)

        if params == {} or body == {}:
            raise ValueError('Params or body is empty')
        
        # Remove keys
        body.pop('database')
        body.pop('id_employee')
        body.pop('warehouse')
        body.pop('id_customer')
        body.pop('role')

        # Request
        response = requests.put(url, headers=headers, params=params, json=body)
        print(response.json())
        # Return response
        return response
    
    # Error
    except Exception as e:
        print (str(e))
        raise ValueError(str(e))
    
def delete_dynamic_queries(db_name:str,params={}) :
    '''
    delete dynamic queries

    Parameters:
    db_name (str): Database name
    params (dict): Params request
    '''

    try: 

        # Get apikey
        apikey = get_apikey(db_name)

        # Url
        url = "https://api.copernicowms.com/wms/dynamic_queries"
        
        # Headers
        headers = {
            "Authorization": apikey
        }

        # Body
        if params is None:
            params = {}
        else:
            params = dict(params)

        if params == {}:
            raise ValueError('Params is empty')

        # Request
        response = requests.delete(url, headers=headers, params=params)
        print(response.json())
        # Return response
        return response
    
    # Error
    except Exception as e:
        print (str(e))
        raise ValueError(str(e))
    

def execute_dynamic_queries(db_name:str,params={}) :
    '''
    execute dynamic queries

    Parameters:
    db_name (str): Database name
    body (dict): Body request
    '''

    try: 

        # Get apikey
        apikey = get_apikey(db_name)

        # Url
        url = "https://api.copernicowms.com/wms/execute/dynamic_queries"
        
        # Headers
        headers = {
            "Authorization": apikey
        }

        # Body
        if params is None:
            params = {}
        else:
            params = dict(params)

        if params == {}:
            raise ValueError('Params is empty')

        # Request
        response = requests.post(url, headers=headers, params=params)
        print(response.json())
        # Return response
        return response
    
    # Error
    except Exception as e:
        print (str(e))
        raise ValueError(str(e))