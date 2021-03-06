import pytest
import requests
import json
import API.TestsApiPyTests.setings as s

def take_token(url_b, url_, user, password):
    url = url_b + url_
    data = {
        "email": user,
        "password": password
    }
    resposne = requests.post(url, data=data)
    res_token = json.loads(resposne.text)
    return res_token['token']


def test_login_successful():
    url = s.url_base + s.url_login
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    resposne = requests.post(url, data=data)
    res_token = json.loads(resposne.text)
    assert resposne.status_code == 200
    assert res_token["token"] == "QpwL5tke4Pnpja7X4"


print(take_token(s.url_base, s.url_login, s.data_user['email'], s.data_user['password']))


def test_token():
    res_token = take_token(s.url_base, s.url_login, s.data_user['email'], s.data_user['password'])
    assert res_token == "QpwL5tke4Pnpja7X4"


def test_list_users():
    url = s.url_base + s.url_login
    resposne = requests.get(url)
    assert resposne.status_code == 200


def test_list_users_short():
    assert requests.get(s.url_base + s.url_login).status_code == 200


def test_single_user():
    assert requests.get(s.url_base + s.url_single_user).status_code == 200


def test_single_user_not_found():
    assert requests.get(s.url_base + s.url_single_user_not_found).status_code == 404


def test_list_resource():
    assert requests.get(s.url_base + s.url_list_resource).status_code == 200


def test_single_resource():
    assert requests.get(s.url_base + s.url_single_resource).status_code == 200


def test_single_resource_not_found():
    assert requests.get(s.url_base + s.url_single_resource_not_found).status_code == 404


def test_create():
    data = s.data_create
    assert requests.post(s.url_base + s.url_users, data).status_code == 201


def test_put_update():
    data = s.data_update
    assert requests.put(s.url_base + s.url_single_user, data).status_code == 200


def test_patch_update():
    data = s.data_update
    assert requests.patch(s.url_base + s.url_single_user, data).status_code == 200


def test_delete():
    assert requests.delete(s.url_base + s.url_single_user).status_code == 204


def test_register_successful():
    data = s.data_register_successful
    assert requests.post(s.url_base + s.url_register_successful, data).status_code == 200


def test_register_unsuccessful():
    data = s.data_register_unsuccessful
    assert requests.post(s.url_base + s.url_register_successful, data).status_code == 400


def test_login_unsuccessful():
    data = s.data_register_unsuccessful
    assert requests.post(s.url_base + s.url_login, data).status_code == 400


def test_delayed_response():
    assert requests.get(s.url_base + s.url_delayed_response).status_code == 200



####
@pytest.mark.parametrize("url_x", [s.url_single_resource, s.url_list_resource, s.url_single_user, s.url_list_users, s.url_users, s.url_delayed_response])
def test_multi(url_x):
    assert requests.get(s.url_base + url_x).status_code == 200


@pytest.mark.parametrize("url_x", [s.url_single_user_not_found, s.url_single_resource_not_found])
def test_multi_not_found(url_x):
    assert requests.get(s.url_base + url_x).status_code == 404


@pytest.mark.parametrize("url_x, data_x", [(s.url_login, s.data_register_unsuccessful), (s.url_register_successful, s.data_register_unsuccessful)])
def test_unsuccessful(url_x, data_x):
    data = data_x
    assert requests.post(s.url_base + url_x, data).status_code == 400


