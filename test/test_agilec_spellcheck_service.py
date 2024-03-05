import unittest
from src.agilec_spellcheck_service import get_response


class AgilecSpellcheckServiceTests(unittest.TestCase):
    def test_get_response_returns_true_for_FAVOR(self):
        self.assertEqual(get_response("FAVOR"), "true")

if __name__ == '__main__':
    unittest.main()
