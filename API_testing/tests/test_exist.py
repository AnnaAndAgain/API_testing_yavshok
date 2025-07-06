import requests
import data
from conftest import get_email, get_age, get_password, register_user
from conftest import User

#--РАБОТАЮТ, если прикрутить рандомайзер (иначе первый перебивает второй)--

def test_exist_true():
    base_url = "http://localhost:3000/exist"
    
    test_user = User(get_email(), get_password(data.MIN_PASSWORD_LENGTH, data.MAX_PASSWORD_LENGTH), get_age(data.MIN_YOUNG_AGE,data.MAX_OLD_AGE))
    temp_token = register_user(test_user)
    
    request_data = {"email": test_user.email}
    
    response = requests.post(base_url, json=request_data)
    
    assert response.json()['exist'] == True
    assert temp_token == temp_token


def test_exist_false():
    base_url = "http://localhost:3000/exist"
    unused_email = get_email()
    
    request_data = {
            "email": unused_email
        }

    response = requests.post(base_url, json=request_data)

    assert response.json()['exist'] == False


