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
    # team = requests.get('http://service-4:5003/Get Team').text

    team = requests.post('http://service-4:5000/Draft Pick',json={'position': position, 'pick': int(pick)}).text

    all_picks = MLBDraft.query.order_by(desc(MLBDraft.id)).limit(5).all()
    new_pick = MLBDraft(team=team,position=position,pick=pick)
    db.session.add(new_pick)
    db.session.commit()

    return render_template('index.html',  team=team, pick=pick, position=position, picks=all_picks)
