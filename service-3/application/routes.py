from application import app
import random
from flask import jsonify

picks=list()
for i in range(1,31):
    picks.append(i)

@app.route('/pick', methods=['GET'])
def gen_pick():
    return jsonify(random.choice(picks))
