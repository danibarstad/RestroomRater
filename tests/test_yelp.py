import yelp
from unittest import TestCase
from unittest.mock import patch, call

class TestZipCode(TestCase):

    def test_zip_code_length(self):
        self.assertEqual(len(str(78626)), len(str(yelp.get_location())))
    
    def test_zip_code_is_integer(self):
        self.assertIsInstance(78626, int)
        self.assertNotEqual('qwert', int)
        self.assertGreater(len(str(yelp.get_location())), 4)
        self.assertLess(len(str(yelp.get_location())), 6)