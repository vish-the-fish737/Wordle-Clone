from enum import Enum
import random
from collections import Counter

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
    LOST = "Lost"

WORD_SIZE = 5

def validate_length(guess):
    if len(guess) != WORD_SIZE:
        raise ValueError("Word must be 5 letters")


def tally(target, guess):
  validate_length(guess)

  return [tally_for_position(position, target, guess) for position in range(0, WORD_SIZE)]

def tally_for_position(position, target, guess):
  if(target[position] == guess[position]):
    return Matches.EXACT_MATCH
  
  letter_at_position = guess[position]
  
  positional_matches = count_positional_matches(target, guess, letter_at_position)
  non_positional_occurrences_in_target = count_number_of_occurrences_until_position(WORD_SIZE - 1, target, letter_at_position) - positional_matches;
    
  number_of_occurances_in_guess_until_position = count_number_of_occurrences_until_position(position, guess, letter_at_position);

  if(non_positional_occurrences_in_target >= number_of_occurances_in_guess_until_position):
    return Matches.PARTIAL_MATCH
    
  return Matches.NO_MATCH

def count_positional_matches(target, guess, letter):
  return len(list(
    filter(lambda index: target[index] == guess[index],
      filter(lambda index: target[index] == letter, range(0, WORD_SIZE)))))

def count_number_of_occurrences_until_position(position, word, letter):
  return len(list(filter(lambda ch: ch == letter, word[0: position + 1])))

def play(attempts, target, guess):
  validate_trie(attempts)
  
  validate_spelling(target, guess)
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
    messages = ['Amazing', 'Splendid', 'Awesome', 'Yay', "Yay", "Yay", 'It was FAVOR, better luck next time']
    if attempts <= 5:
      return messages[attempts]
  
  return ''

def determine_game_status(attempts, tally_result):
  if all(match == Matches.EXACT_MATCH for match in tally_result) and attempts <= 5:
    return GameStatus.WON
  
  else:
    return GameStatus.IN_PROGRESS

def validate_trie(attempts):
  MAX_TRIES = 6
  
  if(attempts >= MAX_TRIES):
    raise Exception("Tries exceeded")
  
def validate_spelling(target, guess):
  if(target != guess):
    raise NameError("Wrong spelling")
