import requests
from BackendApp.functions.api.apikey import get_apikey


def create_shipstation_label(db_name, picking):

    try:
        apikey = get_apikey(db_name)

        print("apikey: ", apikey)

        url = "https://api.copernicowms.com/shipstation/orders"

        headers = {
            "Authorization": apikey
        }

        params = {
            "picking": picking
        }

        print("payload: ", params)


        response = requests.post(url, headers=headers, params=params)

        
        return response
    except Exception as e:
        print(e)
        raise Exception("Error creating label")