# setings.py

url_base = "https://reqres.in"
url_users = "/api/users"
url_login = "/api/login"
url_list_users = url_users + "?page=2"
url_single_user = url_users + "/2"
url_single_user_not_found = url_users + "/23"
url_list_resource = "/api/unknown"
url_single_resource = url_list_resource + "/2"
url_single_resource_not_found = url_list_resource + "/23"
url_register_successful = "/api/register"
url_delayed_response = url_users + "?delay=3"


data_user = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

data_create = {
    "name": "morpheus",
    "job": "leader"
}

data_update = {
    "name": "morpheus",
    "job": "zion resident"
}

data_register_successful = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

data_register_unsuccessful = {
    "email": "eve.holt@reqres.in"
}