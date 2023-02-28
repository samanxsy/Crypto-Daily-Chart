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

    def test_home(self):
        with self.app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
