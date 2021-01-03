import unittest
import requests
import json
import jsonpath
from connfig_api import *


class MyTestCase(unittest.TestCase):

    def test_show_all_certificates_get200(self):
        url = url_base+url_all
        response = requests.get(url)
        assert response.status_code == 200

    def test_show_all_certificates_post500(self):
        url = url_base+url_all
        response = requests.post(url)
        assert response.status_code == 500

    def test_show_all_certificates_heders(self):
        url = url_base+url_all
        response = requests.get(url)
        response_type = response.headers['Content-Type']
        response_transfer = response.headers['transfer-encoding']
        response_date = response.headers['date']

        assert response_type == content_type
        assert response_transfer == transfer_encoding

    def test_show_id_query_params_get200(self):
        url = url_base+url_query_params+query_params_ok
        response = requests.get(url)
        assert response.status_code == 200

    def test_show_id_query_params_response(self):
        url = url_base+url_query_params+query_params_ok
        response = requests.get(url)
        response_id = json.loads(response.text)
        assert response_id['id'] == 1
        assert response_id == {'id': 1, 'organization': 'ISTQB', 'name': 'TEST ANALYST', 'period': 'BEZTERMINOWO', 'trade': 'IT'}

    def test_show_id_query_params_get404(self):
        url = url_base+url_query_params+query_params_error
        response = requests.get(url)
        assert response.status_code == 404

    def test_add_certificate_post201(self):
        url = url_base+url_post
        f = open('add_certificate.json', 'r')
        json_input = f.read()
        f.close()
        request_json = json.loads(json_input)
        response_post = requests.post(url, json=request_json)
        response_json = json.loads(response_post.text)
        id_post = jsonpath.jsonpath(response_json, 'id')
        organization_post = jsonpath.jsonpath(response_json, 'organization')
        name_post = jsonpath.jsonpath(response_json, 'name')
        period_post = jsonpath.jsonpath(response_json, 'period')
        trade_post = jsonpath.jsonpath(response_json, 'trade')
        assert response_post.status_code == 201
        assert organization_post[0] == '2018wsbTest'
        assert name_post[0] == 'Hellprod'
        assert period_post[0] == 'bezterminowo'
        assert trade_post[0] == 'MTB'

    def test_add_certificate_post500(self):
        url = url_base+url_post
        f = open('add_certificate_error.json', 'r')
        json_input = f.read()
        f.close()
        request_json = json.loads(json_input)
        response_post = requests.post(url, json=request_json)
        assert response_post.status_code == 500

    def test_certificate_put200(self):
        id_put = "2"
        url = url_base+url_put+id_put
        f = open('put_certificate.json', 'r')
        json_input = f.read()
        f.close()
        request_json = json.loads(json_input)
        response_put = requests.put(url, json=request_json)
        response_json = json.loads(response_put.text)
        id_put = jsonpath.jsonpath(response_json, 'id')
        organization_put = jsonpath.jsonpath(response_json, 'organization')
        name_put = jsonpath.jsonpath(response_json, 'name')
        period_put = jsonpath.jsonpath(response_json, 'period')
        trade_put = jsonpath.jsonpath(response_json, 'trade')
        assert response_put.status_code == 200
        assert organization_put[0] == '2018wsbTest'
        assert name_put[0] == 'Zmiana'
        assert period_put[0] == '2022'
        assert trade_put[0] == 'XC'

    def test_certificate_put500(self):
        id_put = "2"
        url = url_base+url_put+id_put
        f = open('add_certificate_error.json', 'r')
        json_input = f.read()
        f.close()
        request_json = json.loads(json_input)
        response_put = requests.post(url, json=request_json)
        assert response_put.status_code == 500

    def test_non_existent_certificate_put404(self):
        id_put = "222"
        url = url_base+url_put+id_put
        f = open('add_certificate.json', 'r')
        json_input = f.read()
        f.close()
        request_json = json.loads(json_input)
        response_put = requests.put(url, json=request_json)
        assert response_put.status_code == 404

    def test_show_id_path_params_get200(self):
        url = url_base+url_path_params+path_params_ok
        response = requests.get(url)
        assert response.status_code == 200

    def test_show_id_path_params_response(self):
        url = url_base+url_path_params+path_params_ok
        response = requests.get(url)
        response_id = json.loads(response.text)
        assert response_id['id'] == 1
        assert response_id == {'id': 1, 'organization': 'ISTQB', 'name': 'TEST ANALYST', 'period': 'BEZTERMINOWO', 'trade': 'IT'}

    def test_show_id_path_params_get404(self):
        url = url_base+url_path_params+path_params_error
        response = requests.get(url)
        assert response.status_code == 404

    def test_delete_delete200(self):
        url = url_base+url_delete+delete_id
        response_delete = requests.delete(url)
        assert response_delete.status_code == 200

    def test_delete_delete404(self):
        url = url_base+url_delete+delete_id_error
        response_delete = requests.delete(url)
        assert response_delete.status_code == 404

    def test_delete_add_certificate_delete200(self):
        url = url_base+url_all
        response = requests.get(url)
        response_text = response.text
        response_json = json.loads(response_text)
        last_id = response_json[-1]['id']
        url = url_base + url_delete + str(last_id)
        response_delete = requests.delete(url)
        assert response_delete.status_code == 200


if __name__ == '__main__':
    unittest.main()
