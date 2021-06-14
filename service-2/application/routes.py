from application import app
import random

# positions = ['SP','RP','CP','C','1B','2B','3B','SS','LF','CF','RF']
positions = ['Starting Pitcher','Relief Pitcher','Closing Pitcher','Catcher','1st Baseman','2nd Baseman','3rd Baseman','Short Stop','Left Field','Center Field','Right Field']

@app.route('/position', methods=['GET'])
def gen_position():
    return random.choice(positions)