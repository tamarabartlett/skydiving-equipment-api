import flask
from flask import request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint


app = flask.Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': ""
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


parachutes = [
       {'brand': 'Performance Designs',
        'model': 'Sabre 2',
        'size': 120,
        'nickname': 'Dave White',
        'colors': ['pink', 'black'],
        'serial_number': 0,
        'jumps': '200',
        'DOM': '2019',
        'date_bought': '07/2019',
        'date_updated': '07/2019',
        },
       {'brand': 'Performance Designs',
        'model': 'Sabre 2',
        'size': 135,
        'nickname': 'Sharlene',
        'colors': ['blue', 'purple', 'lime green'],
        'serial_number': 1,
        },
        {'brand': 'Performance Designs',
         'model': 'Sabre 2',
         'size': 135,
         'nickname': 'Larry',
         'colors': ['orange', 'blue', 'gray'],
         'serial_number': 2,
         }
]

aads = [
    {
        'serial_number':'40832',
        'brand':'Cypress',
        'DOM':'1/2008',
        'date_bought':'2/2016',
        'date_updated':'2/2016'
    },{
        'serial_number':'25266',
        'brand':'Vigil 2',
        'DOM':'7/2011',
        'date_bought':'4/2017',
        'date_updated':'2/2016'
    }
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>My Skydiving Equipment</h1><p>Prototype API to return info about my skydiving equipment</p>"


@app.route('/api/v1/equipment/parachutes/all', methods=['GET'])
def parachutes_all():
    return jsonify(parachutes)


@app.route('/api/v1/equipment/parachutes', methods=['GET'])
def parachute():
    if 'serial_number' in request.args:
        serial_number = int(request.args['serial_number'])
    else:
        return "Error: No serial_number field provided. Please specify an serial_number."

    results = []

    for parachute in parachutes:
        if parachute['serial_number'] == serial_number:
            results.append(parachute)

    return jsonify(results)


@app.route('/api/v1/equipment/aads/all', methods=['GET'])
def aads_all():
    return jsonify(aads)


if __name__ == '__main__':
    app.run()
