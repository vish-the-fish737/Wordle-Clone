from enum import Enum

class Matches(Enum):
    EXACT_MATCH = 'Exact Match'
    PARTIAL_MATCH = 'Part Match'
    NO_MATCH = 'No Match'

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