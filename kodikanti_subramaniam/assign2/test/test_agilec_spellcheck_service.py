import unittest
from src.agilec_spellcheck_service import get_response, parse


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
        
if __name__ == '__main__':
    unittest.main()
