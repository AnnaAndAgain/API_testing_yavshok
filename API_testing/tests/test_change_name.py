import requests
import data
from conftest import User
from conftest import get_age, get_email, get_password, get_name, register_user, login_user

def test_change_name_success():
    base_url = data.BASE_URL + "user/name"
    new_name = get_name()

    test_user = User(get_email(), get_password(data.MIN_PASSWORD_LENGTH, data.MAX_PASSWORD_LENGTH), get_age(data.MIN_YOUNG_AGE,data.MAX_OLD_AGE))
    temp_token1 = register_user(test_user)

    temp_token = login_user(test_user)

    request_data = {"name": new_name}
    header = {"Authorization": f"Bearer {temp_token}"}

    response = requests.patch(base_url, headers=header, json=request_data)
   
    assert response.status_code == 200
    assert isinstance(response.json()['user']['id'], int)
    assert response.json()['user']['email'] == test_user.email
    assert response.json()['user']['name'] == new_name
    assert response.json()['user']['age'] == test_user.age

def test_change_name_unauthorized():
    base_url = data.BASE_URL + "user/name"
    new_name = get_name()

    request_data = {"name": new_name}

    response = requests.patch(base_url, json=request_data)
   
    assert response.status_code == 401