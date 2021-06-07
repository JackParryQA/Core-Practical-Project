from application import app, db
from flask import render_template
from application.models import MLBDraft
import requests

@app.route('/')
def index():
    picks = MLBDraft()
    all_picks = picks.query.all()
    response = requests.get('http://service_4:5003').text
    return render_template('index.html', response=response, picks=all_picks)