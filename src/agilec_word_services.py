import requests

def get_response():
  URL = "http://agilec.cs.uh.edu/words"
  words = requests.get(URL)
  wordlist = words.text.split("\n")
  
  return wordlist
