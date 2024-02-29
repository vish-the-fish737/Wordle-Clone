from enum import Enum
import requests
import random
from collections import Counter
import re

class Matches(Enum):
    EXACT_MATCH = 'Exact Match'
    PARTIAL_MATCH = 'Partial Match'
    NO_MATCH = 'No Match'

class PlayResponse(Enum):
    Attempts = 'Attempts'
    TallyResult = 'Tally Result'
    GameStatus = 'Game Status'
    Message = 'Message'
  
class GameStatus(Enum):
    WON = 'Won'
    IN_PROGRESS = "In Progress"

WORD_SIZE = 5

def validate_length(guess):
    if len(guess) != WORD_SIZE:
        raise ValueError("Word must be 5 letters")

def tally(target, guess):
    return [tally_for_position(i, target, guess) for i, letter in enumerate(guess)]

def tally_for_position(position, target, guess):
    if target[position] == guess[position]:
        return 'EXACT_MATCH'
  
def count_positional_matches(target, guess, letter):
    matches = [1 for t, g in zip(target, guess) if t == g and g == letter]
    return sum(matches)

def tally_for_position(position, target, guess):
    letter_at_position = guess[position]
    positional_matches = count_positional_matches(target, guess, letter_at_position)
    non_positional_occurrences_in_target = (
        count_number_of_occurrences_in_guess_until_position(WORD_SIZE - 1, target, letter_at_position)
        - positional_matches
    )
    number_of_occurrences_in_guess_until_position = count_number_of_occurrences_in_guess_until_position(
        position, guess, letter_at_position
    )
    
    if non_positional_occurrences_in_target >= number_of_occurrences_in_guess_until_position:
        return "PARTIAL_MATCH"
    return "NO_MATCH"

def count_occurrences_in_guess_until_position(position, word, letter):
    substring = word[:position + 1]
    matches = re.findall(letter, substring)
    return len(matches)

def play(attempts, target, guess):
  tally_result = tally(target, guess)
  
  message = determine_message(attempts, tally_result)
  game_status = determine_game_status(attempts, tally_result)
  
  return {
          PlayResponse.Attempts: attempts + 1,
          PlayResponse.TallyResult: tally(target, guess),
          PlayResponse.GameStatus: game_status,
          PlayResponse.Message: message
        }

def determine_message(attempts, tally_result):
  if all(match == Matches.EXACT_MATCH for match in tally_result):
    messages = ['Amazing', 'Splendid', 'Awesome', 'Yay', 'Yay']
    
    return messages[attempts]
  
  return ''

def determine_game_status(attempts, tally_result):
  if all(match == Matches.EXACT_MATCH for match in tally_result):
    return GameStatus.WON
  
  return GameStatus.IN_PROGRESS

def get_word(link):
    words = requests.get(link)
    return random.choice(words)