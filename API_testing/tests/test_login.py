import requests
import data
from conftest import User
from conftest import get_age, get_email, get_password, register_user

# ГОТОВЫ, будут работать, когда поставлю рандом на мейлы и пароли

def test_login_success():
    base_url = data.BASE_URL + "auth/login"
    
    test_user = User(get_email(), get_password(data.MIN_PASSWORD_LENGTH, data.MAX_PASSWORD_LENGTH), get_age(data.MIN_YOUNG_AGE,data.MAX_OLD_AGE))
    temp_token = register_user(test_user)

    request_data = {
        "email": test_user.email,
        "password": test_user.password,
    }
    
    response = requests.post(base_url, json=request_data)
   
    assert response.status_code == 200
    assert isinstance(response.json()['token'], str)
    assert isinstance(response.json()['user']['id'], int)
    assert response.json()['user']['email'] == test_user.email
    assert isinstance(response.json()['user']['name'], str)
    assert response.json()['user']['age'] == test_user.age
    assert temp_token == temp_token

def test_login_wrong_pass():
    base_url = data.BASE_URL + "auth/login"
    
    test_user = User(get_email(), get_password(data.MIN_PASSWORD_LENGTH, data.MAX_PASSWORD_LENGTH), get_age(data.MIN_YOUNG_AGE,data.MAX_OLD_AGE))
    temp_token = register_user(test_user)

    request_data = {
        "email": test_user.email,
        "password": get_password(data.MIN_PASSWORD_LENGTH, data.MAX_PASSWORD_LENGTH),
    }
    
    response = requests.post(base_url, json=request_data)
   
    assert response.status_code == 422
    assert response.json()['fields']['password'] == "Неправильный логин или пароль"
    assert temp_token == temp_token


def test_login_invalid_email():
    base_url = data.BASE_URL + "auth/login"
    
    request_data = {
        "email": get_email(),
        "password": get_password(data.MIN_PASSWORD_LENGTH, data.MAX_PASSWORD_LENGTH)
    }
    
    response = requests.post(base_url, json=request_data)
   
    assert response.status_code == 422
    assert response.json()['fields']['password'] == "Неправильный логин или пароль"