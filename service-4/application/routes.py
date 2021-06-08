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


@app.route('/Draft Pick', methods=['GET','POST'])
def draftpick():
    data_sent=request.get_json('utf-8')
    pick = data_sent['pick']
    if pick%2==0:
        return random.choice(NLTeams)
    else:
        return random.choice(ALTeams)
