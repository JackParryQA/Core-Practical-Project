from flask import url_for
from flask_testing import TestCase
from application import app,db
# from unittest.mock import patch
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db"
        )
        return app

    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestHome(TestBase):
    def test_index(self):
        with requests_mock.Mocker() as m:
            m.get('http://service-2:5001/position', text='SS')
            m.get('http://service-3:5002/pick', json=4)
            m.post('http://service-4:5003/draft pick', json={'response':'With pick 4 in the 2021 MLB Draft the Los Angeles Dodgers have selected a SS','team':'Los Angeles Dodgers'})
            
            response = self.client.get(url_for('index'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'With pick 4 in the 2021 MLB Draft the Los Angeles Dodgers have selected a SS', response.data)
        
