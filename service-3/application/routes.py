from application import app
import random
from flask import jsonify

picks=list()
for i in range(31,61):
    picks.append(i)

@app.route('/pick', methods=['GET'])
def gen_pick():
    return str(random.choice(picks))
