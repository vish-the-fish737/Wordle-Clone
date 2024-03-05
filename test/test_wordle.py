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
        ("FAVOR", "AMAST", [PARTIAL_MATCH, NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH]),
        
        ("SKILL", "SKILL", [EXACT_MATCH] * 5),
        ("SKILL", "SWIRL", [EXACT_MATCH, NO_MATCH, EXACT_MATCH, NO_MATCH, EXACT_MATCH]),
        ("SKILL", "CIVIL", [NO_MATCH, PARTIAL_MATCH, NO_MATCH, NO_MATCH, EXACT_MATCH]),
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
    
    def test_play_with_invalid_guess(self):
        with self.assertRaisesRegex(ValueError, "Word must be 5 letters"):
          play(0, "FAVOR", "FAR")
    
    def test_play_attempt_0_wrong_guess(self):
        result = play(0, "FAVOR", "TESTS")
    
        self.assertEqual({
          PlayResponse.Attempts: 1,
          PlayResponse.TallyResult: [NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH],
          PlayResponse.GameStatus: IN_PROGRESS,
          PlayResponse.Message: ''
        }, result)
    
    def test_play_second_attempt_correct_guess(self):
        result = play(1, "FAVOR", "FAVOR")
    
        self.assertEqual({
          PlayResponse.Attempts: 2,
          PlayResponse.TallyResult: [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH],
          PlayResponse.GameStatus: WON,
          PlayResponse.Message: 'Splendid'
        }, result)

    def test_play_second_attempt_wrong_guess(self):
        result = play(1, "FAVOR", "RIVER")
    
        self.assertEqual({
          PlayResponse.Attempts: 2,
          PlayResponse.TallyResult: [NO_MATCH, NO_MATCH, EXACT_MATCH, NO_MATCH, EXACT_MATCH],
          PlayResponse.GameStatus: IN_PROGRESS,
          PlayResponse.Message: ''
        }, result)

    def test_play_third_attempt_correct_guess(self):
        result = play(2, "FAVOR", "FAVOR")
    
        self.assertEqual({
          PlayResponse.Attempts: 3,
          PlayResponse.TallyResult: [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH],
          PlayResponse.GameStatus: WON,
          PlayResponse.Message: 'Awesome'
        }, result)

    def test_play_third_attempt_incorrect_guess(self):
        result = play(2, "FAVOR", "TESTS")
    
        self.assertEqual({
          PlayResponse.Attempts: 3,
          PlayResponse.TallyResult: [NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH],
          PlayResponse.GameStatus: IN_PROGRESS,
          PlayResponse.Message: ''
        }, result)
    
    def test_play_fourth_attempt_correct_guess(self):
        result = play(3, "FAVOR", "FAVOR")
    
        self.assertEqual({
          PlayResponse.Attempts: 4,
          PlayResponse.TallyResult: [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH],
          PlayResponse.GameStatus: WON,
          PlayResponse.Message: 'Yay'
        }, result)
    
    def test_play_fourth_attempt_incorrect_guess(self):
        result = play(3, "FAVOR", "TESTS")
    
        self.assertEqual({
          PlayResponse.Attempts: 4,
          PlayResponse.TallyResult: [NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH],
          PlayResponse.GameStatus: IN_PROGRESS,
          PlayResponse.Message: ''
        }, result)
    
    def test_play_fifth_attempt_correct_guess(self):
        result = play(4, "FAVOR", "FAVOR")
    
        self.assertEqual({
          PlayResponse.Attempts: 5,
          PlayResponse.TallyResult: [EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH, EXACT_MATCH],
          PlayResponse.GameStatus: WON,
          PlayResponse.Message: 'Yay'
        }, result)
    
    def test_play_fifty_attempt_incorrect_guess(self):
        result = play(4, "FAVOR", "TESTS")
    
        self.assertEqual({
          PlayResponse.Attempts: 5,
          PlayResponse.TallyResult: [NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH],
          PlayResponse.GameStatus: IN_PROGRESS,
          PlayResponse.Message: ''
        }, result)
    
    def test_play_sixth_attempt_correct_guess(self):
        result = play(5, "FAVOR", "FAVOR")
    
        self.assertEqual({
          PlayResponse.Attempts: 6,
          PlayResponse.TallyResult: [EXACT_MATCH] * 5,
          PlayResponse.GameStatus: WON,
          PlayResponse.Message: 'Yay'
        }, result)

    def test_play_sixth_attempt_incorrect_guess(self):
        result = play(5, "FAVOR", "RIVER")
    
        self.assertEqual({
          PlayResponse.Attempts: 6,
          PlayResponse.TallyResult: [NO_MATCH, NO_MATCH, EXACT_MATCH, NO_MATCH, EXACT_MATCH],
          PlayResponse.GameStatus: LOST,
          PlayResponse.Message: ''
        }, result)

    def test_play_seventh_attempt_correct_guess(self):
        self.assertRaisesRegex(Exception, "Tries exceeded", play, 6, "FAVOR", "FAVOR")

    def test_play_eigth_attempt_correct_guess(self):
        self.assertRaisesRegex(Exception, "Tries exceeded", play, 7, "FAVOR", "TESTS")
    
    def test_throws_an_exception_for_attempt_1_target_FAVOR_and_guess_FEVER_where_FEVER_is_considered_incorrect_spelling(self):
      self.assertRaisesRegex(Exception, "Not a word", play, 1, "FAVOR", "FEVER", lambda word: False)
    
    def test_play_returns_proper_response_for_attempt_1_target_FAVOR_and_guess_FEVER_where_FEVER_is_considered_correct_spelling(self):
      #self.assertRaisesRegex(Exception, "Not a word", play, 1, "FAVOR", "FEVER", lambda word: True)
      result = play(5, "FAVOR", "RIVER")
      
      self.assertEqual({
          PlayResponse.Attempts: 1,
          PlayResponse.TallyResult: [EXACT_MATCH, NO_MATCH, EXACT_MATCH, NO_MATCH, EXACT_MATCH],
          PlayResponse.GameStatus: IN_PROGRESS,
          PlayResponse.Message: ''
        }, result)
      is_correct_spelling = lambda word: True
      self.assertTrue(is_correct_spelling("FEVER"))
    
    #In the previous test we passed lambda word: False. In this test we need to pass lambda word: True. Can you please implement this one test
    #and make sure it passes. For the assert, we can use one single assertEquals like we did in some tets above.
      
if __name__ == '__main__':
    unittest.main()
