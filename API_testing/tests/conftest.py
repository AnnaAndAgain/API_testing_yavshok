import random
import data
import requests
import secrets
import string

from faker import Faker
from faker.providers import internet, person

class User:
  def __init__(self, email, password, age):
    self.email = email
    self.password = password
    self.age = age

def get_email():
    fake = Faker()
    fake.add_provider(internet)

    new_email = fake.safe_email()
    return new_email

def get_password(min_length, max_length):
    alphabet = string.ascii_letters + string.digits
    pass_length = random.randint(min_length, max_length)

    new_password = ''.join(secrets.choice(alphabet) for i in range(pass_length))
    return new_password

def get_age(min_age, max_age):
   new_age = random.randint(min_age, max_age)
   return new_age

def get_name():
    fake = Faker()
    fake.add_provider(person)

    new_name = fake.name()
    return new_name

def register_user(user_data):
    base_url = data.BASE_URL + "auth/register"
    
    request_data = {
        "email": user_data.email,
        "password": user_data.password,
        "age": user_data.age
        }
    
    response = requests.post(base_url, json=request_data)
    my_token = response.json()['token']

    return my_token

def login_user(user_data):
    base_url = data.BASE_URL + "auth/login"
    
    request_data = {
        "email": user_data.email,
        "password": user_data.password,
    }
    
    response = requests.post(base_url, json=request_data)
    return response.json()["token"]
