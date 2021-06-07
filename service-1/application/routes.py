from application import app, db
from flask import render_template
from application.models import MLBDraft
import request

@app.route('/', methods=['GET','POST'])
def index():
    picks = MLBDraft()
    all_picks = picks.query.all()
    position = request.get('http://service-2:5001').text
    pick = request.get('http://service-3:5002').text

    response = request.post('http://service-4:5003',json={position,pick}).json

    return render_template('index.html', response=response, picks=all_picks)
