import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

parachutes = [
       {'brand': 'Performance Designs',
        'model': 'Sabre 2',
        'size': 120,
        'nickname': 'Dave White',
        'colors': ['pink', 'black'],
        'serial_number': 0,
        # 'jumps'
        # 'DOM'
        # 'date_bought'
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


app.run()
