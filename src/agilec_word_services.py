import requests

def get_response():
  URL = "http://agilec.cs.uh.edu/words" #Feedback: a blank line after this line, please
  words = requests.get(URL)
  wordlist = words.text.split("\n")
  
  return wordlist
  #Feedback: return requests.get(URL).text.split("\n")
  