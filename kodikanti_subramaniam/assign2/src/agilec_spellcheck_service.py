import requests

def get_response(word):
  URL = "http://agilec.cs.uh.edu/spellcheck?check="
  
  return requests.get(f"{URL}{word}").text
