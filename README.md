# Equipment API
Creating an API for funzies to return information about my skydiving equipment. Eventually will dockerize and maybe try to deploy to goog cloud

## Requirements
flask
python 3.7.0

## To Setup
`pip3 install flask`
`pip3 install pytest`

## To Test
`pytest`

## To Run
`export FLASK_APP=api.py`
`flask run`


#API
### /
Homesite
### /api/v1/equipment/parachutes/all
GET all parachutes
### /api/v1/equipment/parachutes?serial_number={SERIAL_NUMBER}
GET parachute with serial number SERIAL_NUMBER
### /api/v1/equipment/aads/all
GET all aads
