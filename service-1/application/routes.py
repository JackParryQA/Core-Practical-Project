from application import app, db
from flask import render_template
from application.models import MLBDraft
import requests

@app.route('/', methods=['GET','POST'])
def index():
    picks = MLBDraft()
    # all_picks = picks.query.all()
    position = requests.get('http://service-2:5000/position').text
    pick = requests.get('http://service-3:5000/pick').text
    # team = requests.get('http://service-4:5003/Get Team').text

    team = requests.post('http://service-4:5000/Draft Pick',json={'position': position, 'pick': int(pick)}).text
    print(team)
    # new_pick = MLBDraft(team=team,position=position,pick=pick)
    # db.session.add(new_pick)
    # db.session.commit()

    return render_template('index.html',  team=team, pick=pick, position=position)
