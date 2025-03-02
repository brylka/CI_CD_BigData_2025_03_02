import unittest
from application import application

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.app = application.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        date = response.data.decode('utf-8')
        self.assertIn('Witaj, BigData z Pythonem!', date)

    def test_status_hello_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
