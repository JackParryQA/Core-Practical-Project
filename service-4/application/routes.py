from application import app
from flask import request,jsonify
import random



ALTeams=['Baltimore Orioles',
    'Boston Red Sox',
    'New York Yankees',
    'Tampa Bay Rays',
    'Toronto Blue Jays',
    'Chicago White Sox',
    'Cleveland Indians',
    'Detroit Tigers',
    'Kansas City Royals',
    'Minnesota Twins',
    'Houston Astros a.k.a Cheaters',
    'Los Angeles Angles',
    'Oakland Athletics',
    'Seattle Mariners',
    'Texas Rangers']

NLTeams=['Atlanta Braves',
    'Miami Marlins',
    'New York Mets',
    'Philadelphia Phillies',
    'Washinton Nationals',
    'Chicago Cubs',
    'Cincinnati Reds',
    'Milwaukee Brewers',
    'Pittsburgh Pirates',
    'St. Louis Cardinals',
    'Arizona Diamondbacks',
    'Colorado Rockies',
    'Los Angeles Dodgers',
    'San Diego Padres',
    'San Francisco Giants']


@app.route('/draft pick', methods=['GET','POST'])
def draftpick():
    data_sent=request.get_json()
    pick = data_sent['pick']
    if pick%2==0:
        team = random.choice(ALTeams)
    else:
        team = random.choice(NLTeams)
    return jsonify({'response':f'We are now in the second round\nWith pick { data_sent["pick"] } in the 2021 MLB Draft the { team } have selected a { data_sent["position"] }', 'team':team})