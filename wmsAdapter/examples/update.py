import requests

def put_article():

    base = 'http://api.copernicowms.com:8000/'
    endpoint = 'wms/art'

    url = base + endpoint

    headers = {
        'Authorization': 'D3SdWq_zZeXmKzskizku2_iJpd5RMt3mfHIOe3MTKqshXmFF9pjY7bmylxl2khZTIak'
    }

    params = {
        'productoean': '20'
    }

    json = {
        # 'productoean': '20',
        'referencia': '21',
        'nuevoean': '21'
    }

    response = requests.put(url, headers=headers, params=params, json=json)

    
    return response.json()