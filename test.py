#!/usr/bin/env python3
import unittest
import app

class TestHello(unittest.TestCase):

    # Initialize the test
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    # Testing if the index page is reachable
    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    # Two new tests
    def test_recent_temps(self):
        rv = self.app.get('/recent_temps')
        self.assertEqual(rv.status, '200 OK')

    def test_get_one_temp(self):
        rv = self.app.get('/get_one_temp_api')
        self.assertEqual(rv.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
