import requests

def get_response(word):
  URL = "http://agilec.cs.uh.edu/spellcheck?check="
  
  return requests.get(f"{URL}{word}").text

def parse(response):
  if response == "true":
    return True
  elif response == "false":
    return False
  elif response == "Invalid text":
    raise Exception("Invalid response")
