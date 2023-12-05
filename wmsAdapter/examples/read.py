import requests

def get_articles(params=None):

    base = 'http://api.copernicowms.com:8000/'
    endpoint = 'wms/art'

    url = base + endpoint

    headers = {
        'Authorization': 'D3SdWq_zZeXmKzskizku2_iJpd5RMt3mfHIOe3MTKqshXmFF9pjY7bmylxl2khZTIak'
    }

    if params:
        response = requests.get(url, headers=headers, params=params)
    else:
        params = {
            'productoean': '0'
        }

        response = requests.get(url, headers=headers, params=params)

    return response.json()

