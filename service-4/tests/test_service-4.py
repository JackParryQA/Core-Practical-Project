from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch
from application.routes import ALTeams, NLTeams
import random

class TestBase(TestCase):
    def create_app(self):
        return app

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


class TestServ2(TestBase):
    def test_service2_NL(self):
            
        response = self.client.get(url_for('draftpick'), json={'position':'SS','pick':2})
        self.assertEqual(response.status_code, 200)
        for team in NLTeams:
            r = response.data.decode()
            if r[1] == team:
                self.assertIn(r, {'response':f'With pick 2 in the 2021 MLB Draft the { team } have selected a SS','team':team} )
    
    def test_service2_AL(self):
        response = self.client.get(url_for('draftpick'), json={'position':'RF','pick':19})
        self.assertEqual(response.status_code, 200)
        for team in ALTeams:
            r = response.data.decode()
            if r[1] == team:
                self.assertIn(r, {'response':f'With pick 19 in the 2021 MLB Draft the { team } have selected a RF','team':team} )
