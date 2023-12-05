import requests

def delete_article():

    base = 'http://api.copernicowms.com:8000/'
    endpoint = 'wms/art'

    url = base + endpoint

    headers = {
        'Authorization': 'D3SdWq_zZeXmKzskizku2_iJpd5RMt3mfHIOe3MTKqshXmFF9pjY7bmylxl2khZTIak'
    }

    params = {
        'productoean': '20'
    }

    response = requests.delete(url, headers=headers, params=params)

    return response.json()

