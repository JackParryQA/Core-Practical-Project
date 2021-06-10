from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

positions = ['SP','RP','CP','C','1B','2B','3B','SS','LF','CF','RF']

class TestServ2(TestBase):
    def test_service2(self):
        for pos in positions:
            with patch('random.choice') as r:
                r.return_value=pos
                response = self.client.get(url_for('gen_position'))
                self.assertEqual(response.status_code, 200)
                self.assertIn(pos, response.data.decode("utf-8"))