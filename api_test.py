import json
import unittest
from api import app

def test_home():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'<h1>My Skydiving Equipment</h1><p>Prototype API to return info about my skydiving equipment</p>'

def test_get_all_parachutes():
    response = app.test_client().get('/api/v1/equipment/parachutes/all')

    assert response.status_code == 200
    assert len(json.loads(response.data)) == 3

def test_get_parachute_no_serial_number():
    response = app.test_client().get('/api/v1/equipment/parachutes')

    assert response.status_code == 200
    assert response.data == b'Error: No serial_number field provided. Please specify an serial_number.'

def test_parachute_fields():
    response = app.test_client().get('/api/v1/equipment/parachutes?serial_number=0')

    assert response.status_code == 200
    jsonData = json.loads(response.data)
    parachute = jsonData[0]

    serial_number_key = 'serial_number' in parachute
    brand_key = 'brand' in parachute
    model_key = 'model' in parachute
    size_key = 'size' in parachute
    nickname_key = 'nickname' in parachute
    colors_key = 'colors' in parachute
    jumps_key = 'jumps' in parachute
    DOM_key = 'DOM' in parachute
    date_bought_key = 'date_bought' in parachute
    date_updated_key = 'date_updated' in parachute

    assert serial_number_key == True
    assert brand_key == True
    assert model_key == True
    assert size_key == True
    assert nickname_key == True
    assert colors_key == True
    assert jumps_key == True
    assert DOM_key == True
    assert date_bought_key == True
    assert date_updated_key == True

def test_aads_fields():
    response = app.test_client().get('/api/v1/equipment/aads/all')

    assert response.status_code == 200
    jsonData = json.loads(response.data)
    aad = jsonData[0]

    serial_number_key = 'serial_number' in aad
    brand_key = 'brand' in aad
    DOM_key = 'DOM' in aad
    date_bought_key = 'date_bought' in aad
    date_updated_key = 'date_updated' in aad

    assert serial_number_key == True
    assert brand_key == True
    assert DOM_key == True
    assert date_bought_key == True
    assert date_updated_key == True


if __name__ == '__main__':
    unittest.main()
