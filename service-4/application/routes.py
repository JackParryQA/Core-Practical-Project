from application import app
from flask import request
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


@app.route('/Draft Pick')
def draftpick():
    data_sent=request.data.decode()
    if int(data_sent["pick"])%2==0:
        team=random.choice(NLTeams)
    else:
        team=random.choice(ALTeams)
    # return f'With the {data-sent["pick"]} the {team} select a {data-sent["position"]}'
    return team
