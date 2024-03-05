import requests

def get_response(word):
  URL = "http://agilec.cs.uh.edu/spellcheck?check="
  
  return requests.get(f"{URL}{word}").text

def parse(boolean): #Feedback: response instead of boolean
  if boolean == "true":
    return True
  #Feedback: return response == 'true'
