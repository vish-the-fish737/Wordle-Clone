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

    def test_is_spelling_correct_throws_network_error_if_getResponse_throws_that_exception(self):
        def get_response_stub(word):
            raise Exception("Network Error")

        with patch("src.agilec_spellcheck_service.get_response", side_effect=get_response_stub):
            self.assertRaisesRegex(Exception, "Network Error", is_spelling_correct, "FAVOR")
        
if __name__ == '__main__':
    unittest.main()
