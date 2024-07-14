def is_pangram(sentence):
  # Define the alphabet set
  alphabet = set('abcdefghijklmnopqrstuvwxyz')

  # Convert the sentence to lowercase and create a set of characters
  sentence_set = set(sentence.lower())

  # Check if all letters in the alphabet are in the sentence set
  if alphabet.issubset(sentence_set):
      return True
  else:
      return False

# The sentence to check
sentence = "The quick brown fox jumps over the lazy dog"
# sentence = "Naruto Uzumaki will survive"

# Check if the sentence is a pangram and print the result
if is_pangram(sentence):
  print("Pangram found")
else:
  print("Pangram not found")
