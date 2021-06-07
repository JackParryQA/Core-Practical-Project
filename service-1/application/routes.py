from application import app, db
from flask import render_template
from application.models import MLBDraft
import requests

@app.route('/')
def index():
    picks = MLBDraft()
    all_picks = picks.query.all()
    position = requests.get('http://service-2:5001').text
    pick = requests.get('http://service-3:5002').text

    response = requests.post('http://service-4:5003',json={position,pick}).json

    return render_template('index.html', response=response, picks=all_picks)