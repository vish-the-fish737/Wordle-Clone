import unittest
import requests
from unittest.mock import patch
from src.agilec_word_services import get_response, get_a_random_word

class AgilecWordServicesTests(unittest.TestCase):
    def test_get_response_returns_list_of_words(self):
        self.assertTrue(len(get_response()) > 0)
        
    def test_get_a_random_word_given_list_of_words(self):
        words = ["FAVOR", "SKILL", "APPLE", "TESTS"]
        
        self.assertTrue(get_a_random_word(words, 1001) in words) #Feedback: no need to send the seed here.
        
    def test_getARandomWord_returns_two_different_words(self):
        words = ["FAVOR", "SKILL", "APPLE", "TESTS"]
        
        self.assertNotEqual(get_a_random_word(words, 100), get_a_random_word(words, 100000051))
