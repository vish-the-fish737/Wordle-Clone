import requests

def get_response(word):
  URL = "http://agilec.cs.uh.edu/spellcheck?check="
  
  return requests.get(f"{URL}{word}").text

def parse(response):
  if response == "true":
    return True
  elif response == "false": #Feedback: no need for else after a retrn or raise
    return False
  elif response == "Invalid text":
    raise Exception("Invalid response")
  
  #Feedback: if response not in ['true', 'false']:
  # raise ...
  #
  #  return response == 'true'

def is_spelling_correct(word):
  return parse(get_response(word))
