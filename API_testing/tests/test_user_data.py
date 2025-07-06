import requests
import data
from conftest import User
from conftest import get_age, get_email, get_password, get_name, register_user, login_user

def test_get_user_data_success():
    base_url = data.BASE_URL + "user/me"

    test_user = User(get_email(), get_password(data.MIN_PASSWORD_LENGTH, data.MAX_PASSWORD_LENGTH), get_age(data.MIN_YOUNG_AGE,data.MAX_OLD_AGE))
    temp_token1 = register_user(test_user)

    temp_token = login_user(test_user)
    header = {"Authorization": f"Bearer {temp_token}"}

    response = requests.get(base_url, headers=header)
   
    assert response.status_code == 200
    assert isinstance(response.json()['user']['id'], int)
    assert response.json()['user']['email'] == test_user.email
    assert isinstance(response.json()['user']['name'], str)
    assert response.json()['user']['age'] == test_user.age

def test_get_user_data_unauthorized():
    base_url = data.BASE_URL + "user/me"
    response = requests.get(base_url)
    assert response.status_code == 401