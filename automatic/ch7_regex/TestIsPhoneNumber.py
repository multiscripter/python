import unittest

from automatic.ch7_regex.is_phone_number import is_phone_number
from automatic.ch7_regex.is_phone_number import is_phone_number_by_regex


class TestIsPhoneNumber(unittest.TestCase):

    def test_is_phone_number(self):
        text = '415-555-4242'
        self.assertTrue(is_phone_number(text))

    def test_is_phone_number_by_regex_only_phone(self):
        text = '415-555-4242'
        self.assertIsNotNone(is_phone_number_by_regex(r'\d{3}-\d{3}-\d{4}', text))

    def test_is_phone_number_by_regex_str(self):
        text = 'My phone number is 415-555-4242. Call me in the evening.'
        self.assertIsNotNone(is_phone_number_by_regex(r'\d{3}-\d{3}-\d{4}', text))

    def test_is_phone_number_by_regex_no_match(self):
        text = 'Call me in the evening.'
        self.assertIsNone(is_phone_number_by_regex(r'\d{3}-\d{3}-\d{4}', text))
