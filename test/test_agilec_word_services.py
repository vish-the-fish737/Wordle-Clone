import unittest
import requests
from unittest.mock import patch
from src.agilec_word_services import get_response

class AgilecWordServicesTests(unittest.TestCase):
    def test_get_response_returns_list_of_words(self):
        self.assertEqual(['FAVOR', 'SMART', 'GUIDE', 'TESTS', "GRADE", "BRAIN", "SPAIN", "SPINE", "GRAIN", "BOARD", ''], get_response())
        #Feedback: the words on the service may change and this test will break.
        #instead assertTrue(len(get_response()) > 0)
        