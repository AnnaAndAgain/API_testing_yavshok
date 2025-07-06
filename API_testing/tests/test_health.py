import requests
import data

#--ГОТОВ, РАБОТАЕТ--

def test_health():
    base_url = data.BASE_URL + "health"

    response = requests.get(base_url)
    assert response.status_code == 200
    
 
    