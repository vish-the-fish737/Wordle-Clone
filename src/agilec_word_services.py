import requests
import random
import time

def get_response():
  URL = "http://agilec.cs.uh.edu/words"
  
  return requests.get(URL).text.split("\n")
  
def get_a_random_word(words, seed=time.time_ns): #Feedback: time.time_ns()
    random.seed(seed)
    
    return random.choice(words)
