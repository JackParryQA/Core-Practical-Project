from application import app, db
from flask import render_template
from application.models import MLBDraft
import requests

@app.route('/', methods=['GET','POST'])
def index():
    picks = MLBDraft()
    all_picks = picks.query.all()
    position = requests.get('http://service-2:5001/position').text
    pick = requests.get('http://service-3:5002/pick').text
    team = requests.get('http://service-4:5003/Get Team').text

    response = requests.post('http://service-4:5003/Draft Pick',json={'position': position, 'pick': pick}).text
    
    new_pick = MLBDraft(team=team,position=position,pick=pick)
    db.session.add(new_pick)
    db.session.commit()

    return render_template('index.html', response=response, picks=all_picks)
