import requests
import random
import time

def get_response():
  URL = "http://agilec.cs.uh.edu/words"
  
  return requests.get(URL).text.split("\n")
  
def get_a_random_word(word_list, seed=None): #Feedback: words instead of word_list. time.....ns instead of None
    random.seed(seed) #Feedback: a blank line after this line, please
    return random.choice(word_list)
  