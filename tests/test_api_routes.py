from app import app
import unittest
import json
from dotenv import load_dotenv
from pathlib import Path

class ApiTest(unittest.TestCase):
    
    def setUp(self):
        dotenv_path = Path('/.env.test')
        load_dotenv(dotenv_path=dotenv_path)
        self.app = app.test_client()
        
    def test_post_api_route(self):
        response = self.app.get('/api/test')
        self.assertEqual(200, response.status_code)

        request_data = json.dumps({"test": "test"})       
        response = self.app.post('/api/test', headers={"Content-Type": "application/json"}, data=request_data)
        self.assertEqual(200, response.status_code)

        response = self.app.post('/api/test', headers={"Content-Type": "application/json"})
        self.assertEqual(400, response.status_code)

    def tearDown(self):
        dotenv_path = Path('/.env')
        load_dotenv(dotenv_path=dotenv_path)