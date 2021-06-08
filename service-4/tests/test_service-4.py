from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch
from application.routes import ALTeams, NLTeams
import random

class TestBase(TestCase):
    def create_app(self):
        return app

# test_cases=[('RF',23),('C', 29),('SP',1),('SS',3)]
picks=list()
for i in range(1,31):
    picks.append(i)

class TestServ2(TestBase):
    def test_service2(self):
        # for case in test_cases:
            # with patch('random.choice') as r:
            #     r.return_value = 'Boston Red Sox'
            #     response = self.client.get(url_for('draftpick'))
            #     self.assertEqual(response.status_code, 200)
            #     self.assertEqual('Boston Red Sox', response.data)
            
        response = self.client.get(url_for('draftpick'), json=(random.randint(1,30)))
        self.assertIn(response.data.decode('utf-8'), (ALTeams,NLTeams) )