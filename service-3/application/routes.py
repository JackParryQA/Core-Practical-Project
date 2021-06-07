from application import app
import random

picks=list()
for i in raneg(1,31):
    picks.append(i)

@app.route('/pick')
def gen_pick():
    return random.choice(picks)
