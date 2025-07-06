import requests
import data
from conftest import User
from conftest import get_email, get_password, get_age, register_user

# написано, работают (если сделать рандом на данные)

def test_register_success():
    test_user = User(get_email(), get_password(data.MIN_PASSWORD_LENGTH, data.MAX_PASSWORD_LENGTH), get_age(data.MIN_YOUNG_AGE,data.MAX_OLD_AGE))
    base_url = data.BASE_URL + "auth/register"

    request_data = {
        "email": test_user.email,
        "password": test_user.password,
        "age": test_user.age
    }
    
    # print(request_data)


    response = requests.post(base_url, json=request_data)
    # print(response.text)

    assert response.status_code == 200
    assert isinstance(response.json()['token'], str)
    assert isinstance(response.json()['user']['id'], int)
    assert response.json()['user']['email'] == test_user.email
    assert response.json()['user']['age'] == test_user.age


def test_register_twice():
    base_url = data.BASE_URL + "auth/register"
    
    test_user = User(get_email(), get_password(data.MIN_PASSWORD_LENGTH, data.MAX_PASSWORD_LENGTH), get_age(data.MIN_YOUNG_AGE,data.MAX_OLD_AGE))
    temp_token = register_user(test_user)

    request_data = {
        "email": test_user.email,
        "password": test_user.password,
        "age": test_user.age
    }
    
    response = requests.post(base_url, json=request_data)
   
    assert response.status_code == 422
    assert response.json()['fields']['email'] == "Пользователь с таким email уже существует"
    # assert isinstance(response.json()['additionalProp1'], str)
    # assert isinstance(response.json()['additionalProp2'], str)
    # assert isinstance(response.json()['additionalProp3'], str)
    assert temp_token == temp_token

