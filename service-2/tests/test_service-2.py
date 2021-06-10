from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

# positions = ['SP','RP','CP','C','1B','2B','3B','SS','LF','CF','RF']
positions = ['Starting Pitcher','Relief Pitcher','Closing Pitcher','Catcher','1st Baseman','2nd Baseman','3rd Baseman','Short Stop','Left Field','Center Field','Right Field']

class TestServ2(TestBase):
    def test_service2(self):
        for pos in positions:
            with patch('random.choice') as r:
                r.return_value=pos
                response = self.client.get(url_for('gen_position'))
                self.assertEqual(response.status_code, 200)
                self.assertIn(pos, response.data.decode("utf-8"))