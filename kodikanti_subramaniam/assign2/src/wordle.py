from enum import Enum

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
    is5Letters(guess)
    allWordLetters = list(target)
    usedLetters = [False] * WORD_SIZE  
    result = [Matches.NO_MATCH] * WORD_SIZE
    
    exactMatches(target, guess, usedLetters, result)
    remainingLetters = lettersLeft(allWordLetters, usedLetters)
    partialMatches(target, guess, usedLetters, result, remainingLetters)
    afterPartialMatches(target, guess, usedLetters, result, remainingLetters)

    return result

#Feedback:  we can turn the above code into functional style. Please see the assign2reviews.txt for some suggestions.

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
