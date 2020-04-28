from unittest import TestCase
import yelp

class TestZipCode(TestCase):

    def test_zip_code_length(self):
        self.assertEqual(len(str(78626)), len(str(yelp.get_location())))
    
    def test_zip_code_is_integer(self):
        self.assertIsInstance(78626, int)
        self.assertNotEqual('qwert', int)
        self.assertGreater(yelp.get_location(), 0)