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

def get_a_random_word(word_list):
  return random.choice(word_list)