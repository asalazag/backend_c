import requests

def post_article():

    base = 'http://api.copernicowms.com:8000/'
    endpoint = 'wms/art'

    url = base + endpoint

    headers = {
        'Authorization': 'D3SdWq_zZeXmKzskizku2_iJpd5RMt3mfHIOe3MTKqshXmFF9pjY7bmylxl2khZTIak'
    }

    # params = {
    #     'productoean': '0'
    # }

    json = {
        'productoean': '20',
        'referencia': '20',
        'nuevoean': '20'
    }

    response = requests.post(url, headers=headers, json=json)

    return response.json()