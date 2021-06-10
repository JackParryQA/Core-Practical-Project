from application import app
import random
from flask import jsonify


@app.route('/pick', methods=['GET'])
def gen_pick():
    return jsonify(random.choice(random.randint(31,60)))
