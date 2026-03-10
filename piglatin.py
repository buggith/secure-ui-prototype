def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  piglatin_words =[]
  for word in words:
    # Create the pig latin word and add it to the list
    piglatin_word = word[1:] + word [0] +"ay"
    piglatin_words.append(piglatin_word)
    # Turn the list back into a phrase
  return " ".join(piglatin_words)
    
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"