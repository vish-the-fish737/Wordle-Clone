import unittest
import requests
from unittest.mock import patch
from src.agilec_word_services import get_response, get_a_random_word

class AgilecWordServicesTests(unittest.TestCase):
    def test_get_response_returns_list_of_words(self):
        self.assertTrue(len(get_response()) > 0)
        
    def test_get_a_random_word_given_list_of_words(self):
        word_list = get_response()
        random_word = get_a_random_word(word_list)
        
        self.assertIn(random_word, word_list)

    def test_getARandomWord_returns_two_different_words(self):
        word_list = get_response()
        
        random_word1 = get_a_random_word(word_list, seed=1001)
        random_word2 = get_a_random_word(word_list, seed=1002)
        
        self.assertNotEqual(random_word1, random_word2)
        