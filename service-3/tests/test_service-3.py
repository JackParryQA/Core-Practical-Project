from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

picks=list()
for i in range(31,61):
    picks.append(i)

class TestServ2(TestBase):
    def test_service2(self):
        for pick in picks:
            with patch('random.choice') as r:
                r.return_value=pick
                response = self.client.get(url_for('gen_pick'))
                self.assertEqual(response.status_code, 200)
                self.assertIn(str(pick), response.data.decode("utf-8"))