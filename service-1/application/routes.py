from application import app, db
from flask import render_template
from application.models import MLBDraft
import requests
from sqlalchemy import desc

@app.route('/', methods=['GET','POST'])
def index():
    picks = MLBDraft()
    
    position = requests.get('http://service-2:5000/position').text
    pick = requests.get('http://service-3:5000/pick').text

    response = requests.post('http://service-4:5000/draft pick',json={'position': position, 'pick': int(pick)})
    response_json=response.json()
    all_picks = MLBDraft.query.order_by(desc(MLBDraft.id)).limit(5).all()
    new_pick = MLBDraft(team=response_json['team'],position=position,pick=pick)
    db.session.add(new_pick)
    db.session.commit()

    return render_template('index.html', response=response_json['response'], picks=all_picks)
