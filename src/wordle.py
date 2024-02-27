from enum import Enum
import requests
import random
from collections import Counter

class Matches(Enum):
    EXACT_MATCH = 'Exact Match'
    PARTIAL_MATCH = 'Part Match'
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

def is5Letters(guess):
    if len(guess) != WORD_SIZE:
        raise ValueError("Word must be 5 letters")

def exactMatches(target, guess, usedLetters, result):
    for i in range(WORD_SIZE):
        if target[i] == guess[i]:
            result[i] = Matches.EXACT_MATCH
            usedLetters[i] = True

def partialMatches(target, guess, usedLetters, result, remainingLetters):
    for i in range(WORD_SIZE):
        if result[i] == Matches.NO_MATCH and guess[i] in remainingLetters:
            result[i] = Matches.PARTIAL_MATCH
            usedLetters[target.index(guess[i])] = True
            
def afterPartialMatches(target, guess, usedLetters, result, remainingLetters):
    for i in range(WORD_SIZE):
        if result[i] == Matches.PARTIAL_MATCH and guess[i] in remainingLetters:
            result[i] = Matches.PARTIAL_MATCH
            usedLetters[target.index(guess[i])] = True
            
def lettersLeft(allWordLetters, usedLetters):
    return [allWordLetters[i] for i in range(WORD_SIZE) if not usedLetters[i]]


def tally(target, guess):
    is_5_letters(guess)
    response = []
    for i in range(WORD_SIZE):
        response.append(tally_for_position(i, target, guess))
    return response

def tally_for_position(position, target, guess):
    if target[position] == guess[position]:
        return Matches.EXACT
    
    letter = guess[position]
    positional_matches = count_positional_matches(target, guess, letter)
    non_positional_occurrences_in_target = count_occurrences_until_position(WORD_SIZE - 1, target, letter) - positional_matches
    occurrences_in_guess_until_position = count_occurrences_until_position(position, guess, letter)
    
    if non_positional_occurrences_in_target >= occurrences_in_guess_until_position:
        return Matches.EXISTS
    
    return Matches.NO_MATCH

def count_positional_matches(target, guess, letter):
    return sum(1 for t, g in zip(target, guess) if t == g and t == letter)

def count_occurrences_until_position(position, word, letter):
    return Counter(word[:position + 1])[letter]

def is_5_letters(guess):
    if len(guess) != WORD_SIZE:
        raise ValueError("Word must be 5 letters")


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
    messages = ['Amazing', 'Splendid', 'Awesome']
    
    return messages[attempts]
  
  return ''

def determine_game_status(attempts, tally_result):
  if all(match == Matches.EXACT_MATCH for match in tally_result):
    return GameStatus.WON
  
  return GameStatus.IN_PROGRESS

def get_word(link):
    words = requests.get(link)
    return random.choice(words)