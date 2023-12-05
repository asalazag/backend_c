import requests
import unittest

APIKEY = '8Yd61laeBJy6vFqgmiqLMNNab2w4WsTl_gxCX9zT3qHO2e9g4UQmIk7HqHw63TOoXPg'
db = 'co_usp_adapter'

def get_articles(params=None):

    base = 'https://api.copernicowms.com/'
    endpoint = 'wms/art'

    url = base + endpoint

    headers = {
        'Authorization': APIKEY
    }

    if params:
        response = requests.get(url, headers=headers, params=params)
    else:
        params = params

        response = requests.get(url, headers=headers, params=params)

    return response.json()


def post_article(json: dict):

    base = 'https://api.copernicowms.com/'
    endpoint = 'wms/art'

    url = base + endpoint

    headers = {
        'Authorization': APIKEY
    }

    response = requests.post(url, headers=headers, json=json)

    return response.json()


def put_article(params: dict, json: dict):

    base = 'https://api.copernicowms.com/'
    endpoint = 'wms/art'

    url = base + endpoint

    headers = {
        'Authorization': APIKEY
    }

    response = requests.put(url, headers=headers, params=params, json=json)

    return response.json()


def delete_article(params: dict):

    base = 'https://api.copernicowms.com/'
    endpoint = 'wms/art'

    url = base + endpoint

    headers = {
        'Authorization': APIKEY
    }

    response = requests.delete(url, headers=headers, params=params)

    return response.json()





class TestTdaWmsArt(unittest.TestCase):

    def test_read_articles1(self):
        params = {
            'productoean': '01010105'
        }
        self.assertEqual(str(type(get_articles(params))), "<class 'list'>", "Should be <class 'list'>")


    def test_read_articles2(self):
        params = {
            'productoean': '20202020'
        }
        self.assertEqual(str(type(get_articles(params))), "<class 'list'>", "Should be <class 'list'>")


    def test_read_articles3(self):
        params = {
            'productoea': '984724896752983'
        }
        self.assertEqual(str(type(get_articles(params))), "<class 'dict'>", "Should be <class 'dict'>")


    def test_read_articles4(self):
        params = {
            'productoea': '984724896752983'
        }
        self.assertEqual(get_articles(params), {'message': 'Field productoea not found'}, {'message': 'Field productoea not found'})


    def test_read_articles5(self):
        params = {
            'productoean': '20',
            'cost': '20'
        }
        self.assertEqual(get_articles(params), {'message': 'Field cost not found'}, "Should be {'message': 'Field cost not found'}")





    def test_post_articles1(self):
        json = {
            'productoean': '20202020'
        }
        self.assertEqual(post_article(json), {'error': f'(\'23000\', "[23000] [microsoft][odbc driver 17 for sql server][sql server]cannot insert the value null into column \'referencia\', table \'{db}.dbo.tda_wms_art\'; column does not allow nulls. insert fails. (515) (sqlexecdirectw)")'}, "Should be an error message")

    def test_post_articles2(self):
        json = {
            'productoea': '20202020'
        }
        self.assertEqual(post_article(json), {'error': 'Field productoea not found'}, {'error': 'Field productoea not found'})


    def test_post_articles3(self):
        json = {
            'productoean': '20202020',
            'referencia': '20202020'
        }
        self.assertEqual(post_article(json),{'error': f'(\'23000\', "[23000] [microsoft][odbc driver 17 for sql server][sql server]cannot insert the value null into column \'nuevoean\', table \'{db}.dbo.tda_wms_art\'; column does not allow nulls. insert fails. (515) (sqlexecdirectw)")'}, "Should be an error message")


    def test_post_articles4(self):
        json = {
            'productoean': '20202020',
            'referencia': '20202020',
            'nuevoean': '20202020'
        }

        self.assertEqual(post_article(json),{'success': 'Article created'}, {'success': 'Article created'})

    def test_post_articles5(self):
        json = {
            'productoean': '20202020',
            'referencia': '20202020',
            'nuevoean': '20202020'
        }

        self.assertEqual(post_article(json),{'error': 'The product with productoean 20202020 already exists'}, {'error': 'The product with productoean 20202020 already exists'})




    def test_put_articles1(self):
        params = {
            'productoean': '20202020'
        }
        json = {
            'productoean': 'Unittest'
        }

        self.assertEqual(put_article(params, json),{'error': 'The productoean field cannot be updated'},{'error': 'The productoean field cannot be updated'})


    def test_put_articles2(self):
        params = {
            'productoean': '20202020'
        }
        json = {
            'descripcio': 'Unittest'
        }

        self.assertEqual(put_article(params, json),{'error': 'Field descripcio not found in the body'},{'error': 'Field descripcio not found in the body'})


    def test_put_articles3(self):
        params = {
            'productoea': '20202020'
        }
        json = {
            'descripcion': 'Unittest'
        }

        self.assertEqual(put_article(params, json),{'error': 'Field productoea not found'},{'error': 'Field productoea not found'})



    def test_put_articles4(self):
        params = {}
        json = {
            'descripcion': 'Unittest'
        }

        self.assertEqual(put_article(params,json),{'error': 'Only one product can be updated at a time'},{'error': 'Only one product can be updated at a time'})


    def test_put_articles5(self):
        params = {
            'productoean': '20202020'
        }
        json = {}

        self.assertEqual(put_article(params, json),{"error": "No data to update"},{"error": "No data to update"})


    def test_put_articles6(self):
        params = {
            'productoean': '20202020'
        }
        json = {
            'descripcion': 'Unittest'
        }


        self.assertEqual(put_article(params, json),{'success': 'Article updated'},{'success': 'Article updated'})




    def test_delete_articles1(self):
        params = {
            'productoea': '20202020'
        }
        self.assertEqual(delete_article(params), {'error': 'Field productoea not found'}, "Should be {'error': 'Field productoea not found'}")


    def test_delete_articles2(self):
        params = {}
        self.assertEqual(delete_article(params), {'error': 'More than one product found'}, {'error': 'More than one product found'})


    def test_delete_articles3(self):
        params = {
            'productoean': '20202020'
        }
        self.assertEqual(delete_article(params), {'success': 'Article deleted'}, {'success': 'Article deleted'})

    def test_delete_articles4(self):
        params = {
            'productoean': '20202020'
        }
        self.assertEqual(delete_article(params), {'error': 'Product not found'}, {'error': 'Product not found'})




if __name__ == '__main__':
    unittest.main()