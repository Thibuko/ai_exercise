"""basic unit tests"""
import unittest
from app import app  # Replace 'app' with your Flask app instance

class TestApp(unittest.TestCase):
    """class for all unis test"""
    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        """Check is home page is displayed"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Multiple Choice Quiz', response.data)

    def test_result_page(self):
        """Check if result page is displayed"""
        response = self.app.get('/result')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Quiz Results', response.data)

if __name__ == '__main__':
    unittest.main()
