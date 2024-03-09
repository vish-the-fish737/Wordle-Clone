import unittest
import requests
from unittest.mock import patch
from src.agilec_word_services import get_response

class AgilecWordServicesTests(unittest.TestCase):
    def test_get_response_returns_list_of_words(self):
        self.assertTrue(len(get_response()) > 0)
        