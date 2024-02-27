import unittest
from parameterized import parameterized
from src.wordle import tally, play, Matches, PlayResponse, GameStatus

globals().update(Matches.__members__)
globals().update(GameStatus.__members__)

class WordleTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
        
    @parameterized.expand([
        ("FAVOR", "FAVOR", [EXACT_MATCH] * 5),
        ("FAVOR", "TESTS", [NO_MATCH] * 5),
        ("FAVOR", "RAPID", [PARTIAL_MATCH, EXACT_MATCH, NO_MATCH, NO_MATCH, NO_MATCH]),
        ("FAVOR", "MAYOR", [NO_MATCH, EXACT_MATCH, NO_MATCH, EXACT_MATCH, EXACT_MATCH]),
        ("FAVOR", "RIVER", [NO_MATCH, NO_MATCH, EXACT_MATCH, NO_MATCH, EXACT_MATCH]),
        ("FAVOR", "AMAST", [PARTIAL_MATCH, NO_MATCH, PARTIAL_MATCH, NO_MATCH, NO_MATCH]),

        ("SKILL", "SKILL", [EXACT_MATCH] * 5),
        ("SKILL", "SWIRL", [EXACT_MATCH, NO_MATCH, EXACT_MATCH, NO_MATCH, EXACT_MATCH]),
        ("SKILL", "CIVIL", [NO_MATCH, PARTIAL_MATCH, NO_MATCH, PARTIAL_MATCH, EXACT_MATCH]),
        ("SKILL", "SHIMS", [EXACT_MATCH, NO_MATCH, EXACT_MATCH, NO_MATCH, NO_MATCH]),
        ("SKILL", "SILLY", [EXACT_MATCH, PARTIAL_MATCH, PARTIAL_MATCH, EXACT_MATCH, NO_MATCH]),
        ("SKILL", "SLICE", [EXACT_MATCH, PARTIAL_MATCH, EXACT_MATCH, NO_MATCH, NO_MATCH]),
    ])
    
    def test_tally(self, target, guess, expected):
        self.assertEqual(tally(target, guess), expected)

    
    @parameterized.expand([
        ("FAVOR", "FOR", "Word must be 5 letters"),
        ("FAVOR", "FERVER", "Word must be 5 letters"),
    ])
    def test_exception_length(self, target, guess, expected_exception):
        with self.assertRaisesRegex(ValueError, expected_exception):
            tally(target, guess)


    def test_play_attempt_0_correct_guess(self):
        result = play(0, "FAVOR", "FAVOR")
        
        self.assertEqual({
          PlayResponse.Attempts: 1,
          PlayResponse.TallyResult: [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH],
          PlayResponse.GameStatus: WON,
          PlayResponse.Message: 'Amazing'
        }, result)

if __name__ == '__main__':
    unittest.main()
