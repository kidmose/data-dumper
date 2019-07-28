from flask import Flask, request, jsonify


import json
import sys

from plate import Plate, PlateList

"""
Mock up of cloud API that can received info about plate produced.
"""

app = Flask(__name__)

plates_list = PlateList()

@app.route("/api/v0/getPlateList")
def getPlateList():
    return json.dumps([p.toDict() for p in plates_list.get_list()])

@app.route('/api/v0/addPlate', methods=['POST'])
def add_message():
    content = request.get_json()
    new_plate = Plate(content['serial'])

    plates_list.append(new_plate)

    return "Plate registered"

if __name__ == "__main__":
    app.run()

