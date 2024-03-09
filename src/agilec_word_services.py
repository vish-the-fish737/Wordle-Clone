import requests
import random

def get_response():
  URL = "http://agilec.cs.uh.edu/words"
  
  return requests.get(URL).text.split("\n")
  
def get_a_random_word(word_list, seed=None): #Feedback: we should set the seed to time ns value so each time it is called it can get a different seed
    return random.choice(word_list) #Feedback: we're not using the seed? Then why receive it?
#Feedback: exactly one blank line at the bottom of each file, please    