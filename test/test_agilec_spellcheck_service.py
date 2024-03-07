import unittest
from unittest.mock import patch
from src.agilec_spellcheck_service import get_response, parse, is_spelling_correct


class AgilecSpellcheckServiceTests(unittest.TestCase):
    def test_get_response_returns_true_for_FAVOR(self):
        self.assertEqual(get_response("FAVOR"), "true")

    def test_get_response_returns_false_for_FAVRR(self):
        self.assertEqual(get_response("FAVRR"), "false")

    def test_parse_true_returns_True(self):
        self.assertTrue(parse("true"))
       
    def test_parse_false_return_False(self):
        self.assertFalse(parse("false"))
      
    def test_parse_takes_invalid_text(self):
        self.assertRaisesRegex(Exception, "Invalid response", parse, "Invalid text")

    @patch('src.agilec_spellcheck_service.get_response', return_value='true')
    @patch('src.agilec_spellcheck_service.parse', return_value=True)
    def test_is_spelling_correct_returns_true_if_getResponse_returns_true_and_uses_parse(self, mock_parse, mock_get_response):
        self.assertTrue(is_spelling_correct("FAVOR"))
        
        mock_get_response.assert_called_once_with("FAVOR")
        mock_parse.assert_called_once_with('true')
    
    @patch('src.agilec_spellcheck_service.get_response', return_value='false')
    @patch('src.agilec_spellcheck_service.parse', return_value=False)
    def test_is_spelling_correct_returns_false_if_getResponse_returns_false_and_uses_parse(self, mock_parse, mock_get_response):
        self.assertFalse(is_spelling_correct("FAVOR"))
        
        mock_get_response.assert_called_once_with("FAVOR")
        mock_parse.assert_called_once_with('false')

    @patch('src.agilec_spellcheck_service.get_response', side_effect=Exception("Network Error"))
    def test_is_spelling_correct_throws_network_error_if_getResponse_throws_that_exception(self, mock_get_response):
        self.assertRaisesRegex(Exception, "Network Error", is_spelling_correct, "FAVOR")

#Feedback: please remove feedback notes and commented out stuff
        #Feedback: Good work on this test. We can make this simpler.
        #@patch('src.agilec_spellcheck_service.get_response', side_effect=Exception("Network Error"))
        #then within the test we can call self.assertRaisesRegex...

#Feedback:  please remove the following
#    @patch("src.agilec_spellcheck_service.requests.get")
#    def test_getResponse_returns_list_of_words(self, mock_get):
#        mock_get.return_value.text = "FAVOR"
#        words = get_response("http://agilec.cs.uh.edu/spellcheck")
#        self.assertTrue("FAVOR" in words)
#
#    
#    def test_getARandomWord_given_list_of_words(self):
#        word_list = ["FAVOR", "SKILL", "APPLE"]
#        random_word = get_a_random_word(word_list)
#        self.assertIn(random_word, word_list)
#
#    def test_getARandomWord_returns_two_different_words(self):
#        word_list = ["FAVOR", "SKILL", "APPLE"]
#        random_word1 = get_a_random_word(word_list)
#        random_word2 = get_a_random_word(word_list)
#        self.assertNotEqual(random_word1, random_word2)
    
        
if __name__ == '__main__':
    unittest.main()
