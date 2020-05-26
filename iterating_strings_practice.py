###Write a new function called get_length() that takes a string as an input and returns the number of characters in that string. 
###Do this by iterating through the string, don’t cheat and use len()

def get_length(string):
  counter = 0
  for length in string:
    counter += 1
  return counter
