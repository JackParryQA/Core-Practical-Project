from application import app
import random

positions = ['SP','RP','CP','C','1B','2B','3B','SS','LF','CF','RF']

@app.route('/position')
def gen_position():
    return random.choice(positions)