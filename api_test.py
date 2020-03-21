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


if __name__ == '__main__':
    unittest.main()
