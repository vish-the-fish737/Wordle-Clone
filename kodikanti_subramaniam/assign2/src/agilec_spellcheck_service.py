import requests
import random

def get_response(word):
  URL = "http://agilec.cs.uh.edu/spellcheck?check="
  
  return requests.get(f"{URL}{word}").text

def parse(response):
  if response not in ["true", "false"]:
    raise Exception("Invalid response")
  
  return response == "true"

def is_spelling_correct(word):
  return parse(get_response(word))

#Feedback: please remove this from here. Single Responsibilty Princple. This funtion below is not related to anything above. It should be in its own file
#def get_a_random_word(word_list):
#  return random.choice(word_list)