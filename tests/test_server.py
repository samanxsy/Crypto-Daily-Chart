import unittest
from flask import Flask
import app.common.status as status
import app.server as server


class BaseTest(unittest.TestCase):

    def setUp(self):
      self.app = Flask("Crypto Daily Charts", static_folder="./app/static")
      self.app.add_url_rule('/', view_func=server.home)
      self.app.add_url_rule('/calculate', view_func=server.chart)
      self.app.add_url_rule('/error', view_func=server.error)


class TestServer(BaseTest):
    """This should return 200 OK upon success"""
    def test_home(self):
        with self.app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_error_handle(self):
        """This should redirect to the error page after a ValueError"""
        with self.app.test_client() as c:
            response = c.get('/calculate?market=wooodcoin&days=14')
            self.assertIn(b"Redirecting", response.data)


    def test_correct_value(self):
        """This should return 200 OK upon success"""
        with self.app.test_client() as c:
            response = c.get('/calculate?market=bitcoin&days=14')
            self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_error(self):
        """This should return 200 OK upon success"""
        with self.app.test_client() as c:
            response = c.get('/error')
            self.assertEqual(response.status_code, status.HTTP_200_OK)


if __name__ == '__main__':
    unittest.main()